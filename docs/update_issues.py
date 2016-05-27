#!/usr/bin/env python
# encoding: utf-8
from eight import input

from collections import namedtuple
from requests.auth import HTTPBasicAuth
import codecs
import json
import os
import requests
import sys
import uuid


HEADER = """.. _knownissues:

Known Issues
============

"""

ENHANCEMENTS = """Enhancements
````````````

"""

REPO = """{name}
{dashes}

`{name} <http://bitbucket.org/cmutel/{name}/issues/>`__

"""

ISSUES = """Issues
``````

"""

ISSUE = """* #{id} `{title} <{url}>`__\n"""


Issue = namedtuple('Issue', ['id', 'title', 'priority', 'url', 'kind'])


class NotFoundError(Exception):
    pass


def _(x):
    return x.replace("`", "\`")


ISSUES_KIND = {'task', 'bug'}
ENHANCEMENT_KIND = {'enhancement', 'proposal'}


def main():
    data = [
        (
            name,
            sorted(
                get_issues_for_repo(name),
                key=lambda x: x.url
            )
        )
        for name in get_repositories()
    ]

    with open("issues.rst", "w") as f:
        f.write(HEADER)

        for name, issues in sorted(data):
            if not issues:
                continue

            print('{}: {} issues'.format(name, len(issues)))

            iss = [x for x in issues if x.kind in ISSUES_KIND]
            enh = [x for x in issues if x.kind in ENHANCEMENT_KIND]

            f.write(REPO.format(name=name, dashes="-" * len(name)))

            if iss:
                f.write(ISSUES)
                for obj in iss:
                    f.write(ISSUE.format(
                        title=_(obj.title),
                        id=obj.id,
                        url=obj.url
                    ))
                f.write("\n")

            if enh:
                f.write(ENHANCEMENTS)
                for obj in enh:
                    f.write(ISSUE.format(
                        title=_(obj.title),
                        id=obj.id,
                        url=obj.url
                    ))
                f.write("\n")


def run_query(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if response.status_code == 404:  # not found
            raise NotFoundError(url)
        raise
    return response.json()


def get_repositories():
    url = "https://api.bitbucket.org/2.0/repositories/cmutel?pagelen=100"
    return [
        x['name']
        for x in run_query(url)['values']
        if 'brightway2' in x['name']
    ]


def get_issues_for_repo(name):
    url = "https://api.bitbucket.org/2.0/repositories/cmutel/{name}/issues?pagelen=100&q=%28state+%3D+%22new%22+OR+state+%3D+%22open%22%29"
    try:
        result = run_query(url.format(name=name))
    except NotFoundError as e:
        sys.stderr.write('{}\n'.format(repr(e)))
        return

    for issue in result['values']:
        yield Issue(
            id=issue['id'],
            title=issue['title'],
            priority=issue['priority'],
            url=issue['links']['self']['href'],
            kind=issue['kind'],
        )


if __name__ == '__main__':
    sys.exit(main())
