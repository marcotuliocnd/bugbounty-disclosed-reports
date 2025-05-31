# Internal API endpoint is accesible for everyone

## Report Details
- **Report ID**: 1066790
- **URL**: https://hackerone.com/reports/1066790
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-26T21:55:14.606Z
- **Disclosed**: 2020-12-28T08:48:55.752Z

## Reporter
- **Username**: arnonymous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: who-covid-19-mobile-app

## Vulnerability Information
## Summary:
It looks like the endpoint **/internal/cron/refreshCaseStats** as configured in [cron.yaml]  (https://github.com/WorldHealthOrganization/app/blob/master/server/appengine/src/main/webapp/WEB-INF/cron.yaml#L3) is accesible for everyone. Since it is configured as a cronjob to run every 5 minutes and starts with internal, this should not be the case, and could worst case lead to DoS if it's a costly operation.

## Steps To Reproduce:

  1. Go to https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```time curl -v https://hack.whocoronavirus.org/internal/cron/refreshCaseStats```

{F1130894}
Show that it takes about 20 seconds, before a 200 OK response returns (with a single request).

## Supporting Material/References:
https://github.com/WorldHealthOrganization/app/blob/master/server/appengine/src/main/webapp/WEB-INF/cron.yaml#L3

## Impact

Depending on the impact / performance of the action 'refresh case stats'  this could lead to unnecesarry load on the backend (and charges) or even DoS.

## Attachments
- curl-corona.png
