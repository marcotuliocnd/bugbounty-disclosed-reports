# Recaptcha Secret key Leaked

## Report Details
- **Report ID**: 1416665
- **URL**: https://hackerone.com/reports/1416665
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-12-04T09:27:44.939Z
- **Disclosed**: 2021-12-04T18:07:14.326Z

## Reporter
- **Username**: aif_lill
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Greeting from @kashifinfo90,

I hope **Paragonie Security Team** is doing great, Following **Secret Keys** are leaked:
> "secret-key": "6Ldy5BYTAAAAAPBh868BMm2nGZelOUyXJHTUE4no",
   "site-key": "6Ldy5BYTAAAAACk3Tj8wDUBLcVxSL2JXFBw-Dtj3"
  "secret-key": "6Ld27iETAAAAAF6tsd5SaoCgc5cFX-tkfHqx7FtX",
  "site-key": "6Ld27iETAAAAAI51EVcu0nBw2wkxQiZxg1zGv2uI"

##Steps To Reproduce:
To find the leak please [Click Here](https://github.com/paragonie/airship/commit/037c03db5621409103f45b2f6dc6da8ae8f12ee6#diff-2f87b6e210a2b88cc43a283065ab08a53ead3159288cb52b94a17509b7ece910)

## Impact

To avoid any legal issue i didn't try anything with these key, hence it up to you to fully investigate them and figure out if they have any security impact.
Note: If it is out of scope or your figure out that the security impact is un considerable please  allow me to selfclose it, It will prevent decrease in my current reputation points.

kind Regards,
@kashifinfo90.

## Attachments
No attachments
