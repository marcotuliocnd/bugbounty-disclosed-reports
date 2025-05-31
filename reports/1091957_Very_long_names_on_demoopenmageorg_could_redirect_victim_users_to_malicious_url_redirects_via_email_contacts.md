# Very long names on demo.openmage.org could redirect victim users to malicious url redirects via email contacts.

## Report Details
- **Report ID**: 1091957
- **URL**: https://hackerone.com/reports/1091957
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-01T11:56:23.692Z
- **Disclosed**: 2021-04-29T08:44:54.794Z

## Reporter
- **Username**: lmhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: openmage

## Vulnerability Information
### Summary:
We found that the maximum length of the first and last name fields was not set to 32 characters at registration and to 1000 characters when using the profile update form. The attacker can use this method as a malware attack, the user will redirect to a website that contains malware or hijack.

**Descriptions**
  * very long name vulnerabilities use refferals
  * control character allowed in username
  * Email spoofing can redirect victim to malware attack


### Steps To Reproduce:
  * Open directory register page https://demo.openmage.org/customer/account/create/
  * In F/L name paste your ``payload-name``
  * Paste a victim emails to sent a mallware attack
  * Sent repreat to burp suite - and boom you can see the response has been ``200 OK``

**Request**
```
POST /customer/account/createpost/ HTTP/1.1
Host: demo.openmage.org/
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 91

Content-Disposition: form-data; name="error_url"


------WebKitFormBoundaryZaGjL6AhSOgUPeQl
Content-Disposition: form-data; name="form_key"

8aHBFidQJt9At8Ux
------WebKitFormBoundaryZaGjL6AhSOgUPeQl
Content-Disposition: form-data; name="firstname"

hello your account has been deleted permanenty please visit here evil.com your account has been blocked permanenty ,please confrim your verification here evil.com
------WebKitFormBoundaryZaGjL6AhSOgUPeQl
Content-Disposition: form-data; name="lastname"

hello your account has been deleted permanenty please visit here evil.com your account has been blocked permanenty ,please confrim your verification here evil.com
------WebKitFormBoundaryZaGjL6AhSOgUPeQl
Content-Disposition: form-data; name="email"

victim-email@address.com
------WebKitFormBoundaryZaGjL6AhSOgUPeQl
Content-Disposition: form-data; name="password"

memek@123
------WebKitFormBoundaryZaGjL6AhSOgUPeQl
Content-Disposition: form-data; name="confirmation"

memek@123
------WebKitFormBoundaryZaGjL6AhSOgUPeQl--
```

## Supporting Material/References:
F1179531
F1179532

## Impact

* Attacker can sent a malware attack to victim email using a server notification emails this is can leads to Business Logic Errors
  * Email Hijacking
  * Control character allowed in username

## Attachments
- Screenshots.png
- Screenshots_2.png
