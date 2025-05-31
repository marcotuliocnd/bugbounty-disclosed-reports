# Incorrect logic in MySQL & MariaDB protocol leads to remote SSRF/Remote file read

## Report Details
- **Report ID**: 156511
- **URL**: https://hackerone.com/reports/156511
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-04T14:18:37.287Z
- **Disclosed**: 2019-11-12T23:49:32.705Z

## Reporter
- **Username**: squashbroom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Overview
Wrong logic in realization of LOAD DATA LOCAL INFILE function leads to remote attacker can read files from server. Problem exists in many MySQL-drivers and frameworks, on many programming languages, like Python, Java, PHP etc.

For exploitation this vulnerability we need to connect to our special MySQL server (A) from "attacking" remote server (B).
For example:
- I found phpMyAdmin interface with connect to any server ability (AllowArbitraryServer option in config) on server B.
- Next I'm run special-MySQL server on my A host.
- Then connect through phpMyAdmin to host A
- After successful connection I can see content of /etc/passwd file from host B in log file on host A

## Details
For testing purposes take latest MySQL server, client and tcpdump
- Start server on local machine
- Run tcpdump
- Connect to local MySQL through native mysql-console client
- Run LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn FIELDS TERMINATED BY '\n'
- Bye

Look inside packet dump file for LOCAL DATA INFILE query works:
- Client connect initialize.
- Server answers with greeting packet (protocol thread id, version, type of mysql authentication etc.)
- Next authentication packet (username, password, dbs)
- Next packet from client with query LOAD DATA LOCAL INFILE...
- Now here is strange packet from server. Call it `FB`-packet: `0c 00 00 01 fb 2f 65 74 63 2f 70 61 73 73 77 64`

`0c` - size
`000001` - packet No
`fb` - packet type
`2f6574632f706173737764` - filename (/etc/passwd)

There is problem looks like: server says to client what file he needs to read.
We need to create special MySQL server which do authorization with any data and then send FB packet with remote filename as payload. That's it.

In attach image successfully exploitation another MySQL administration interface - Adminer

Exploit: https://github.com/allyshka/Rogue-MySql-Server/blob/master/rogue_mysql_server.py
See also: http://russiansecurity.expert/2016/04/20/mysql-connect-file-read/


## Attachments
- adminerread.jpg
