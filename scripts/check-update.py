#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


example = sys.stdin.read()


def version_compare(versions: str):
    version_list = [i for i in versions.split()]
    current = version_list[0]
    latest = version_list[1]
    v1 = current.split(".")
    v2 = latest.split(".")
    v1_arr = [int(i) for i in v1]
    v2_arr = [int(i) for i in v2]
    if len(version_list) != 2:
        return f"Trouble getting current version, building version: {latest}"
    for i in range(len(v1_arr)):
        if v1_arr[i] < v2_arr[i]:
            return "True"
        else:
            return "False"


version_compare(example)
