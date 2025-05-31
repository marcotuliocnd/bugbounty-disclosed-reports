# Targeted phishing attacks in Login flow v2

## Report Details
- **Report ID**: 1169033
- **URL**: https://hackerone.com/reports/1169033
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-19T18:35:52.117Z
- **Disclosed**: 2023-03-03T07:38:55.211Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The login flow v2 is used by the desktop client.

The attack vector assumes the attacker knows the recipient somehow and knows their username and email (or other way to contact them).

In short it is following the steps from https://docs.nextcloud.com/server/21/developer_manual/client_apis/LoginFlow/index.html#login-flow-v2
(examples are also taken from there)

1. Attacker send a request to: curl -X POST https://cloud.example.com/index.php/login/v2
   They can even set the user agent to something that the user will trust. Like 'Company X verification', 'or just dekstop client' or whatever.

2. Attacker obtains the response like

{
    "poll":{
        "token":"mQUYQdffOSAMJYtm8pVpkOsVqXt5hglnuSpO5EMbgJMNEPFGaiDe8OUjvrJ2WcYcBSLgqynu9jaPFvZHMl83ybMvp6aDIDARjTFIBpRWod6p32fL9LIpIStvc6k8Wrs1",
        "endpoint":"https:\/\/cloud.example.com\/login\/v2\/poll"
    },
    "login":"https:\/\/cloud.example.com\/login\/v2\/flow\/guyjGtcKPTKCi4epIRIupIexgJ8wNInMFSfHabACRPZUkmEaWZSM54bFkFuzWksbps7jmTFQjeskLpyJXyhpHlgK8sZBn9HXLXjohIx5iXgJKdOkkZTYCzUWHlsg3YFg"
}

3. Now the attacker send the login URL to the victim.
4. The victim logs in, granting the attacker an access token to access all their data.

The login URL seems to only be valid for 10 minutes. However this is still a 10 minute window the user can be attacked.
The attacker could even setup a url that when clicked on will perform the steps in the background and then redirecting them. Making sure the token is always valid.

The issue here is that there is no warning for the victim that what they are about to do is potentially giving an attacker access to their data. And they can do all the checks when they are on the auth page but it is actually the legit page of their Nextcloud instance.

I'd suggest to work with some verification.For example. Show a 2 digit code (or as many digits as you are comfortable with) and have that be entered in the desktop client screen. That way the attacker has to time it right and be very lucky. Making the attack a lot less likely. As the victim would also notice 'what do you mean I have to enter a code on my device?'

## Impact

Possible granting of access token to the attacker. Resulting in access to all data of a victim.

## Attachments
No attachments
