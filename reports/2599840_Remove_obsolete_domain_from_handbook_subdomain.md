# Remove obsolete domain from handbook subdomain

## Report Details
- **Report ID**: 2599840
- **URL**: https://hackerone.com/reports/2599840
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-07-12T18:52:34.734Z
- **Disclosed**: 2024-10-01T16:41:52.627Z

## Reporter
- **Username**: tefa_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello team ,

When i research i found link Via broken domain link hijacking and i will explain that.

## Steps To Reproduce:

POC:-

1. Go to https://handbook.gitlab.com/handbook/business-technology/data-team/platform/
2. Search about this word { Snowflake roles.yml  }
3. Now you will show this domain https://gitxlab.com/gitlab-data/analytics/-/blob/master/permissions/snowflake/roles.yml and when you go to that domain https://gitxlab.com/ you will show that domain is Expired and can buy that domian.
4. In this way the attacker can takeover that domain or register by that name.

## How_To_Fix:-

Must be fix that by remove that domain from source code or replace to working domain.

## Impact

1. Domain Takeover
2. The researchers can be further deceived if they click on the hijacked link. A specific case might be for a malicious user to create a fake domian on that broken redirection link and deceive researchers arriving on that link. For example, the attacker can ask the researcher to submit his report to him first and if he approves, then only he can submit it to your official page. In this way, it can cause huge damage to your company if a critical severity report is mis-directed to the attacker.

## Attachments
No attachments
