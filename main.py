#!/usr/bin/python

import glob
import json
import os
import re
import sys


def __get_seo_tags(jzon):
    seoTags = [
        {
            'name': 'generator',
            'mode': 'delete',
            're': re.compile('<meta name="?generator"?\s*.*?>', flags=re.IGNORECASE),
            'replace': ''
        },
        {
            'name': 'viewport',
            'mode': 'upsert',
            're': re.compile('<meta name="?viewport"?\s*.*?>', flags=re.IGNORECASE),
            'replace': '<meta name=viewport content="width=device-width,initial-scale=1">'
        },

        {
            'name': 'canonical',
            'mode': 'upsert',
            're': re.compile('<link rel="?canonical"?\s*.*?>', flags=re.IGNORECASE),
            'replace': f'<link rel=canonical href={jzon["data"]["permalink"]} >'
        },
        {
            'name': 'title',
            'mode': 'upsert',
            're': re.compile('<title>.*?</title>', flags=re.IGNORECASE | re.DOTALL),
            'replace': f'<title>{jzon["data"]["pagetitle"] if jzon["data"]["pagetitle"] is not None and jzon["data"]["pagetitle"] != "" else jzon["data"]["title"]  }</title>'
        },
        {
            'name': 'description',
            'mode': 'upsert',
            're': re.compile('<meta name="?description"?\s*.*?>', flags=re.IGNORECASE),
            'replace': f'<meta name=description content="{jzon["data"]["summary"]}">'
        },
        {
            'name': 'robots',
            'mode': 'upsert',
            're': re.compile('<meta name="?ROBOTS"?\s*.*?>', flags=re.IGNORECASE),
            'replace': f'<meta name=robots content="index, follow">'
        },
        {
            'name': 'googlebot',
            'mode': 'upsert',
            're': re.compile('<meta name="?GOOGLEBOT"?\s*.*?>', flags=re.IGNORECASE),
            'replace': f'<meta name=googlebot content="noarchive">'
        },

    ]
    return seoTags


def __update_html_with(html, tag):
    html = re.sub(tag['re'], '', html)
    if tag['mode'] == 'upsert':
        html = re.sub(r'<head>', '<head>' + tag['replace'], html)
    return html


def __write_seo_tags(html, jzon):
    tags = __get_seo_tags(jzon)
    for tag in tags:
        html = __update_html_with(html, tag)
    return html


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
                html = ''

                with open(content_file, 'r+') as html_file:
                    html = html_file.read()
                    html = __write_seo_tags(html, jzon)

                with open(content_file, 'w') as output:
                    output.write(html)


if __name__ == "__main__":
    main()
