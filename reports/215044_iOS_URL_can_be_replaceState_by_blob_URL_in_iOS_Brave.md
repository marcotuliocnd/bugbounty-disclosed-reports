# [iOS] URL can be replaceState by blob URL in iOS Brave

## Report Details
- **Report ID**: 215044
- **URL**: https://hackerone.com/reports/215044
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-21T08:02:27.496Z
- **Disclosed**: 2017-08-10T05:08:59.263Z

## Reporter
- **Username**: xifengweiyu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

URL can be replace by blob URL using function history.replaceState()

## Products affected: 

iOS brave version 1.3.1(17.02.14.11)

## Steps To Reproduce:

- Add a html named "blob.html" which link is "http://192.168.1.111/blob.html"

- And its source is:
```
<script>
history.replaceState('','','blob:http://192.168.1.111/xxxx')
</script>
```
- then visit this page,you will find that URL has been replace by blob URL successfully!



## Attachments
- IMG_3124.PNG
