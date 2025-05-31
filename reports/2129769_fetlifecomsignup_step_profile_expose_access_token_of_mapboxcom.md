# fetlife.com/signup_step_profile expose access_token of mapbox.com

## Report Details
- **Report ID**: 2129769
- **URL**: https://hackerone.com/reports/2129769
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-31T04:14:11.695Z
- **Disclosed**: 2023-11-01T00:17:26.046Z

## Reporter
- **Username**: deepblue29
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fetlife

## Vulnerability Information
Hi fetlife, I'm investigate on registration step on your site, in registration step at https://fetlife.com/signup_step_profile

when user type in field "private_location_name"

{F2652527}

it use frontend call to api.mapbox.com directly thus expose `access_token`, I was able to call it directly via command line:

```
curl 'https://api.mapbox.com/geocoding/v5/mapbox.places/ho%20chi.json?limit=10&types=place%2Clocality&autocomplete=true&language=en&access_token=pk.eyJ1IjoiZmV0bGlmZSIsImEiOiJjazhwMjNrajUwN2luM2xwcmxmMDNoajFoIn0.vge5GmfaG4OTyth8uS_N6w' \
  -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
  -H 'Referer: https://fetlife.com/' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

Upon having this access_token, I could freely use your token on my site, even though fetlife have `Referer: https://fetlife.com/`, I could navigate around that easily using direct http call from my server and inject Referer header as `https://fetlife.com/`.

----------------------------------------------------------------------------------------------------------

Another issue (not security related), this request is for validating attribute unhandle email case yet :

```
curl 'https://fetlife.com/users/attributes/email?email=deepblue29@wearehackerone.com' \
  -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
  -H 'Accept: application/json' \
  -H 'Referer: https://fetlife.com/signup_step_profile' \
  -H 'X-CSRF-Token: WbVVfdWFF2nIoWJ7yJHpjVMtt1i1_VFMTpDyq4dRI72NG3onq_MOtQmhHXD6nlD-aKAYoqpvAhCAWu8z6zf_qQ' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

```
500 Internal Server Error
If you are the administrator of this website, then please read this web application's log file and/or the web server's log file to find out what went wrong.%
```

----------------------------------------------------------------------------------------------------------

Another issue I see there is two `authenticity_token` on registration hidden input, I believe this is a mistake (?) 

{F2652528}

## Impact

exposing access_token on mapbox give me freely use of your resources (I use, you pay).

## Attachments
- image.png
- Screenshot_from_2023-08-31_11-07-58.png
