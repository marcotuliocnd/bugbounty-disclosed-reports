# Default settings leak federated cloud id to lookup server of all users

## Report Details
- **Report ID**: 1173436
- **URL**: https://hackerone.com/reports/1173436
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-23T19:30:51.348Z
- **Disclosed**: 2021-06-10T13:41:03.219Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So with the default settings Nextcloud still sends requests to the lookup server if users update their profile. Even if none of the fields are set to 'published'. 
I must admit this is somewhat of a surprise as there is no reason for this. As long as the visibility of none of the fields change and none of them are published. 

The background job is inserted in the function
https://github.com/nextcloud/server/blob/master/apps/lookup_server_connector/lib/UpdateLookupServer.php#L62

And the DELETE that is executed
https://github.com/nextcloud/server/blob/master/apps/lookup_server_connector/lib/BackgroundJobs/RetryJob.php#L156

Looking at the lookup server code it seems to actually do the delete. Still users of course can't verify what is running there. So we have to assume the worst case scenario where the lookup server has a list of a significant portion of all the nextcloud users out there.

## Impact

The nextcloud server is still sharing the federated cloud id of every user to the lookupserver. Unless an admin explicitly disables the lookupserver.
Even if non of the fields are set to published.

## Attachments
No attachments
