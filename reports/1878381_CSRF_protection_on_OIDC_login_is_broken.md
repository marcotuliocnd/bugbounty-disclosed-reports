# CSRF protection on OIDC login is broken

## Report Details
- **Report ID**: 1878381
- **URL**: https://hackerone.com/reports/1878381
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-18T11:43:16.493Z
- **Disclosed**: 2023-04-04T08:03:38.236Z

## Reporter
- **Username**: mikaelgundersen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
To protect against CSRF the "state" is used in the OIDC flow. On callback this code is verified against the code stored in the session for that user. However in case the token does not match a JSON response is provided that includes the expected state. Thus making it trivial for the attacker to obtain the correct state.

Judging from the code it clearly seem to be debug leftovers https://github.com/nextcloud/user_oidc/blob/main/lib/Controller/LoginController.php#L336-L344

Fixing the todo there should mitigate the issue and ensure the OIDC flow is more secure.


I didn't test ID4ME. But the code is almost identical. So I assume the bug is also the same https://github.com/nextcloud/user_oidc/blob/main/lib/Controller/Id4meController.php#L175-L181

## Impact

The CSRF protection provided with the state is practically useless now.

## Attachments
No attachments
