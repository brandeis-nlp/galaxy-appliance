# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
import os
import shutil

if __name__ == '__main__':

    ofile_name = 'outputs'
    temp_ofile_name = 'temp_outputs'
    corpus_path = "/var/corpora/htrc-samples-annotated"


    if not os.path.isdir(ofile_name):
        os.makedirs(ofile_name)
    for line in argv[1].split('__cn__'):
        for filename in os.listdir(os.path.join(corpus_path, line)):
            shutil.copy(os.path.join(corpus_path, line, filename),
                        os.path.join(ofile_name, "{}__{}".format(line, filename)))
