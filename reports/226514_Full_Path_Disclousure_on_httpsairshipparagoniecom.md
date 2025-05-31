# Full Path Disclousure on https://airship.paragonie.com

## Report Details
- **Report ID**: 226514
- **URL**: https://hackerone.com/reports/226514
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-06T08:17:30.515Z
- **Disclosed**: 2017-05-07T01:41:36.811Z

## Reporter
- **Username**: ruisilva
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Hi , i found an full path disclousure vulnerability on https://airship.paragonie.com

For reproduce this vulnerability go to: https://airship.paragonie.com/my/cabins
You will see something like this : Class '\ParagonIE\Airship\Cabins' not found #0 /var/www/paragonie/framework/Router.php(236): ParagonIE\Tuner\Router::passArgs(Array, Array, Array) #1 /var/www/paragonie/framework/Router.php(150): ParagonIE\Tuner\Router::serve(Array, Array, Array) #2 /var/www/paragonie/framework/Router.php(107): ParagonIE\Tuner\Router::site(Array) #3 /var/www/paragonie/public_html/index.php(26): ParagonIE\Tuner\Router::route(Array) #4 {main}

See attached file 
Thanks 

## Attachments
- FPD_Airship.png
