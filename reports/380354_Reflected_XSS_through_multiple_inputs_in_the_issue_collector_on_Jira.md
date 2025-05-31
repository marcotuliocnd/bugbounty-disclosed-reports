# Reflected XSS through multiple inputs in the issue collector on Jira

## Report Details
- **Report ID**: 380354
- **URL**: https://hackerone.com/reports/380354
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-11T00:51:16.595Z
- **Disclosed**: 2020-03-24T19:56:12.757Z

## Reporter
- **Username**: jackb898
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: roblox

## Vulnerability Information
**Note I put this as Medium because that's what the CVE is. This vulnerability is known and it's classified under CVE-2018-5230. Here's a link to the thread on it by Atlassian: https://jira.atlassian.com/browse/JRASERVER-67289
Description
---------------------
I noticed when testing that your Jira installation at jira.roblox.com is running on version 7.6.3, which isn't the latest version. When you have something like Jira or Wordpress, having the latest installation is critical because lots of vulnerabilities for previous versions will be disclosed right after the company releases the latest version. That was the case here.

So I decided that since it was on 7.6.3, I'd check CVEs and see if there were any that effected Jira installations 7.6.3 and newer. After a LOT of scouring (there's tons of CVEs for Jira on older or different platforms) I found CVE-2018-5230, which isn't very helpful but it led me in the direction of the issue collector.

CVE-2018-5230 outlines "XSS in the issue collector" but doesn't specify anything, so that was left up to me.

Locations
---------------------
After some testing in all of the issue collector, I've compiled this list of the reflected XSS locations in it. To make it easier, I've set this up with each having it's own number and explanation on how to use it.

There's only one filter that I've found for these; when using certain HTML tags like "src=" and in JS alerts using alert("texthere"), it appends two backslashes, ex. if you put in this payload: 
```
<iframe src="//google.com"></iframe>
```
The output in the page will be:
```
<iframe src="\&quot;//google.com\&quot;"></iframe>
```
HOWEVER I found a bypass to this filter; instead of using double quotes, simply use all single quotes in payloads. For example if you use the payload 
```
<iframe src='//google.com'></iframe>
```
The output will be:
```
<iframe src="//google.com"></iframe>
```

1ST AREA
https://jira.roblox.com/issues/?filter=-8 in the "Updated Date" section. 
HOW TO EXPLOIT:
1. Go to the link above
2. Click the "Updated Date:" text area
3. Put your XSS payload in "More than [ ] minutes ago" (15 character payload limit) or in "In range [   ] to [   ]" (No length limit, ONLY put the payload in the first box)
4. Click Update
5. Payload will run. If it doesn't run chances are you used double quotes somewhere. Only use single quotes!

Each area past this first one uses the exact same method of exploitation and has the same inputs/outputs so I'll just put the links to them
https://jira.roblox.com/issues/?filter=-7
https://jira.roblox.com/issues/?filter=-6



Resolution
---------------------
Update your JIRA version to 7.6.7 or later, might as well update to the latest version. This should sufficiently patch all of these vulnerabilities.

Additional Information
---------------------
I know this isn't a core Roblox domain but I strongly believe it has the same impact regardless; as you can see from the attachment: 
{F319184} 
The core Roblox cookies are shared onto this domain, so that's a main factor in why this has equal impact as to if it were on roblox.com.

## Impact

An attacker could use carefully crafted payloads with simple social engineering to steal Roblox user's accounts. As I've mentioned, the cookies from Roblox's core site are shared with this one as well, and while it may not be a core Roblox site, it's still a *.roblox.com so any suspicions of phishing by the victim could be excused with that reasoning.

Additionally, with XSS you can use specially designed iframes linked to your own JS content, allowing jacking of cookies and other information from the victim.

## Attachments
- fb6e03df7ca0f99504a9d2b39770dc0d.png
