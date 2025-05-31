# Misconfiguration in AWS CloudFront CDN configuration makes rubygems.org serve (and cache) content from a unclaimed S3-bucket

## Report Details
- **Report ID**: 2262939
- **URL**: https://hackerone.com/reports/2262939
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-11-24T10:36:08.555Z
- **Disclosed**: 2023-12-07T14:57:26.668Z

## Reporter
- **Username**: p4fg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This is reported as suggested by the rubygems-program on hackerone. 
Report: https://hackerone.com/reports/2256740

I stumbled on the URL `https://rubygems.org/names`

That was giving the following response:
```xml
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<Error>
<Code>NoSuchBucket</Code>
<Message>The specified bucket does not exist</Message>
<BucketName>index.rubygems.org</BucketName>
<RequestId>KF8VDAZNXRZ3S9YQ</RequestId>
<HostId>MgMX9WXs1oJ0Rx8ABtxR+6UHFgVLyoqwqy/CRRPVMjlPLuSFdebn3E2L/8b7ZDL8QyF56JFL004=</HostId>
</Error>
```

Claiming the bucket in `index.rubygems.org` in region `us-east-2` gives a different error on the url `https://rubygems.org/names` indicating that the cloudfront-configuration tries to access the bucket using the wrong region:
```xml
<Error>
<Code>TemporaryRedirect</Code>
<Message>Please re-send this request to the specified temporary endpoint. Continue to use the original request endpoint for future requests.</Message>
<Endpoint>index.rubygems.org.s3.us-east-2.amazonaws.com</Endpoint>
<Bucket>index.rubygems.org</Bucket>
<RequestId>6AFP30FTX2AF5FEM</RequestId>
<HostId>BAVFkSyL0+Y7oMTL8li45vFTb0UCtSVB/pPFFQvRrSf8cSVAURS0SLjeb58XZ+E8me8Crw8jVKc=</HostId>
</Error>
```
Claiming the bucket `index.rubygems.org` in region `us-west-2` makes the endpoint start returning data from a file named `names` in the bucket, using the content-type specified by me on the file in the bucket. 
This response will be cached by Cloudfront for quite some time, so in the logs (below) only the cache-misses are logged.

## Impact

This bug would allow me to set the content-type using AWS S3 CLI to text/html and serve stored XSS on the page. This could affect a logged in maintainer in a very bad way.

I could also affect the availability for connected systems that relied on the list of names for CI-pipelines (for example).

Several artifactory instances were also observed in the S3-logs trying to access files from the bucket, this is just a sample:

```
2023-11-22T14:05:52+0000 "GET /info/effective_learndash HTTP/1.1" index.rubygems.org 167.82.143.38 "Artifactory/7.55.6 75506900"
2023-11-22T14:05:53+0000 "GET /info/embulk-parser-msgpack HTTP/1.1" index.rubygems.org 167.82.143.44 "Artifactory/7.55.6 75506900"
2023-11-22T14:05:57+0000 "GET /info/fluent-plugin-k8s-metrics-agg HTTP/1.1" index.rubygems.org 167.82.143.38 "Artifactory/7.55.6 75506900"
2023-11-22T14:06:00+0000 "GET /info/geo_labels HTTP/1.1" index.rubygems.org 167.82.143.76 "Artifactory/7.55.6 75506900"
2023-11-22T14:06:10+0000 "GET /info/google-cloud-shell-v1 HTTP/1.1" index.rubygems.org 167.82.143.108 "Artifactory/7.55.6 75506900"
2023-11-22T14:06:13+0000 "GET /info/groupdocs_parser_cloud HTTP/1.1" index.rubygems.org 167.82.143.78 "Artifactory/7.55.6 75506900"
2023-11-22T14:06:18+0000 "GET /info/ipizza HTTP/1.1" index.rubygems.org 167.82.143.93 "Artifactory/7.55.6 75506900"
2023-11-22T14:06:24+0000 "GET /info/lifeform HTTP/1.1" index.rubygems.org 167.82.143.78 "Artifactory/7.55.6 75506900"
2023-11-22T14:08:10+0000 "GET /info/jruby-pageant HTTP/1.1" index.rubygems.org 167.82.143.68 "Artifactory/7.71.4 77104900"
2023-11-22T14:40:48+0000 "GET /info/active_record_slave HTTP/1.1" index.rubygems.org 167.82.143.54 "Artifactory/7.55.10 75510900"
2023-11-22T14:40:51+0000 "GET /info/aws HTTP/1.1" index.rubygems.org 167.82.143.56 "Artifactory/7.55.10 75510900"
2023-11-22T14:41:13+0000 "GET /info/jdbc-mariadb HTTP/1.1" index.rubygems.org 167.82.143.119 "Artifactory/7.55.10 75510900"
2023-11-22T14:49:24+0000 "GET /info/rspec-core HTTP/1.1" index.rubygems.org 167.82.143.115 "Artifactory/6.23.28"
2023-11-22T15:00:16+0000 "GET /info/danger-rails_best_practices HTTP/1.1" index.rubygems.org 167.82.143.116 "Artifactory/7.55.10 75510900"
2023-11-22T15:27:44+0000 "GET /info/aws-sdk-chimesdkidentity HTTP/1.1" index.rubygems.org 167.82.143.41 "Artifactory/7.49.8 74908900"
2023-11-22T15:44:40+0000 "GET /info/bootscale HTTP/1.1" index.rubygems.org 167.82.143.89 "Artifactory/7.55.10 75510900"
2023-11-22T15:44:43+0000 "GET /info/chewy-resque HTTP/1.1" index.rubygems.org 167.82.143.28 "Artifactory/7.55.10 75510900"
2023-11-22T15:44:50+0000 "GET /info/ffi-extra HTTP/1.1" index.rubygems.org 167.82.143.28 "Artifactory/7.55.10 75510900"
2023-11-22T15:57:18+0000 "GET /info/comgate_ruby HTTP/1.1" index.rubygems.org 167.82.143.48 "Artifactory/7.55.6 75506900"
2023-11-22T15:58:20+0000 "GET /info/tencentcloud-sdk-lp HTTP/1.1" index.rubygems.org 167.82.143.102 "Artifactory/7.73.1 77301900"
2023-11-22T16:03:58+0000 "GET /info/fuzzily HTTP/1.1" index.rubygems.org 167.82.143.75 "Artifactory/7.49.8 74908900"
2023-11-22T16:51:39+0000 "GET /info/native_enum HTTP/1.1" index.rubygems.org 167.82.143.51 "Artifactory/7.55.10 75510900"
2023-11-22T16:51:46+0000 "GET /info/resque-honeybadger HTTP/1.1" index.rubygems.org 167.82.143.22 "Artifactory/7.55.10 75510900"
2023-11-22T17:03:16+0000 "GET /info/environment_helpers HTTP/1.1" index.rubygems.org 167.82.143.92 "Artifactory/7.55.6 75506900"
2023-11-22T17:03:41+0000 "GET /info/iri HTTP/1.1" index.rubygems.org 167.82.143.92 "Artifactory/7.55.6 75506900"
2023-11-22T17:05:49+0000 "GET /info/hostlist_expression HTTP/1.1" index.rubygems.org 167.82.143.75 "Artifactory/7.55.10 75510900"
```

As these endpoints contain the checksums for the gems for different versions, a supply-chain-attack could probably have been attempted as the checksums could be set to anything the attacker wanted. See [https://rubygems.org/info/aws](https://rubygems.org/info/aws) for example.

A full log of accessed files are attached to this report: {F2880368}

## Attachments
- index.rubygems.org.log
