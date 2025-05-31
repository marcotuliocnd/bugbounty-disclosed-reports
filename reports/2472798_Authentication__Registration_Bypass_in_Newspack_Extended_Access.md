# Authentication & Registration Bypass in Newspack Extended Access

## Report Details
- **Report ID**: 2472798
- **URL**: https://hackerone.com/reports/2472798
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-04-21T03:37:31.991Z
- **Disclosed**: 2024-05-20T21:32:56.061Z

## Reporter
- **Username**: xurizaemon0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:

The Newspack Extended Access plugin omits to validate JWT signing on the registration and login JSON endpoint. This permits registration of accounts with arbitrary (user-supplied) details, and auth bypass and account hijack if a target account email is known.

## Platform(s) Affected:

Any website using [Newspack Extended Access plugin](https://github.com/Automattic/newspack-extended-access).

## Steps To Reproduce:

Create an unsigned JWT containing payload value `{email: "target@example.org"}`. Use a browser to supply this data to the Extended Access registration endpoint. Browser will be authenticated as the target user.

Alternative attack path: use lack of validation to create new accounts with "Customer" role via same endpoint using untrusted inputs. Potential for malicious inputs or DoS through unprotected user creation endpoint.

### Requirements

  1. Site installed and configured with Newspack Extended Access (+ dependencies incl WooCommerce, WC Memberships, Newspack).
  1. Target user email is known (for account hijack)

Notes:

  1. For account hijack, target user must be registered via SwG / Extended Access initially
  1. For account hijack, target user is not Administrator or Editor (but may be any other privileged or unprivileged role)

### Reproduction (account hijack)

1. Be logged out of the target website
1. Create a JWT token with value `email` set to the target account email. This can be done using the website https://token.dev - the `email` value is the only significant input for account hijack. Copy the resulting token value.
1. Visit the target website and use the following code in browser console to authenticate as the target user:

```
// Endpoint URL
let url = `${window.location.protocol}//${window.location.hostname}/wp-json/newspack-extended-access/v1/google/register`;
// JWT contents - this JWT contains email "test@example.org".
let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUub3JnIiwiaWF0IjoxNzEzNjY2NjQ5LCJleHAiOjE3MTM2NzAyNDl9.I8D18nWsn5H6AylwJdak8727APyiMCWkcnXH95vMF_k";
// Provide token to authentication endpoint.
fetch(  
    url,  
    {  
       cache: 'no-store',  
       method: 'POST',  
       headers: {  
          'Content-type': 'text/plain',  
       },  
       body: token  
    }  
).then(response => {  
    console.log(response.json(), 'response');  
})
```

The browser will now be logged into the target account. Personal data (eg the target user's additional account details, billing address etc) will be visible to the attacker.

### Reproduction (account creation)

Submitting new accounts via the above method is also possible. Accepting untrusted user submitted input here may allow for additional attack paths when user details are displayed to administrator. Potential for abuse of unprotected submissions via the endpoint would likely permit additional attacks by creating excessive user accounts.

## Supporting Material/References:

JWT is accepted without validation of JWT signature. Ref https://github.com/Automattic/newspack-extended-access/blob/trunk/includes/class-rest-controller.php#L81-L87

Mitigation: Newspack Extended Access prevents sign-in via this method if the user has role "Editor" or "Administrator", but does not prevent sign-in if the user has other privileged roles eg "Shop Administrator". Ref https://github.com/Automattic/newspack-extended-access/blob/trunk/includes/class-rest-controller.php#L96-L99

Mitigation: Newspack restricts authentication to user accounts which have metadata indicating that Signin with Google was used for initial sign-in. Ref https://github.com/Automattic/newspack-plugin/blob/trunk/includes/reader-activation/class-reader-activation.php#L681-L690

## Impact

- Registration of accounts with arbitrary (user-supplied) details
- Authentication bypass if the target account email is known
- Injection of untrusted data into user profiles

## Attachments
No attachments
