# IDOR on HackerOne Feedback Review

## Report Details
- **Report ID**: 262661
- **URL**: https://hackerone.com/reports/262661
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-23T18:47:42.902Z
- **Disclosed**: 2017-09-02T05:37:54.901Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi HackerOne Team,

**Summary:**

I have found an IDOR on HackerOne feedback review functionality, below are the following issues.

- Security teams can create public feedback to the hacker which is did not submit any report to them, please note that public feedback will be seen on hackers profile.

- Information Disclosure, the hacker will be able to see the __private feedback__ and the __report title__ that will be sent to his email even that is not his report title.

Lets focus on the first one which have direct security risk to all hackers, because it can be used to downgrade their profile reputations using the "__What Programs Say__"

**Description (Include impact)**:

A malicious user can create a public review to any hackers that he wants using the IDOR on hacker review functionality, the public review will be displayed on the hackers profile, therefor if the malicious person creates a disgusting review, all hackerone users can see that on victims user profile "__What Programs Say__", and may downgrade the users profile reputation.

**Steps to reproduce**:

Please note that i ask permission to the following persons below, before i reproduce my findings:

- @phspade a bug hunting buddy and a close friend of mine from Parrot Sec (who is the PH ambassador of Parrot Security OS and one of the sec team member who handle reports on Parrot Sec program)

- @jong_jong my other half <3

Lets proceed to the steps to reproduce:

  1. I used @jong_jong accounts to submit test report to Parrot Sec program.
  2. @phspade closed my test report then i ask him to review me and give him some instruction to perfrom an IDOR.
  3. @phspade click the review button and put the below necessary info: Selected `Friendliness` radio button, __Public feedback:__ `Japz is awesome :)`, __Private feedback:__ `Thanks for your report.`
  4. Submit the report and capture the request, on __POST /hacker_reviews HTTP/1.1__ you will see this parameters with it's values `hacker_username=jong_jong&report_id=<redacted>&positive=true&behavior=friendly&private_feedback=Thanks+for+your+report.`
  5. The vulnerable param is the __hacker_username__ , change the  value to victims username. (e.g `hacker_username=japzdivino`) and forward the request.
  
__japzdivino__ will received an email notification regarding the review, but it should be jong_jong should be the one to received

{F215257}

Also japz profile will display the public review, instead of jong_jong's profile.

{F215258}

Let me know if anything else is needed.

Regards
Japz









## Attachments
- feedback_email_notification.png
- whatprogramsay.png
