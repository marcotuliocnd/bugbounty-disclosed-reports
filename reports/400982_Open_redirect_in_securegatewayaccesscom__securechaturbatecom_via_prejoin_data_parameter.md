# Open redirect in securegatewayaccess.com / secure.chaturbate.com via prejoin_data parameter

## Report Details
- **Report ID**: 400982
- **URL**: https://hackerone.com/reports/400982
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-27T13:13:21.961Z
- **Disclosed**: 2018-09-19T23:46:03.983Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Summary##
Hello, I have found that if there is a valid `weg_digest` parameter in the in the GET request to https://secure.chaturbate.com/post and other parameters are invalid, a Location header will be automatically constructor based on the contents of the `prejoin_data` parameter. This allows someone to change the base root and create an open redirect.

Even more, it has been observed that this specific request also works under the https://securegatewayaccess.com domain and an open redirect can also be created from that domain.

PS : Because this affects both URL's and `securegatewayaccess.com` seems to be a critical I have marked this as medium instead of low.

## Steps To Reproduce:
- Call in browser this URL :

```
https://securegatewayaccess.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c
```

- Or under the secure.chaturbate domain this URL :

```
https://secure.chaturbate.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c
```

- This can also be linked with the /external_link request from the root url to create a chained redirect :

```
https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c
```

All requests will have as answer this header :

```
Location: http://evil.com/?=/tipping/purchase_tokens/
```

## Supporting Material/References:
N/A

## Impact

Open redirect that facilitate potential phishing attacks.

## Attachments
No attachments
