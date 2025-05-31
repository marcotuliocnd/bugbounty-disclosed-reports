# [user_oidc] Unencrypted Communications

## Report Details
- **Report ID**: 1687005
- **URL**: https://hackerone.com/reports/1687005
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-08-31T12:01:57.262Z
- **Disclosed**: 2022-12-18T11:29:27.728Z

## Reporter
- **Username**: lauritz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The [OpenID Connect User Backend](https://github.com/nextcloud/user_oidc/) allows users to login to Nextcloud using SSO and is - according to [the policy](https://hackerone.com/nextcloud?type=team) - part of the main scope of this program. The implementation supports plain HTTP without TLS and transfers sensitive information such as OIDC **client_secrets** in an unencrypted manner.

[According to the OpenID Connect specification](https://openid.net/specs/openid-connect-core-1_0.html#TLSRequirements), "*to protect against information disclosure and tampering, confidentiality protection MUST be applied using TLS with a ciphersuite that provides confidentiality and integrity protection*".

I did not find anything related to this within your threat model (which is unavailable at the moment btw. - therefore I am referring to this snapshot: https://web.archive.org/web/20220320042405/https://nextcloud.com/security/threat-model).

## Steps to reproduce
0. Setup Nextcloud using the docker image:
```console
docker run -p 8081:80 nextcloud:latest
```
1. Enable `user_oidc` module via http://localhost:8081/settings/apps/integration/user_oidc
2. Configure plugin via http://localhost:8081/settings/admin/user_oidc - add a provider with arbitrary identifier, client_id and client_secret. Include a burp collaborator URL with `http://` scheme:      
{F1894137}
3. In a private window, visit http://localhost:8081/login an click the login button "test".
4. Observe incoming request using plain HTTP:      
{F1894136}

In a working SSO setup, sensitive information such as the client_secret is sent in plain text by Nextcloud, as can be seen in the following screenshot (Token Request issued by Nextcloud):      
{F1894138}

## Fix
The `user_oidc` should enforce HTTPS in its default configuration.

## Impact

Sensitive information such as the OIDC client credentials and tokens are sent in plain text of HTTP without TLS.

## Attachments
- unencrypted_communication2.png
- unencrypted_communication.png
- unencrypted_communication3.png
