# Formula injection via CSV exports in WordCamp Talks plugin

## Report Details
- **Report ID**: 277525
- **URL**: https://hackerone.com/reports/277525
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-15T23:19:41.070Z
- **Disclosed**: 2017-10-23T18:47:08.830Z

## Reporter
- **Username**: whitehatter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
The WordCamp Talks plugin does not attempt to sanitize CSV exports, which can lead to spreadsheet formula injection via malicious inputs.

POC
========

* Submit a new talk with the title of `=1+1`. 
* Visit the All Talks page (/wp-admin/edit.php?post_type=talks)
* Click the CSV Export link
* Open the downloaded file in Excel, Numbers, or similar
* Note that the talk's title is displayed as `2`, showing the title was imported as a formula.

Impact
===========

Excel allows external commands to be executed via formulas after a warning prompt. The warning says "Do not enable this content unless you trust the source of this file", but since most users _do_ trust the source (their WordCamp site), they may be more likely to allow it.

Lots of arbitrary commands can be executed this way, including installing other commands in a way that can bypass antivirus scanning. 

More details can be found at https://pentestmag.com/formula-injection/

Remedy
=========

`wct_generate_csv_content()` needs to ensure that the first character in each value is not one of `=`, `-`, or `+`. These can come from several columns such as the title, categories, and tags, so all data should be sanitized.

Further info:

https://www.owasp.org/index.php/CSV_Excel_Macro_Injection
https://hackerone.com/reports/72785

## Attachments
No attachments
