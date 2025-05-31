# Trojan:JS/CoinMiner in npm files

## Report Details
- **Report ID**: 687325
- **URL**: https://hackerone.com/reports/687325
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-03T22:19:03.200Z
- **Disclosed**: 2019-10-04T20:08:53.273Z

## Reporter
- **Username**: mada_uk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hello,

I am a front end developer and use Vue.js and Visual Studio Code and have had an issue recently with scripts not running in my terminal so decided to fault find.

All programmes that I can think of are up to date, and today I decided to do a full windows defender scan and found the above file.

I cannot say how to reproduce it as I'm not sure how I got it in the first place.

These are my global packages:

`PS C:\web-dev\adp-run> npm list -g --depth 0
C:\Users\mada7\AppData\Roaming\npm
+-- @vue/cli@3.11.0
+-- @vue/cli-upgrade@3.9.0
+-- core-js@3.2.1
+-- eslint@5.7.0
+-- firebase-tools@7.3.0
+-- git@0.1.5
+-- json-server@0.15.0
+-- netlify-cli@2.12.0
+-- npm@6.11.2
`-- serve@10.1.1`

I’ve done some research and cant find what npm package the file came from (if any) so was wondering if :

I) This file is from a compromised npm package I’ve used?
II) This file is from node.js? I’ve done a fresh install of node within the last 7 days
III) Whether I’m one of many infected with this malware, I am not aware of using the event-stream package that was infected previously

Thanks for any help, Windows Defender tells me the threat is blocked.


Adam

## Impact

This threat can perform a number of actions of a malicious hacker's choice

## Attachments
- miner.PNG
