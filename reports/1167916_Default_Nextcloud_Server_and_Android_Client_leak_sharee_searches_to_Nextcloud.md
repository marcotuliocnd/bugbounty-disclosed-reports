# Default Nextcloud Server and Android Client leak sharee searches to Nextcloud

## Report Details
- **Report ID**: 1167916
- **URL**: https://hackerone.com/reports/1167916
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-18T18:12:19.193Z
- **Disclosed**: 2021-06-15T19:11:31.101Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
On a clean Nextcloud setup the functionality "Search global and public address book for users" is enabled.

Now when searching for a sharee to share with. The lookup parameter is not passed to the server. Resulting in
https://github.com/nextcloud/server/blob/master/apps/files_sharing/lib/Controller/ShareesAPIController.php#L144

the lookup being true. So the lookup server of Nextcloud will be searched by default.
It seems that the lookup server is down now. But this seems to be an error I assume?

## Impact

Anybody sharing trough the android app. Leaks their sharee searches to the Nextcloud lookup server.
Now the server can can only see the origin Nextcloud server (or rather the IP of that). Still. This should not be leaked by default.

On the web and desktop there is first a local search. And only if the user explicitly presses the search globally the lookup server is queried. (to be fair this could also be more clear that it actually sends data to other systems)

## Attachments
No attachments
