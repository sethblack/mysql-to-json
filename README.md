# mysql-to-json

Connects to a MySQL database and exports selected data to JSON.

## Installation

```
$> pip3 install mysql-to-json
```

## Usage
```
mysql-to-json [-h] [-d DATABASE] [-H HOSTNAME] [-P PORT] [-u USER] [-p]
                     [-e QUERY]

optional arguments:
  -h, --help            show this help message and exit
  -d DATABASE, --database DATABASE
                        MySQL database name.
  -H HOSTNAME, --hostname HOSTNAME
                        MySQL host name.
  -P PORT, --port PORT  MySQL port number.
  -u USER, --user USER  MySQL username.
  -p, --password        Shh! It's a secret.
  -e QUERY, --query QUERY
                        Query to run.
```

## Examples

All examples simple select all table information from `information_schema` and save it to `tables.json`

### Simple

This assumes we have full access to the mysql database from localhost.

```
$> mysql-to-json -e 'SELECT * FROM information_schema.tables' > tables.json
```

### Medium Complexity

This explicitly sets a user and asks for a password, while still connecting to localhost.

```
$> mysql-to-json -d mysql -u seth -p -e 'SELECT * FROM information_schema.tables' > tables.json
```

### All The Things!

This explicitly sets every command line option available.

```
$> mysql-to-json -h mydbserver.myhost.com -P 3306 -d mysql -u seth -p -e 'SELECT * FROM information_schema.tables' > tables.json
```
