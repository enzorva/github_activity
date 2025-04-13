import sys
import urllib.request
import urllib.error
import json

if len(sys.argv) < 2:
    print("Usage: python github_activity.py <username>")
    sys.exit(1)

user_name = sys.argv[1]
url = f"https://api.github.com/users/{user_name}/events"
response = urllib.request.urlopen(url)
raw_data = response.read()
print(raw_data)

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




user_name = sys.argv[1]
url = f"https://api.github.com/users/{user_name}/events"
data = fetch_data_from_git(url)

if data:
    print("Data fetched successfully.", data)
else:
    print("Failed to fetch data.")