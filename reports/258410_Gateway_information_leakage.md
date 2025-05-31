# Gateway information leakage

## Report Details
- **Report ID**: 258410
- **URL**: https://hackerone.com/reports/258410
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-09T20:52:01.353Z
- **Disclosed**: 2019-07-30T14:42:04.222Z

## Reporter
- **Username**: hackerfactor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Many DoD systems use BlueCoat gateways. These gateways insert unique BlueCoat ids that permit tracking DoD users and gaining insight into the DoD network architecture when DoD users access the Internet.

**Description:**
I run a popular web service (FotoForensics.com -- it's around 150,000 in the Alexa list of top web sites).  My public web site is explicitly for research and gets visitors from all over, including from the DoD.  One of the research project collects non-standard HTTP headers.  The BlueCoat HTTP headers immediately stood out as non-standard.

Someone with a BlueCoat gateway will have headers that look like:

> POST /upload-file.php HTTP/1.1
> Host: www.fotoforensics.com
> Content-Length: 70869
> Cache-Control: max-age=0
> Origin: http://www.fotoforensics.com
> Upgrade-Insecure-Requests: 1
> User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
> Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryPaSgeQQ5m6kh7aaZ
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
> Referer: http://www.fotoforensics.com/
> Accept-Language: en-█████████,en;q=0.8
> ██████████: ██████ (███) SC
> Connection: Keep-Alive
> █████████: █████████

(This example came from a user at the United States Patent and Trademark Office.)

The id found on the "██████████" line is unique to the Bluecoat device; it is not unique to the user. However, if this ID ever shows up at a different network address, then it permits a remote (outside of DoD) system to identify associated network addresses, multiple proxy exits, and potentially non-attributable networks. Similarly, if a single IP address is associated with multiple Bluecoat ids, then it denotes a single exit proxy and identifies the (minimum) number of subnets that use the proxy.

For example:

> █████████
> ██████
> ██████████
> █████████
> ████████
> ██████
> ██████████

My server has seen this one IP address associated with 7 different Bluecoat devices.

> ███
> ████
> █████████
> ██████████

This single bluecoat ID has been linked to four different network addresses.

> ███
> ████████

This bluecoat id (████) is interesting because it has been seen on two very different subnets.

> █████████
> ███

This bluecoat ID moved locations: it was seen in████ and in/near ███████. (Imagine what it could tell an observer if it were to suddenly appear in █████████...)

I have currently collected 243 bluecoat IDs associated with "████████". In addition, I've collected 120 bluecoat IDs from the █████████ Group, 71 ids from the "Headquarters, ██████████AISC", and ids from many other government organizations.

For example:
> ██████
> ███
> █████
> █████
> █████

This one bluecoat id has been observed with both the Department of the Interior and with ██████████GS. The first 3 ip addresses have hostnames that say "usgs.gov", but the others either lack hostnames or are from the national parks service (nps.gov). And this one id is from 5 IP addresses that span 4 different subnets.

## Impact
DoD uses Bluecoat gateways with unique IDs enabled. The unique IDs are supposed to prevent proxy forwarding loops between Bluecoat devices. However, they permit external observers from (1) determining that a Bluecoat device is in use, (2) tracking the device, and (3) gaining insight into the DoD network architecture.

When combined with user-agent strings and other distinct and unique identifiers, this combination of ID and IP address permits determining who likely works with whom.

(Let me know if you want the full list for DoD bluecoat devices. And if you want them for other ██████ Gov/Mil groups, let me know.)

## Suggested Mitigation/Remediation Actions
It varies by Bluecoat device, but buried in each system's configuration menu is an option to disable the unique ID. These should be disabled everywhere.


## Attachments
No attachments
