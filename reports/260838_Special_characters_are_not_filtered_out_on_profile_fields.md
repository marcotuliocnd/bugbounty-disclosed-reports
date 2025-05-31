# Special characters are not filtered out on profile fields 

## Report Details
- **Report ID**: 260838
- **URL**: https://hackerone.com/reports/260838
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-16T22:33:17.411Z
- **Disclosed**: 2017-08-26T23:24:32.058Z

## Reporter
- **Username**: falconnexus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
hi there , 

While looking around into your web application I noticed in the fields Firstname and Lastname you can set a url . example ` ( http://www.evilsite.com) ` .  where I am using special characters like `://` and `.` . but when I try out other special characters - or particularly a payload such as `"><svg/onload=prompt(1)>` , it will not be allowed in the first name and last name fields . which means as a protection mechanism this is getting filtered out along with the additional special characters . again using null valus like `%00%` , is allowed in the fields and updates First name or last name , so it means when you are trying to update your name with such values your name is getting reverted back to the old one .

The intended behavior is not applied for all cases , that is why first name and last name can be updated with multiple special characters and null values . I think usage of special characters should be controlled and checked again by you guys . as you are filtering out payloads which potentially contain multiple special characters but you are allowing usage of special characters in under few circumstances . 

I am also attaching a video . Hope you will check and get back with a response soon . 

Thanks . 



## Attachments
- legalrobot.mov
