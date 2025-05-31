# Registeration Link "Jacking&Redirecting"

## Report Details
- **Report ID**: 145306
- **URL**: https://hackerone.com/reports/145306
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T07:40:48.820Z
- **Disclosed**: 2016-08-05T05:30:56.860Z

## Reporter
- **Username**: raad_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: veris

## Vulnerability Information
Hello Team ,
i found dangerous issue in your register application ,
once i tried to register , the request was like that :

~~~~~~~~~~

POST /portal/register/ HTTP/1.1
Host: sandbox.veris.in
User-Agent: [[My 'User-Agent' Details]]
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://sandbox.veris.in/portal/register/
Content-Length: 1139
Cookie: csrftoken=[[CSRF]]
Connection: close

csrfmiddlewaretoken=[[CSRF]]&email=[[registered Email]]&g-recaptcha-response=[[reCaptcha]]&sub_link=----------->portal%2Fverify-email<--------------


~~~~~~~

when i edited the "sub_link" parameter with another website , ex : "example.com" .

it sends to the [[registered Email]] to verify his/her account . i realized that the link was edited to be like this :

http://example.com/registered@Email/verification/code/ !!!

user will be redirected to evil website that comes from YOUR COMPANY email telling the user to continue the registeration process .

some Evil-Hacker can do Evil-Things , like :
1) redirect to Evil Page , includes some Evil codes !
2) redirect to his OWN website , listening on port , jacking the verification code !
3) force the user with "Social Engineering" tricks to change his/her account details from Evil-Hacker website . 
and much more ...

## Attachments
No attachments
