#!/usr/bin/env python
# encoding: utf-8
from collections import namedtuple
from requests.auth import HTTPBasicAuth
import codecs
import json
import os
import requests
import sys

USERNAME = "cmutel"
PASSWORD = os.environ['BITBUCKET_PASSWORD']

HEADER = """Known Issues
============

"""
REPO = """{slug}
{dashes}

`{owner}/{slug} <http://bitbucket.org/{owner}/{slug}/issues/>`__

"""
ISSUE = """* #{id} `{title} <{url}>`__\n"""


Issue = namedtuple('Issue', ['id', 'title', 'priority', 'url'])


def _(x):
    return x.replace("`", "\`")


class NotFoundError(Exception):
    pass


class Query(object):
    REPOSITORY = 0
    ISSUES = 1


URLS = {
    Query.REPOSITORY: 'https://bitbucket.org/api/1.0/user/repositories/',
    Query.ISSUES:     ('https://bitbucket.org/api/1.0/repositories/'
                       '{owner}/{slug}/issues/?status=new&status=open'),
}


def main():
    with open("issues.rst", "w") as f:
        f.write(HEADER)
        for repo in run_query(Query.REPOSITORY):
            owner, slug = repo['owner'], repo['slug']

            if not "brightway2" in slug or slug in ("pandarus",):
                continue

            issues = list(get_issues_for_repo(owner, slug))
            sys.stdout.write('{}/{}: {} issues\n'.format(owner, slug, len(issues)))
            if issues:
                f.write(REPO.format(owner=_(owner), slug=_(slug), dashes="-" * len(slug)))
                for issue in get_issues_for_repo(owner, slug):
                    f.write(ISSUE.format(title=_(issue.title), id=issue.id,
                            url=_(issue.url)))
            f.write("\n")

def run_query(query, **args):
    url = URLS[query]
    url = url.format(**args)
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if response.status_code == 404:  # not found
            raise NotFoundError(url)
        raise
    return response.json()


def get_issues_for_repo(owner, slug):
    try:
        result = run_query(Query.ISSUES, owner=owner, slug=slug)
    except NotFoundError as e:
        sys.stderr.write('{}\n'.format(repr(e)))
        return

    for issue in result['issues']:
        if issue['status'] == 'resolved':
            continue
        yield Issue(
            id=issue['local_id'],
            title=issue['title'],
            priority=issue['priority'],
            url=make_issue_url(owner, slug, issue['local_id']))


def make_issue_url(owner, slug, issue_id):
    return 'https://bitbucket.org/{}/{}/issue/{}'.format(
        owner, slug, issue_id)


if __name__ == '__main__':
    if not PASSWORD:
        raise ValueError("Specify bitbucket password")
    sys.exit(main())
