# S3 Bucket Takeover : brave-apt

## Report Details
- **Report ID**: 1791558
- **URL**: https://hackerone.com/reports/1791558
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-03T18:16:08.727Z
- **Disclosed**: 2023-04-26T19:48:25.515Z

## Reporter
- **Username**: j3rry-1729
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Hi Team,

Hope Everything is going well on your side.

Recently I was enumerating `brave.com` and I found that there is an unclaimed S3 bucket that can be takeover by any attacker and was being used in the installation of brave-browser in Linux distros.

Vulnerable URL:-

https://s3-us-west-2.amazonaws.com/brave-apt/

Here there is an S3 Bucket that is pointing towards domain hosting services so that these domains can be taken over can be used to do any type of attack mostly I can make a fake login page on your behalf and spoof your users; this is a critical vulnerability and needs to be fixed. In this case, it was pointing toward an unclaimed S3-Bucket.

-->POC:-

Check out the attachments for more information I have claimed the subdomain through AWS S3 services. As soon as you will resolve this issue, I will release it.

 {F2060639}

I have uploaded proof.txt for further clarification.

Also, Bucket Takeover screenshots are attached.

--> Before Takeover
 {F2060641} 

AWS 
 {F2060640}


--> URL:-

`https://s3-us-west-2.amazonaws.com/brave-apt/proof.txt`


--> Steps To Reproduce:-

1) Go to any of the below-mentioned URLs

`https://community.brave.com/t/updates-on-linux-error-messages-appearing/103564`
`https://elementaryforums.com/index.php?threads/brave-browser.2390/`
`https://github.com/brave/browser-laptop/issues/13861`
`https://github.com/brave/browser-laptop/issues/12636`
`https://forums.linuxmint.com/viewtopic.php?t=300633`

2) Here you can find the `https://s3-us-west-2.amazonaws.com/brave-apt/` the S3 bucket is used for downloading brave-browser in linux distros.

3) Many users who visit the webpage to see how to install brave-browser in Linux will be redirected to the S3-Bucket, which is controlled by the attacker.

--> Video POC:-

{F2060642}

## Impact

An attacker can take over the unclaimed s3 bucket and can spread the malware using this release of brave browser then, an attacker can create a malicious file with custom payloads and can harm the user by downloading the malicious file instead of the original file.


--> References:-

https://hackerone.com/reports/1316650

https://blog.sweepatic.com/subdomain-takeover-principles/

https://hackerone.com/reports/32825

https://hackerone.com/reports/175070

https://hackerone.com/reports/172137

https://github.com/EdOverflow/can-i-take-over-xyz

## Attachments
- Screenshot_2022-12-03_at_11.28.27_PM.png
- Screenshot_2022-12-03_at_11.28.43_PM.png
- Screenshot_2022-12-03_at_11.32.33_PM.png
- Screen_Recording_2022-12-03_at_11.39.22_PM.mov
