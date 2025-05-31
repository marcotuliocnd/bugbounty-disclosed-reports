# Report Bulk endpoint "agree-on-going-public" action may reveal Report disclosure state for invite-only programs

## Report Details
- **Report ID**: 1219011
- **URL**: https://hackerone.com/reports/1219011
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-07T11:05:09.334Z
- **Disclosed**: 2021-06-30T14:21:24.299Z

## Reporter
- **Username**: clubbable
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello,
 Hope you are doing well,
                                                                                                                                    SUMMARY
->In hackerone user doesn't have permission to do any action like "disclosing/undiclosing" in disclosed report.
->Here user can send the "cancel-disclosure-request" request to the server and server accepts the request gave 200ok response with 
                               "{"flash":"The request to disclose the report has been cancelled."}"
->Here server didn't validate the report ID, so that user can perform this action successfully..
->But sadly the response was updated in disclosed report, but you can clearly see in the response "cancellation has been done " properly.

                                                                                                                                    STEP TO REPRODUCE
1.Take a disclosed report in your account,
2.Basically you don't have permission to capture the "cancel-disclosure-report",
3.So that take an another report which wasn't disclosed, And now request for the disclosure and capture the request in burp repeater,
4.Now again request for "cancel-disclosure-request" and capture it send it to the repeater..
                                                                                                                                   Cancel-disclosure-request
POST /reports/bulk HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/bugs?subject=user&report_id=901468&view=pending_disclosure&filters%5B%5D=not-public&filters%5B%5D=going-public-user&filters%5B%5D=going-public-team&reported_to_team=&text_query=&program_states%5B%5D=2&program_states%5B%5D=3&program_states%5B%5D=4&program_states%5B%5D=5&sort_type=latest_activity&sort_direction=descending&limit=25&page=1
X-CSRF-Token: ██████
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 184
Origin: https://hackerone.com
Connection: close
Cookie: █████
Sec-GPC: 1

message=hi&reference=&add_reporter_to_original=true&reply_action=cancel-disclosure-request&mark_ineligible_for_bounty=false&reports_count=1&report_ids%5B%5D=1078081&bounty_currency=USD
======================================================================================================================
5.Now go to repeater change the value "report_id"  to already disclosed report_id,
        My disclosed report_id:1078081
6.And send it to the server.. as you can see server accepts the request and reuqested to cancellation of disclosure of that report.
7.So after that I've try to request for disclosure for  that report, server response is report has been disclosed.
8.But when you try again for cancellation of disclosure server response is similar for older one(6th point).

## Impact

-> By this user has escalated his privileges and Done some action which were not supposed to do.
 ->IN hacker one No one has permission to cancel the disclosure the report after disclosing it.
 ->But Here user bypassed it and requested for cancellation..
 If I've done any mistake please be excuse my mistakes, And for better understanding I've attached Video POC and some pictures too..
 Thank you.
 @clubbable

## Attachments
No attachments
