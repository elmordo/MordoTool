# -*- coding: utf8 -*-

import os
import sys


def run(**kwargs):
    project_name = kwargs["project"]
    action = kwargs["action"]
    base_path = os.getcwd()
    
    if project_name == "all":
        projects = discover_repos(base_path)
    else:
        projects = [ project_name ]

    if action == "add":
        git_fn = git_add
    else:
        git_fn = common_git_action

    for project in projects:
        # go to directory and run git action
        project_dir = "%s%s%s" % (base_path, os.sep, project)
        print project_dir
        goto_dir(project_dir)

        git_fn(project_name, action)

        # restore directory
        goto_dir(base_path)

def goto_dir(directory):
    os.chdir(directory)

def git_add(project_name, action):
    print "Adding all to %s" % project_name

    cmd = "git add ."
    os.system(cmd)

    print "Data added"

def common_git_action(project_name, action):
    print "Starting pull of %s" % project_name
    cmd = "git %s" % action
    os.system(cmd)
    print "Pull finished"

def discover_repos(dest_path):
    """ search for all git repositories in subdirs of dest_path

    Args:
        dest_path (str): path to search in

    Returns:
        list: set of all repositories
    """
    repos = list()
    subdirs = os.listdir(dest_path)

    for entry in subdirs:
        # assemble full path to repository
        repo_path = "%s%s%s%s.git" % (dest_path, os.sep, entry, os.sep)

        if os.path.isdir(repo_path):
            repos.append(entry)

    return repos

