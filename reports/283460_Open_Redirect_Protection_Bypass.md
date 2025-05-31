# Open Redirect Protection Bypass

## Report Details
- **Report ID**: 283460
- **URL**: https://hackerone.com/reports/283460
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-27T09:07:11.514Z
- **Disclosed**: 2017-12-23T07:48:36.407Z

## Reporter
- **Username**: avinash_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi

Report #281538 is fixed but Attacker can Bypass this Open Redirect Protection.

Give this link ``` https://twitter.com/teams/authorize?target_screen_name=&authorize_callback=//www.facebook.com``` to authorized victim.Twitter will say him to authorize a different account for create team.After authorization victim will be redirected to ```www.facebook.com```

Vulnerable point ```//www.facebook.com``` (You can use //www.example.com )

Open Redirection Protection Bypassed.

PoC video attached

With Best Regards

## Attachments
- PoC_Friday_27_October_2017_02_09_34__IST.mp4
