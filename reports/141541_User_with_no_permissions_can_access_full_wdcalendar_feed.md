# User with no permissions can access full wdcalendar feed

## Report Details
- **Report ID**: 141541
- **URL**: https://hackerone.com/reports/141541
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-27T20:13:45.187Z
- **Disclosed**: 2016-11-25T16:02:11.700Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
Hi All,
I've found a vulnerability related to access the calendar when a user has no permissions.

##Vulnerability
I've create a doctor's account with a user who has no permission. Browsing the site, I noticed a call to ```https://1337test.drchrono.com/wdcalendar/datafeed/105756?method=list&showdate=5%2F27%2F2016&viewtype=examroom&timezone=0&doctors[]=99120```

Using this URL via the account with no permissions appears to return the full calendar feed (I've trimmed it for this report):

{"templates": [], "start": "05/27/2016 00:00", "end": "05/28/2016 00:00", "events": [["30273638", "Daniel Kivatinos: Exam 4", "05/27/2016 09:00", "05/27/2016 09:45", "0", "0", "0", "2", "4", "#BFBFFF", {"provider_id": 99120, "secondary_insurer": " ", "primary_insurer": " ", "billing_status": "", "duration": 45, "appt_is_break": false, "scheduled_time": "09:00 AM", "appointment_status": "", "patient_name": "Daniel Kivatinos", "chartid": "KIDA000005", "provider": "[ [ 5*5 ] ] [ [ 5*5 ] ]", "patient_id_for_photo": 59493758, "exam_room_name": "Exam 4", "real_examroom": 4, "view_id": "30273638", "display_examroom": 4, "reason": "General Visit", "birthday": "03/20/1980", "date": "Friday May 27", "referring_doctor": "", "patient_phone": "", "office_name": "[ [ 5*5 ] ]", "copay": "No copay information on file", "patient_provider": "[ [ 5*5 ] ] [ [ 5*5 ] ]", "gender": "Male", "age": "36", "readable_datetime": "Fri May 27 at 09:00 AM", "office_id": 105756, "billing_status_disabled": false, "created_at_utc": "2016-05-25T20:21:28+00:00", "notes": ""}, 99120, ""], 

##Steps to reproduce
1. Create a doctor's account
2. Add a staff member with no permissions
3. If you have access to a proxy like burp, use it and visit the calendar
4. Log out and log in as the staff member
5. Open the proxy and grab the wdcalendar feed url
6. Paste it in the browser

You now have access to the calendar data

##Vulnerability
This seems to be a pretty significant information disclosure vulnerability. Each patient's billing information is available, some personal information (gener, age, phone, etc), appointment notes, etc. All appointments appear available as well.

Please let me know if you have any questions.
Pete

## Attachments
No attachments
