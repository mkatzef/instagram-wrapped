#!/usr/bin/python2
from __future__ import print_function
import re

following_filename = "following.html"
follower_filename = "followers.html"


def get_usernames(page_text):
    user_list = page_text.split('role=\"presentation">')[-1]
    usernames = re.findall('href="https://www.instagram.com/([a-zA-Z0-9_\-\.]+)/"', user_list)
    return set(usernames)


def get_usernames_from_file(filename):
    with open(filename, "r") as f:
        return get_usernames(f.read())


if __name__ == "__main__":
    following_set = get_usernames_from_file(following_filename)
    follower_set = get_usernames_from_file(follower_filename)
    print("People not following you:\n" + "\n".join(sorted(list(following_set - follower_set))))
