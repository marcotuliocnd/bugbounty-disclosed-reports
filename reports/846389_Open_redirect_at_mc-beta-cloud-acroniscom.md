# Open redirect at mc-beta-cloud-acronis.com

## Report Details
- **Report ID**: 846389
- **URL**: https://hackerone.com/reports/846389
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-04-10T11:43:47.907Z
- **Disclosed**: 2022-11-15T09:49:28.190Z

## Reporter
- **Username**: angeltsvetkov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Open Redirect Vulnerability

Steps To Reproduce:
Type in this URL:

https://mc-beta-cloud.acronis.com/api/2/idp/authorize?client_id=f2e82dbb-78af-4b5b-bc7f-651d4f42a722&redirect_uri=%2Fbc%2Fapi%2Fgateway%2Fcb&response_type=code&scope=offline_access+openid+profile+email&state=http://evil.com&nonce=yhokbempqmmqllfbwpsfzfmf

You got redirect to evil.com

Parameter: state

## Impact

n attacker can use this vulnerability to redirect users to other malicious websites, which can be used for phishing and similar attacks

## Attachments
No attachments
