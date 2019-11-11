#!/usr/bin/python

import glob
import json
import os
import re
import sys


def __tweak_seo_tag(html, jzon):
    pass


def main():
    # print command line arguments
    args = sys.argv[1:]
    publish_folder = args[0]
    seo_folder = f'{publish_folder}/bw-seo'
    files = [x for x in glob.glob(
        f'{seo_folder}/**', recursive=True) if os.path.isfile(x)]

    for seo_file in files:
        # print(f)
        content_file = seo_file.replace(
            seo_folder, publish_folder).replace('.seo', '.html')
        if not os.path.exists(content_file):
            print('NOT found > ' + content_file + ' <> ' + seo_file)
        else:
            print('Found  > ' + content_file + ' <> ' + seo_file)
        with open(seo_file, 'r') as jr:
            jzon = json.loads(jr.read())
            with open(content_file, 'w') as html_file:
                html = html_file.read()
                __tweak_seo_tag(html, jzon)
            # print(jzon)


if __name__ == "__main__":
    main()
