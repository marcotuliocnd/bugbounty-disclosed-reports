# Authentication Issue

## Report Details
- **Report ID**: 176979
- **URL**: https://hackerone.com/reports/176979
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-20T08:27:36.425Z
- **Disclosed**: 2017-01-05T23:08:09.038Z

## Reporter
- **Username**: bugdiscloseguys
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
Hello there,
I noticed while creating Recurring payment while 2FA is enabled it asks a user to enter verification code.
So when someone confirm the Reccuring payment a request is sent to :

```
POST /recurring_payments/58087a3d6861ee015644fc48/confirm HTTP/1.1
Host: beta.coinbase.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://beta.coinbase.com/recurring_payments
X-NewRelic-ID: XA4HVVZTGwIAVFVXBAAG
X-CSRF-Token: /hSt/DD82VwI6ks+4P0VTHTDULz5EhHKowGAGfryWcVCZd47s+rQZDCgr70pJK4EeFHkKWRd0SJbVq1K64IZLA==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 28
Cookie: __utma=117893787.1205167212.1468114999.1475980536.1476020583.48; __utmz=117893787.1475796788.43.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=https%3A%2F%2Fwww.coinbase.com%2Fusers%2Ffa1f4606a31526801960b8c5703e2fa3%2Fverify; _coinbase=SDhMZytnck5TRi9McEMvMnpzY09OcjhJSlZ3TTZwYlFpWEZWcVlXcW13a1UzL3ZwdVFpdUlBd3RJSXBnSEhnOXZNZkExS1EyQXNNMitWSDVtQVpMVTdrdFRZTGFPRkVFMjZUbGZpVUhaYXA2aFdZa2hmWk55c0JzODM3ZzR0cHFTTmF1RHduOGhuZHFoOExDQ3craFdBWlJDalpOckhISlVtdzArWVMvdy9VSzJ2ZG9tejVIN3FQZXltSTlpeHRMd1VnNVRJL296b0tCT2VkWDlhaVJTWlU0ZkJDVkpPVFVwVXBnY09SVE5tcHVsYXNyMzdmUDdLS0NEbUhPSnI1d2ptM2JFcHFEQ0xQK1VCOWxMZXJFVG9HNlR1MnJXVk9TNjJuczlMN2NQdytWQnVuenZQeVI0bTF0dEc4b0FnWVY0WVZOcUVqOXE1RjYxVUVHV2pXSEdmTDVaYXI4dGNuVFhLb3JJb1N6eGwyMXNPSDRzWXRXNGhMd3l6aS8vSmp1bE94VlVYcit3UEVjc1JaKzVQalFlQzZuNnZLcDMwRE95UHR3MEpIUk1XZnliRlNSRWljR0NjN1JjUG90czd4UVY1TUp4YURJMkc5QUkrMGtiNVduSTc4WE9DT1ZsYzRKUERlNXAwakxQWWZlM2lQWDhydis5RStmYlAvVmtWS1h1OVhNTEtxSHNLOHkxa0hsOHkxaGpUdU1NdDJkRE1qU1EweEc0QVBKTEVnVjhvWlJQNFZiQ2pLYzRMYTNteUJjb1prMmIwRmtaMVlZc0w1aStBN3BkVEVqQXUxbDR0M2hITlN2SG1NVTQ3ZmZjT3QzamJERWY0RFIwSE5QL0tkTC0tdklic3RLUW1PZGhMNUErbUduRHNvQT09--d62907cee478b842f0368b067911107b93901fd5; df=730203b840afd60662e0f702672e42c0; ba=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010.11%3B%20rv%3A51.0)%20Gecko%2F20100101%20Firefox%2F51.0%23Intel%20Mac%20OS%20X%2010.11%234%2320100101%2320161019004013%23en-US%7C-330%23-330%23Thu%20Jan%2001%201970%2005%3A30%3A00%20GMT%2B0530%20(IST)%231%2F1%2F1970%2C%205%3A30%3A00%20AM%7C1280%23800%231280%23773%231%2324%230%2363%7C92f0112e7e19a58c900cddb7a717071a%23eca2166361dcd2ed64208e3d3543f751%23747b82b0027818ce808067ac0bb5118c%23383d750ac35ce7f8529ea4feefe52bd5%2390043fe540993e69ecde6102236dee71%7C%7CAAAAwBMBMpARDHcHAAhAAAAAAOQFaY6AAg%3D%3D; wcsid=2LddXtSmHNylLs5x1T41E46ICJKMJ18e; hblid=EdBhoju3s0gWxyDX1T41E46ICJk0KMTy; _oklv=1476950540058%2C2LddXtSmHNylLs5x1T41E46ICJKMJ18e; _okdetect=%7B%22token%22%3A%2214769450025350%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22beta.coinbase.com%22%7D; olfsk=olfsk6806335012267972; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1476945007028%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=8678-140-10-4291; _ga=GA1.3.1205167212.1468114999; __cfduid=d18d5c640e53cb87b90006494522c47431476945463; _ga=GA1.2.1205167212.1468114999; __ssid=b49e9a04-f751-4f59-a56f-845e27fe3277; mp_mixpanel__c=316; sft=7f8f7e817da5d65688adc609f2c7405d; address_58086c598ace9202b6531de0=580878636861ee03a644fc45; _gat=1; mp_7c112173efca4899213c618484d8f5fe_mixpanel=%7B%22distinct_id%22%3A%20%2257e87cd8694c037037f2b78b%22%2C%22country_code%22%3A%20%22IN%22%2C%22REACT%22%3A%20true%7D; request_method=POST; _gali=recurring_payments_modal
Connection: keep-alive

utf8=%E2%9C%93&_method=patch
```
Now when someone delete this reccuring payment there is no such option to restore it and note that for re-creating it you need a VERIFICATION CODE.
But if someone repeat the request which was obtained while confirming payment the reccuring payment is restored to particular payment ID.

Thanks
God is great <3

**Please mark it as informative if you dont believe its a security threat for you**


## Attachments
No attachments
