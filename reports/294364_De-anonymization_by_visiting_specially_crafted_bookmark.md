# De-anonymization by visiting specially crafted bookmark.

## Report Details
- **Report ID**: 294364
- **URL**: https://hackerone.com/reports/294364
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-02T00:41:24.597Z
- **Disclosed**: 2018-07-03T04:35:59.675Z

## Reporter
- **Username**: qab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
There is a way to import logs in 'about:memory' from local disk, however, (tested on windows) you can pass a network url that may point to attack controlled server which logs IP's. This connection is done by windows (presumably) and so doesn't hide real IP of Tor user.

1. Have victim drag and drop an anchor tag pointing to 'about:memory?file=\\localhost\\q.json.gz' inside bookmarks bar.
2. Victim then clicks on bookmark to visit URL.
3. An unproxied connection is made to 'localhost'

## Impact

De-anonymization. If coupled with a bug to open privileged pages (which about:memory is) one could theoretically achieve a very dangerous exploit to expose real ips of victims.

## Attachments
No attachments
