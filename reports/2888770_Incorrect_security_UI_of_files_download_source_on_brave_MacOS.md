#  Incorrect security UI of files' download source on brave MacOS

## Report Details
- **Report ID**: 2888770
- **URL**: https://hackerone.com/reports/2888770
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-12-09T11:15:46.105Z
- **Disclosed**: 2025-01-16T22:17:26.441Z

## Reporter
- **Username**: syarif07
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
This vulnerability involves the incorrect display of the download source in the Brave download alert. Instead of displaying the actual source of the downloaded file, the browser displays the referrer header value, which may mislead the user into believing that the file is from a trusted source. This behavior creates a potential security risk as it could allow attackers to trick users into downloading malicious files.

## Products affected: 
Brave is up to date
Version 1.73.97 Chromium: 131.0.6778.108 (Official Build) (arm64)

## Steps To Reproduce:
1. Victim visit: https://ybt01.github.io/upload/google.html#
2. Victim click `click me to download google apk` and will pop up download location with wrong files origin

{F3826618}

## POC 
{F3826622}

## Expected result

The origin source on the download pop up should accurately reflect the actual source of the downloaded file, indicating the URL from which the file was downloaded directly (e.g., https://ybt01.github.io).

## Actual Result

The origin source on the pop up displays the URL of the referring page (e.g., https://google.com), thus misleading the user about the actual source of the downloaded file.

## Supporting Material/References:
This issue is similar to the one in the report: https://issues.chromium.org/issues/352681108 
but this is a different case because in chrome it is not affected. and in brave it is affected in the download pop up while in the chromium report it is affected in chrome: //downloads. However, in terms of impact and scenario this case is similar.

## Impact

This vulnerability can significantly impact user security by providing misleading information about file downloads. Users may unknowingly trust files downloaded from malicious sources, believing they originated from reputable domains. This can facilitate the distribution of malware and other harmful software, especially in targeted attacks by Advanced Persistent Threat (APT) groups or malicious websites that employ social engineering tactics. As a result, the risk of unintentional malware installation on user systems increases, undermining the overall security posture of users.

## Attachments
- image.png
- Screen_Recording_2024-12-09_at_17.58.51.mov
