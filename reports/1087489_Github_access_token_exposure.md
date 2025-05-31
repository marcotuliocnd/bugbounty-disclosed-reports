# Github access token exposure

## Report Details
- **Report ID**: 1087489
- **URL**: https://hackerone.com/reports/1087489
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-01-26T13:03:40.914Z
- **Disclosed**: 2021-07-26T19:50:02.320Z

## Reporter
- **Username**: augustozanellato
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
While dissecting an application made by one of your employees I found his GitHub Personal Access Token (PAT), he's a member of the org with pull and push access to all of your repositories. 
As a proof I can tell you that on the repo github.com/Shopify/shopify at commit hash `cea9c273391d` the sha512 of the README.md is `69750574bec56c1f1052db3471252b1daacdc9dda9f6d5332a3400a847fa413ec1caf19ef0b5501f18a5a76c232e7210d5f3b91c24c9439f4e0f64c02d6db824`.

## Impact

Read and write access to all your private github repositories.

## Attachments
No attachments
