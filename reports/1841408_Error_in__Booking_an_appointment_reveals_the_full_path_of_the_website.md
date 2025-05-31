# Error in  Booking an appointment reveals the full path of the website

## Report Details
- **Report ID**: 1841408
- **URL**: https://hackerone.com/reports/1841408
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-20T03:41:26.488Z
- **Disclosed**: 2023-06-18T11:29:18.848Z

## Reporter
- **Username**: themarkib0x0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
I figured out that when there is configuration of smtp then the user can reveal the full path of the website when booking an appointment.

## Steps To Reproduce:

1. Go to calendar and create and appointment.
2. Now visit that appointment with burp proxy on.
3. Select time and try to book the appointment.
4. Following request will be observed
```
POST /index.php/apps/calendar/appointment/9/book HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
requesttoken: <token>
Content-Length: 138
Origin: http://129.146.173.97
DNT: 1
Connection: close
Cookie:<any valid-cookie>

{"start":1674205200,"end":1674205500,"displayName":"attackerbikram","email":"ohp@gmail.com","description":"","timeZone":"UTC"}
```
5. We will get following response
```
HTTP/1.1 500 Internal Server Error
Date: Fri, 20 Jan 2023 03:25:36 GMT
Server: Apache
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, no-store, must-revalidate
X-Request-Id: lETN8J5NgoiwfMPABX3g
x-calendar-response: true
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
X-Robots-Tag: none
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Content-Length: 4472
Connection: close
Content-Type: application/json; charset=utf-8

{"status":"error","message":"Could not send mail: Connection could not be established with host 127.0.0.1 :stream_socket_client(): Unable to connect to 127.0.0.1:25 (Connection refused)","data":{"type":"OCA\\Calendar\\Exception\\ServiceException","message":"Could not send mail: Connection could not be established with host 127.0.0.1 :stream_socket_client(): Unable to connect to 127.0.0.1:25 (Connection refused)","code":0,"trace":[{"file":"\/var\/snap\/nextcloud\/33060\/nextcloud\/extra-apps\/calendar\/lib\/Service\/Appointments\/BookingService.php","line":159,"function":"sendConfirmationEmail","class":"OCA\\Calendar\\Service\\Appointments\\MailService"},{"file":"\/var\/snap\/nextcloud\/33060\/nextcloud\/extra-apps\/calendar\/lib\/Controller\/BookingController.php","line":185,"function":"book","class":"OCA\\Calendar\\Service\\Appointments\\BookingService"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/AppFramework\/Http\/Dispatcher.php","line":225,"function":"bookSlot","class":"OCA\\Calendar\\Controller\\BookingController"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/AppFramework\/Http\/Dispatcher.php","line":133,"function":"executeController","class":"OC\\AppFramework\\Http\\Dispatcher"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/AppFramework\/App.php","line":172,"function":"dispatch","class":"OC\\AppFramework\\Http\\Dispatcher"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/Route\/Router.php","line":298,"function":"main","class":"OC\\AppFramework\\App"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/base.php","line":1047,"function":"match","class":"OC\\Route\\Router"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/index.php","line":36,"function":"handleRequest","class":"OC"}],"previous":{"type":"Swift_TransportException","message":"Connection could not be established with host 127.0.0.1 :stream_socket_client(): Unable to connect to 127.0.0.1:25 (Connection refused)","code":0,"trace":[{"function":"{closure}","class":"Swift_Transport_StreamBuffer"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/3rdparty\/swiftmailer\/swiftmailer\/lib\/classes\/Swift\/Transport\/StreamBuffer.php","line":264,"function":"stream_socket_client"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/3rdparty\/swiftmailer\/swiftmailer\/lib\/classes\/Swift\/Transport\/StreamBuffer.php","line":58,"function":"establishSocketConnection","class":"Swift_Transport_StreamBuffer"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/3rdparty\/swiftmailer\/swiftmailer\/lib\/classes\/Swift\/Transport\/AbstractSmtpTransport.php","line":143,"function":"initialize","class":"Swift_Transport_StreamBuffer"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/3rdparty\/swiftmailer\/swiftmailer\/lib\/classes\/Swift\/Mailer.php","line":65,"function":"start","class":"Swift_Transport_AbstractSmtpTransport"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/Mail\/Mailer.php","line":191,"function":"send","class":"Swift_Mailer"},{"file":"\/var\/snap\/nextcloud\/33060\/nextcloud\/extra-apps\/calendar\/lib\/Service\/Appointments\/MailService.php","line":138,"function":"send","class":"OC\\Mail\\Mailer"},{"file":"\/var\/snap\/nextcloud\/33060\/nextcloud\/extra-apps\/calendar\/lib\/Service\/Appointments\/BookingService.php","line":159,"function":"sendConfirmationEmail","class":"OCA\\Calendar\\Service\\Appointments\\MailService"},{"file":"\/var\/snap\/nextcloud\/33060\/nextcloud\/extra-apps\/calendar\/lib\/Controller\/BookingController.php","line":185,"function":"book","class":"OCA\\Calendar\\Service\\Appointments\\BookingService"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/AppFramework\/Http\/Dispatcher.php","line":225,"function":"bookSlot","class":"OCA\\Calendar\\Controller\\BookingController"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/AppFramework\/Http\/Dispatcher.php","line":133,"function":"executeController","class":"OC\\AppFramework\\Http\\Dispatcher"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/AppFramework\/App.php","line":172,"function":"dispatch","class":"OC\\AppFramework\\Http\\Dispatcher"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/private\/Route\/Router.php","line":298,"function":"main","class":"OC\\AppFramework\\App"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/lib\/base.php","line":1047,"function":"match","class":"OC\\Route\\Router"},{"file":"\/snap\/nextcloud\/33060\/htdocs\/index.php","line":36,"function":"handleRequest","class":"OC"}],"previous":null}},"code":0

```

## Impact

Some internal paths of the website are disclosed.

## Attachments
No attachments
