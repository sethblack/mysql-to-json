#!/usr/bin/env python3

import argparse
import json
import MySQLdb

def main():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-d', '--database', help='MySQL database name.', default='mysql')
    arg_parser.add_argument('-H', '--hostname', help='MySQL host name.', default='localhost')
    arg_parser.add_argument('-P', '--port', help='MySQL port number.', default='3306')
    arg_parser.add_argument('-u', '--user', help='MySQL username.', default='root')
    arg_parser.add_argument('-p', '--password', help='Shh! It\'s a secret.', default='')
    arg_parser.add_argument('-e', '--query', help='Query to run.')
    arg_parser.add_argument('-o', '--outfile', help='Output file name.')

    args = arg_parser.parse_args()

    #if args.output_format == 'html':

    conn = MySQLdb.connect(host='localhost', user='root', passwd='')

    cursor = conn.cursor()

    cursor.execute("SHOW GLOBAL STATUS")

    rs = cursor.fetchall()

    result = dict(rs)

    with open('result.json', 'w') as f:
        json.dump(result, f)

if __name__ == "__main__":
    main()
