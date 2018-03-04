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
    concat = len(argv) == 3 and argv[2] == '-c'

    ids = []
    for line_num, line in enumerate(argv[1].split('__cn__')):
        if line_num == 0:
            query_by_pages = "/" in line
        ids.append(process_input_line(line, query_by_pages))

    if not query_by_pages:
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
