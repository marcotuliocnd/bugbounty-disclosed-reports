# Error when editing a calendar appointment returns stacktrace and query

## Report Details
- **Report ID**: 2108342
- **URL**: https://hackerone.com/reports/2108342
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-14T08:18:52.033Z
- **Disclosed**: 2024-01-17T08:25:02.428Z

## Reporter
- **Username**: st0nzyy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

After some testing in Calendar App, i found when im trying to Edit calendar appointment details and change the appointment  to non-exsist id there is ```HTTP/1.1 500 Internal Server Error``` that disclose full path & internal SQL query.


## Steps To Reproduce:

-  login and navigate to ```/nextcloud/index.php/apps/calendar/dayGridMonth/now```

{F2599201}

- Edit Appointment and save the request

- in the below request change  ```id ``` value to 4 like example

## Request
```
PUT /nextcloud/index.php/apps/calendar/v1/appointment_configs/3 HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0
.
.
.

{"id":3,"token":"scjGreGCEkTQ","name":"abc","description":"","location":"","visibility":"PRIVATE","targetCalendarUri":"personal","availability":{"timezoneId":"Asia/Riyadh","slots":{"MO":[{"start":1691992800,"end":1692021600}],"TU":[{"start":1691992800,"end":1692021600}],"WE":[{"start":1691992800,"end":1692021600}],"TH":[{"start":1691992800,"end":1692021600}],"FR":[{"start":1691992800,"end":1692021600}],"SA":[],"SU":[]}},"length":300,"increment":900,"preparationDuration":0,"followupDuration":0,"timeBeforeNextSlot":0,"futureLimit":5184000,"calendarFreeBusyUris":[]}
```

##Resonse

```

HTTP/1.1 500 Internal Server Error
.
.
.
.

{
    "status": "error",
    "message": "Could not find a record for id",
    "data": {
        "type": "OCA\\Calendar\\Exception\\ClientException",
        "message": "Could not find a record for id",
        "code": 0,
        "trace": [
            {
                "file": "/var/www/html/nextcloud/apps/calendar/lib/Controller/AppointmentConfigController.php",
                "line": 254,
                "function": "findByIdAndUser",
                "class": "OCA\\Calendar\\Service\\Appointments\\AppointmentConfigService"
            },
            {
                "file": "/var/www/html/nextcloud/lib/private/AppFramework/Http/Dispatcher.php",
                "line": 230,
                "function": "update",
                "class": "OCA\\Calendar\\Controller\\AppointmentConfigController"
            },
            {
                "file": "/var/www/html/nextcloud/lib/private/AppFramework/Http/Dispatcher.php",
                "line": 137,
                "function": "executeController",
                "class": "OC\\AppFramework\\Http\\Dispatcher"
            },
            {
                "file": "/var/www/html/nextcloud/lib/private/AppFramework/App.php",
                "line": 183,
                "function": "dispatch",
                "class": "OC\\AppFramework\\Http\\Dispatcher"
            },
            {
                "file": "/var/www/html/nextcloud/lib/private/Route/Router.php",
                "line": 315,
                "function": "main",
                "class": "OC\\AppFramework\\App"
            },
            {
                "file": "/var/www/html/nextcloud/lib/base.php",
                "line": 1071,
                "function": "match",
                "class": "OC\\Route\\Router"
            },
            {
                "file": "/var/www/html/nextcloud/index.php",
                "line": 36,
                "function": "handleRequest",
                "class": "OC"
            }
        ],
        "previous": {
            "type": "OCP\\AppFramework\\Db\\DoesNotExistException",
            "message": "Did expect one result but found none when executing: query \"SELECT `id`, `token`, `name`, `description`, `location`, `visibility`, `user_id`, `target_calendar_uri`, `calendar_freebusy_uris`, `availability`, `start`, `end`, `length`, `increment`, `preparation_duration`, `followup_duration`, `time_before_next_slot`, `daily_max`, `future_limit` FROM `*PREFIX*calendar_appt_configs` WHERE (`id` = :dcValue1) AND (`user_id` = :dcValue2)\"; ",
            "code": 0,
            "trace": [
                {
                    "file": "/var/www/html/nextcloud/lib/public/AppFramework/Db/QBMapper.php",
                    "line": 361,
                    "function": "findOneQuery",
                    "class": "OCP\\AppFramework\\Db\\QBMapper"
                },
                {
                    "file": "/var/www/html/nextcloud/apps/calendar/lib/Db/AppointmentConfigMapper.php",
                    "line": 55,
                    "function": "findEntity",
                    "class": "OCP\\AppFramework\\Db\\QBMapper"
                },
                {
                    "file": "/var/www/html/nextcloud/apps/calendar/lib/Service/Appointments/AppointmentConfigService.php",
                    "line": 138,
                    "function": "findByIdForUser",
                    "class": "OCA\\Calendar\\Db\\AppointmentConfigMapper"
                },
                {
                    "file": "/var/www/html/nextcloud/apps/calendar/lib/Controller/AppointmentConfigController.php",
                    "line": 254,
                    "function": "findByIdAndUser",
                    "class": "OCA\\Calendar\\Service\\Appointments\\AppointmentConfigService"
                },
                {
                    "file": "/var/www/html/nextcloud/lib/private/AppFramework/Http/Dispatcher.php",
                    "line": 230,
                    "function": "update",
                    "class": "OCA\\Calendar\\Controller\\AppointmentConfigController"
                },
                {
                    "file": "/var/www/html/nextcloud/lib/private/AppFramework/Http/Dispatcher.php",
                    "line": 137,
                    "function": "executeController",
                    "class": "OC\\AppFramework\\Http\\Dispatcher"
                },
                {
                    "file": "/var/www/html/nextcloud/lib/private/AppFramework/App.php",
                    "line": 183,
                    "function": "dispatch",
                    "class": "OC\\AppFramework\\Http\\Dispatcher"
                },
                {
                    "file": "/var/www/html/nextcloud/lib/private/Route/Router.php",
                    "line": 315,
                    "function": "main",
                    "class": "OC\\AppFramework\\App"
                },
                {
                    "file": "/var/www/html/nextcloud/lib/base.php",
                    "line": 1071,
                    "function": "match",
                    "class": "OC\\Route\\Router"
                },
                {
                    "file": "/var/www/html/nextcloud/index.php",
                    "line": 36,
                    "function": "handleRequest",
                    "class": "OC"
                }
            ],
            "previous": null
        }
    },
    "code": 0
}
.

```

{F2599200}

as you can see, internal paths,files functions disclosed also SQL query: 

"message": "Did expect one result but found none when executing: query \"SELECT `id`, `token`, `name`, `description`, `location`, `visibility`, `user_id`, `target_calendar_uri`, `calendar_freebusy_uris`, `availability`, `start`, `end`, `length`, `increment`, `preparation_duration`, `followup_duration`, `time_before_next_slot`, `daily_max`, `future_limit` FROM `*PREFIX*calendar_appt_configs` WHERE (`id` = :dcValue1) AND (`user_id` = :dcValue2)\"; ",
 


## Supporting Material/References:

https://hackerone.com/reports/1841408

## Impact

internal paths & internal SQL query of the website are disclosed.

## Attachments
- request.JPG
- calender-page.JPG
