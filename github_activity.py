import sys
import urllib.request
import urllib.error
import json

def fetch_data_from_git(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = response.read().decode()
            return json.loads(data)
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e.msg}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    except TimeoutError:
        print("Request timed out. Please try again later.")

def format_github_activity(data):
    formatted_activities = []
    repo_commit_counts = {}  

    for event in data:
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name", "unknown repository")

        if event_type == "PushEvent":
            commit_count = len(event.get("payload", {}).get("commits", []))
            if repo_name in repo_commit_counts:
                repo_commit_counts[repo_name] += commit_count
            else:
                repo_commit_counts[repo_name] = commit_count

        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "performed an action on")
            formatted_activities.append(f"- {action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            formatted_activities.append(f"- Starred {repo_name}")
        elif event_type == "ForkEvent":
            forked_repo = event.get("payload", {}).get("forkee", {}).get("full_name", "unknown repository")
            formatted_activities.append(f"- Forked {repo_name} to {forked_repo}")
        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action", "performed an action on")
            pr_number = event.get("payload", {}).get("number", "unknown")
            formatted_activities.append(f"- {action.capitalize()} pull request #{pr_number} in {repo_name}")
        elif event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type", "unknown")
            ref = event.get("payload", {}).get("ref", "unknown")
            formatted_activities.append(f"- Created {ref_type} {ref} in {repo_name}")
        elif event_type == "DeleteEvent":
            ref_type = event.get("payload", {}).get("ref_type", "unknown")
            ref = event.get("payload", {}).get("ref", "unknown")
            formatted_activities.append(f"- Deleted {ref_type} {ref} in {repo_name}")
        elif event_type == "ReleaseEvent":
            action = event.get("payload", {}).get("action", "performed an action on")
            release_name = event.get("payload", {}).get("release", {}).get("name", "unknown release")
            formatted_activities.append(f"- {action.capitalize()} release {release_name} in {repo_name}")
        elif event_type == "GollumEvent":
            formatted_activities.append(f"- Updated a wiki page in {repo_name}")
        elif event_type == "PublicEvent":
            formatted_activities.append(f"- Made {repo_name} public")
        elif event_type == "MemberEvent":
            action = event.get("payload", {}).get("action", "performed an action on")
            member = event.get("payload", {}).get("member", {}).get("login", "unknown member")
            formatted_activities.append(f"- {action.capitalize()} member {member} in {repo_name}")
        else:
            formatted_activities.append(f"- {event_type} in {repo_name}")

    for repo, total_commits in repo_commit_counts.items():
        formatted_activities.append(f"- Pushed {total_commits} commits to {repo}")

    return formatted_activities

user_name = sys.argv[1]
url = f"https://api.github.com/users/{user_name}/events"
data = fetch_data_from_git(url)

if data:
    print("Data fetched successfully:\n")
    activities = format_github_activity(data)
    for activity in activities:
        print(activity)
else:
    print("Failed to fetch data.")