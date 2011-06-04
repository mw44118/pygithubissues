# vim: set expandtab ts=4 sw=4 filetype=python:

"""
This will likely be rewritten into something with classes.
"""

import json
import logging
import subprocess

def setup_logging():

    log = logging.getLogger('pygithubissues')
    h = logging.StreamHandler()
    f = logging.Formatter("%(levelname)s %(asctime)s %(message)s")
    h.setFormatter(f)
    log.addHandler(h)

    return log

log = setup_logging()


def list_issues_for_repo(username, password, repo_owner, repo):

    """
    Does this::

        curl -u "username:password" \\
        https://api.github.com/repos/repo_owner/repo/issues

    """

    auth_option = '%s:%s' % (username, password)

    url = ('https://api.github.com/repos/%s/%s/issues'
        % (repo_owner, repo))

    args = ['curl', '-u', auth_option, url]

    p = subprocess.Popen(args, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    results = p.communicate()

    return json.loads(results[0])

def get_a_single_issue(username, password, repo_owner, repo, issue_id):

    """
    Does this::

        curl -u "username:password" \\
        https://api.github.com/repos/:repo_owner/:repo/issues/:issue_id

    """

    auth_option = '%s:%s' % (username, password)

    url = ('https://api.github.com/repos/%s/%s/issues/%s'
        % (repo_owner, repo, issue_id))

    args = ['curl', '-u', auth_option, url]

    p = subprocess.Popen(args, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    results = p.communicate()

    return json.loads(results[0])



def list_milestones_for_repo(username, password, repo_owner, repo):

    """
    Does this::

        curl -u "{username}:{password}" \\
        https://api.github.com/repos/{repo_owner}/{repo}/milestones

    """

    auth_option = '%s:%s' % (username, password)

    url = ('https://api.github.com/repos/%s/%s/milestones'
        % (repo_owner, repo))

    args = ['curl', '-u', auth_option, url]

    p = subprocess.Popen(args, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    results = p.communicate()

    return json.loads(results[0])


def list_issues_in_milestone(username, password, repo_owner, repo,
    milestone_number):

    """
    Does this::

        curl -u "username:password" \\
        https://api.github.com/repos/repo_owner/repo/issues \\
        ?milestone={milestone_number}

    """

    auth_option = '%s:%s' % (username, password)

    url = ('https://api.github.com/repos/%s/%s/issues?milestone=%s'
        % (repo_owner, repo, milestone_number))

    args = ['curl', '-u', auth_option, url]

    p = subprocess.Popen(args, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    results = p.communicate()

    return json.loads(results[0])
