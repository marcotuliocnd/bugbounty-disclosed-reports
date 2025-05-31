# User Controllable Cookie

## Report Details
- **Report ID**: 459502
- **URL**: https://hackerone.com/reports/459502
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-10T07:19:06.476Z
- **Disclosed**: 2018-12-21T11:41:02.137Z

## Reporter
- **Username**: 8r33
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

User Controllable Cookie

## Impact

Hi Team.

I dont know whether it is eligible for bounty or not, just want to let you know that cookies are not validating by the server when the requests comes from an un-authenticated user. Which means an attacker can set user cookie (Physically) and later attacker can set the same cookie at his browser and can perform malicious activities (can't track user activities accurately).

Also tested it is not possible with the authenticated user but may lead other possible vulnerabilities in future as it is a important cookie (PHPSESSID). Please check the screenshot and also the below URL (Only for reference provided netsparker link and not used for scanning or to attack).

https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/user-controllable-cookie/

Request:

GET /prices/ HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.semrush.com/
Connection: close
Cookie: __cfduid=d9a20cdc29bb669cf81a08a4c2163b3fd1544327906; ref_code=__default__; _ga=GA1.2.2040835093.1544327932; _gid=GA1.2.80444391.1544327932; _gcl_au=1.1.1610616523.1544327935; firstVisitLangPopover=1544327939775; tracker_ai_user=o4IKL|2018-12-09T03:59:02.368Z; XSRF-TOKEN=HLvWVGzDM4djGHhZKL60AQ3bnVmzvifQiVlTYZcW; community-semrush=sOumS5cgNF3LBF88Llo8Fn156SI8OvNb84TySmXa; blog_split=A; mindboxDeviceUUID=8d068032-f62b-43ab-ada6-4e40d62b4a45; directCrm-session=%7B%22deviceGuid%22%3A%228d068032-f62b-43ab-ada6-4e40d62b4a45%22%7D; _fbp=fb.1.1544327977281.107930240; usertype=Unlogged-User; marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D; db=us; PHPSESSID=abcdefghijklmnopqrstuvwxyz123456; n_userid=LuWkzVwMlitLugAnBhGfAg==; localization=%7B%22locale%22%3A%22en%22%7D; community_layout=3bme3nsv8m2oghsd1ar1qmdo42; csrftoken=kyH9GSPJMyWz07vXyo2T6opdO0HQrGuDvXCTjMN5bQz6SclCubwPCUpRCTof0mmr; _gat=1
Upgrade-Insecure-Requests: 1

## Attachments
- 4.png
