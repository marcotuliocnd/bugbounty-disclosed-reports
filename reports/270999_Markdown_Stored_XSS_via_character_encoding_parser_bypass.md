# [Markdown] Stored XSS via character encoding parser bypass

## Report Details
- **Report ID**: 270999
- **URL**: https://hackerone.com/reports/270999
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-22T20:33:25.117Z
- **Disclosed**: 2017-10-18T12:24:50.694Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi @briann and team,

A carefully crafted injection used against the Markdown input parser can be leveraged to store and execute arbitrary JavaScript on GitLab 10.0 hosts. Given the nature of this injection, which makes use of a rather esoteric filter bypass, the scope for exploitation may vary.

## Proof of concept
I have been able to exploit the following vulnerability within project Wiki pages. Consequently, prior to reproducing this issue please set up a test GitLab 10.0 instance with a Markdown-formatted project wiki. For ease of exploitation, the use of a web intercept proxy (e.g. Burp Suite) is recommended.

1. Please proceed to access your Wiki, then select "Edit" on the homepage (or create a new Markdown page).

2. Next, please activate your web intercept proxy. After doing so, enter generic text into the "Content" field and select the "Save Changes" button.

3. Return to your web intercept proxy, and identify the POST request to the `wikis` endpoint. Within this request, please identify the `content ` parameter and replace this with the below payload.

4. Finally, please POST the request and disable your web intercept proxy. Upon arriving on the updated Wiki page, please select the hyperlink to execute the JavaScript payload.

### Markdown parser payload

```
%3Ca+href%3D%22%01java%03script%3Aconfirm%28document.domain%29%22%3EClick+to+execute%3Ca%3E%0D%0A
```

### Supporting evidence

{F223200}

## Verified conditions

At the time of testing, I have successfully confirmed exploitability in the following environment:

* Firefox 55.0.3 stable (32-bit) on Ubuntu 16.04.3 LTS
* Fresh GitLab 10.0.0 CE install

Thanks,

Yasin

## Attachments
- GitLab_Markdown_XSS.png
