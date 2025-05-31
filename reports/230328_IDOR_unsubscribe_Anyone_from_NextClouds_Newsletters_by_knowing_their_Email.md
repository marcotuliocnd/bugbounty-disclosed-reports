# IDOR unsubscribe Anyone from NextClouds Newsletters by knowing their Email 

## Report Details
- **Report ID**: 230328
- **URL**: https://hackerone.com/reports/230328
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-20T21:09:48.352Z
- **Disclosed**: 2017-09-16T12:08:09.114Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team, 

I Was Looking around your website and then I found a subdomain newsletter.nextcloud.com on the main page it shows us 3 Options i choose 1st that was ( Subscribe to our newsletter ) , Then I click on this Option and I was Taken to  https://newsletter.nextcloud.com/?p=subscribe&id=1 The page where i have to put my info to subscribe to NextClouds Newsletter....

###Now the Subscription Mechanism have 3 Verification Methods Before anyone can Subscribe to your news letter 

1) Type Email Twice 
2) reCAPTCHA
3) A link which the person will receive in Email to confirm his/her subscription

Now I Did all these Steps and Successfully subscribed to Your Newsletter with my Email

Then For Testing purpose I took the link from where i subscribed 

#Subscription Link
https://newsletter.nextcloud.com/?p=subscribe&id=1

And added 'un' before it the link become like:

#Unsubscribe Link:
https://newsletter.nextcloud.com/?p=unsubscribe&id=1

Now the page shows me a Single Input Place where i have to Put my Valid Email ( From Which I have subscribed ) , I Simply Put my email their and Clicked on Continue 
And the Page Displayed a Message

"You have been unsubscribed from our newsletters and you will receive a confirmation message shortly"

And at the End I Received A email with the Confirmation that i have been unsubscribed from the NextClouds Newsletter

I did The Process again with different Emails and every time i was able to unsubscribe without Any Confirmation, unlike the Subscription Form where I had to put My Email twice, the reCAPTCHA & the Confirmation email from newsletter@nextcloud.com

#How can it effect?

Well its a Hard question but as it have no confirmation or a CAPTCHA Cotrol on the page a malicious User can Unsubscribe anyone that have subscribed to newsletter by simply knowing his email somehow, also a Case can be like thsi as i mentioned No CAPTCHA Control a Bruterforce Can be Done like getting an email list and performing the attacl ( To try this i have send more than 60 request under a minute through Burp Intruder and teh response to all the Requests was 200OK means No rate limiting ) Resulting Bruterforcing.

#Remedy?

Well you can add a reCAPTCHA on the Unsubscribe page and also add an email Confirmation same as one a user get while subscribing same Newsletters...

#Note:
I have attached all the Screenshots with the report, & Also If you don't accept Reports about your Website on Hackerone Kindly send a Way by whichi can send this report... 


Thanks,
Muhammad Khizer Javed
https://hackerone.com/babayaga_
https://bugcrowd.com/MuhammadKhizerJaved

## Attachments
- 01.PNG
- 02.PNG
- 03.PNG
- 04.PNG
- 05.PNG
- 06.PNG
- 07.PNG
- 08.PNG
