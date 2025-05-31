# Open redirect due to scanning QR code via brave browser

## Report Details
- **Report ID**: 1946534
- **URL**: https://hackerone.com/reports/1946534
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-14T02:48:43.133Z
- **Disclosed**: 2023-06-08T04:52:38.278Z

## Reporter
- **Username**: roland_hack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:
This vulnerability was discovered in Brave's QR code scanner, which allows users to read QR codes and open corresponding links. Exploitation of this vulnerability allows attackers to direct users to malicious sites without their consent or knowledge. This vulnerability can put the security of Brave users at risk and allow them to be exposed to phishing, phishing and malware attacks. In this report, we'll describe the vulnerability in more detail, assess its severity, and provide recommendations to address it.



## Products affected: 

Brave 1.50.114, Chromium 112.0.5615.49 on Android 11; Build/RP1A.200720.011

## Steps To Reproduce:

{F2291837}

The QR code above is the one I generated to replicate the attack.
To create my QR code, I used the site https://app.qr-code-generator.com.
 I included a malicious link in this QR code. As an example link, I used www.evil.com

#  Steps To Reproduce

 -  Open the browser 
- Then in your browser you can click on the "scan a QR code" option and scan the QR code in which I have included my malicious link. 
This will automatically redirect you to the malicious site I inserted in the QR code, without even asking your opinion.
- However, some QR code scanners do not automatically redirect the user to the malicious site, but rather display the link with the "Go to site" option. Other scanners don't even show this option. 
- However, in the case of Brave, the browser automatically redirects the user to the malicious site without their consent, which poses a significant security risk to users.


## Supporting Material/References:

https://resources.infosecinstitute.com/topic/security-attacks-via-malicious-qr-codes/
https://shahjerry33.medium.com/open-redirection-qr-code-magic-18ace1a0170f

## Impact

Here are some potential business impacts that this security vulnerability could have in Brave 1.50.114, Chromium 112.0.5615.49 on Android 11; Build/RP1A.200720.011:

The fact that Brave's QR code scanner opens the link without the user's notice has a big impact on user security. This vulnerability allows an attacker to redirect a Brave user to a malicious site without the user being able to see the link and make an informed decision. This can lead to exposure to malware or phishing attacks that can compromise user data.

The actual impact depends on the nature of the malicious link to which the user is redirected. In the worst case, the link may be designed to steal sensitive information, such as credit card information, credentials, or other personal information. This can lead to loss of privacy and financial damage to the user.

Moreover, if the user is redirected to a malicious site that contains malware, then it can compromise the security of the user's device and lead to loss of important data. Overall, the fact that Brave's QR code scanner automatically opens malicious links without user's notice poses a significant risk to user security and should be fixed as soon as possible.

    Increased Risk of Phishing: Exploiting this vulnerability could allow attackers to direct Brave users to malicious sites that can be used to steal sensitive information such as usernames, passwords, banking and other personal information.

    Exposure to malware: Malicious sites that users are redirected to may also contain malware that can infect Brave users' devices with malicious programs such as viruses, Trojans or ransomware.

    Privacy loss: Brave users may also be at risk of privacy loss if sensitive information is stolen as a result of the exploitation of this vulnerability.

    Loss of user trust: If Brave users fall victim to attacks as a result of exploiting this vulnerability, they may lose trust in the application and seek out more secure alternatives, which could impact reputation of the application and the company.

    Financial costs: If users fall victim to attacks as a result of this vulnerability, they may suffer financial losses, which may lead to legal action and financial costs to the company responsible for the application.

## Attachments
- QR_CODE_BRAVE.png
- brave_poc.mp4
- goole_lens.mp4
- brave_poc_-QQYAkWpYDyu5Qz_U3pIXg.mp4
