# Access private list metadata

## Report Details
- **Report ID**: 178506
- **URL**: https://hackerone.com/reports/178506
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-27T23:17:56.864Z
- **Disclosed**: 2016-12-24T08:35:09.037Z

## Reporter
- **Username**: sameoldstory
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
# Overview

When user creates a list, they can choose to not make it public. However the attacker can still access the information that user chose to hide.

# Steps to Reproduce

1. Log in to Instacart.
2. Choose a private list that you want to see, for example the one with id = 10.
3. Go to https://www.instacart.com/api/v2/recipes/10
4. Response reveals all metadata of the list including title, description and image.

# Security Implications

The attacker can use this vulnerability to obtain metadata of any list regardless of what the visible flag is set to. Also, since list id is incremental it's easy to fetch metadata for all Instacart lists, both public and private.

## Attachments
No attachments
