# XXE at ecjobs.starbucks.com.cn/retail/hxpublic_v6/hxdynamicpage6.aspx

## Report Details
- **Report ID**: 500515
- **URL**: https://hackerone.com/reports/500515
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-02-24T15:49:52.803Z
- **Disclosed**: 2019-11-13T00:36:25.662Z

## Reporter
- **Username**: johnstone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Description:**
Hi,guys,when i was visited the jobs of starbucks websites in China(https://ecjobs.starbucks.com.cn), i found a features of uploaded user's photo.Thought the bypass the security restrictions of upload,i can upload html|xhtml|xml|config files etc.The uploaded html file can realize the danger of stored xss,and the uploaded xml file can be  parsed by the server,Through tested, the server does not prohibit the use of doctypes, entities, and access to external dtd files. 

## Steps To Reproduce:

Upload and XXE vulnerability: 
1. Log in to the user, enter the personal information settings page, click Upload Image 
2. Intercept https access information through Burp suite
3. addd "html;" attributes in the parameter of "allow_file_type_list",or you can delete the params of "allow_file_type_list",then replace the filename's Suffix name ".jpg" to ".html"
4. Get the server's response information,visited the uploaded file URL.
https://ecjobs.starbucks.com.cn/retail/tempfiles/temp_uploaded_641dee35-5a62-478e-90d7-f5558a78c60e.html
5. uploaded a malicious xml file to the server,change the parameter of "_hxpage"，like

>POST /retail/hxpublic_v6/hxdynamicpage6.aspx?_hxpage=tempfiles/temp_uploaded_d4e4c8c5-c4ab-4743-a6fd-c2d779a29734.xml&max_file_size_kb=1024&allow_file_type_list=xml;jpg;jpeg;png;bmp;

or change the "HX_PAGE_NAME" params of xml date by post

>POST /retail/hxpublic_v6/hxxmlservice6.aspx HTTP/1.1
HX_PAGE_NAME=&quot;tempfiles/temp_uploaded_71cc275c-64fc-40fc-a9cc-52cce5a02858.xml&quot;


post the edited request,the starbucks's server will visit the attacker's server to get the DTD file.

## Impact

The vulnerability can  let the attacker upload the evil files in the server which will spoof the user,steal the user's cookie and informations.The XXE  vulnerability disclose some server's informations ,denial of service attack，maybe will cause NTLMv2 hash attacks through XXE(the starbucks'server environment is iis 7.5+asp.net+windows), which could lead to  attackers having full control over the server and the entire inner domain.
By the way,if the report isn't considered eligible.please let me close this report myself.Thank you

## Attachments
- iis_log.png
- html_1.png
- xxe1_1.png
- xxe2_2.png
