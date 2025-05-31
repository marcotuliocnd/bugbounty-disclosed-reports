# Information leakage via CSV when content is valid JavaScript

## Report Details
- **Report ID**: 207266
- **URL**: https://hackerone.com/reports/207266
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-18T05:31:54.750Z
- **Disclosed**: 2017-05-23T14:44:32.654Z

## Reporter
- **Username**: mikkocarreon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
The function "**Download as CSV**" might leak information to 3rd domains. The exploitation seems unlikely and purely theoretical but it might work in some cases. 

**Description (Include Impact):**
Take downloading payments as CSV, for example, which is recently launched. The response to 
https://hackerone.com/settings/bounties.csv
returns CSV which is indeed, a comma separated values. There is a field which is influenced by user input i.e. report_title.
And, as we all know, `script` inclusions are exempt from SOP. So, if the returned CSV forms valid JavaScript, it's possible that we can read information.

### Steps To Reproduce
For demonstration;
I created an HTML page as follows;
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'/>
    <script>
        var report_id,report_title,program_name,total_amount,amount,bonus_amount,currency,awarded_at,status;
    </script>
  </head>
  <body>
    <script src='https://hackerone.com/settings/bounties.csv'></script>
  </body>
</html>
```

And, edited returned response (using BurpSuite) as follows;
```JavaScript
report_id,report_title,program_name,total_amount,amount,bonus_amount,currency,awarded_at,status
████████
████
█████████
████████
██████
████████
```

So, what I did is added ```=` ```  right after first word of first report. Similarly added ``` `//``` right after last word of last report.
This makes it a valid JavaScript, and `XSS` a valid variable which now have all details in it. 

### Optional: Your Environment (Browser version, Device, etc)
Firefox version 45.7.0
UA:  Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Safari may also work.


## Attachments
No attachments
