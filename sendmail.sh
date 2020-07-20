#!/bin/sh
message=$(echo -e $1 | tr "\r\n" "\n")
subject=$(echo -e $2 | tr "\r\n" "\n")
sendto=
echo "$message" | /usr/bin/mail -s "$subject" $3
