# Disclosure of User Information

## Report Details
- **Report ID**: 753725
- **URL**: https://hackerone.com/reports/753725
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-07T17:18:15.954Z
- **Disclosed**: 2020-01-16T01:52:02.714Z

## Reporter
- **Username**: shardulb_23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Hi Team,
 
We can get information about the users registered (such as: id, name, login name, etc.) and employees of NordVPN without authentication on https://www.nordvpn.com

Vulnerable URL:  https://nordvpn.com/wp-json/wp/v2/users/
Vulnerable URL: https://nordvpn.com/?rest_route=/wp/v2/users/

POC: Screenshots are attached 
---------------------------------------------------------------------------------------------------------------------------------------
Response 1: 
{
  "id": 1,
  "name": "21232f297a57a5a743894a0e4a801fc3",
  "url": "",
  "description": "",
  "link": "",
  "slug": "admin",
  "avatar_urls": {
    "24": "https://secure.gravatar.com/avatar/2a6282462b7001cbf7ec9d1e2c9d1053?s=24&d=mm&r=g",
    "48": "https://secure.gravatar.com/avatar/2a6282462b7001cbf7ec9d1e2c9d1053?s=48&d=mm&r=g",
    "96": "https://secure.gravatar.com/avatar/2a6282462b7001cbf7ec9d1e2c9d1053?s=96&d=mm&r=g"
  },
  "meta": [],
  "_links": {
    "self": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users/1"
      }
    ],
    "collection": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users"
      }
    ]
  }
}
----------------------------------------------------------------------------------------------------------------
Response 2:
{
  "id": 8,
  "name": "Christina Craig",
  "url": "",
  "description": "Christina is a community manager and the heart, the voice and the soul of NordVPN. She is always up for a conversation with our community of users and blog readers.",
  "link": "",
  "slug": "christina",
  "avatar_urls": {
    "24": "https://secure.gravatar.com/avatar/f956d82ca0b55da2fa45d6f1d062d18e?s=24&d=mm&r=g",
    "48": "https://secure.gravatar.com/avatar/f956d82ca0b55da2fa45d6f1d062d18e?s=48&d=mm&r=g",
    "96": "https://secure.gravatar.com/avatar/f956d82ca0b55da2fa45d6f1d062d18e?s=96&d=mm&r=g"
  },
  "meta": [],
  "_links": {
    "self": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users/8"
      }
    ],
    "collection": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users"
      }
    ]
  }
}
------------------------------------------------------------------------------------------------------------------------------------
Thanks and waiting for your response.

## Impact

1) Attacker can user these valuable information for advance attack as bruteforce login.
2)It is possible to get all the users registered on the system and create a bruteforce directed to these users.

## Attachments
- adminuser.PNG
- User_details.PNG
- Userdetails.PNG
- Userdetails2.PNG
