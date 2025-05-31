# Reflected xss on https://█████████

## Report Details
- **Report ID**: 1988560
- **URL**: https://hackerone.com/reports/1988560
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-15T22:10:49.364Z
- **Disclosed**: 2023-06-02T18:23:11.578Z

## Reporter
- **Username**: rektile404
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The domain ███ is vulnerable to reflective xss.
By clicking the following link you will get an alert message: https://█████/sec.html?redirect=javascript:alert(document.cookie);//://██████/
The error occurs due to a flaw in the check that verifies the validity of the redirect URL. 
The function takes the value of the redirect parameter and checks if the portion after the first `://` begins with any of the values in the array. 
This check does not include protocol checking, allowing us to prepend the value with `javascript:`. 
Then we can append a commented-out section at the end to ensure that the `isSafeHost` function returns True.
This is the function that checks if it is valid:
```js
function isSafeHost(uri) {
      var safeHosts = ['█████/', '███/', '████/', '██████████'];
      // Only consider localhost for local testing
      if (window.location.host.includes('localhost')) {
        safeHosts.push('localhost');
      }
      return safeHosts.find((host) => uri.slice(uri.indexOf('://') + 3).startsWith(host));
    }
```
At the end of the check the redirect parameter is used as follows:

```js
window.location.href = rawRedirect;
```

## References

## Impact

- Take over a user's account
- Phish users
- Show malicious content 
- Redirect users

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Click on the following link: https://█████████/sec.html?redirect=javascript:alert(1);//://████/
You can change the `alert(1)` for your own payload

## Suggested Mitigation/Remediation Actions
Do a check for protocol and make sure the host comes directly after this protocol.



## Attachments
No attachments
