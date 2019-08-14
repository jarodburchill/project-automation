import os
import subprocess


# global variables
projectName = ""
repoName = ""


# gets variables from main script
def Init(project, repo):
    global projectName
    global repoName
    projectName = project
    repoName = repo


# proccess for blank projects
def Blank():
    os.mkdir(projectName)
    os.chdir(projectName)
    subprocess.check_call(f"echo {repoName} >> README.md", shell=True)


# process for react projects
def React():
    subprocess.check_call(
        f"npx create-react-app {projectName}", shell=True)
    os.chdir(projectName)


# process for react typescript projects
def ReactTS():
    subprocess.check_call(
        f"npx create-react-app {projectName} --typescript", shell=True)
    os.chdir(projectName)


# process for nodejs projects
def Node():
    Blank()
    subprocess.check_call("npm init", shell=True)


# process for expressjs projects
def Express():
    Node()
    subprocess.check_call("npm install express --save", shell=True)


# process for laravel projects
def Laravel():
    subprocess.check_call(f"laravel new {projectName}", shell=True)
    os.chdir(projectName)


# project types dict with values for correct process function
types = {
    'blank': Blank,
    'react': React,
    'react-ts': ReactTS,
    'node': Node,
    'express': Express,
    'laravel': Laravel
}
