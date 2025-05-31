# CSRF token validation is missing

## Report Details
- **Report ID**: 221043
- **URL**: https://hackerone.com/reports/221043
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-14T18:25:57.134Z
- **Disclosed**: 2017-04-19T06:55:51.732Z

## Reporter
- **Username**: 596a96cc7bf9108cd896f33c4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Greetings,

Hello Security Team,

### Summary
I know this is a medium risk issue but i want you guys to be aware of it that the CSRF token validation is missing at the time of login on `https://portal.nextcloud.com/login.php` login page.

### PoC Code:
```
<form name="frmlogin" action="https://portal.nextcloud.com/login.php" method="post" onsubmit="return ValidateForm();">
	<div class="row">
		<div class="col-xs-12">
			<div class="form-group">
				<label class="control-label">Email</label>
				<input type="text" name="member_username" id="member_username" value="" class="form-control">
			</div>
		</div><!-- col-sm-12 -->
		<div class="col-xs-12">
			<div class="form-group">
				<label class="control-label">Password</label>
				<input type="password" name="member_password" class="form-control">
			</div>
		</div><!-- col-sm-12 -->
		<div class="col-xs-12">
			<div class="form-group text-center">
				<button class="btn btn-search btn-primary col-xs-12 mb10" style="padding:10px;margin-top:10px;" type="submit" name="login" value="Login Now">Login Now</button>
				<a href="https://support.nextcloud.com/#password_reset">Forgot Password?</a>
			</div>
		</div><!-- col-sm-12 -->
	</div><!-- End Row -->
</form>
<script type="text/javascript">
	var tabs = '';
	//<![CDATA[
	function ValidateForm()
	{
		var f = document.frmlogin;
		if(f.member_username.value=='')
		{
			alert('Please enter the Username.');
			f.member_username.focus(); return false;
		}
		if(f.member_password.value=='')
		{
			alert('Please specify the Password.');
			f.member_password.focus(); return false;
		}
	}
	//]]>
</script>
```
### PoC Attached is the html code: {F175917}

### Impact:
* An attacker can Brute force their password.
* Brute force Attack


Regards,
j3

## Attachments
- csrf_token_is_missing.html
