# Bypassing lock protection

## Report Details
- **Report ID**: 490946
- **URL**: https://hackerone.com/reports/490946
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-04T10:52:20.351Z
- **Disclosed**: 2019-07-26T07:42:20.235Z

## Reporter
- **Username**: doragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Nextcloud allows multi account within the android client app and relies on a single lock

Based on the (exposed) intent nc://login, it is possible to add a new account under attacker domain and open the Nextcloud without the lock check.

# Proof of concept
1. open the NC app with the lock displayed
2. triggers the following intent 
adb shell am start -a android.intent.action.VIEW -d "nc://login/server:MY_SERVER\&user:ME\&password:PWD  --es "ACCOUNT" "not_valid"
3. if the "add an account" action fails, attacker can still add an account in the screen
the app opens and attacker can check other accounts installed on the app.

# Remark
note that the "adb shell" comamnds could also be trigger with an app, making adb access not required
the "--es" option is required to prevent an app crash on

     AuthenticatorActivity.java:303
      mAccount = getIntent().getExtras().getParcelable(EXTRA_ACCOUNT);

## Impact

Lock can be removed and then data can be retrieved / alter / uploaded

## Attachments
No attachments
