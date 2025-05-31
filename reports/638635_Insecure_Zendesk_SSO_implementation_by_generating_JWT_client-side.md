# Insecure Zendesk SSO implementation by generating JWT client-side

## Report Details
- **Report ID**: 638635
- **URL**: https://hackerone.com/reports/638635
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-09T23:30:54.992Z
- **Disclosed**: 2019-09-08T09:55:04.583Z

## Reporter
- **Username**: xh3n1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trint

## Vulnerability Information
## Summary:
app.trint.com implements SSO to Zendesk, it does this by using JWT as described at https://support.zendesk.com/hc/en-us/articles/203663816-Enabling-JWT-JSON-Web-Token-single-sign-on

This functionality has not been implemented securely because the JWT generation happens in the client-side. This is done by the Zendesk secret being hardcoded in the JavaScript code.
The secret is used to create JSON Web Tokens and then you can use the generated token to impersonate any customer in Zendesk. (therefore potentially getting access to their support tickets)

Whilst support.trint.com is marked as out of scope for the program, the described vulnerability isn't caused by Zendesk. The vulnerable component is in app.trint.com.

## Assessment
The JavaScript source map files are available next to the minified production files. This significantly makes analyzing this issue easier.

- JavaScript file: https://app.trint.com/static/js/app.e984c9df.js
- Sourcemap file: https://app.trint.com/static/js/app.e984c9df.js.map

Looking at some of the UI views, I stumbled upon `static/js/modules/auth/pages/ZendeskLoadingPage.js`. I've attached a stripped version which shows the JWT generation:

```js
[snip]
import { ZENDESK_DOMAIN } from 'modules/core/constants/index';

const { REACT_APP_ZENDESK_SECRET } = process.env;

[snip]

function RedirectToZendesk(props) {
  const { user, history } = props;

  function generateZendeskTokenAndRedirect() {
    const TIME_NOW_OBJECT = moment(Date.now());
    try {
      const payload = {
        iat: TIME_NOW_OBJECT.unix(),
        jti: uuid.v4(),
        name: `${user.profile.firstName} ${user.profile.lastName}`,
        email: user.username,
      };

      // encode zendesk token
      const zendeskToken = jwt.sign(payload, REACT_APP_ZENDESK_SECRET);
      window.location = `${ZENDESK_DOMAIN}/access/jwt?jwt=${zendeskToken}`;
    } catch (err) {
      history.push('/error');
    }
  }

  useEffect(
    () => {
      generateZendeskTokenAndRedirect(user);
    },
    [user],
  );

  return <Loader />;
}

[snip]

export default ZendeskLoadingPage;
```

Searching for `REACT_APP_ZENDESK_SECRET` in the sourcemap will show the JWT secret: 

```js
var REACT_APP_ZENDESK_SECRET = "oq1HJ4jXo99Wt41bwvLh9BXBVdgpi52CjkXbThow7UhWQGtJ";
```

Generating the JWT on the client-side like this allows anyone to mint an arbitrary JWT. It would probably be better to generate this on the server-side.

## Reproduction steps

- As logged-in user press "Support" on https://app.trint.com
- Intercept the traffic and see the call to `https://trintsupport.zendesk.com/access/jwt?jwt=[JWT_TOKEN]`
- Logout of Zendesk
- Put the JWT token from above URI into https://jwt.io and decode it.

Example:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjI3MDk2NTksImp0aSI6IjIxZDAyOTg3LWU3YWItNDQ5MC05N2Q3LTc2YTBmMzJhOTVjOCIsIm5hbWUiOiJUZXN0IFRlc3QiLCJlbWFpbCI6ImIzODcxNjk0QHVyaGVuLmNvbSJ9.mnnx7dbpXbvU7xr5Bp5pad2eHVN01mSsXApmZoFj73c
```

```
{
  "iat": 1562709659,
  "jti": "21d02987-e7ab-4490-97d7-76a0f32a95c8",
  "name": "Test Test",
  "email": "b3871694@urhen.com"
}
```

- Now we can continue with tampering the JWT 
  - Change IAT to the current Unix timestamp
  - Change JTI to a random UUID v4
  - Change email to the victim email address
  - Insert `oq1HJ4jXo99Wt41bwvLh9BXBVdgpi52CjkXbThow7UhWQGtJ` as HMAC secret.
- Use the resulting JWT in a call to `https://trintsupport.zendesk.com/access/jwt?jwt=[JWT_TOKEN]`. You will be logged in as the victim.

## Impact

Access to the Zendesk account of Trint customers. This includes potentially the support history of said user.

I haven't verified whether the same SSO flow can also be used against Zendesk administrators. If so, the risk would be higher.

## Attachments
No attachments
