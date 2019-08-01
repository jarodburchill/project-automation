import sys
import subprocess
import getpass
from git import Repo
from github import Github

subprocess.run("pip install -r Requirements.txt", shell=True)

# global project variables
localPath = "L:/Projects/"
projectName = input("Project name: ")


# global GitHub credentials
repoName = ""
username = ""
password = ""


def get_credentials():  # gets user input to update GitHub credentials
    global repoName
    global username
    global password
    repoName = input("Enter new GitHub repository name: ")
    username = input("Enter your GitHub username: ")
    password = getpass.getpass("Enter your GitHub password: ")


get_credentials()
valid = False


while valid == False:  # creates repo if credentials are valid, requests user to re-enter if invalid
    try:
        user = Github(username, password).get_user()
        user.create_repo(repoName)
        valid = True
    except Exception as e:
        print(e)
        get_credentials()


subprocess.run(f"cd /D {localPath}", shell=True)
#subprocess.run(f"npx create-react-app {projectName}", shell=True)
subprocess.run(f"mkdir {projectName}", shell=True)
subprocess.run(f"cd {projectName}", shell=True)
subprocess.run("git init", shell=True)


# sets local repo remote origin to the GitHub repo URL
# repo = Repo(localPath + projectName)
# repo.create_remote('origin', url=f"https://github.com/{username}/{repoName}")


subprocess.run("git add *", shell=True)
subprocess.run("git commit - m 'initial commit'", shell=True)
subprocess.run(
    f"git add remote origin https://github.com/{username}/{repoName}",
    shell=True)
subprocess.run("git push origin master", shell=True)
