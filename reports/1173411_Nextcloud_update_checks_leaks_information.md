# Nextcloud update checks leaks information

## Report Details
- **Report ID**: 1173411
- **URL**: https://hackerone.com/reports/1173411
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-04-23T18:40:54.452Z
- **Disclosed**: 2021-05-01T10:53:03.940Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,

I think this is more of a privacy concern than a security concern. However I wanted to check here first. Please direct me to an other suitable location if needed.

It is in relation to https://github.com/nextcloud/server/blob/master/lib/private/Updater/VersionCheck.php#L78

This is sending several things related to servers to Nextcloud. Especially the 'installedat' seems to have a very high likely hood to be unique for an instance. Allowing Nextcloud to track instances when doing the requests.

I especially wonder why you chose this method here. Instead of the 'appstore' approach were you just have an big blob and have the server figure everything out.

Other than that I could not find any mention about what data is send to Nextclouds servers and why.  One could argue that pinging the updates.nextcloud.com has a legitimate reason. However I doubt that regarding the more track sensitive information. And even then it would be OK if you'd communicate about this clearly.

Again sorry if this is the wrong place. But I didn't wanna post this publicly if it is in any way sensitive.

## Impact

This could potentially cause legal issues if you are sending data that is not needed and identifiable.

## Attachments
No attachments
