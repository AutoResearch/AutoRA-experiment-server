# Using Python Copier

## Installing Copier

### 1. Install Python

First, ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### 2. Install Copier

#### On Windows:

1. Open Command Prompt (you can search for `cmd` in the Start menu).

2. Run the following command to install Copier using pip (Python's package installer):

   ```sh
   pip install copier
   ```

#### On MacOS:

1. Open Terminal (you can find it in Applications > Utilities).

2. Run the following command to install Copier using pip:

   ```sh
   pip install copier
   ```

#### On Linux:

1. Open your Terminal.

2. Run the following command to install Copier using pip:

   ```sh
   pip install copier
   ```

## Using Copier with the GitHub Repo

1. Open your terminal (Command Prompt on Windows, Terminal on MacOS/Linux).

2. Navigate into the directory where you want to create your new web experiment project and run the following command:

   ```sh
   copier github.com:gt-sse-center/AutoRA-experiment-server .
   ```
   
   Note: The dot (.) means "here in this folder". You can also replace the dot with a path to an existing folder, or the name you would like the new directory to have and it will be created.


4. Follow the [prompts](docs%questionnaire.md). Copier will generate the web experiment files based on our GitHub template.

### 3. Committing the Resulting Code to GitHub (optional but recommended)

#### If you have or want to use the GitHub Command-Line Interface (CLI):

##### Windows: Download and run the installer from the [GitHub CLI releases page](https://github.com/cli/cli/releases).

##### MacOS: Install using Homebrew:
      ```bash
      brew install gh
      ```
##### Linux: Follow the installation instructions for your specific distribution from [cli.github.com](https://cli.github.com/).
    
##### Open a terminal.
##### Authenticate with your GitHub account:
      ```bash
      gh auth login
      ```
##### Follow the prompts to log in via your web browser or enter a personal access token.
##### Navigate to your local code directory:
      ```bash
      cd /path/to/your/code
      ```
##### Initialize a Git repository:
      ```bash
      git init
      ```
##### Create a new GitHub repository using the GitHub CLI:
      ```bash
      gh repo create
      ```
##### Follow the interactive prompts. You can specify the repository name, description, visibility (public or private), and whether to add a README file.
    - Add all your files to the staging area:
      ```bash
      git add .
      ```
##### Commit the files:
      ```bash
      git commit -m "Initial commit"
      ```
##### Push your local repository to GitHub:
      ```bash
      git push -u origin HEAD
      ```

#### If you Prefer not to Configure the GitHub CLI:

- Create the repository in GitHub following [their instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository). 
- Take note of the URL of your new repository. It should look something like this: `https://github.com/yourusername/your-repo-name`
```sh
git init
git add .
git commit -m "Initial commit"
# note that .git has been appended to the repository URL below
git remote add origin https://github.com/yourusername/your-repo-name.git
git push -u origin main
```