import os
import subprocess
import getpass
from github import Github


subprocess.run("pip install PyGithub", shell=True)


# global project variables
localPath = "L:/Projects/"
projectName = input("Project name: ")
projectType = input("Project type: ")


# global GitHub credentials
repoName = ""
username = ""
password = ""


def GetProjectProcess(projectType):
    switcher = {
        'react': f"npx create-react-app {projectName}"
    }
    return switcher.get(projectType, "invalid")


def GetCredentials():  # gets user input to update GitHub credentials
    global repoName
    global username
    global password
    repoName = input("Enter new GitHub repository name: ")
    username = input("Enter your GitHub username: ")
    password = getpass.getpass("Enter your GitHub password: ")


while GetProjectProcess(projectType) == "invalid":
    print("Invalid project type, please try again.")
    projectType = input("Project type: ")


GetCredentials()
valid = False


while valid == False:  # creates repo if credentials are valid, requests user to re-enter if invalid
    try:
        user = Github(username, password).get_user()
        user.create_repo(repoName)
        valid = True
    except Exception as e:
        print(e)
        GetCredentials()


os.chdir(localPath)
subprocess.run(GetProjectProcess(projectType), shell=True)
os.chdir(projectName)


# git proccesses
subprocess.run("git init", shell=True)
subprocess.run("git add *", shell=True)
subprocess.run("git commit -m 'initial commit'", shell=True)
subprocess.run(
    f"git remote add origin https://github.com/{username}/{repoName}",
    shell=True)
subprocess.run("git push origin master", shell=True)
subprocess.run("code .", shell=True)
subprocess.run("npm start", shell=True)
