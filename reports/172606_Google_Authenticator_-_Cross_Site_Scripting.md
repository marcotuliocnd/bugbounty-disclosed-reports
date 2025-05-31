# Google Authenticator - Cross Site Scripting

## Report Details
- **Report ID**: 172606
- **URL**: https://hackerone.com/reports/172606
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-28T10:52:23.720Z
- **Disclosed**: 2016-10-11T17:21:56.901Z

## Reporter
- **Username**: iamsha4yan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hello
#Vulnerable File: :
`/views/token-prompt.php`

#Vulnerable Link : 
`15`
`<input type="hidden" name="gapup_login_nonce" value="<?php echo esc_attr( $_REQUEST['gapup_login_nonce'] ) ?>" />`

# Vulnerable Code:
`<?php echo esc_attr( $_REQUEST['gapup_login_nonce'] ) ?>`

Good Luck/

## Attachments
No attachments
