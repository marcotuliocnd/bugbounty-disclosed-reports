# Can use the Reddit android app as usual even though revoking the access of it from reddit.com

## Report Details
- **Report ID**: 1632186
- **URL**: https://hackerone.com/reports/1632186
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-09T10:25:27.729Z
- **Disclosed**: 2022-07-16T11:10:55.959Z

## Reporter
- **Username**: sateeshn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Hi Team,

For the last 4 days, I kept testing reddit web. That time, I revoked app access from the old.reddit.com and i checked my app and as expected i was not able to use the account in my app. 

After 2 days I was checking the chat invites feature on the web and after some time I turned on the internet on my mobile and got a Reddit "invitation accept"  notification. I clicked on that and I was surprised that I was able to use the previously revoked user account again in the Reddit app.

After I tried to reproduce the scenario again. I  thought the revoked account get access again after clicking on the app "chat invite" notification. 
- I again revoked the app access from the old.reddit.com
- I sent a chat invitation link to another test account and replied with the test account so that I get a "chat accept" notification in the mobile
- After several tries from several test accounts, Finally, I received the "chat accept" invitation, only one time on the mobile (Note: this is also an issue)
- I clicked on the notification and I was not able to access anything in the app (it was showing some error)
- I tried to reproduce the issue again, I don't know the reason But this time I was not able to view the chat invite links from any accounts. (it was showing some error)
- It took my whole day and I stopped testing.

The next day again I got a post notification on my mobile. I clicked on that and again I see that the app was working as usual with a previous logged-in user!!!

Finally, I came to the conclusion that whenever we revoke the app access, it works fine. But if you check the app approximately after 20+ hours you can reuse the previously logged-in account again.

## Steps To Reproduce:
  1. log in to your account from both the android mobile app and from the web(reddit.com or old.reddit.com)
  2. On the Reddit web go to https://www.reddit.com/account-activity 
  3. Navigate to the "Apps you have authorized" section
  4. Find "Reddit on Android" click the revoke access and confirm
  5. Now open the Reddit app where you have logged in step 1
  6. You are no more able to access any info about the user and it will show errors like "Let's try that again" or "uh oh something went wrong but we're not     sure what"
  7. Open the app approximately after 20+ hours and see that you can reuse the previously logged-in account without any issue.

## Supporting Material/References:
I see that I got the latest app update and trying to reproduce the issue again on the latest version i.e 2022.25.1 I will update you on it again. I assume previously my Reddit app version was 2022.25.0 or 2022.24.1
Device and version info{F1814768}
The account/username used for testing is: sateeshn_1

## Impact

Unauthorized access to account even though revoking the access.

## Attachments
- app-version.jpg
