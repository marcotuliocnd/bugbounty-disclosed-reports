#  CORS (Cross-Origin Resource Sharing)

## Report Details
- **Report ID**: 310579
- **URL**: https://hackerone.com/reports/310579
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-30T17:02:25.250Z
- **Disclosed**: 2018-03-20T11:49:02.606Z

## Reporter
- **Username**: asad_anwar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Affected URL: https://ta.semrush.com/version/


Description: The application implements an HTML5 cross-origin resource sharing (CORS) policy for this request which allows access from any domain. Allowing access from all domains means that any domain can perform two-way interaction with the application via this request. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
Production Steps: Just look at the header. You found Access-Control-Allow-Origin: * .
The HTML5 cross-origin resource sharing policy controls whether and how content running on other domains can perform two-way interaction with the domain which publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If another domain is allowed by the policy, then that domain can potentially attack users of the application.
If a user is logged in to the application, and visits a domain allowed by the policy, then any malicious content running on that domain can potentially retrieve content from the application, and sometimes carry out actions within the security context of the logged in user. Even if an allowed domain is not overtly malicious in itself, security vulnerabilities within that domain could potentially be leveraged by a third-party attacker to exploit the trust relationship and attack the application which allows access

## Impact

Response :
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 30 Jan 2018 16:43:03 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: DNT,Authorization,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Origin: *
Cache-Control: public,must-revalidate,proxy-revalidate,max-age=0
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Length: 304

{"product_info":{"version":"3.7.3","name": "master","hash":"b2d1a97ed81b5802544bb9043b84aa4f177765da"},"data_info":{"version":"traffic_analyzer 2.3.0","host":"████","hash":"0bfa89621da124bb128b34adfbe9a94a","start_timestamp":1515705673,"final_timestamp":1515705729,"last_op":"read_reports"}}


Additional Info: Cross-site HTTP requests are HTTP requests for resources from a different domain than the domain of the resource making the request. For instance, a resource loaded from Domain A (http://domaina.example) such as an HTML web page, makes a request for a resource on Domain B (http://domainb.foo), such as an image, using the img element (http://domainb.foo/image.jpg). This occurs very commonly on the web today — pages load a number of resources in a cross-site manner, including CSS stylesheets, images and scripts, and other resources.

Thank You

## Attachments
- sem.JPG
