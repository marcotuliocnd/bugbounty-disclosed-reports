# S3 Bucket Takeover  "brave-browser-rpm-staging-release-test"

## Report Details
- **Report ID**: 1835133
- **URL**: https://hackerone.com/reports/1835133
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-01-14T06:46:59.149Z
- **Disclosed**: 2023-04-26T19:48:38.825Z

## Reporter
- **Username**: j3rry-1729
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Hi Team,

I hope Everything is going well on your side.

Recently I was enumerating `brave.com` and I found that there is an unclaimed S3 bucket that can be a takeover by any attacker and was being used in getting keyrings of brave-browser in Linux distros.

Vulnerable URL:-

https://s3-us-west-2.amazonaws.com/brave-browser-rpm-staging-release-test/

Here an S3 Bucket is pointing towards domain hosting services so that these domains can be taken over and can be used to do any attack. Mostly, I can make a fake login page on your behalf and spoof your users; this is a critical vulnerability and needs to be fixed. In this case, it was pointing toward an unclaimed S3-Bucket.

-->POC:-

Check out the attachments for more information I have claimed the subdomain through AWS S3 services. As soon as you resolve this issue, I will release it.



I have uploaded proof.txt for further clarification.

Also, Bucket Takeover screenshots are attached.

--> Before Takeover

{F2120563}

AWS 

{F2120566}

After Takeover:

{F2120564}

--> URL:-

`https://s3-us-west-2.amazonaws.com/brave-browser-rpm-staging-release-test/proof.txt`


--> Steps To Reproduce:-

1) Go to the below-mentioned URL

`https://community.brave.com/t/cant-install-brave-in-opensuse-leap-15-1/157685/3`

2) Here you can find the `https://s3-us-west-2.amazonaws.com/brave-browser-rpm-staging-release-test/` the S3 bucket is used for getting the keyrings in linux distros.

***Moreover this keyrings were hosted on this bucket previously but now I think the bucket is changed to `https://s3-us-west-2.amazonaws.com/brave-browser-rpm-staging-release/` for downloading the binaries but  this `test` bucket is not reclaimed so that's why I am making this report***

You can also see this by using this URL where you can download the keyrings from the original bucket `https://s3-us-west-2.amazonaws.com/brave-browser-rpm-staging-release/x86_64/brave-keyring-1.8-1.noarch.rpm`.

{F2120562}


But from the `test` bucket you can't download as it is available for takeover.

3) Many users who visit the webpage to see how to get the keyrings for brave-browser in Linux will be redirected to the S3-Bucket, which is controlled by the attacker.

## Impact

An attacker can take over the unclaimed s3 bucket and can spread the malware using this keyrings of brave browser then, an attacker can create a malicious file with custom payloads and can harm the user by downloading the malicious file instead of the original file.


--> References:-

https://hackerone.com/reports/1316650

https://blog.sweepatic.com/subdomain-takeover-principles/

https://hackerone.com/reports/32825

https://hackerone.com/reports/175070

https://hackerone.com/reports/172137

https://github.com/EdOverflow/can-i-take-over-xyz

## Attachments
- Screenshot_2023-01-14_at_12.01.27_PM.png
- Screenshot_2023-01-14_at_12.00.40_PM.png
- Screenshot_2023-01-14_at_12.11.03_PM.png
- Screenshot_2023-01-14_at_12.13.29_PM.png
