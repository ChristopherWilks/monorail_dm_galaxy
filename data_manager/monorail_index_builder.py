#!/usr/bin/env python

import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--config-file' )
    parser.add_argument( '--value' )
    parser.add_argument( '--dbkey' )
    parser.add_argument( '--name' )
    parser.add_argument( '--subdir' )
    parser.add_argument( '--data-table' )
    parser.add_argument( '--index-version' )

    args = parser.parse_args()

    if args.dbkey in [ None, '', '?' ]:
        raise Exception(
            '"%s" is not a valid dbkey. You must specify a valid dbkey.'
            % ( args.dbkey )
        )

    data_manager_dict = {
        'data_tables': {
            args.data_table: [
                {
                    "value": args.value,
                    "dbkey": args.dbkey,
                    "name": args.name,
                    "path": args.subdir,
                    "version": args.index_version
                }
            ]
        }
    }
    open( args.config_file, 'w' ).write( json.dumps( data_manager_dict ) )


if __name__ == "__main__":
    main()