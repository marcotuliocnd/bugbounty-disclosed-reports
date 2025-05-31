# Bypassing Digits origin validation which leads to account takeover

## Report Details
- **Report ID**: 129873
- **URL**: https://hackerone.com/reports/129873
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-11T17:02:26.419Z
- **Disclosed**: 2020-06-24T17:55:18.018Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an important issue that affects websites that has integrated "Signin with Digits" , leading to potential account takeover.

#Detail
In Digits architecture, the data communication channel between Digits and customer's site relies on *postMessage()*. In order to prevent malicious websites prevent themselves to be the legit Digits website and send arbitrary commands to the customer's websites, an origin validation is in place in the SDK. Specifically, the code that's responsible to perform the validation is as follow:

**File: https://cdn.digits.com/1/sdk.js**
```javascript
e.exports = {
    sdk_host: "https://www.digits.com",
[..]
onReceiveMessage: function(t) {
    this.config && -1 !== this.config.get("sdk_host").search(t.origin) && this.resolve(t.data)
},
```
In short, the event origin is checked against Digits' origin in this line:`-1 !== this.config.get("sdk_host").search(t.origin)`, which is the same as `-1 !== "https://www.digits.com".search(t.origin)`. In essence, it looks for the occurrence of Digit's origin from sender's origin.

The way the validation is done is however flawed. According to the [docs of String.prototype.search()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search), the method takes a regular repression object instead of a string. If anything other than regexp is passed, it will get implicitly converted into a regexp. In this case, `t.origin` which is a string is converted into a regexp.

In regular expression, a dot (.) is treated as a wildcard. In other words, any character of Digits' origin can be replaced with a dot. An attacker can take advantage of it and use a special domain instead of the official one to bypass the validation, such as `www.d.gits.co`

An example of comparing such a special domain looks like this: 
`www.d.gits.co`
`www.digits.com`
Notice that `www.d.gits.co` is now a subset of `www.digits.com`, thus it effective bypasses the validation.

#Impact
It affects websites that have integrated Digits signin feature, leading to potential account takeover issue on those websites. Twitter official applications like Fabric is also affected.

#PoC
To provide a concrete example of how this vulnerability can lead to account takeover, a Proof of Concept against Fabric is presented.

1. Make sure you have logged in Fabric.io
2. Go to https://www.d.gits.co/fabric.html
3. Click the button
4. You will see a phone number is automatically associated with your account
5. Now, attacker can use the reset password with Digits feature to takeover the account

Notice the attack can be done silently without user interaction and awareness.

A video demo: https://vimeo.com/162397716 (password: origin)

#Fix
In my opinion, a simple string comparison is enough for validation. Therefore I recommend changing it to use either `indexOf` or `===`.

## Attachments
No attachments
