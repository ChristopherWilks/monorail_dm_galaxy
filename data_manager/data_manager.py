#based off of "Gene Annotation Fetcher" https://testtoolshed.g2.bx.psu.edu/repository?repository_id=c0f5466df187cc04&changeset_revision=444300ec9185
import argparse
import datetime
import json
import os
import shutil
import sys
import tarfile
import urllib2
import zipfile

parser = argparse.ArgumentParser(description='Create data manager json.')
parser.add_argument('--out', dest='output', action='store', help='JSON filename')
parser.add_argument('--name', dest='name', action='store', default=None, help='Data table entry unique ID')
parser.add_argument('--url', dest='url', action='store', help='Monorail Indexes Base URL', default="http://snaptron.cs.jhu.edu/data/monorail/ath10")

args = parser.parse_args()

def main(args):
    workdir = os.path.join(os.getcwd(), 'monorail_index')
    data_manager_entry = {}
    ref = args.url.split('/')[-1]
    if args.name is None:
        args.name = ref
    data_manager_entry['value'] = args.name.lower()
    data_manager_entry['name'] = args.name
    jsonin = open(args.output).read()
    sys.stderr.write(jsonin)
    params = json.loads(jsonin)
    target_directory = params['output_data'][0]['extra_files_path']
    data_manager_entry['path'] = params['output_data'][0]['extra_files_path']
    data_manager_entry['exons_path'] = data_manager_entry['path'] + os.sep + ref + os.sep + 'gtf' + os.sep + 'exons.bed'
    data_manager_json = dict(data_tables=dict(monorail_index=data_manager_entry))
    file(args.output, 'w').write(json.dumps(data_manager_json))

if __name__ == '__main__':
    main(args)
