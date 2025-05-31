# Search query text, including from potentially undisclosed reports, sent to Google Analytics on Inbox query page

## Report Details
- **Report ID**: 280770
- **URL**: https://hackerone.com/reports/280770
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-10-19T20:36:52.264Z
- **Disclosed**: 2017-11-01T20:54:41.075Z

## Reporter
- **Username**: holvonix-advay
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Search query text, including from potentially undisclosed reports, sent to Google Analytics on Inbox query page

**Description (Include Impact):**
Since search query text can both include content of private vulnerabilities, it shouldn't be sent to Google Analytics.  Furthermore, the information sent to GA includes information indicating the presence of a report and its status associated with a particular company (if there is a non-zero report_id and a filtered reported_to_team parameter), which further pins down that a company has a report with certain yet-undisclosed text in said report. Finally, search query text can contain PII, and therefore should not be sent to GA (however, I am not a lawyer, and this is not legal advice).

**Mitigation:**  Client-side redaction of the 'reported_to_team' and 'text_query' params (at the least) before posting to GA.

### Steps To Reproduce

1. Visit the permalink URL for an inbox search query (for example, searching for "SOME_UNDISCLOSED_REPORT_OR_PII_INFO_HERE" and filtering to HackerOne gives a URL like: 
https://hackerone.com/bugs?subject=user&report_id=0&view=custom&substates%5B%5D=pre-submission&substates%5B%5D=new&substates%5B%5D=needs-more-info&substates%5B%5D=triaged&substates%5B%5D=duplicate&substates%5B%5D=informative&substates%5B%5D=resolved&substates%5B%5D=not-applicable&substates%5B%5D=spam&reported_to_team=security&text_query=SOME_UNDISCLOSED_REPORT_OR_PII_INFO_HERE&program_states%5B%5D=2&program_states%5B%5D=3&program_states%5B%5D=4&program_states%5B%5D=5&sort_type=pg_search_rank&sort_direction=descending&limit=25&page=1 )

2. Note in the browser network inspector a www.google-analytics.com/collect post containing the sensitive information in the dl param (I have omitted all numeric identifiers for the sake of future disclosure) :
`v=1&_v=***&a=***&t=pageview&_s=1&dl=https%3A%2F%2Fhackerone.com%2Fbugs%3Fsubject%3Duser%26report_id%3D0%26view%3Dcustom%26substates%255B%255D%3Dpre-submission%26substates%255B%255D%3Dnew%26substates%255B%255D%3Dneeds-more-info%26substates%255B%255D%3Dtriaged%26substates%255B%255D%3Dduplicate%26substates%255B%255D%3Dinformative%26substates%255B%255D%3Dresolved%26substates%255B%255D%3Dnot-applicable%26substates%255B%255D%3Dspam%26reported_to_team%3Dsecurity%26text_query%3DSOME_UNDISCLOSED_REPORT_OR_PII_INFO_HERE%26program_states%255B%255D%3D2%26program_states%255B%255D%3D3%26program_states%255B%255D%3D4%26program_states%255B%255D%3D5%26sort_type%3Dpg_search_rank%26sort_direction%3Ddescending%26limit%3D25%26page%3D1&ul=en-us&de=UTF-8&dt=HackerOne&sd=24-bit&sr=***&vp=***&je=0&_u=***~&jid=&gjid=&cid=***&uid=***&tid=UA-***-1&_gid=***&z=***`



### Optional: Your Environment (Browser version, Device, etc)

 * Mac OS High Sierra, Chrome 61.0.3163.100

### Optional: Supporting Material/References (Screenshots)

 * 

## Attachments
No attachments
