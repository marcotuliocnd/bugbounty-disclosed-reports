# [██████████] — Directory traversal via `/aerosol-bin/███████/display_directory_████_t.cgi`

## Report Details
- **Report ID**: 686343
- **URL**: https://hackerone.com/reports/686343
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-02T13:07:41.992Z
- **Disclosed**: 2020-05-14T18:03:22.211Z

## Reporter
- **Username**: usamasood
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Description

On the domain `https://█████████`, there is a vulnerable endpoint that lets an attacker preview and browse the whole server including all the server's critical directories such as `etc` , `var`, `cache` etc. located in the root directory of this Linux web server.

This vulnerable endpoint is found on many pages across this web app including:

https://www.██████████/aerosol-bin/██████/█████.html_t.cgi?date=20070301

## Proof of concept

Please visit the following URLs for the POC:

1. https://www.█████████/aerosol-bin/████/display_directory_███_t.cgi?DIR=/etc

███

2. https://www.████████/aerosol-bin/████████/display_directory_████████_t.cgi?DIR=/var

█████

3. https://www.███/aerosol-bin/█████/display_directory_████_t.cgi?DIR=/var/lib

██████

## Fix

To fix this issue, the `DIR` parameter must be properly validated to show only data in the directories that is supposed to be public and must not go above public folders (public_html) in any case.

## Impact

This vulnerability can reveal all the information about the web server including any libraries installed, any sensitive directories, potentially allowing an attacker to leverage this to compromise the web server.

Thanks,
Usama

## Attachments
No attachments
