# bypass of this Fixed #2437131 [ Inadequate Protocol Restriction Enforcement in curl ]

## Report Details
- **Report ID**: 2905552
- **URL**: https://hackerone.com/reports/2905552
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-12-18T04:33:49.646Z
- **Disclosed**: 2024-12-19T11:52:13.197Z

## Reporter
- **Username**: hackeriron1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

A flaw has been identified in the curl command-line tool related to its protocol selection mechanism. Specifically, the protocol restrictions set by the --proto option can be bypassed, allowing unintended protocols to be used despite explicit restrictions. This flaw can result in plaintext communication being used even when the user has attempted to disable all protocols except encrypted ones.

##Vulnerability Details
   Command Triggering the Issue:
curl --proto -all,-http http://example.com

##Observed Behavior:
    The command was intended to disable all protocols and then explicitly disable HTTP.
However, the actual behavior allowed HTTP requests to be made, indicating that the protocol restrictions were not enforced correctly.

##Bypass Example:
```
    curl --proto =all http://example.com
    curl --proto http http://evil.com
```

The command curl --proto =all appears to override the protocol restrictions, allowing HTTP requests to bypass the intended restrictions.

##Steps to Reproduce
 Execute Command with Protocol Disabling:
```curl --proto -all,-http http://example.com```

Observe Error Message:
    Error: curl: (1) Protocol "http" disabled

Execute Bypass Command:
   ` curl --proto http http://evil.com`
    
Observe Successful Request:
The request is made over HTTP despite the initial restrictions.

##Potential Risks
    Security Breach: Users may believe they have enforced secure communication protocols, but the flaw could result in unencrypted communication, increasing the risk of eavesdropping or man-in-the-middle attacks.
User Trust: Users trusting curl for secure communication may be misled by incorrect protocol enforcement.

##Mitigation
    Update curl: Ensure that you are using the latest version of curl, as this issue might be addressed in newer releases.
Use Explicit Protocols: Instead of disabling protocols, explicitly specify the protocols you want to allow:
   ` curl --proto https https://example.com`

##Recommendation
    Report to Maintainters: Consider reporting this issue to the curl maintainers if it has not been already reported. Provide them with detailed reproduction steps and observed behavior.

## Impact

## Summary:
Unencrypted Communication: The flaw allows requests to be made over unencrypted protocols (such as HTTP) even when the user has explicitly disabled plaintext protocols.
Data Exposure Risk: This can lead to potential exposure of sensitive data if transmitted over an unencrypted link.

## Attachments
No attachments
