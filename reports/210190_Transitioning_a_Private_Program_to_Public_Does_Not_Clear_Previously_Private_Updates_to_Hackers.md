# Transitioning a Private Program to Public Does Not Clear Previously Private Updates to Hackers

## Report Details
- **Report ID**: 210190
- **URL**: https://hackerone.com/reports/210190
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-02T20:17:22.083Z
- **Disclosed**: 2017-04-05T17:25:35.014Z

## Reporter
- **Username**: 0xffe4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Transitioning a private program to public does not clear the previously private updates to hackers 

**Description (Include Impact):**
If you are managing a private bug bounty program and choose to message hackers in the program with a targeted bounty campaign or other limited / private messaging, then when you take the program public that messaging will not be removed from program update page located at  https://hackerone.com/<INSERT PROGRAM>/updates.

I observed this in the wild while transitioning the Rockstar Games program to being public.  As expected, the transition properly reset all change history on the policy page (https://hackerone.com/rockstargames/policy_versions?change=3548056), but it did not clear the messaging published to just the participating hackers when the program was private.  

In this case,, we ran a special targeted bounty campaign while the program was private that we did not want to be publicly visible on launch.  We all associated messaing from the program scope prior to launching.  Once we launched the program, we noticed the text on the updates page and had to get the content manually taken down by HackerOne Support (request 22233).  This ended up being a privacy/security concern for Rockstar and could easily be one for any other program that would reasonably expect that transitioning the program messaging posted while the program was private would not be visible once public. 

The support rep who helped was: @jobert.

### Steps To Reproduce

1. Create a private program in HackerOne
2. Invite hackers/researchers to participate
3. In the program settings page, browse to Hacker Management -> Message Hackers and send a message to "All hackers who have submitted a report to your program" containing new bounty information meant for just those members of your private program"
4. Update the program scope to include information about the targeted bounty that was previously messaged to hackers
5. Run your private program as planned
6. When ready to take the program live, remove the targeted private bounty details from the program scope  
7. Launch the program public by going to Hacker Management-> Invite Hackers, then selecting the option to take the program public.  Click through the prompts to successfully publish the program.
8. Browse to https://hackerone.com/<INSERT PROGRAM>/update and find the message sent to the select hackers during the private program now publicly accessible.  


## Attachments
No attachments
