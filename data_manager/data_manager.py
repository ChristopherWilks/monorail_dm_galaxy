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
parser.add_argument('--config', dest='config', action='store', help='JSON filename')
#parser.add_argument('--name', dest='name', action='store', default=None, help='Data table entry unique ID')
parser.add_argument('--url', dest='url', action='store', help='Monorail Indexes Base URL', default="http://snaptron.cs.jhu.edu/data/monorail/1.0.0/ath10")
parser.add_argument('--subdir', dest='subdir', action='store', help='subdirectory where the indexes are temporarily downloaded to')
#parser.add_argument('--version', dest='version', action='store', help='Version of Monorail as a whole (not a particular index/program)')

args = parser.parse_args()

def main(args):
    workdir = os.path.join(os.getcwd(), 'monorail_index')
    data_manager_entry = {}
    #URL syntax assumes that the last two components of the URL are: <version>/<ref>
    #e.g. 1.0.0/ath10
    url_comps = args.url.split('/')
    ref = url_comps[-1]
    version = url_comps[-2]
    data_manager_entry['dbkey'] = ref.lower()
    data_manager_entry['value'] = ref.lower()
    data_manager_entry['name'] = ref.lower()
    jsonin = open(args.config).read()
    params = json.loads(jsonin)
    #target_directory = params['output_data'][0]['extra_files_path']
    #data_manager_entry['path'] = params['output_data'][0]['extra_files_path']
    data_manager_entry['path'] = args.subdir
    data_manager_entry['exons_path'] = args.subdir
    data_manager_entry['version'] = version
    #data_manager_entry['exons_path'] = data_manager_entry['path'] + os.sep + 'gtf' + os.sep + 'exons.bed'
    data_manager_json = {'data_tables':{'monorail_index': [data_manager_entry]}}
    file(args.config, 'w').write(json.dumps(data_manager_json))

if __name__ == '__main__':
    main(args)
