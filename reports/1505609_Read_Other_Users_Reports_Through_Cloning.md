# Read Other Users Reports Through Cloning

## Report Details
- **Report ID**: 1505609
- **URL**: https://hackerone.com/reports/1505609
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-09T20:31:35.124Z
- **Disclosed**: 2022-05-26T12:41:28.682Z

## Reporter
- **Username**: imthatt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
## Summary:
I team, I have found a vulnerability where I am able to read other users reports through the clone report function.
If an attacker goes to try read another users report, we get a 500 internal error response.
But if an attacker uses the clone report function, we are able to clone a victims report and read it on our attacker account

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Victim account has a scorecard created under https://demo.sftool.gov/tws/
  2. Attacker goes to https://demo.sftool.gov/tws/ and selects clone scorecard
 3. Attacker enters name of score card (any name)
4. Attacker clicks choose score card (have to have an existing scorecard on attacker account prior) and selects scorecard
5 Attacker turns on interceptor and changes name of scorecard to that of victim scorecard under the parameter nTwsUserScorecard.Template=    (use value testnew to see my scorecard)
6 attacker submits request

you have now cloned my scorecard into your own scorecard and can read my details (see poc attached)

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

If an attacker goes to try read another users report, we get a 500 internal error response.
But if an attacker uses the clone report function, we are able to clone a victims report and read it on our attacker account reading sensitive report data of another user

## Attachments
- Desktop_2022.03.09_-_20.26.33.03.mp4
