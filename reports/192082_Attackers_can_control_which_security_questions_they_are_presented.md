# Attackers can control which security questions they are presented (████████)

## Report Details
- **Report ID**: 192082
- **URL**: https://hackerone.com/reports/192082
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-17T23:31:35.839Z
- **Disclosed**: 2019-12-02T17:51:37.334Z

## Reporter
- **Username**: korprit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
When clicking on the forgot password link on ██████, the questions used to verify identify can be arbitrarily selected by an attacker.
**Description:**
When clicking on the forgot password link on ██████████, the questions used to verify identify can be arbitrarily selected by an attacker. 
## Impact
This allows an attacker to attack the account with only one piece of information requested from the verification process. See screenshot below. In this case, if the attacker knows where the victim wants to live 'the most', they can orchestrate a verification process asking the same question three times.
## Step-by-step Reproduction Instructions

1.  Click on the forgot password link, and modify the url such that the rq parameter is the number of the question for which there is a known answer (in this case 02): https://█████/PinLetterConfirm.aspx?globalID=DNET000720161122131230W0821236&AccessString=DJMSAA~||DMDAA,CV,PRI|AKO,CV,ALT||ALERT,1,1,1,1,1||Answers=8%27%22&att=Initial&rq=02,02,02
2.
3.

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions

## Attachments
No attachments
