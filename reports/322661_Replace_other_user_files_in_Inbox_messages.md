# Replace other user files in Inbox messages 

## Report Details
- **Report ID**: 322661
- **URL**: https://hackerone.com/reports/322661
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-05T21:31:42.132Z
- **Disclosed**: 2018-05-01T21:35:32.882Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Summary
When a store publishes their listing, a user can message them if they are interested. Company can reply to this query and also add a file. When a file is uploaded, the link looks like this: 
https://shopify-exchange-private.s3.amazonaws.com/attachments/<filename>. This file can be replaced if the attacker knows the filename. 

# Description
After submitting the store validation bypass, I played around with the application and noticed that when I submit a query it lands on my inbox: 
{F269678}

Inside the inbox there is an option to attach files. When I replied to the query with a file attached, I noticed that it uploaded the file. For this test, I created a file with the name `dudeuranium238.pdf`. This was an empty PDF I made with `touch dudeuranium238.pdf` in my computer. Once I uploaded the file, I visited to https://shopify-exchange-private.s3.amazonaws.com/attachments/dudeuranium238.pdf and saw this: 

{F269679}

Now thinking as a malicious hacker, I decided to make another store and publish that as well. I did the same process all over again and replied again with the file `dudeuranium238.pdf` but this time, this file actually had content. It contained a PDF with `Scanner report for Uber` that I keep when hacking. So, once uploaded I went back to https://shopify-exchange-private.s3.amazonaws.com/attachments/dudeuranium238.pdf and the file was replaced: 

{F269682}

# Reproduction
1. Make sure you have 2 published store. 
2. Start a query in one store and send an attachment through inbox. 
3. In the second store do the same thing as number 2 but make sure you replace the file ***content** not the name

## Impact

Replacing content of someone else's file.

## Attachments
- Screen_Shot_2018-03-05_at_1.26.43_PM.png
- Screen_Shot_2018-03-05_at_1.28.27_PM.png
- Screen_Shot_2018-03-05_at_1.30.17_PM.png
