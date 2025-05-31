# IDOR allows an attacker to delete anyone's featured photo.

## Report Details
- **Report ID**: 1608735
- **URL**: https://hackerone.com/reports/1608735
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-22T01:59:55.808Z
- **Disclosed**: 2023-08-24T02:49:54.239Z

## Reporter
- **Username**: adilnbabras
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
Hi Team, previously I submitted a bug report #1606896  that closed as informative without understanding my proof-of-concept and I believe that the bug is 100% exploitable so here I am again explaining my proof-of-concept. I hope this time you people get my point.
I found an IDOR while deleting featured images, allowing me to delete anyone's featured images all over Linkedin. The request takes two main parameters ==ImageId== and ==ProfileId==. Both of these parameters are almost impossible to guess or brute force, but when I'm looking at the victim's profile featured images I noticed that both of the ==required parameters are available in the link itself==.
> Hence, there is no need to guess or enumerate the parameters and then I can delete anyone featured images.

==Note: If you can't get any point then please let me know.==

Step To Reproduce:
-------------------
1. Make two accounts one is for the victim and the other for an attacker.
    
2. Add some featured images in both accounts. Go to
    Profile --> Add Profile Section --> Recommended --> Add Featured

3. Delete an image on the attacker's account and capture that request using burp and sent it to the repeater.
    It makes a delete request like the one, given below.
```
DELETE /voyager/api/voyagerIdentityDashProfileTreasuryMedia/urn:li:fsd_profileTreasuryMedia:(█████████,███████)?sectionUrn=urn:li:fsd_profile:███████
```

4. It takes consists of thress things ==ProfileId== (██████████) , ==ImageId== (██████████) and ==sectionUrn== which also take same ProfileId value.
    

5. Now visit the victim's profile featured images without logging in as the victim.
    Copy the link of the image you want to delete from the victim's profile, which looks like this.

```
https://www.linkedin.com/in/tension-███████/details/featured/██████/single-media-viewer?type=IMAGE&profileId=██████&lipi=urn:li:page:d_flagship3_profile_view_base_featured_details%3B███████
```

6.  Paste that link into your notepad and notice that in this link, we got both ==ProfileId== , ==ImageId==.
In the above link, I get these.    
profileId = █████
ImageId = ████

7. Now simply replace the respected values of required parameters in the repeater and send a request.

8. You see that the targeted featured image from the victim's profile was successfully deleted.

##POC:

████

## Impact

I am able to delete anyone's featured images on Linkedin.

Thanks,
Regards
AdilnBabras

## Attachments
No attachments
