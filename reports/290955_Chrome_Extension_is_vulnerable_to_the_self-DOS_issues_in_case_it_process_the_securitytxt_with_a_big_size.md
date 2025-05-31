# Chrome Extension is vulnerable to the self-DOS issues in case it process the security.txt with a big size

## Report Details
- **Report ID**: 290955
- **URL**: https://hackerone.com/reports/290955
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-16T18:27:13.862Z
- **Disclosed**: 2017-12-18T20:21:01.933Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
##Description
Hello. Before all, thanks for the invite:) Here is keyword: `frog`
I discovered the self-DOS issue, which affects Chrome extension.

##Impact
I marked the impact as low, because it will affect only the browser tab, and will not impact other browser tabs. The issue happens due to processing the large files using AJAX call in the `getSecuritytxt` function.

##Steps to reproduce
1. Create security.txt with the size of 1-2 GB on your host.
2. Navigate to this site in the Chrome Browser (at this time you may notice traffic and CPU utilization increasing due to pre-flight check of the security.txt)
3. Click on the extension. Depending on the Chrome version, amount of RAM and CPU, you can experience one of (or all together):
 * Extension hang
 * Tab hang
 * Tab crash

##Suggested fix
Since we are making AJAX calls to the untrusted hosts, end extension is working for the every site we opened in the tab, we should get rid from such kind of issues. I suggest to implement `timeout` on the AJAX calls using
```
xhr.timeout = 15000; //some value in milliseconds
xhr.ontimeout = function (e) {
//handling timeout
}; 
```
I will link the Github PR in the comment below:)


## Attachments
No attachments
