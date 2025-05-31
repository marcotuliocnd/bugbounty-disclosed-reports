# Sensei LMS IDOR to send message

## Report Details
- **Report ID**: 1592596
- **URL**: https://hackerone.com/reports/1592596
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-06T19:08:06.531Z
- **Disclosed**: 2022-08-04T10:17:38.560Z

## Reporter
- **Username**: ghimire_veshraj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi there, hope you are doing great.
So, there is an option to send message to teacher privately by student on Sensei LMS.
Each message sent by student will have different ID,
Student1 cannot access or send message to the message from Student2 (which is meant to be private with teacher)
Similarly Student2 cannot view/send message sent by student1 to the teacher.

But due to lack of access control, it is possible for any student to reply on any thread of Student to teacher just by simply changing ID of the thread which is numeric.

This may sound a bit complex but i will try to explain this with video POC, please let me know if you still didn't understood the vulnerability here:
{F1759226}

## Impact

Any student can reply to other student's thread which is meant to be private between the original student [who sent message] and teacher.

## Attachments
- recording-1654542444545.webm
