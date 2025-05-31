# csrf blogs.starbucks.com

## Report Details
- **Report ID**: 198470
- **URL**: https://hackerone.com/reports/198470
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-01-14T22:18:13.663Z
- **Disclosed**: 2017-08-15T00:47:38.122Z

## Reporter
- **Username**: w2w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
We can add comments on any article from the the user's account
Request

POST /blogs/customer/archive/2016/05/06/starbucks-doubleshot-174-energy-coffee-makes-a-flavorful-foray-into-the-realm-of-spiced-coffee.aspx HTTP/1.1
Host: blogs.starbucks.com
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://blogs.starbucks.com/blogs/customer/archive/2016/05/06/starbucks-doubleshot-174-energy-coffee-makes-a-flavorful-foray-into-the-realm-of-spiced-coffee.aspx
Cookie: CommunityServer-UserCookie2101=lv=Sat, 14 Jan 2017 08:58:35 GMT&mra=Sat, 14 Jan 2017 13:55:33 GMT; optimizelyEndUserId=oeu1484428996826r0.3642673872554443; optimizelySegments=%7B%22192119771%22%3A%22false%22%2C%22192128716%22%3A%22direct%22%2C%22192132656%22%3A%22ff%22%2C%222529560039%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; AMCV_5EE340D7545285B80A4C98A2%40AdobeOrg=283337926%7CMCIDTS%7C17181%7CMCMID%7C82885818390245048184434598124321834684%7CMCAID%7CNONE%7CMCAAMLH-1485033823%7C6%7CMCAAMB-1485033856%7Chmk_Lq6TPIBMW925SPhw3Q%7CMCCIDH%7C1508474359; s_pers=%20s_dfa%3D%7C1484431330615%3B%20v10%3Danonymous%7C1515965612151%3B%20gpv_p5%3Dus%253Astarbucks%253Aaccount%253Acreate%7C1484431412157%3B%20s_visit%3D1%7C1484431412158%3B%20s_lv%3D1484429612160%7C1579037612160%3B%20s_lv_s%3DFirst%2520Visit%7C1484431412160%3B; s_sess=%20s_cc%3Dtrue%3B; _ga=GA1.2.182169753.1484429018; __utma=247112134.182169753.1484429018.1484429023.1484429023.1; __utmc=247112134; __utmz=247112134.1484429023.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=247112134.|2=Username=F65FB5D9-B713-46A9-841A-0721C04B670D=1^4=Loyalty=NotMember=1; aam_uuid=82892360004990649684433061568237689286; CommunityServer-LastVisitUpdated-2101=; .SBUX=DB0D6453A2B4CD018D7B843BA27297ADD40E8B5BBA2ADD184660BB263519EB25863A4B664A928D6110F72EE4029C616CD605CE665884E8C32E26B495E71280F1C357BD6F4479FEBE0853E6A24B29B10187A3F4968482468149D368CED2A3E2D6B1B972E1C99094C0A694FCCC987D025186402C7AFDB59AF0B88CE0A2816574367A06AFAA8C650CF80BA90970433A48D69CF75BF123B4B7532C712CF96A40F9483BE5E63494774931598A9B0FB2DDA11B2A65EF1365745DAE6FFC878F7D63F351A3CFB1F1E973BBFF14FECA42C7790DC3F99C8446FD3DEA227D41C9C680FFD550DC61C524407B1A14F5BB0DD589A36FD6B5E0C8509AA9E3872556C049526EDA006CDE8794; .SBUXMSI=Email=admin1@blogs.starbucks.com&CommonName=admin1&EnableDisplayName=true&AppUserToken=&SSO-LastUpdated=06/00/2017&Partner=False&Site=MSI; _gat_mobifyTracker=1; CommunityServer-UserCookie116960=lv=Fri, 01 Jan 1999 00:00:00 GMT&mra=Sat, 14 Jan 2017 14:07:03 GMT; CommunityServer-LastVisitUpdated-116960=; .CSRoles=bjT4TeyC4qbCpZr-FgXAwR8UP_kbu_O89t8gVolKk9M9tN3_7EqO-Rk_JfVdHMFVufh7Pntjkrbnwfg-V9yX3noLColJRZ1PDSMQNxcBpZUY-YndG0O-QqqGcMdndrzGui3BJKKNAu2dXClVFRYULJDqwdQ3UBV4wYF3ThYR-3e8tGRfeX1lSElahsuC-HwAG3HoLCpxLzumSmtyUsED1uKd_TvgK8G1IBCbPZR3Siehd8Jg7wMS13gsPtXiObtpZDQnzy2JClu5469rE9xZbg9Jw0OVdNokM3bFqN6mmsVDqciqkmiaIHe7ZhbzlqZWgr3DBLJ5Np0IHMGC7gJLveLYY3JBayvM6zROqlAeqfM4JFwXgmZd7kTxqWVuKX0dUYoUwXpuF1rDeqBt1Fe56P3LPHfdoC__KHXvOo7DHMtHfBpcdkZElOLPkAGzOq2U0hV2bKqQpSYcV18uSp7H5gBe0HPcGcSGzdb1wM3y13MmaU_lxUir3LSf7bJuGhHjYP_04v0eaa4qkoaYjMT58TLFU5VfXVxSvNQdwgj_5UDXFwsvRJ725s0IPjlT_1tdHDScGU41jIpEInzcn2CdVtuWLWY1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 737

__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTAzMjQzOTk5N2QYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFP2N0bDAwJGN0bDAwJGN0bDAwJGJjciRiY3IkYmNyJGN0bDA1JGN0bDAyJGN0bDAxJGN0bDA1JGJ0blN1Ym1pdAVYY3RsMDAkY3RsMDAkY3RsMDAkd2lkZ2V0cyR3aWRnZXRzJGN0bDAwJGN0bDAxJGN0bDAwJGN0bDAxJGN0bDAxJGN0bDAwJFRpdGxlQmFyU2VhcmNoVGV4dK6mHQmFRTslZmBQA9gstDzF%2Bweu&ctl00%24ctl00%24ctl00%24bcr%24bcr%24bcr%24ctl05%24ctl02%24ctl01%24ctl05%24tbComment=qwqw&ctl00%24ctl00%24ctl00%24bcr%24bcr%24bcr%24ctl05%24ctl02%24ctl01%24ctl05%24btnSubmit.x=51&ctl00%24ctl00%24ctl00%24bcr%24bcr%24bcr%24ctl05%24ctl02%24ctl01%24ctl05%24btnSubmit.y=23&ctl00%24ctl00%24ctl00%24widgets%24widgets%24ctl00%24ctl01%24ctl00%24ctl01%24ctl01%24ctl00%24TitleBarSearchText=search

Missing CSRF token and Content-Type: application/x-www-form-urlencoded , good, make csrf exploit

https://securityz.net/starg.html .

When the victim went to the link, a comment will be added in a few minutes:
Thanks for sharing your feedback! If your feedback doesn't appear right away, please be patient as it may take a few minutes to publish.

Please, add csrf token to this request..

## Attachments
No attachments
