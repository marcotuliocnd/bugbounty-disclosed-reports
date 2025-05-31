# Open Redirect at https://oauth.secure.pixiv.net

## Report Details
- **Report ID**: 972601
- **URL**: https://hackerone.com/reports/972601
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-02T01:56:14.470Z
- **Disclosed**: 2020-12-22T01:24:27.491Z

## Reporter
- **Username**: zimmer75
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pixiv

## Vulnerability Information
## Summary:
Hello @pixiv security team,  i hope you are well, i noticed you can redirect users to another domain if you send an invalided scope.

**Vulnerable Url**

* `https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=Y1olfIApoCNuSGzx9kTgIbf5Wk4R&redirect_uri=https%3A%2F%2Fsketch.pixiv.net%2Fsession%2Fpixiv%2Fcallback&response_type=code&scope=read-email+read-x-restrict+read-birth+write-upload+read-profile+write-profile+read-favorite-users&state=security_token%3D5cb310fefea19a5cb56307af3488a816921413bc70b5b142%2Crequest_type%3Ddefault`

## Steps To Reproduce:

  *   In the request looks for the **scope** parameter and change his value to *ggg*.
 
  *    Looks for the **redirect_uri** parameter and change it for an arbitrary domain, i.e `https://example.com`

  *   Open the link in your browser and done.
  
  *   `https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=Y1olfIApoCNuSGzx9kTgIbf5Wk4R&redirect_uri=https%3A%2F%2Fexample.com%2Fsession%2Fpixiv%2Fcallback&response_type=code&scope=ggg&state=security_token%3D5cb310fefea19a5cb56307af3488a816921413bc70b5b142%2Crequest_type%3Ddefault`

{F972733}

## Impact

It may lead users to a phishing site and an attacker can steals his credentials.

## Attachments
- pixiv_open_redirect_poc.mkv
