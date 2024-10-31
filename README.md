# GitHub License Year Updater

This tool automates the process of updating the copyright year in the LICENSE files of your GitHub repositories to the current year. It uses the GitHub API to access your repositories, identify the LICENSE files, and update them accordingly. The tool also handles the commit and push process to update the repositories.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatically fetches all repositories for a given GitHub username.
- Identifies and updates the copyright year in the LICENSE files.
- Uses the GitHub API to perform updates.
- Handles the commit and push process to update the repositories.

## Prerequisites

- Python 3.6 or higher
- A GitHub Personal Access Token (PAT) with the necessary permissions to read and write repository contents.
- Git installed on your system.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sharma-IT/license-year-updater.git
   cd license-year-updater
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Add your GitHub Personal Access Token to the `.env` file in the root directory of the project:

   ```plaintext
   GITHUB_TOKEN=your_github_token_here
   ```

2. Run the script:

   ```bash
   python update_license.py
   ```

3. The script will automatically update the LICENSE files in your repositories.

## Configuration

- **GitHub Username**: Update the `username` variable in the `main()` function of `update_license.py` with your GitHub username.

- **License File Name**: The script assumes the LICENSE file is named `LICENSE`. If your repositories use a different name (e.g., `LICENSE.md`), you will need to adjust the script accordingly.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the GNU General Public License v3.0 License. See the [LICENSE](LICENSE) file for details.

---

### Notes:

- **Local Cloning**: The script clones each repository locally to perform the commit and push operations. This requires Git to be installed on your system.
- **Security**: Be cautious with your GitHub token. Ensure it has the necessary permissions and is stored securely.
- **Cleanup**: The script cleans up the local clone after committing and pushing changes.
