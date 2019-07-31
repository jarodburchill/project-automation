import sys
from github import Github

username = sys.argv[1]
password = sys.argv[2]

user = Github(username, password).get_user()
user.create_repo(sys.argv[3])
