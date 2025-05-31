# Host header injection that bypassed protection and allowed accessing multiple subdomains

## Report Details
- **Report ID**: 1783015
- **URL**: https://hackerone.com/reports/1783015
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-24T00:48:45.623Z
- **Disclosed**: 2022-12-21T17:37:36.842Z

## Reporter
- **Username**: musashi42
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: urbancompany

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Name of Vulnerability:*Host header injection/SSRF
**Areas affected:** [App/ Website + URL/Location] https://www.urbancompany.com  and it allowed accessing otherwise inaccessible subdomains https://av.urbancompany.com , https://ims.urbancompany.com , https://mesh.urbancompany.com
**User Details:** [Registered Email and Registered Mobile Number used for the purpose of signing up an account with Urbanclap] N/A
**Summary:** [add summary of the vulnerability] Ability to access certain subdomains (which should be presumably only for internal/trusted sources ) through host header manipulation.
to be able to access.
**Description:** [add more details about this vulnerability]

## Steps To Reproduce:

(Add details for how we can reproduce the issue through manual testing only)

  1. Go to any of the three subdomains using any browser and after a while you'll see this:

{F2046658}


  2. Using burp and Match and Replace rule:

{F2046655}

 3. Now using burp chromium go to https://www.urbancompany.com , 
and you'll see the following for the Host: mesh.urbancompany.com:

{F2046657}


and for Host: av.urbancompany.com:

{F2046651}

and for Host: ims.urbancompany.com:

{F2046654}


Some interesting endpoints:
For av.urbancompany.com:

{F2046652}


{F2046653}



For mesh.urbancompany.com, potentially means ability to access user files, but because I don't know any of the files I was unable to confirm if it would ask for some authorization upon request to the existing file:

{F2046659}

This endpoint looks interesting, but for some reason it doesn't actually initiate any uploading when I tried to upload files with mentioned extension:

{F2046656}


Additional note:
All three subdomains resolve to the same ip address, which implies that if you have other subdomains associated with this ip address those subdomains are probably affected by this bypass as well.

Thank you for looking into this, and please let me know if you have any questions and/or if you need me to do some more testing, like fuzzing all the found endpoints to determine if there are some interesting bugs there.

Sincerely,
@musashi42

## Supporting Material/References:
Attached are the screenshots.
  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Impact is dependent on whether ability to access the subdomains in question is considered as a bypass and if any of the disclosed information (especially various accessible js files) shouldn't be accessible in this way, in addition if there are more sensitive endpoints that I simply didn't find with my limited wordlists but larger wordlists would find. In addition, there's also a question if more interesting subdomains are associated with the same ip address as the three that I mentioned in the report and if those subdomains are even more interesting for the attacker because this bypass should work on any subdomain that's been associated with the ip address of the three mentioned subdomains.

## Attachments
- av-login.png
- av-forgotpasswd-emaildisclosed.png
- av-reportsaspx-groupnames-disclosed.png
- ims-login.png
- match-replace.png
- mesh-player.png
- mesh-loginscreen.png
- mesh-timedout.png
- mesh-userfiles.png
