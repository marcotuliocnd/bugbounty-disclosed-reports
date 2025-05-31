# index.php/apps/files_sharing/shareinfo endpoint is not properly protected

## Report Details
- **Report ID**: 1173684
- **URL**: https://hackerone.com/reports/1173684
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-24T10:20:41.349Z
- **Disclosed**: 2021-08-11T09:18:40.381Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
When federated shares between two Nextclouds are created they do not use standard webdav to communciate. But to obtain the filelist they seem to use the `SERVER/index.php/apps/files_sharing/shareinfo` endpoint.

Unlike the other endpoint for tokens (like public link shares). There is no brute force protection here. So this could be used as enumeration endpoint for available tokens. This is not likely to generate a hit due to the search space. But considering you do limit this on the public link endpoint for example it still seems relevant.

Now this brings me to the second part that struck me on this endpoint. It is essentially sending back the entire file tree below it. Meaning if this is a big file tree it you could just keep sending requests to the server keeping it quite busy. (and all requests are valid and won't be flagged). There is no rate limiting at all.

Then this brings me to the final part This endpoint accepts all token shares. Even link share tokens (meaning you don't even have to use the 'add to your Nextcloud'),  (and there is no check if federation is enabled). So in short. If you have a link share with a big file tree (or you create it yourself if there is write access).

## Impact

Possible to perform denial of service attacks by sending a lot of valid request that could lead to a significant number of queries and memory usage on the system.

## Attachments
No attachments
