#! /usr/bin/env python3
from __future__ import absolute_import, division, print_function

from sys import argv

import os

# -*- coding: utf-8 -*-

"""
This program is to:
wraps around python wrapper that wraps around HTRC data API as a Galaxy tool
"""
import sys
from htrc import volumes
import shutil
import re

reload(sys)
sys.setdefaultencoding('utf8')

__author__ = 'krim'
__date__ = '3/29/17'
__email__ = 'krim@brandeis.edu'


def parse_pages(pages_string):
    page_ids = []
    for ran in [ran for ran in re.split(r",\s+", pages_string)]:
        if "-" in ran:
            page_ids.extend([str(x) for x in range(int(ran.split("-")[0]),
                                                   int(ran.split("-")[1]) + 1)])
        else:
            page_ids.append(ran)

    return ",".join(page_ids)


def process_input_line(line, volume_id_only):
    if volume_id_only:
        if "/" not in line:
            raise IOError("INPUT error: " +
                          "Cannot retrieve data with a mixed form of query.")
        vol_id, pages = line.split("/")
        page_ids = parse_pages(pages)
        return "{}[{}]".format(vol_id, page_ids)
    else:
        if "/" in line:
            raise IOError("INPUT error: " +
                          "Cannot retrieve data with a mixed form of query.")
        return line

if __name__ == '__main__':

    ofile_name = 'outputs'
    temp_ofile_name = 'temp_outputs'

    ids = []
    for line_num, line in enumerate(argv[1].split('__cn__')):
        if line_num == 0:
            query_by_pages = "/" in line
        ids.append(process_input_line(line, query_by_pages))

    if not query_by_pages:
        volumes.download_volumes(ids, temp_ofile_name)
    else:
        volumes.download_pages(ids, temp_ofile_name)

    os.makedirs(ofile_name)
    for volume in os.listdir(temp_ofile_name):
        vol_path = os.path.join(temp_ofile_name, volume)
        for page in os.listdir(vol_path):
            page_path = os.path.join(vol_path, page)
            shutil.move(page_path,
                        os.path.join(ofile_name, "{}__{}".format(volume, page)))
    shutil.rmtree(temp_ofile_name)
