# HTML INJECTION on coins.state.gov

## Report Details
- **Report ID**: 1844830
- **URL**: https://hackerone.com/reports/1844830
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-24T10:45:04.343Z
- **Disclosed**: 2023-04-26T21:04:19.065Z

## Reporter
- **Username**: devdevrl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
##Summary 

Hi team i hope you are well t is a pleasure to work in your program. I will begin to present the vulnerability that I found it: An html injection on coins.state.gov


##Steps


 Vulnerable Link :
```
1.https://coins.state.gov/Errors.aspx?aspxerrorpath=Gxss
```

***Steps to reproduce ***

###first step :
    1. i used gxss and katana like tools to find vulnerable domain : https://coins.state.gov/Errors.aspx?aspxerrorpath=Gxss
    2. i tried to xss but no result for now i  tried it manually but no result.


###second step :
       1.i had an idea to use dalfox tool to try xss or html injection.
       2. it work only for html injection 
      3. a video below can help you to see the result
      4. when i refresh the browser and i keep dalfox run there is another payload generated on the page

```bash
echo https://coins.state.gov/Errors.aspx?aspxerrorpath=Gxss | dalfox pipe
```

{F2135442}
{F2135443}

## Impact

It can allow an attacker to modify the page. To steal another person's identity. The attacker discovers injection vulnerability and decides to use an HTML injection attack. Attacker crafts malicious links, including his injected HTML content, and sends it to a user via email

## Attachments
No attachments
