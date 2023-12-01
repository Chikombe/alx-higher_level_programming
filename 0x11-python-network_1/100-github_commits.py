#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""

import requests
import sys

if __name__ == '__main__':

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for itr in range(10):
            print("{}: {}".format(
                commits[itr].get('sha'),
                commits[itr].get('commit').get('author').get('name')))
    except IndexError:
        pass
