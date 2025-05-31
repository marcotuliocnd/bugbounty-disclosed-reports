# Private target account appears in search results

## Report Details
- **Report ID**: 708696
- **URL**: https://hackerone.com/reports/708696
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-10-06T20:58:36.402Z
- **Disclosed**: 2019-11-06T09:00:06.202Z

## Reporter
- **Username**: magic_spell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
##Summary
At policy page, there are special tailor account, highly confidential & secret !
{F600997}

- Hide this profile from search results on Liberapay
- Prevent this profile from being listed on Liberapay
- Target account `hackerone-target-team`

##Description
In this exploit, I found Privacy setting unable to perform well.

This will give owner an idea of what we are capable of doing against a victim's account on the Liberapay platform.

###Step to Reproduce
1 Without an account created, no authentication

2 Go to https://liberapay.com/ 
{F601006}



3 Now click the search button, located at magnificent icon

4 Please type `hackerone-target-team` . Click Go button

5 Now narrow down to the search list, Found Matching Usernames. You will found it appears

Proof-of-Concept
{F601007}

6 When you hover the first one (upper-left in green square), you will get the node appear, which is same exactly to policy page target account URL. https://liberapay.com/hackerone-target-team

Please click & you'll success found this hidden target account

Proof-of-Concept `hackerone-target-team`
{F601036}

7 This mean the setting of privacy doesn't work well :(
Because `hackerone-target-team` should not appear at search result & listed there.

8 If we narrow down a bit, the other hidden account just found under this embedded page `hackerone-target`
{F601045}

## Impact

- Privacy violation for `hackerone-target-team` . Even the setting had set to hide this profile from search result by program owner

- Attacker succeed to crawl `hackerone-target-team` from search listing,
victim privacy break here

## Attachments
- confidential2.png
- search_button.png
- found_in_Search.png
- hackerone-target-team.png
- hackerone-target.png
