# Privilege escalation allows to use iframe functionality w/o upgrade

## Report Details
- **Report ID**: 594080
- **URL**: https://hackerone.com/reports/594080
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-06-02T17:09:25.032Z
- **Disclosed**: 2019-06-05T08:03:55.287Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hello team!

I've found a privilege escalation issue which allows to set iframes to the projects w/o upgrading.

### Steps to reproduce
- Login
- Navigate to the project
- Choose `integrations` and click the `IFrame`
- See that you'll get `upgrade now` notification
{F501019}
- Inspect the page with developer tool and choose the `upgrade` from `IFrame` icon
- Delete the `data-upgrade="true"` part
{F501023}
- Click the `IFrame` and see that you are able to add iframe to the page w/o upgrade
{F501024}


If you need any information please let me know.

Cheers!

## Impact

Users can use functionalities without paying

## Attachments
- upgrade.png
- data-upgrade.png
- iframe.png
