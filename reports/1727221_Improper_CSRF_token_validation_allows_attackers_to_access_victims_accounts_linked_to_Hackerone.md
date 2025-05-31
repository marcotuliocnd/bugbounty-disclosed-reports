# Improper CSRF token validation allows attackers to access victim's accounts linked to Hackerone

## Report Details
- **Report ID**: 1727221
- **URL**: https://hackerone.com/reports/1727221
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-10-08T11:11:49.758Z
- **Disclosed**: 2023-06-19T20:15:24.936Z

## Reporter
- **Username**: medmahmoudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
### Overview:

Organisations in Hackerone can automate their workflow by integrating their accounts with their existing tools like Github or Jira. Most of these integrations are built on top of Tray.io's embedded product.

According to this [article](https://tray.io/customers/story/hackerone). Hackerone has established Tray Embedded as central integration hub to deliver high-quality customer integration.

### Flawed Authorization flow

I have created two sandbox Hackerone accounts and picked the github integration for testing. This [link](https://docs.hackerone.com/programs/github-integration.html) explains very well how to setup the integration on your account.

When we click on "New Authentication", an exchange starts between Hackeron's integration authentication server and the service provider. 

{F1976245}

The authentication integration server is ```hackerone.integration-authentication.com```. The following are steps of the authorization flow:

1. The flow starts with a POST request to
```hackerone.integration-authentication.com/session```

 {F1976252}

The response contains two tokens: ***session*** and ***csrf***. 

2. The frontend takes those values and uses them to send a request to the oauth2 endpoint to generate the authorization link.

```
https://hackerone.integration-authentication.com/oauth2/auth/:authentication_id?csrf=QDXo8g3vciWTiV9Mm1L-VpYl6hKQCE-4ORmMFliZNh8=&scope=read:org%20repo&session=78NgOnCMPISn0LPw4Zto5HFSRLJwJyLaJqqi6_bFmXU=
```

 {F1976253}

3. Following the redirection takes us to the authorization page of the service provider

 {F1976255}

If we choose to Authorize Hackerone, we will get redirected to the token callback endpoint:
```
hackerone.integration-authentication.com/oauth2/token?code=47b070b577c905d66124&state=507dad3e-aa80-4fee-8ec1-a04ad95aea83%2CQDXo8g3vciWTiV9Mm1L-VpYl6hKQCE-4ORmMFliZNh8%3D%2C%2Chackerone.integration-configuration.com%2Cproduction%2C78NgOnCMPISn0LPw4Zto5HFSRLJwJyLaJqqi6_bFmXU%3D
```
 

This endpoint validates the code received from Github, the backend relies on the ***state*** parameter to determine to which user should the Github access token be appropriated. Then it redirects us to the callback endpoint ```https://hackerone.integration-configuration.com/auth/cb?id=507dad3e-aa80-4fee-8ec1-a04ad95aea83``` which sends a postmessage to the embedded iframe to validate the integration on the client side.

By analyzing these requests, I found that step 2 was not well protected against cross site forgery attacks. The unproper validation of the CSRF token puts all Hackerone's customers at a big risk. With one click from the victim, the attacker couldtrick the victim to link their Github(or any other integration built on top of Tray.io) to the attacker's account.

### POC:
{F1976267}


### Reproduction Steps:
. Attacker creates a program then starts setting up a an integration(for example Github)

. Attacker keeps forwarding requests until a GET request similar to

```
https://hackerone.integration-authentication.com/oauth2/auth/<Auth ID>?csrf=F_Sr5vd7hWMLSkZoubYOTMbwROI922ZU6q1S4fEF43E=&scope=read:org%20repo&session=1iydW3sIKpyTGxhG8lxeWY9ddzaUknoUJT9Rr51ptMc=
```

. Attacker copies the request's url then drops it. He then sends it to the victim and hopes for the best

. Victim clicks on the link

Two options:
1. if the victim has already linked the company's Github to the Hackerone. Github won't ask for user's conscent. The victim would be redirected the callback endpoint

```
https://hackerone.integration-configuration.com/auth/cb?id=<Auth ID>
```

The victim would have no idea of what happened

2. The app would ask the user if they'd give their conscent to Hackerone. If the victim trusts Hackerone, there is a high chance they would click Yes.

. Once the victim's authorization is finished. The attacker can change the location of authentication window to 

```
https://hackerone.integration-configuration.com/auth/cb?id=<Auth ID>
```

This step is just to convince the frontend that the authorization has successfully finished.
The victim's account is linked to the attacker's account now. Depending on the scope of each integration, there is a wide variety of post exploitation scenarios the attackers could use.

## Impact

Once the victim's app is connected to the attacker's hackerone account, there are a lot of post exploitation scenarios an attacker can use. The tray's graphql basically gives the attacker the option to make unauthorized arbitrary calls to the API of the application is question. What makes this vulnerability critical is that it could be reproduced on multiple integrations.

What an attacker could do for example is prepare a list of exploit links and prepares a javascript code that opens all the links is seperate windows. Each link would try taking over a specific integration. This way, the attacker could take multiple integrations at once with one user click.

### Post Exploitation:

One of those options is using the Tray.io's graphql. Tray.io has a graphql for its customers that takes care of requesting the integration API's for them.
 
For example, the query to fetch the the victim's github repositories, including the private ones is similar to this one:

```
POST /graphql HTTP/2
Host: tray.io
Content-Length: 512
Sec-Ch-Ua: "Not;A=Brand";v="99", "Chromium";v="106"
Accept: */*
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer aad14176400b44bb97b703b4ae1077a5c84c3b7f97e34f5383643c1c8a22cdf4
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://hackerone.integration-configuration.com
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackerone.integration-configuration.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{"operationName":"CallConnector","variables":{"input":{"connector":"github","version":"2.2","operation":"raw_http_request","authId":"22583997-4aa0-4bb8-87cb-28326dc97868","input":"{\"method\":\"GET\",\"parse_response\":\"true\",\"include_raw_body\":\"false\",\"url\":{\"endpoint\":\"/user/repos?per_page=50&page=1&affiliation=owner%2Ccollaborator%2Corganization_member\"}}"}},"query":"mutation CallConnector($input: ConnectorCallInput!) {\n  callConnector(input: $input) {\n    output\n    __typename\n  }\n}\n"}
```

## Attachments
- image.png
- image.png
- image.png
- image.png
- PoC_Hackerone.webm
