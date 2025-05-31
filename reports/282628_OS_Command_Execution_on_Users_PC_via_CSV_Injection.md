# OS Command Execution on User's PC via CSV Injection

## Report Details
- **Report ID**: 282628
- **URL**: https://hackerone.com/reports/282628
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-24T21:25:20.992Z
- **Disclosed**: 2017-11-02T23:55:51.672Z

## Reporter
- **Username**: cornerpirate
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** Twitter is vulnerable to CSV Injection. If an attacker can successfully exploit this, then they will compromise the PC of the user. The injection point is via a tweet (on the main twitter.com site) while the retrieval point is via the “Export Data” option on the analytics site.

**Description:** No user would ever tweet their own payload surely? Well I have found an issue also with the “Share this article” intent (specifically the “text” parameter). It handles URL encoded newline characters “%0A”. The default behaviours on some web browsers show the bottom line of text in the tweet only. Therefore, it is possible for an attacker to entice a user to tweet a malicious payload. 

If that victim then exports their analytics, opens the “csv” file in Excel and accepts a warning then their computer would be compromised. 

This is Dynamic Data Injection (DDE) into a formula which is evaluated in Excel. 

## Steps To Reproduce:

To verify the injection point safely simply:

  1. Tweet a benign payload: =1+55 
  2. Goto the analytics page and ensure that tweet is within the date range before clicking "export data"
  3. Open the exported CSV file within Excel

The most recent tweet should be at the top. Your first row will say 56 which is proof the addition worked.

Modifying the payload can convert this from an arithmetic formula to triggering Dynamic Data Exchange (DDE).

  1. Modify the payload to: =cmd|' /C calc'!A0
  2. Repeat the export and opening process.
  3. This time Excel will warn users about the DDE. Accepting these warnings will trigger calc.exe to open.

These error messages are Microsoft's response to DDE code execution. It has been established that users do not necessarily understand these warnings and that they instead rely on their implicit trust of the service which generated the file.

So far how to replicate the injection has been shown. The second part of this is how to influence a user to post a tweet which would harm themselves? I located a flaw in the "Share this article" intent through the "text" parameter. The URL for this is:

https://twitter.com/intent/tweet?text=[value]

The value allows URL encoded control characters such as: %0A

This is interpreted as a newline character and can be used to obfuscate the payload. The following URL includes a payload which can be used to replicate the issue:

https://twitter.com/intent/tweet?text=%3DSUM(1%2B1)*cmd%7C%27%20%2FC%20calc%27!A0%0A%0D%0A%0D%0A%0D%0A%0Dbbb

Essentially it begins with a DDE payload, injects several newlines and then writes “bbb” which could be the string the victim believes they are posting. By default FireFox (at least on Windows) was found to scroll down to the bottom of the text field meaning it displayed the string "bbb". There were over 100 characters remaining in which to replace that string with a reasonable message to entice the victim.

## Impact: This matters if you want to ensure your users can invest their trust in Twitter. 

The impact for Twitter is indirect. It is most likely going to affect trust in the service.
The impact for affected users is likely the full compromise of their computers. 

The attack requires multiple (but trivial) steps. If an attacker controlled a website and was able to make an article on that site "go viral". Then they could exploit users via the "Share this article" feature. While the payload would be delivered instantly it is at a later date most likely when the victim would export their data to complete the attack. An attacker would require patience. For this reason I would say there is a high impact, low difficulty of exploitation, but a degree of patience is required on the attackers part. 

I would say the CVSS rating is honestly way too high given the hoops to jump through but using that calculator can be a mixed bag. Gimmie a choice I'd say "high impact if exploited on the user side", but "probably not going to affect that many people" so average out and finger in the air at "medium" risk. If I was consulting for Twitter I would raise it for discussion and even if it winds up as "low" on your risk criteria point out the universality and simplicity of the remediation.

The following shows how a list of modern web browsers (on Windows) behaved:

Firefox 56.0.1	Yes - Vulnerable
Chrome 62.0.3202.62	No – less vulnerable
Internet Explorer 11.674.15063.0	No – less vulnerable
Edge 40.15063.674.0	No – less vulnerable
Opera  48.0.2685.50	No – less vulnerable

FireFox was the only one which scrolled the user to the bottom of the text field. All others are less vulnerable to exploitation.

## Remediation

Modify the “Export Data” function on the analytics host to prefix:=, +, - and @ symbols with a '. The single quote escapes the dangerous characters and prevents code execution client side.

Sounds cheap to me? A 5 minute code change to fix a potentially interesting issue. What else can you get done in 5 minutes?

## Supporting Material/References:

I have uploaded the following PDF which includes the same discussion and has screenshots etc for more confirmation:

  * F232489: Tweet_DDE_to_Me .pdf



## Attachments
- Tweet_DDE_to_Me_.pdf
