# Staff and Triage can modify the initial post of a report, including of already disclosed reports

## Report Details
- **Report ID**: 2096271
- **URL**: https://hackerone.com/reports/2096271
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-04T09:51:22.679Z
- **Disclosed**: 2023-08-28T11:33:37.531Z

## Reporter
- **Username**: zerotea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
FULL DISCLOSURE: I am a HackerOne employee and learned about it through this submission: https://███████-/issues/67828

**Summary:**

Members of the HackerOne program (and likely other program members on their own program) and Triage can edit the information of the original report

I used https://hackerone.com/reports/2000000 to demonstrate and the changes have since been reverted.

**Description:**

### Steps To Reproduce

1. Go to any report, disclosed or undisclosed
2. Press "edit information" on the original post
3. Edit & save.
4. Your changes are saved 

### Optional: Supporting Material/References (Screenshots)

{F2560190}
{F2560189} {F2560191}
{F2560195}

## Impact

Members and Triage can rewrite the story the hacker is trying to tell and edits are not transparant

- Give hackers a bad image in disclosed reports
- Tell a different story or lower impact artificially
- The body is supposed to be immutable after 20 minutes

## Attachments
- Screenshot_2023-08-04_at_11.50.05.png
- Screenshot_2023-08-04_at_11.48.18.png
- Screenshot_2023-08-04_at_11.50.26.png
- Screenshot_2023-08-04_at_11.53.14.png
