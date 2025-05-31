# Names not completely redacted despite "Redact the names of the involved users" is selected

## Report Details
- **Report ID**: 2122644
- **URL**: https://hackerone.com/reports/2122644
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-08-24T15:19:41.159Z
- **Disclosed**: 2023-08-29T09:51:52.217Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi @security @zerotea,

Hope you are doing well.

Today I have found a special edge case where the names are still visible despite "Redact the names of the involved users" is selected on export as .pdf report. This is similar to the resolved reports #2109009 and #2054222.

But this time, looks like the root cause is coming from a team member that triggers the `agreed on going public` and `report became public` activity on the report but did not leave any single comment on the report, I have found that when the involve user (names) of a team member that did not put any comments but he is the one who agreed to disclose this report, then his name will be visible on the report despite the  `"Redact the names of the involved users"` is selected

Please note that just observed that today because of this disclosed report today from @linkedin: 

Disclosed Rerport: [Improper access control on Linkedin Page](https://hackerone.com/reports/1587246)

While reading that report, i tried to export that as .pdf and I selected the option `Redact the names of the involved users`, then I saw that the name of the team member who `agreed to disclose report report` is still visible on the activity.

__Name:__ `Emmanuel L.` 


### Steps To Reproduce

1. Go to this disclosed report from LinkedIn: https://hackerone.com/reports/1587246
2. Export the report as .pdf , make sure to select the `Redact the names of the involved users`
3. Check the report output and you will see below acitivity

`Emmanuel L. 2023-08-24 02:42 report became public Public`
`Emmanuel L. 2023-08-24 02:42 agreed on going public Public`

For easier step to reproduce, you can just visit this https://hackerone.com/reports/1587246.pdf?redact_usernames=true&pdf_type=reporter

{F2632963}

## Impact

Disclosing the supposed to be redacted data, sensitive information disclosure.

Let me know if you have any question

Regards,
@japz

## Attachments
- poc0.PNG
