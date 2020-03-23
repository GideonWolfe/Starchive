from github import Github
from gitlab import Gitlab
import git

# user: username on gitlab/hub | token: personal access token


def get_github_repos(user,token):
    gh = Github(token)
    repos = []

    for repo in gh.get_user().get_starred():
        repos.append(repo.clone_url) 

    return repos

def get_gitlab_repos(user,token):
    gl = Gitlab('https://gitlab.com', private_token=token)
    repos = []

    for repo in gl.projects.list(starred=True):
        print(repo.web_url)
    
    return repos

def clone_repos(repos, repo_dir):
    for r in repos:
        print(r)
        git.Git(repo_dir).clone(r)