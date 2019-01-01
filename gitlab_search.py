#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""project-toolkit -- gitlab project search toolkit

Usage:
  ptk_search <keyword> [-n NAMESPACE]
  ptk_search --version

Options:
  -n --namespace=NAMESPACE     target reference.
  -h --help                    Show this screen.
  --version                    Show version.
"""
import re

import gitlab
from docopt import docopt
from termcolor import colored

import gitlab_auth
import ptk_config


def main():
    args = docopt(__doc__, version='v1.0.0')

    config = ptk_config.get_config()

    gitlab_url = config['gitlab']['address']
    access_token = gitlab_auth.init_token(gitlab_url)
    gl = gitlab.Gitlab(gitlab_url, access_token, api_version=4)

    namespace = args['--namespace']
    keyword = args['<keyword>']

    projects = gl.projects.list(all=True)

    for project in projects:
        if namespace and not match_namespace(namespace, project.namespace):
            continue
        search_results = project.search('blobs', keyword)
        if len(search_results) > 0:
            title = "======== '{0}' found:{1} =========".format(project.path_with_namespace,
                                                                 len(search_results))
            print_title(title)
            for sr in search_results:
                sub_title = "------ '{0}' line:{1} ------".format(sr['filename'], sr['startline'])
                print_sub_title(sub_title)
                print_code_snippet(sr['data'], keyword)


def match_namespace(target, gl_namespace):
    return target in (gl_namespace['name'], gl_namespace['full_path'], gl_namespace['path'])


def print_title(title):
    print('\n\n')
    print((colored(title, 'cyan', attrs=['bold'])))
    print('\n')


def print_sub_title(sub_title):
    print((colored(sub_title, 'yellow')))


def print_code_snippet(snippet, keyword):
    assert isinstance(snippet, str)
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    print(pattern.sub(lambda m: colored(m.group(0), 'magenta', attrs=['underline']), snippet))


def find(items, filter_func):
    assert isinstance(items, list)
    for items in items:
        if filter_func(items):
            return items
    return None


if __name__ == '__main__':
    main()
