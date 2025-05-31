# Full access to InDrive jira panel via exposed API token 

## Report Details
- **Report ID**: 1785145
- **URL**: https://hackerone.com/reports/1785145
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-11-27T16:29:51.090Z
- **Disclosed**: 2023-06-28T09:21:07.265Z

## Reporter
- **Username**: bogdantcaciuc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
**Description**

Hello!

Browsing through GitHub I found the following repository:

███


Looking for interesting keywords, the following file popped up:

███████


```
package ru.indriver.jira.api

object Constants {
    const val jiraHost = "https://indriver.atlassian.net"
    const val baseUrl = "$jiraHost/rest"
    const val token = "██████"

    ███
    // const val token = "██████=="
}
```


The repository wasn't updated in a while, but I still decided to give it a change and try to make an API call with the auth token:

curl -i -s -k -X $'GET' \
    -H $'Host: indriver.atlassian.net' -H $'Cache-Control: max-age=0' -H $'Authorization: Basic ████' -H $'Content-Type: application/json' -H $'Sec-Ch-Ua: \"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'Sec-Ch-Ua-Platform: \"macOS\"' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: none' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Sec-Fetch-Dest: document' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7' \
    -b $'atlassian.xsrf.token=450f5681-becb-48d1-a8bc-efc045d75244_08e86700250ae917acc90fead0122eca3628f5a5_lout' \
    $'https://indriver.atlassian.net/rest/api/2/issue/67212'

Surprisingly, this was sucessfull and I was able to fetch a random issue ID, which normally I wouldn't have access to because you're instantly getting redirect to the atlassian OAuth flow if you're visiting https://indriver.atlassian.net/


**Steps to reproduce:**


1. Do the following cURL:
```
curl -i -s -k -X $'GET' \
    -H $'Host: indriver.atlassian.net' -H $'Cache-Control: max-age=0' -H $'Authorization: Basic ████████' -H $'Content-Type: application/json' -H $'Sec-Ch-Ua: \"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'Sec-Ch-Ua-Platform: \"macOS\"' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: none' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Sec-Fetch-Dest: document' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7' \
    -b $'atlassian.xsrf.token=450f5681-becb-48d1-a8bc-efc045d75244_08e86700250ae917acc90fead0122eca3628f5a5_lout' \
    $'https://indriver.atlassian.net/rest/api/2/issue/67212'
```
Notice the response:

███████

We have full access to the InDrive Atlassian panel, ability to fetch sensitive information.

## Impact

Sensitive information disclosure - full access to the Atlassian panel - projects/issues/accounts etc.

## Attachments
No attachments
