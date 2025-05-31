# Multiple issues in Libxml2 (2.9.2 - 2.9.5)

## Report Details
- **Report ID**: 293126
- **URL**: https://hackerone.com/reports/293126
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-27T06:37:31.070Z
- **Disclosed**: 2019-10-14T04:37:04.847Z

## Reporter
- **Username**: xixabangm4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Libxml2 is the XML C parser and toolkit developed for the Gnome project. Due to its flexible C implementation and continuous development, Libxml2 is known to be very portable, the library builds and works on a variety of systems (Linux, Unix, Windows, CygWin, MacOS, MacOS X, RISC Os, OS/2, VMS, QNX, MVS, VxWorks, ...). It is or has been adopted by many major vendors or products including Google (Chrome), VMWare, Apple (Safari, Mac OSX, iOS, ...), and many embedded systems. As in the [Google Patch Rewards](https://www.google.com.sg/about/appsecurity/patch-rewards) , Libxml2 is listed in the category of core infrastructure data parsers.

From 2015-2016, our fuzzing work on Libxml2 has systematically identified a sequence of bugs including use-after-free, out-of-bound read, infinite recursions, they are submitted to both Libxml2 and Apple (which internally maintains a highly-synchronized branch of the official Libxml2), some of the bugs are resolved in recent releases, including the following:

Credited in both Libxml2-2.9.4 and Apple iOS 9.3.2 / OSX 10.11.5:

https://support.apple.com/en-sg/HT206568

CVE-2016-1835: Libxml2 Use-after-Free in xmlSAX2AttributeNs 
https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-1835
https://bugzilla.gnome.org/show_bug.cgi?id=759020

CVE-2016-1836: Libxml2 Use-after-Free in xmlParseNCNameComplex 
https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-1836
https://bugzilla.gnome.org/show_bug.cgi?id=759398

CVE-2016-1837: Libxml2 Use-after-Free in htmlParsePubidLiteral / htmlParseSystemLiteral 
https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-1837
https://bugzilla.gnome.org/show_bug.cgi?id=760263

Credited in Apple iOS 9.2 / OSX 10.11.2, and (silently) fixed in Libxml2-2.9.3:

https://support.apple.com/en-sg/HT205635

CVE-2016-7115: Libxml2 xmlParseNCNameComplex OOB Read 
https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-7115

CVE-2016-7116: Libxml2 xmlParseTryOrFinish OOB Read 
https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-7116

And a few others:
https://support.apple.com/en-sg/HT206902
https://support.apple.com/en-sg/HT206167

[CVE-2016-1762](https://nvd.nist.gov/vuln/detail/CVE-2016-1762): Libxml2 xmlParseInternalSubset Out-of-Bound Read Vulnerability (iOS/OSX) 
https://bugzilla.gnome.org/show_bug.cgi?id=759671

[CVE-2016-4447](https://nvd.nist.gov/vuln/detail/CVE-2016-4447): Libxml2 xmlParseElementDecl Out-of-Bound Read Vulnerability (iOS/OSX)
https://bugzilla.gnome.org/show_bug.cgi?id=759573

Recently in Libxml2 2.9.7:

[CVE-2017-16931](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-16931): Libxml2 xmlParseNameComplex Use-after-Free Vulnerability
https://bugzilla.gnome.org/show_bug.cgi?id=766956
https://github.com/GNOME/libxml2/commit/e26630548e7d138d2c560844c43820b6767251e3

[CVE-2017-16932](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-16932): Libxml2 Parameter Entity Infinite Recursion Vulnerability
https://bugzilla.gnome.org/show_bug.cgi?id=759579
https://github.com/GNOME/libxml2/commit/899a5d9f0ed13b8e32449a08a361e0de127dd961

Much efforts of patch work should be attributed to Daniel Veillard (Libxml2 developer), David Kilzer (Apple), Pranjal Jumde (Apple), Nick Wellnhofer and possibly others.

## Impact

Exploitability subject to context, especially when the parser is exposed to external XML. In some situations if the XML engine is used in conjunction with a JS engine, exploitation could be easier.

## Attachments
No attachments
