# Wordpress Users Disclosure (/wp-json/wp/v2/users/) on data.gov

## Report Details
- **Report ID**: 942481
- **URL**: https://hackerone.com/reports/942481
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-25T15:48:16.952Z
- **Disclosed**: 2020-07-28T00:12:56.419Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
## Summary:
Hello TTS Bug bounty team!

I have found data.gov  User/admin usernames disclosed.
Using REST API, we can see all the WordPress users/author with some of their information.

## Steps To Reproduce:

  You can find the information disclosure by going to (data.gov/wp-json/wp/v2/users/)

Supporting Video:
{F922807}

Response:
```javascript
[{"id":600633,"name":"Aaron Borden","url":"","description":"","link":"https:\/\/www.data.gov\/author\/aaron-bordengsa-gov\/","slug":"aaron-bordengsa-gov","avatar_urls":etc....
```
## Fix:
Use this code will hide the users list and give 404 as the result, while rest of the api calls keep running as they were.
```javascript
add_filter( 'rest_endpoints', function( $endpoints ){
    if ( isset( $endpoints['/wp/v2/users'] ) ) {
        unset( $endpoints['/wp/v2/users'] );
    }
    if ( isset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] ) ) {
        unset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
    }
    return $endpoints;
});
```
## Similar reports:
(https://hackerone.com/reports/356047)
(https://hackerone.com/reports/370777)
(https://hackerone.com/reports/772744)

Thank you very much.

## Impact

Malicious counterpart could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known), making it less harder to penetrate the data.gov systems.

## Attachments
- data.gov.mov
