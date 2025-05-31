# Gitlab Pages token theft using service workers

## Report Details
- **Report ID**: 1439552
- **URL**: https://hackerone.com/reports/1439552
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-02T21:42:03.018Z
- **Disclosed**: 2022-06-08T14:06:40.906Z

## Reporter
- **Username**: ehhthing
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
It is possible to steal Gitlab Pages session tokens by intercepting requests to the `/auth` endpoint on a Pages site using service workers. 

### Attack Flow
**Setup**
1. The attacker creates a private Gitlab Pages site at the root of their user page `attacker.gitlab.io`, ensuring that the project is `private to collaborators` for Gitlab Pages visibility. 
2. The attacker invites the victim to collaborate to the project, thus giving them access to the private Pages site.
3. The victim clicks on a link to `attacker.gitlab.io`, and a service worker is registered for the domain, passing through all requests back to the server except the `/auth` endpoint, which it intercepts.

**Bypassing the CSRF protection (OAuth2 `state` param)**
4. A script on the website requests a valid session cookie and redirection URL from an attacker controlled website.
5. The attacker controlled website sends its own request to `attacker.gitlab.io`, and retrieves a redirection URL and a session cookie.
6. A script on the website redirects the victim to the redirection URL retrieved by the attacker, and the user authenticates (since the user is already logged in, this does not require any kind of interaction)

**Intercepting the OAuth2 Response**
7. The OAuth2 service redirects the user back to `attacker.gitlab.io/auth` with the code and state, which is intercepted by the attacker's service worker and sent to the attacker controlled website.
8. The attacker controlled website sends a request to the auth endpoint with the original session cookie and the intercepted code and state to obtain an authenticated session cookie.
9. The attacker can use this cookie to access other GitLab Pages sites that the victim has access to.

### Steps to reproduce
1. Create an attacker account and victim account. The victim account should have access to a private GitLab Pages site that the attacker does not have access to.
2. Start the attacker controlled server (ensure that it is on a remote server with HTTPS)
3. Import the Proof of Concept repository into the attacker's account, rename it to `{attacker username}.gitlab.io` and change the attacker server to the server deployed in step 2.
4. Invite the victim to collaborate on the `{attacker username}.gitlab.io` project.
5. While logged into the victim account, visit `{attacker username}.gitlab.io`.
6. The attacker controlled server will output a valid `gitlab-pages` session cookie, which can be inserted into a browser or curl command (`curl -v --cookie '{cookie}' https://{victim username}.gitlab.io/{private Gitlab Pages project}`) to gain access to the private Gitlab Pages project on the victim's account.

### Examples

**Proof of Concept:**

Pages Project export: F1565711
Pages Project on gitlab.com: https://gitlab.com/dotchinavideo/dotchinavideo.gitlab.io
Attacker controlled server: F1565227 (requires `flask` and `flask-cors` installed, outputs the stolen token to stdout)

### What is the current *bug* behavior?
The current behavior is that `gitlab-pages` session cookies are not properly validated to ensure that the requested subdomain is the same as the subdomain to which the session cookie was issued for.

### What is the expected *correct* behavior?
The expected behavior is for each `gitlab-pages` session cookie be validated to prevent cross-subdomain usage.

### Relevant logs and/or screenshots
F1565251

### Output of checks
This bug happens on GitLab.com

#### Results of GitLab environment info
This bug happens on GitLab.com

## Impact

Once an attacker has a valid Pages session token, they are able to access every private Gitlab Pages site that the victim has access to.

## Attachments
- app.py
- exploit.mp4
- 2022-01-02_21-40-801_dotchinavideo_dotchinavideo.gi_export.tar.gz
