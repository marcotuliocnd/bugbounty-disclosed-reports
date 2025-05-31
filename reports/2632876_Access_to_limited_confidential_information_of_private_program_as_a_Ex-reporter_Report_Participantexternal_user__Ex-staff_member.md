# Access to limited confidential information of private program as a Ex-reporter, Report Participant(external user) & Ex-staff member

## Report Details
- **Report ID**: 2632876
- **URL**: https://hackerone.com/reports/2632876
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-08-03T08:26:48.061Z
- **Disclosed**: 2024-12-24T08:48:15.122Z

## Reporter
- **Username**: sarthakbhingare015
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Technically, there are four types of users on HackerOne: Reporter, Report Participant, Triager & Staff member. Each user is part of a private program in different ways. When any of these user leave the private program, they lose access to private program. And the report participant of a private program's report already doesn't have access to the private program. None of them can view the private program with the conditions mentioned.

But I have found that after leaving the program or as a report participant of private program's report- Reporter, Report Participant & Staff member can visit private program's policy page to view limited private program details. The information exposed includes the introduction, contact email, program highlights, current state of program, when was the program details last updated, top hackers on the program, vpn state and more setting related to program in graphql request. 

This is due to a endpoint called `/:handle/hacker_demand` that seems to be for setting goals and parameters. Based on these, it shows a list of hackers who can be invited. This list of hackers is shown in a GraphQL request when you visit the endpoint. I'm sorry if this is incorrect, as I couldn't find any documentation about it. This endpoint leaks details of any program to any authenticated user on HackerOne (but this is not main concern in my report). For example: As a hacker I visited https://hackerone.com/security/hacker_demand
{F3482988}

**Description:**
So there are 3 actors in this bug- Report Participant, Ex-Staff Member & Ex-Reporter of a private program
- Report Participant (confirmed)
1. A user who is not part of private program is invited as a report participant on the private program's report. By default none of the report participant of a private program's report who is not a invited hacker/triager/staff of that program have access to the private program details.
1. When a report participant visit the /:private_program_handle, 404 Not Found page is displayed.
1. Now report participant visits /:private_program_handle/hacker_demand.
1. It will be redirected to the page similar to screenshot below.
{F3486623}
1. Upon clicking Introduction, Program Highlights, Overview, or any button below it, the hacker will be redirected to the private program's policy page revealing introduction, contact email, program highlights, current state of program, when was the program details last updated, top hackers on the private program, vpn state and more setting related to program in graphql request.
- Ex-Staff member (confirmed)
1. As a staff member, the flow of attack is exactly same: Staff leaves/is removed from the program > Visits /:private_program_handle/hacker_demand > And all the information is exposed.
1. But the only condition which must be true for Staff member is that there should be a report submitted by that staff member, only then this bug will be successful.
- Ex-Reporter (unconfirmed)

*Note: I am marking this as unconfirmed because I'm have not tested this bug for reporter. As a staff member is able to get access to the private program through a report, similarly I believe that the reporter might get too. I am informing this to make sure that the engineering team, fix this part of the bug too, if it is executable.*
1. A hacker gets invited to private program.
1. He/She submits couple of reports.
1. Hacker leaves the program.
1. When a hacker visit the /:private_program_handle, 404 Not Found page is displayed.
1. Now hacker visits /:private_program_handle/hacker_demand.
1. It will be redirected to the page similar to screenshot below.
{F3486623}
1. Upon clicking Introduction, Program Highlights, Overview, or any button below it, the hacker will be redirected to the private program's policy page revealing introduction, contact email, program highlights, current state of program, when was the program details last updated, top hackers on the private program, vpn state and more setting related to program in graphql request.

## Reference report
#2278865 - Some limited confidential information can still be accessed after a user exits a private program
#386997 - Private program policy page still accessible after user left the program
#347693 - Program metrics disclosed response_efficiency_percentage via /program_name json response despite the team decided not to show on their profile

## Impact

I classify this bug as a bypass of the referenced reports. The impact of this bug is High compared to the referenced reports. In those cases, HackerOne fixed the issue where only ex-reporters of a private program could access certain information. However, this bug leaks information to three different actors on the HackerOne platform. A report participant who was never part of a private program is able to view private program's information. This is a serious access control flaw. None of these users(Ex-reporter, Report Participant(external user) & Ex-staff member) have consent to access this data, yet they are able to.

*I apologize for not providing video proof of concept (POC). I am unable to record a POC due to technical issues with my laptop, and the HackerOne screen recorder is also not working for me.*

## Attachments
- Screenshot_2024-07-31_19_09_54.png
- Screenshot_2024-08-01_22_23_23.png
