#!/bin/sh
# wait-for-mysql.sh

set -e

host="$1"
shift
cmd="$@"

#docker exec chatroom_db_1
until mysqladmin --user=root --password=1234 -h "$host" ping --silent; do
  >&2 echo "Mysql is unavailable - sleeping"
  sleep 1
done

>&2 echo "Mysql is up - executing command"
exec $cmd