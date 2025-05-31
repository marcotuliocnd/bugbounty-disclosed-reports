# ██████████ bruteforceable RIC Codes allowing information on contracts 

## Report Details
- **Report ID**: 647409
- **URL**: https://hackerone.com/reports/647409
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-17T08:58:45.362Z
- **Disclosed**: 2019-12-02T19:14:22.856Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I'm entirely sure if this is anything useful from an attacker's purpose. Close the report if its not sensitive or non impactful. I noticed the DoD Warning mentioned it's sensitive so I thought to report it regardless just incase

I noticed ████████  has a functionality to let you look up RIC Codes. 3 digit Alphabetical code. This can be brutefored extremely easy to reveal various contract esque information 
**Description:**

The end point located at ██████/███████/s_search/query_ric.asp?ric=XXX
Normally functions to let anyone who knows the 3 digit code to access the endpoint. There is a captcha in place but once you verify that, you're able to access it unhindered. 

The usage of 3 character is inherently weak as it's only 857375 possibilities and I was able to find several already. The possibility to bruteforce it is trivial with the previous lack of enforcement

## Impact
Medium/High? Uncertain
## Step-by-step Reproduction Instructions
Visit https://www.███/███████/s_search/query_ric.asp?ric=ERX
We can then get the RIC DODAAC and further reveal information on it
https://www.█████████/█████████/s_search/query_dodaac.asp?dodaac=EZ2822

## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Enforce a complex method to codify possibly

## Impact

I'm entirely unsure what the attacker would be able to achieve but it looks possible to reveal point of contacts for contracts which could allow targeted phishing attacks, locations of contracts, what service they're under,etc. Other wise my lack of knowledge of the structure and general importance of the contents is lost on me which is why I'm uncertain if it's worth reporting

## Attachments
No attachments
