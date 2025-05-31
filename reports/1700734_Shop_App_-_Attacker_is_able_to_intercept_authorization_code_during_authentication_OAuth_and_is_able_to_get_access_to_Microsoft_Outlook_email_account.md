# Shop App - Attacker is able to intercept authorization code during authentication (OAuth) and is able to get access to Microsoft Outlook email account

## Report Details
- **Report ID**: 1700734
- **URL**: https://hackerone.com/reports/1700734
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-14T19:13:42.938Z
- **Disclosed**: 2023-03-02T21:21:51.265Z

## Reporter
- **Username**: kun_19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:

### Deep linking 
Mobile apps have a unique vulnerability that is non-existent in the web: deep linking. Deep linking is a way of sending data directly to a native application from an outside source. A deep link looks like app:// where app is your app scheme and anything following the // could be used internally to handle the request.
Deep links are NOT secure and you should never send any sensitive information in them. The reason deep links are not secure is because there is no centralized method of registering URL schemes. As an application developer, you can use almost any url scheme you choose by configuring it in Xcode for iOS or adding an intent on Android. There is nothing stopping a rogue application from hijacking your deep link by also registering to the same scheme and then obtaining access to the data your link contains.

### Shop app - Microsoft Outlook Oauth flow and the vulnerability
The **Shop App** allows users to connect to their Microsoft Outlook  account to import orders from the emails (via OAuth flow). Therefore, the custom url scheme `shopapp://` is used for transmitting the authorization code at the end of the Oauth flow to the Shop App, which finally can be used to exchange the the authorization code with a valid session token from Microsoft.

Another (malicious) app is also able to claim the **same url scheme** and can intercept the authorization code! When the operating system has two or more applications to choose from when opening a link, Android will show the user a modal and ask them to choose which application to use to open the link. On iOS however, the operating system will make the choice for you, so the user will be blissfully unaware. Apple has made steps to address this issue in later iOS versions (iOS 11) where they instituted a first-come-first-served principle. Thus, if the malicious app is installed **BEFORE** the official Shop App, the malicious app "wins" and will receive the authorization code.

Normally, a special Oauth flow for mobile apps (**Authorization Code Flow with Proof Key for Code Exchange (PKCE)**) is used to prevent this ! It prevents an attacker, if the authorization code was intercepted, to exchange the authorization code with a valid session token (see here for more information https://auth0.com/docs/flows/authorization-code-flow-with-proof-key-for-code-exchange-pkce). 
This specific Oauth flow (PKCE) is not implemented by the Shop App for connecting a Microsoft Outlook account.

Thus, it is vulnerable to such kind of attacks. I created a malicious Android app which is able to intercept the authorization code (see PoC).

## Steps To Reproduce:

  1. Install the attached malicious Android App (F1926639) on your device.
  2. Install the official/legit Shop App from the Google Play Store.
  3. Open the legit Shop App, create an account and start connecting to your Microsoft Outlook account:  
{F1926639}
  4. Just log in to your Microsoft account and grant the Shop App the  permissions to access/read your emails: 
{F1926645}
  5. After the login, a modal is shown which asks the user which app should handle the authentication. Choose "Shop PRO" (the malicious App):  
{F1926673}
  6. The malicious App successfully intercepted the authorization code, which can now be exchanged to get a valid session token to read the victim's emails:  
{F1926677}

**NOTE**: Keep in mind that under iOS the *first-come-first-served principle* applies. If the malicious App is installed **BEFORE** the official Shop App, the malicious app "wins" and will receive the authorization code.

## Impact

An attacker is able to intercept an authorization code and exchanges it for a valid session token from Microsoft to gain read access to the victim's emails.

Or the attacker uses the intercepted authorization code to link the Outlook account to his own Shop account via the endpoint https://server.shop.app/graphql (operation name: `LinkOutlookAccount`). Thus, all orders can now be tracked by the attacker.

## Attachments
- outlook_connect.png
- outlook_login.png
- modal.png
- intercepted_auth_code.png
- shop_pro.apk
