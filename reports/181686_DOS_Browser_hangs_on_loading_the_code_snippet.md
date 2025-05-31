# [DOS] Browser hangs on loading the code snippet

## Report Details
- **Report ID**: 181686
- **URL**: https://hackerone.com/reports/181686
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-12T01:42:23.773Z
- **Disclosed**: 2018-05-06T21:02:40.473Z

## Reporter
- **Username**: tikoo_sahil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Basically the function location.reload() is causing browser to hang as browser is not able to handle multiple reloads but similar issue cannot be seen in Firefox and chrome as i am able to close the current tab.

## Products affected: 

Latest brave browser in linux.

## Steps To Reproduce:
Use the below code and save it as html file and then open it up on browser :-

<script>
open("");
setInterval('location.reload()',1);
</script>

Or

open up pop.html that i have attached

## Supporting Material/References:

i have attached html file that contains the code causing denial of service,


## Attachments
- pop.html
