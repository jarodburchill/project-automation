import sys
import getpass
from git import Repo
from github import Github


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


# sets local repo remote origin to the GitHub repo URL
path = sys.argv[1]
projectName = sys.argv[2]
repo = Repo(path + projectName)
repo.create_remote('origin', url=f"https://github.com/{username}/{repoName}")
