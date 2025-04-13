# GitHub Activity Tracker

This project is a Python script that fetches and displays a user's recent activity on GitHub in a human-readable format. It uses the GitHub Events API to retrieve data and processes it to provide a summary of actions such as commits, issues, pull requests, and more.

## Features
- Fetches recent activity for a specified GitHub user.
- Displays activity in a user-friendly format, such as:
  - Pushed commits to repositories.
  - Opened or closed issues.
  - Starred repositories.
  - Forked repositories.
  - Created or deleted branches/tags.
  - Published releases.
- Handles various GitHub event types, including `PushEvent`, `IssuesEvent`, `WatchEvent`, `ForkEvent`, and more.

## Requirements
- Python 3.6 or higher
- Internet connection

## Installation
1. Clone this repository or download the script `github_activity.py`.
2. Ensure Python is installed on your system. You can check by running:
   ```bash
   python --version
   ```
3. Install any required dependencies (if applicable).

## Usage
1. Open a terminal or command prompt.
2. Run the script with the following command:
   ```bash
   python github_activity.py <GitHub username>
   ```
   Replace `<GitHub username>` with the username of the GitHub user whose activity you want to track.

### Example
```bash
python github_activity.py kamranahmedse
```
Output:
```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```

## How It Works
1. The script fetches data from the GitHub Events API for the specified user.
2. It processes the data to extract relevant information about the user's activity.
3. The activity is formatted into a readable list and displayed in the terminal.

## Limitations
- The GitHub API has rate limits. If you exceed the limit, you may need to wait before making additional requests.
- The script only fetches public events. Private events are not accessible via the GitHub Events API.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.