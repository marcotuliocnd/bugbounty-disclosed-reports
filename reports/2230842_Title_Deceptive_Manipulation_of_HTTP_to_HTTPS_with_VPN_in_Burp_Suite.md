# Title: Deceptive Manipulation of HTTP to HTTPS with VPN in Burp Suite

## Report Details
- **Report ID**: 2230842
- **URL**: https://hackerone.com/reports/2230842
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-29T02:55:41.989Z
- **Disclosed**: 2023-10-31T09:10:56.646Z

## Reporter
- **Username**: rexifylo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Description:
I identified a deceptive behavior in the Burp Suite application, combined with the use of a VPN, that can potentially mislead attackers into thinking a website has downgraded from HTTPS to HTTP when it is still using HTTPS. This action may not pose a significant threat, but it can lead to attacker misdirection. The scenario can be categorized under CWE-319: Cleartext Transmission of Sensitive Information.

Steps to Reproduce:

    Set up the target website and ensure that it uses HTTPS for secure communication.

    Open the Burp Suite application and configure it to intercept and manipulate traffic between the client and server.

    Initiate a session with the target website through Burp Suite's proxy.

    In Burp Suite, manipulate the response to make the attacker believe the website has downgraded to HTTP (e.g., modify response headers).

    Use a VPN for added anonymity during this process.

    Observe the attacker's response and their behavior, as they might adapt their attack techniques thinking the connection is unencrypted.

## Impact

Deception: The attacker is misled into thinking the connection is unencrypted (HTTP), which might lead them to adjust their attack techniques. This can provide a slight advantage to the defenders.

    Wasted Resources: The attacker may allocate unnecessary resources to exploit an apparently vulnerable HTTP connection, which can be seen as a waste of their time and efforts.

    False Sense of Security: On the flip side, if the attacker believes the website has downgraded to HTTP, they might not take encryption and security precautions as seriously, potentially leading to data breaches if they act recklessly.

And Reputational damage due to when the attacker finds out it is really HTTPS not HTTP they might find a different application besides burp suite

## Attachments
- 2023-10-28_22-52-35.mkv
