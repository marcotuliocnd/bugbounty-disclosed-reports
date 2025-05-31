# Program profile_metrics.json contains time to triage for deptofdefense even it's turned off

## Report Details
- **Report ID**: 318399
- **URL**: https://hackerone.com/reports/318399
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-02-22T05:39:50.827Z
- **Disclosed**: 2018-03-09T16:04:06.402Z

## Reporter
- **Username**: kunal94
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello Hackerone Security Team,

#Summary
>1) Well, in your previous report, it was revealing about ```Time to Triage``` for WordPress which you fixed it.

>2) However, the program US dept of defense doesn't have profile metrics which we can't display any certain info.
But, still profile_metrics.json leaks the ```time to triage``` parameter for US DEPT OF DEFENSE  though it disabled from the side of Profile Metrics (Response Efficiency).

#Step to Reproduce

1) Go To ```https://hackerone.com/deptofdefense```.

2)Note: you can see there is no response efficiency.

3) Now, use the profile_metrics.json at the end of program parameter.

https://hackerone.com/deptofdefense/profile_metrics.json

4) The response is 

{"mean_time_to_first_response":null,```"mean_time_to_triage":1173600```,"mean_time_to_resolution":null,"mean_time_to_bounty":null,"total_bounties_paid_prefix":null,"total_bounties_paid":null,"average_bounty_lower_range":null,"average_bounty_upper_range":null,"top_bounty_lower_range":null,"top_bounty_upper_range":null}

The parameter ```mean_time_to_triage``` has been leaked even though it should be set to ```null```.

As this is the case of deptofdefense, then this type of parameters should always be set to null and be private.

Thanks
Kunal

(Attaching with POC)


F265751

## Impact

An attacker can gain information regarding deptofdefense (Triage time) even though it's turned off.

## Attachments
- poc1.png
