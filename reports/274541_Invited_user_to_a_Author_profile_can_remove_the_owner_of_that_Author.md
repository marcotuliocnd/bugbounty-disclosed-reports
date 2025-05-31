# Invited user to a Author profile can remove the owner of that Author

## Report Details
- **Report ID**: 274541
- **URL**: https://hackerone.com/reports/274541
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-05T09:06:48.197Z
- **Disclosed**: 2017-10-16T05:48:39.116Z

## Reporter
- **Username**: ranjit_p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
##SUMMURY:

-------------------------------------
A user invite another user to his author by giving ownership.
------------------
Later invited user can completely remove the real owner from  that author .
-------------------

-----------------------------------


##STEP TO REPRODUCE:

-----------------------------

1. Create two user ABC and XYZ.
--------------------
2. Create a author profile in user ABC and invite user XYZ to that author using public_id. Give the ownership to user XYZ.Now user XYZ has full access to that author profile.
---------------------
3. Now goto user XYZ account  and  remove user ABC from that author.
---------------
And see ABC is owner of that author is completely removed from  that author and ABC user cant able to access that Author.
---------------
4. finally user XYZ is the main owner of that author
------------



-----------------------
##FIX:

--------------------------------
check before invited user try to remove  real owner from his Author profile.
-----------
if so , access denied that invited user cant delete real owner from his author profile.
---------

## Attachments
No attachments
