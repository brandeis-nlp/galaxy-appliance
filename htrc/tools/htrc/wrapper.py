#!/usr/bin/env python
from __future__ import absolute_import, division, print_function

from sys import argv
import os

# -*- coding: utf-8 -*-

"""
This program is to:

"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')

__author__ = 'krim'
__date__ = '3/29/17'
__email__ = 'krim@brandeis.edu'

import htrc.tools.topicexplorer
from argparse import Namespace
import shutil


if __name__ == '__main__':

    ifile_name = 'input'
    ofile_name = 'outputs'
    temp_ofile_name = 'temp_outputs'

    with open(ifile_name, 'w') as f:
        for line in argv[1].split('__cn__'):
            f.write(line + '\n') 
    htrc.volumes.download(Namespace(
        func='download',
        file=ifile_name,
        output=temp_ofile_name,
        username=None,
        password=None
    ))

    os.makedirs(ofile_name)
    for volume in os.listdir(temp_ofile_name):
        vol_path = os.path.join(temp_ofile_name, volume)
        for page in os.listdir(vol_path):
            page_path = os.path.join(vol_path, page)
            shutil.move(page_path, 
                    os.path.join(ofile_name, "{}__{}".format(volume, page)))
    shutil.rmtree(temp_ofile_name)
    os.remove(ifile_name)
