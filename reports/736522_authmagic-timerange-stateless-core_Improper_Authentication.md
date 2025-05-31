# [authmagic-timerange-stateless-core] Improper Authentication

## Report Details
- **Report ID**: 736522
- **URL**: https://hackerone.com/reports/736522
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-13T02:12:02.597Z
- **Disclosed**: 2020-09-16T05:07:49.580Z

## Reporter
- **Username**: ermilov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Improper Authentication in `authmagic-timerange-stateless-core`
It allows to forge user's identity.

# Module

**module name:** authmagic-timerange-stateless-core
**version:** 0.0.9
**npm page:** `https://www.npmjs.com/package/authmagic-timerange-stateless-core`

## Module Description

Stateless and passwordless authentication core for authmagic (https://github.com/authmagic/authmagic).

## Module Stats

[20] weekly downloads

# Vulnerability

## Vulnerability Description

`authmagic-timerange-stateless-core` is an npm module that runs an API for stateless and passwordless authentication by utilizing JWT tokens. The module is also one of the core dependencies of `authmagic` which is an authorization service.
The module defined to handle authentication but does not validate the JWT token sent by the user when reissuing a new token (POST request to `/token` endpoint). Therefore it allows modifying payload within the token and also reissuing new token which will be signed by the system and become valid. This weakness provides an opportunity to forge the user's identity by changing the information inside the token's payload that is used to authenticate the client.

## Steps To Reproduce:

source code example:

https://github.com/authmagic/authmagic-timerange-stateless-core/blob/master/core.js#L11

```javascript
const checkRefreshToken = (token, refreshToken, key) => {
  try {
    if(jwt.verify(refreshToken, key)) {
      return jwt.decode(token, {complete: true}).signature === jwt.decode(refreshToken).signature;
    }
  } catch(e) {
    return false;
  }

  return false;
};
```
while comparing signatures in `token` and `refreshToken` only the `refreshToken` is verified, the `token` itself has to include the same sign like the one stored in `refreshToken`'s payload but the validity of the `token` is not checked.

the `authmagic-timerange-stateless-core` is utilized by `Authmagic` (https://github.com/authmagic/authmagic) so it is handy to use `Authmagic example app` (https://github.com/authmagic/authmagic-getting-started-example) for testing, as it demonstrates the behaviour of the module in a situation that is near to production.

* create directory for testing
```bash
mkdir poc
cd poc/
```

* install and run authmagic example app
```bash
npm install -g authmagic-cli
npm init -y
authmagic init -e
authmagic install
authmagic
```

```
Note: make sure name in your package.json is not named as authmagic if you do not want to get an error npm refusing to install as a dependency of itself.
```

* go to http://localhost:3000
F632927

* enter email and click `Send authorization link`
* follow `Preview url` form the console (similar to one on screenshot)
F632928

* follow `Click here`
F632929
```
Note: next I provide steps to intercept and change jwt token with BurpSuite and its JSON Web Tokens (JWT4B) plugin, as it is the easiest and quick way if more detailed explanation required let me know.
```

* click 'Refresh token' and intercept its request
F632930
F632931

* change payload parameter `u` inside `token` (e.g with `JSON Web Tokens (JWT4B)` plugin)
F632932
F632933
* different email will be displayed
F632934

While testing you can put a breakpoint in `poc/node_modules/authmagic-timerange-stateless-core/core.js` file to line 10:
```
const checkRefreshToken = (token, refreshToken, key) => {
  try {
    if(jwt.verify(refreshToken, key)) {
...
```

or add a console.log after it like to this 
```javascript
console.log(jwt.decode(token, {complete: true}), jwt.decode(refreshToken));
```
to make sure that it is the `authmagic-timerange-stateless-core` responsible for handling token verification

## Patch

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Linux Mint current
- NODEJS VERSION: 12.7.0
- NPM VERSION: 6.10.0

# Wrap up

- I contacted the maintainer to let them know: [N]
- I opened an issue in the related repository: [N]

## Impact

This weakness provides opportunity to forge user's identity by changing information inside token's payload that is used to verify the client.

## Attachments
- ______________2019-11-08_09-30-14.png
- ______________2019-11-08_09-31-02.png
- ______________2019-11-08_09-31-34.png
- ______________2019-11-08_09-31-49.png
- ______________2019-11-08_09-32-33.png
- ______________2019-11-08_09-32-57.png
- ______________2019-11-08_09-33-15.png
- ______________2019-11-08_09-33-32.png
