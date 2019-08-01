import sys
import getpass
from github import Github

repoName = ""
username = ""
password = ""


def get_credentials():
    global repoName
    global username
    global password
    repoName = input("Enter new GitHub repository name: ")
    username = input("Enter your GitHub username: ")
    password = getpass.getpass("Enter your GitHub password: ")


get_credentials()
valid = False

while valid == False:
    try:
        user = Github(username, password).get_user()
        user.create_repo(repoName)
        valid = True
    except Exception as e:
        print(e)
        get_credentials()
