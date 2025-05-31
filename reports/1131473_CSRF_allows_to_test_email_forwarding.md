# CSRF allows to test email forwarding

## Report Details
- **Report ID**: 1131473
- **URL**: https://hackerone.com/reports/1131473
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-23T08:10:37.413Z
- **Disclosed**: 2021-05-13T05:22:36.482Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
It is possible to send email forwarding emails in the name of victim. The main problem is that you don't verify the `X-CSRF-Token` in the endpoint `/security_email_forwarding/test_forwarding.json?id=$id`. 
 

## Steps To Reproduce:

- Login as an program user who has access to the `Email Forwarding`
- Navigate to the `https://hackerone.com/hackerone_h1p_bbp3/security_email_forwarding` and add new  email here (use e.g. wearehackerone.com address)
- This will most likely fail. Atleast in our tests this used to happen
- Make the following HTML file:

```
<script>
for (i = 300; i < 350; i++){
var url = "https://hackerone.com/$program-id/security_email_forwarding/test_forwarding.json?id="+i;
var CSRF = new XMLHttpRequest();
CSRF.open("GET", url, true);
CSRF.withCredentials = 'true';
CSRF.send();
}
</script>
```

Note: set your forwarding id to be in this loop `for (i = 300; i < 350; i++){` (the purpose of this for loop is just to show that an attacker could verify all these emails). Also, set your program name to as a value of `$program-id`.

- Open this email to the new tab of the current browser 
- The email forwarding test messages will be sent

## Recommendation:

Verify that `X-CSRF-Token` which is already part of original HTTP request.

## References:

`https://owasp.org/www-community/attacks/csrf`

## Impact

CSRF allow to send email forward test messages

## Attachments
No attachments
