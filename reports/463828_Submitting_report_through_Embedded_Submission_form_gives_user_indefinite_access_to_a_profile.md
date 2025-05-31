# Submitting report through Embedded Submission form gives user indefinite access to a profile

## Report Details
- **Report ID**: 463828
- **URL**: https://hackerone.com/reports/463828
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-17T13:12:53.576Z
- **Disclosed**: 2019-01-03T10:01:02.311Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team, @jobert , @ben

After testing on the sandbox, I noticed that one of my accounts(which I removed from the program) can see some of the information. I don't know if it affects other programs that have other States - `private-only`, `private-only` whit external link.  I could not find the uuid of any of these programs, perhaps you could help me with this (`Give me uuid of one of the programs :)`)? or check it yourself


**Description:**
After sending the report, and exit the program, we can continue to see the main page of the program.
I can't fully imagine the situation here, as it was done on the sandbox and the account that was team_member

If you can help me figure it out, I'll be happy. I think that it will work for ordinary users as well. After sending such a report, we will be able to see the main page of the program, which we do not have access to


### Steps To Reproduce

My PoC for report

1. Create sandbox program
2. Invite any user ( my 2 account - █████████)
3. Admin create embedded_submissions link for program
4. 2 account create report for /embedded_submissions link

My link - ██████████

5. Next we leaved the program , or admin kick(delete) 2 account
████████

6. Check the page with the second account
█████████

7. We are will be see main page info.

I think it's a bit like this report #386997

### Optional: Did you use recon data made available by HackerOne to find this vulnerability?

no

I understand the complexity of the operation here, but also, I understand that if it works for the average user and the program is not public, then the seriousness will increase. But unfortunately I can't verify that. I barely found this connection . I created a report in support when I didn't see the connection, but now I can find it. So you can close that report -- https://support.hackerone.com/hc/en-us/requests/256487

***I want to ask you to check the connection of the steps***

1) Create embedded_submissions report for external program whit private page
2) Create embedded_submissions report for external program whitout private page
3) Create embedded_submissions report in a private program (located in it), after leaving it, and check whether we will see the main page


And at the end check whether the user will see the program page

If it turns out to be invalid, please give me a chance to close the report myself.

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

Viewing information of the program, after leaving her

## Attachments
No attachments
