# Wordpress users Disclosure [ /wp-json/wp/v2/users/ ]  Not Resolved () 

## Report Details
- **Report ID**: 1784999
- **URL**: https://hackerone.com/reports/1784999
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-11-27T08:01:11.526Z
- **Disclosed**: 2022-12-28T14:10:19.124Z

## Reporter
- **Username**: thewikiii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
On this report's #735586  You closed the report and changed the status to Resolved.
But it's Not Resolved The Bug  It's Still there 

##url: https://www.mtn.com/wp-json/wp/v2/users/

Sorry to say this still i can reproduce this issue please remove  [ /wp-json/wp/v2/users/ ] file if your domain dont use that file
i will send the proof below still this issue is present on the domain 

##Summary:

Using REST API, we can see all the WordPress users/author with some of their information. Which can even be Personal information of employees/author. The file v2/users at:  https://www.mtn.com/wp-json/wp/v2/users/   is enabled and this give the attacker many users names like:  Amogelang Maluleka Greg Davies karenbyamugisha Marc Ilunga mitchprinsloo

## Steps To Reproduce:

  1. Go to https://www.mtn.com/wp-json/wp/v2/users/ [ Allows anyone to view active usernames ]
   
{F2050760}

## Supporting Material/References:

https://hackerone.com/reports/356047
https://hackerone.com/reports/370777

##Fix:

Use this code will hide the users list and give 404 as the result, while rest of the api calls keep running as they were.
 ```
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
- Screenshot_(306).png
