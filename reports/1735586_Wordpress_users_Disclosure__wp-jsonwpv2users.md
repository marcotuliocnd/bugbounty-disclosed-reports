# Wordpress users Disclosure [ /wp-json/wp/v2/users/ ]

## Report Details
- **Report ID**: 1735586
- **URL**: https://hackerone.com/reports/1735586
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-10-14T13:29:56.108Z
- **Disclosed**: 2022-11-27T03:25:02.082Z

## Reporter
- **Username**: shubham_srt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Using REST API, we can see all the WordPress users/author with some of their information. Which can even be Personal information of employees/author. The file v2/users at:  https://www.mtn.com/wp-json/wp/v2/users/   is enabled and this give the attacker many users names like:  `Amogelang Maluleka` `Greg Davies` `karenbyamugisha` `Marc Ilunga` `mitchprinsloo`

## Steps To Reproduce:

  1.  Go to https://www.mtn.com/wp-json/wp/v2/users/  [ Allows anyone to view active usernames ]

{F1985941}

## Supporting Material/References:
https://hackerone.com/reports/356047
https://hackerone.com/reports/370777

###Fix:
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

## Impact

Malicious counterpart could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known), making it less harder to penetrate the data.gov systems.

## Attachments
- image.png
