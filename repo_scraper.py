import re
import os
import git
from github import Github
from gitlab import Gitlab


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
        try:
            git.Git(repo_dir).clone(r)
        except:
            gr = git.Git(r)

            basename = os.path.basename(gr.working_dir)
            repo_name = re.sub(r'.git', "", basename)

            pull_repo = git.Repo(repo_dir + "/" + repo_name)
            o = pull_repo.remotes.origin
            o.pull()


