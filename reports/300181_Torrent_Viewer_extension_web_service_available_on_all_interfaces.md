# Torrent Viewer extension web service available on all interfaces

## Report Details
- **Report ID**: 300181
- **URL**: https://hackerone.com/reports/300181
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-23T08:21:57.137Z
- **Disclosed**: 2018-01-26T14:06:40.705Z

## Reporter
- **Username**: spipm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

When files are downloaded via the Torrent Viewer, a local web service is spun up that allows the user to download the files. This web service listens on all interfaces, allowing anyone in the network to view what files are being downloaded, and download them from the user. This mostly affects the privacy of the user.

## Products affected: 

 * This issue was tested on the Brave browser on OSX, using version 0.19.122. Full specs:

Name	Version
Brave	0.19.122
rev	009e792
Muon	4.5.31
libchromiumcontent	63.0.3239.108
V8	6.3.292.48
Node.js	7.9.0
Update Channel	Release
OS Platform	macOS
OS Release	17.2.0
OS Architecture	x64

## Steps To Reproduce:

* Disable local firewall if set to block all external connections
* Load a torrent in the Brave browser, for example:
https://zooqle.com/download/wiv7v.torrent
* Click on "Start download"
* Either hover over the "Save file" button to see the port to the web service (button_link.png), or perform an external portscan.
* Use different device to connect to the port. 
* See what the user is downloading (see Open torrent webservice.png)

Note that the port changes every time a download is started, but an attacker can simple perform a portscan to find this port.

## Supporting Material/References:

* I've included two screenshots that show the port (button_click.png) and me viewing downloaded files from a VM (Open torrent webservice.png). This issue has also been tested from a phone instead of the VM, to ensure that it wasn't just my vmnet being viewed as a local address.

## Impact

If an 'attacker' (or any privacy-snooping agent) is on the same network as the user, it's possible to list all files that are currently downloaded. It's also possible to download these files from the user. 

This vulnerability does not affect users that have their firewall set to block all incoming connections.

## Attachments
- Open_torrent_webservice.png
- button_link.png
