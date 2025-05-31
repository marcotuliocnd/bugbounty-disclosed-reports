#  Account Takeover on unverified emails in File Sync & Share 

## Report Details
- **Report ID**: 906790
- **URL**: https://hackerone.com/reports/906790
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-24T11:47:00.171Z
- **Disclosed**: 2021-06-16T18:26:18.227Z

## Reporter
- **Username**: 0xcrypto
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
The name change functionality in File Sync & Share is expected to change the name in File Sync & Share. But the API endpoint used in it also allows changing email to any email without having to verify the email. The login email stays the same but the email within File Sync & Share application changes to the new email without verification. This allows user to pretend to be someone else. If the victim has not verified his email, the bug can allow attacker to take over his File Sync & Share account.

## Steps to Reproduce
1. Given the attacker has user access to the File Sync & Share, Login (as attacker) at https://mc-beta-cloud.acronis.com/fc/access.
2. In the dashboard of File Sync & Share ie. https://mc-beta-cloud.acronis.com/fc/access#/nodes, click on right top Profile button and click on your name. A modal should open which allows you to change the name.
{F880834}
4. After the modal box appears, you can see that the email field is disabled. To change it, click on save while capturing the request in any proxy like Burpsuite. The request should look like:

```http
PUT /fc/api/v1/account HTTP/1.1
Host: mc-beta-cloud.acronis.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://mc-beta-cloud.acronis.com/fc/access
Content-Type: application/json;charset=utf-8
ACCESS_WEB_UI: ACCESS_WEB_UI
X-CSRF-Token: L+0MN5lQqnozdt86Ot276c10PuwLrvpSCK0MrInGkuz5Ei29eyEy8VN37jELA+CwUFHWbEZq3oOv3CUpJMKNvA==
Content-Length: 74
DNT: 1
Connection: close
Cookie: NodesTable_state=%7B%22columnInfo%22%3A%7B%7D%7D; host="https://mc-beta-cloud.acronis.com"; accountsrv_locale=en; device_cookie=gAAAAABe8yaMOtGcfCPWSB1PAHZPMAVgHdifpxs35gAsVWeeav-xAM_N4jBNUxCpMTK499VvRQ3DsnLAuX822D8JwxrjZCeD9v2GMc7MiM-NdDdybJIOrrGXNTQyE1UYSdnRU5rmU2unZ16UFsDY78M6rDwcIgU4U7lOsIaKAzrSIOZrr-xvd0JcspJ6oASazUioge-kI2bg; rest_access_token=L%2B0MN5lQqnozdt86Ot276c10PuwLrvpSCK0MrInGkuz5Ei29eyEy8VN37jELA%2BCwUFHWbEZq3oOv3CUpJMKNvA%3D%3D; _activecho_session=46a70775f93123cc9bd6485f0b8fb02c; server_return_to=%2Ffc%2Faccess

{"name":"Staff Member","email":"0xcrypto+staffmember1@wearehackerone.com"}
```

5. The ```email``` parameter in the above request is changeable. Enter email of any unverified user (you can also enter any email you wish to use even if it is not registered):

```
{"name":"Human Resource","email":"hr@acronis.com"}
```

If you get email already taken, the email has been already verified by the user and account takeover is not possible. So try any other email.

If you get ```204 No Content``` the email has been changed successfully and account takeover is successful.

To verify if email has been changed or not, you can go to https://mc-beta-cloud.acronis.com/fc/access#/log within your account.

This does not changes the email ID for the main profile but only File Sync & Share ie. the attacker can login using the old credentials but the new Email is shown everywhere within the File Sync & Share.

I tested the folder/file sharing feature after taking over the account and found that the email used to login can no longer be invited and the email changed using this method is now available to be invited. While the invites goes in the new email, the account is controlled by the attacker.

If the administrator tries to check the email, the taken over email is not reflected in Management Control Dashboard. If the victim verifies his email after the takeover and tries to access File Sync & Share, he gets the error **This account has not been created yet** but his account gets verified.
{F880837}

So the attack is quite stealth.

I haven't tested other applications and whether this taken over email is reflected in other places or not. But I suspect that it gets reflected in other applications as well.

## Impact

The attacker could trick the users by pretending to be anyone. Also, the attacker could steal important files by taking over unverified accounts.

## Attachments
- Screenshot_2020-06-24_16-53-03.png
- Screenshot_2020-06-24_16-58-38.png
