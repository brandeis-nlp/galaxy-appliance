#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program is to:
wraps around python wrapper that wraps around HTRC data API as a Galaxy tool
"""

from sys import argv
import os
from htrc import volumes
import shutil
import re

def parse_pages(pages_string):
    page_ids = []
    for ran in [ran for ran in re.split(r",\s+", pages_string)]:
        if "-" in ran:
            page_ids.extend([str(x) for x in range(int(ran.split("-")[0]),
                                                   int(ran.split("-")[1]) + 1)])
        else:
            page_ids.append(ran)

    return ",".join(page_ids)

def is_query_mixed(query):
    return "#" in query

def process_input_line(line, expecting_mixed_form_query):
    if expecting_mixed_form_query:
        if not is_query_mixed(line):
            raise IOError("INPUT error: " +
                          "Cannot retrieve data with a mixed form of query.")
        vol_id, pages = line.split("/")
        page_ids = parse_pages(pages)
        return "{}[{}]".format(vol_id, page_ids)
    else:
        if is_query_mixed(line):
            raise IOError("INPUT error: " +
                          "Cannot retrieve data with a mixed form of query.")
        return line

if __name__ == '__main__':

    ofile_name = 'outputs'
    temp_ofile_name = 'temp_outputs'
    concat = len(argv) == 3 and argv[2] == '-c'

    ids = []
    for line_num, line in enumerate(argv[1].split('__cn__')):
        line = line.replace(':', '+').replace('/', '=')
        if line_num == 0:
            mixed = is_query_mixed(line)
        ids.append(process_input_line(line, mixed))

    if not mixed:
        volumes.download_volumes(ids, temp_ofile_name, concat=concat)
    else:
        volumes.download_pages(ids, temp_ofile_name, concat=concat)

    os.makedirs(ofile_name)
    for volume in os.listdir(temp_ofile_name):
        if not concat:
            vol_path = os.path.join(temp_ofile_name, volume)
            for page in os.listdir(vol_path):
                page_path = os.path.join(vol_path, page)
                shutil.move(page_path,
                            os.path.join(ofile_name, "{}__{}".format(volume, page)))
        else:
            shutil.move(os.path.join(temp_ofile_name, volume), 
                    os.path.join(ofile_name, volume))
    shutil.rmtree(temp_ofile_name)
