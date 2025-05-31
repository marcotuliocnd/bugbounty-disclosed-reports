# Reflected XSS on www.hackerone.com and resources.hackerone.com

## Report Details
- **Report ID**: 840759
- **URL**: https://hackerone.com/reports/840759
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-05T20:14:22.252Z
- **Disclosed**: 2020-05-05T17:47:24.733Z

## Reporter
- **Username**: todayisnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Good day :)

I hope your doing as well as can be during these difficult times.

I have found xss at 2 endpoints:

https://www.hackerone.com/resources/

and 

https://resources.hackerone.com

The payloads that work are here:

https://www.hackerone.com/resources/read/embed_mini/11690/122736?miniPop=false&alwaysCover=false&miniTitle=XSS+POC&miniColor=333333&miniLinkToTitle=true&miniUrl=http://example.com%22%22,})%3C/script%3E%3Csvg+onload=confirm(location)%3E&miniBg=FFFFFF&hideBg=true&width=380&height=330&sharing=true

https://resources.hackerone.com/resources/read/embed_mini/11690/122736?miniPop=false&alwaysCover=false&miniTitle=XSS+POC&miniColor=333333&miniLinkToTitle=true&miniUrl=http://example.com%22%22,})%3C/script%3E%3Csvg+onload=confirm(location)%3E&miniBg=FFFFFF&hideBg=true&width=380&height=330&sharing=true


I've attached screenshots, the xss is intermittent, I'm not sure why maybe a cookie, maybe ip blocking, I'm not sure, but it happens :)

If it helps for others I have no idea what I am doing most of the time and brute force try things until they work :) 

Always learning, always feeling I know so little, and so much to learn, its awesome working together we all contribute our knowledge and effort :)

I've been taking a break the last few weeks to help to support family in this time of need, any bounty that is awarded I'm adding hackforgood as a collaborator and donating 100% of the bounty.  

It is great that hackerone is implementing this option to let us if we are in the position to share to donate funds, we have the option via the platform :)

It was shared with me that "You can add hackforgood as a collaborator on your reports and weight your bounty percentage on how much you’d like to donate. Our team will submit donations at the end of each month to WHO’s Covid-19 Response Fund" hope it works here will give it a shot :)

As always I wish you well on your side of the screen, to your loved ones, and that you can find both mental and physical wellness as much as possible right now :)

-Eric

## Impact

xss on the site, low risk since a marketing site :)

## Attachments
- resources.hackerone.com-xss.png
- www.hackerone.com-xss.png
