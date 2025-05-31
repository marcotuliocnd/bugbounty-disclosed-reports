# Open redirect in fastify-static via mishandled user's input when attempt to redirect

## Report Details
- **Report ID**: 1354255
- **URL**: https://hackerone.com/reports/1354255
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-09-29T03:57:50.669Z
- **Disclosed**: 2021-10-11T16:39:32.003Z

## Reporter
- **Username**: drstrnegth
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fastify

## Vulnerability Information
## Summary:
When fastify-static is mounted at root and the register option `redirect: true`, the following 2 lines cause open redirect bug: https://github.com/fastify/fastify-static/blob/master/index.js#L156-L157. A remote attackers can redirect users to arbitrary web sites via a double forward slash: `//`, for example if attacker wants to redirect to google.com: `http://<domain_name>//google.com/%2e%2e`.

This bug is similar to CVE-2015-1164 in ExpressJS, they published on their page about the security bugs here (you can Ctrl+F and search for CVE-2015-1164): https://expressjs.com/en/advanced/security-updates.html

## Steps To Reproduce:

  1. Download my PoC [here](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/mt31wp8hbrsn9sul3hfsa2mhe8l2?response-content-disposition=attachment%3B%20filename%3D%22fastify-static-poc.zip%22%3B%20filename%2A%3DUTF-8%27%27fastify-static-poc.zip&response-content-type=application%2Fzip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ6QHNYGOQ%2F20210929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210929T035204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCICrqoxGo75Ivmq34ngOkjvDEcfUY2whU4qL3udAE0zqmAiASKig5F4T2N4P5bLqP5E6AYAc97skXJzkNuuBCInxZpiqDBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAIaDDAxMzYxOTI3NDg0OSIM6dgTIefGOABRi6G7KtcDMm6z2WDPjxIq0AsFDl8JeZZlGwFmypSkrJVvMrqJwOfGKE%2F4ElRQV6xNoobQCZqscQRvbSxSOdi%2Bpr19I89hhaND9cIf6EcwozYCPZTR5zOEocHTs2QM1yZszHDaf0QfqgwW%2BKdeNyH%2B914CyDrrJKaswbqIVh9JgYaFm5KT86M63LlbR66HVVXUGEF5auFRnsTECEclmigWMgbj7CGbQRtcpQGXVh4KXC5IiN%2FsDSlI%2Fj6JsPB1WxLPwp0vH6IEIW7qR3AvIWojBOwiflgNu8wBF%2B8w7eCMT8UNKQCC0%2FT0b%2BTlHIe9BPvW%2Bf36xVjY6sqFCMlfQUbYTL%2FPqiS7qWgbZgZkJyCa48qN%2F82c8pbOiMA%2FLs1ketjuoU4OlpYWdPAxda4UOXdKrTyHtjaeKm%2BF3sRktJsVW9vlnsmfxH%2BPgakzwIU5YYlouoGYUzQAMrLtRw7Ok%2BehS%2BPVMNhbVwpWaKEkrNQgYc0SEJ5vs3NGxCkJrB9LevJXk%2BmXsfure%2BIYX0nwTC9useVhmQ4aMcBBVkgEQI2OQ2EcmwcFw0yo%2FgaH9%2BbxRK%2BGGeEU9GTi2886gvX%2B2TcZNSlCNu%2BD5Aw7pRCoMvR%2FX9rjt3QgVgrWhwpvA5eWMJmfzooGOqYBy3AxhRsfuF0ydzpe5lWLslA1TbBdc2Lj%2FssN5e54t0SlOp1v83sBjx%2FTj9RL6o3ZJd2QGTxTAHgyHak%2FePXMxePfF1x2vG%2B0cZaiwi1TResFqYUBJUCXl%2BQoGHLcKGk4yxL7jseKXDI5xO9xzF3jFOh%2BvA%2FwdnF%2B35qRwi7VlUDUGU0DL1TE6KQeCR2%2BkngI8EtnqCWYSIPZweLxkxTsptOkljLRGQ%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=06d043b90fbcfd78b96978116c17683ef0506089cdd9b55c9065994651513bc2)
  2. `bash run.sh`
  3. Use Firefox to navigate to `http://localhost:3000//google.com/%2e%2e`. You will see that you are redirected to https://www.google.com/

Request:
```
GET //google.com/%2e%2e HTTP/1.1
Host: localhost:3000
Accept-Encoding: gzip, deflate
Connection: close
```

Response:
```
HTTP/1.1 301 Moved Permanently
location: //google.com/%2e%2e/
content-length: 0
Date: Wed, 29 Sep 2021 03:34:22 GMT
Connection: close
```

I tested and it only works in Firefox but not in Chrome, Edge, Opera, Safari 😂, it is because different browsers handle the response differently.

## Impact

The most straight-forward impact is phishing.
However, open redirect is a gadget that enables attackers to be able to exploit further, for example:
- Bypassing SSRF protection
- Token stealing in OAuth

## Attachments
- fastify-static-poc.zip
