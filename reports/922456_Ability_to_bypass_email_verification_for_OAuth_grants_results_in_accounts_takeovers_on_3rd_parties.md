# Ability to bypass email verification for OAuth grants results in accounts takeovers on 3rd parties

## Report Details
- **Report ID**: 922456
- **URL**: https://hackerone.com/reports/922456
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-13T10:47:32.845Z
- **Disclosed**: 2020-10-01T18:13:14.253Z

## Reporter
- **Username**: cache-money
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
There's a limitation that requires a validated email before going through the OAuth flow, however this is bypassable. Bypassing this means the target site assumes your email is validated, and actually ends up signing you in with an non-validated email. This behavior can frequently lead to account takeovers in 3rd parties since they often use the email as an identifier, and fold all OAuth/manually created accounts into one. In my example I am going to demonstrate an account takeover on https://laravelshift.com/, however this concept is widely exploitable.

It should also be possible to use this technique to get into internal company using pages that just look for `@domain.com` in the email before allowing them access.

### Steps to reproduce
1) Create a Bitbucket or GitHub account with a random email, and login to https://laravelshift.com/. (We're seeding a victim account).
2) In a different browser, create a new GitLab account with that same email but never confirm it.
3) In that browser, visit LaravelShift and click "Sign in with GitLab", notice you land on a page that states you cannot complete the OAuth grant without validating your email.

Run the following request in Burp replacing your cookies, CSRF token, and state parameter.

```
POST /oauth/authorize HTTP/1.1
Host: gitlab.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 354
DNT: 1
Connection: close
Cookie: [COOKIES]

utf8=%E2%9C%93&authenticity_token=[CSRF TOKEN]&client_id=6dd35c52b02a99eca3454505c4b1f1fa761ad1125bcdccdbc1c290877ef25093&redirect_uri=https%3A%2F%2Flaravelshift.com%2Fauth%2Fgitlab%2Fcallback&state=[STATE VALUE FROM URL]&response_type=code&scope=&nonce=
```
4) Notice the request succeeds with a 302 to LaravelShift with the `code`.
5) Visit that URL and notice you get logged into the victim's account from step 1. This works since the GitLab email is assumed to be trusted and validated.

### Impact

Account takeovers on 3rd parties due to developers assuming GitLab is properly checking validated emails.

### What is the current *bug* behavior?

It's possible to play the `/oauth/authorize` request directly to bypass the `Verify the email address in your account profile before you sign in.` prompt.

### What is the expected *correct* behavior?

The email verification check should be enforced at this step of the process as well.

## Impact

Thanks,
-- Tanner

## Attachments
No attachments
