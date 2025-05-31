# Existence of Folder path by guessing the path through response

## Report Details
- **Report ID**: 174645
- **URL**: https://hackerone.com/reports/174645
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-08T12:20:18.534Z
- **Disclosed**: 2017-05-02T15:15:47.153Z

## Reporter
- **Username**: ashish_r_padelkar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: files

## Vulnerability Information
**Enter the support PIN from your test site:**
 423088
**Enter the name of your test site :**
 https://bugbounty5.brickftp.com
**Enter the subdomain from your test site :**
 https://bugbounty5.brickftp.com

----

**Description**

Suppose there are 2 `Folders` in the site

`Test1`
`Test2`

but a member has only `Admin` permission to `Test1` , he cant see the folder `Test2`

However, it is possible to know if such `folder/path` (Test2) exist in a site by guessing the names of the folder.


**Steps**

1.There are 2 `folders` in a site namely `Test1` and `Test2`
2. Member has full `Admin` permission to `Test1` and no permission at all to `Test2`. Member wont be able to see the folder `Test2` in his account at all.
3. Now member selects any file from `Test1` using checkbox and select move option from dropdown. he gets only path to `Test1` folders. 
4. now if i type some random names of the folders in the box and say move, it will throw the error. but if type the valid names of folders which may be in a site, it will say can not write. 
5. this proves that, if you can guess correct name of folder/path, it tells you the existence of the path.

**POC**
https://youtu.be/mzPXVHIDnzs

**Resolution**
The response should be same for both requests. folder exist or not, it should throw 404!



**The date you tested for and found the vulnerability**
08/10/2016

**The following affirmative statement **
I HAVE READ AND UNDERSTAND AND AGREE TO THE TERMS OF THE BUG BOUNTY PROGRAM. I AGREE TO THE BRICKFTP TERMS OF SERVICE. I HAVE COMPLIED AND WILL COMPLY WITH THE RULES OF THE PROGRAM AND THE TERMS OF SERVICE. I HAVE NOT DISCLOSED THIS SUBMISSION TO ANYONE. I DISCOVERED IT MYSELF. I WILL NOT DISCLOSE THIS SUBMISSION TO ANYONE. I DO WANT MY NAME PUBLISHED ON YOUR HALL OF FAME IF THIS IS ACCEPTED


## Attachments
No attachments
