# Resource Consumption DOS on Edgemax v1.10.6

## Report Details
- **Report ID**: 406614
- **URL**: https://hackerone.com/reports/406614
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-06T21:13:32.532Z
- **Disclosed**: 2019-08-04T15:12:07.986Z

## Reporter
- **Username**: grampae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Resource consumption Denial of service.

1: The request below shows that when you feed the beaker.session.id cookie variable a payload of 250 characters or more, the web management portal will produce an error page showing full path disclosure and more as shown in screenshots error1.png and error2.png.  

GET / HTTP/1.1
Host: 192.168.1.100
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: beaker.session.id=v8iG24fDKn8x5uD3V2uICZA1FJEoUJpqH5VTa03xB5blDRNOe5AfFp2GNIBpDX8th1IO8sS5ejsz4Swm175nUvipwU211S4n4RtCv0A6r18fsgJbrrbmhFT9k2cAXF3yyg0Uu0B0wPOWP7BOrMVnXp44aHoXSfJ06ZXk7HrD5J5R9AZIgQLmGutM9ESNxw3CVJtW4Rfxeh7JE2AD04B3g78FxRgBxY82I2Gzf6ZPMsc39d37LM90dd9cFA
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
-----------------------------------------------------------

2: When providing a valid length payload of 249 characters or less it will be stored as a *.cache filename in the /var/run/beaker/container_file/ directory,this can easily be turned in to a denial of service by filling up the space of the device with unique beaker.session.id requests.  The web portal will display either a 500 error as shown in DOS1.png or a python error screen as shown in DOS2.1.png and DOS2.2.png.  Typically the web portal will stop functioning after the /run mount has reached 50% by sending requests using iterations of 1-15681 as a beaker.session.id variable, however any length of payload can be used up to 249 characters.  This can be recovered from by deleting all files within the /var/run/beaker/container_file/ directory.


Although once the /run mount can not accept any more files /var/log will start to fill up with complaints about not being able to write to /var/run/beaker/container_file/, then after /var/log fills up the device will stop responding all together until it has been power cycled.  

3: I have created a video showing you how it is accomplished, I stopped the video at only 7% resources consumed on the /run mount as the video would be pretty long if we waited until the edgerouter went offline.  I am hoping this is enough for you to be able to reproduce this.  I am thinking that this could be fairly bad if made in to a python script along with google dorks and automation.  Or even a python script that someone has to only enter in an IP address and it will take the router offline in about 5 minutes or so until the router owner unplugs and plugs it back in.

## Impact

Any resources served by the edgemax device will be unavailable until the physical device has it's power cycled, then it should function as normal.  However it would be easy to just perform the attack again after it has been brought back online.

## Attachments
- out.ogv
- Dos2.2.png
- DOS2.1.png
- DOS1.png
- EdgeosError2.png
- EdgeosError1.png
