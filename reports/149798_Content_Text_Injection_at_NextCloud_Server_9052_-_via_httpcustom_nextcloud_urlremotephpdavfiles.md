# Content (Text) Injection at NextCloud Server 9.0.52 - via http://custom_nextcloud_url/remote.php/dav/files/ 

## Report Details
- **Report ID**: 149798
- **URL**: https://hackerone.com/reports/149798
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-07-07T16:31:36.225Z
- **Disclosed**: 2016-12-02T20:01:48.371Z

## Reporter
- **Username**: abcdefghijklmnopqrstuvwxyzabc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Dear Next Cloud Security Team,

I would like to report an issue. This is not a critical issue since the affect and not even "touch" something sensitive that stored at the server via the application. As a summary, this is issue need the user interaction for exploiting the "target". So, based on this simple summary, I put it as a "Design Issue".

I. Introduction
---------------------
Generally, Content (which is Text in this case) Injection is an Attack that using the missing input validation at an trusted URL or even form in the specific web application. Usually, this attack can work with the non-aware user that targeted as a victim. In short, based on OWASP, this attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. 
.

II. Summary of the Issue
---------------------
As described above, the issue could allow the Attacker inject any "very convince" message via the URL that not give the "total" validation of the input yet. Please kindly note, I put the word of "total" because the validation is only for "/" character.
.

III. Situation and Condition
---------------------
3.1. The location of this affected URL could be found in 2 (two) different URL, which is: `http://nextcloud_custom_URL/remote.php/dav/files/<Inject_here>` and `http://nextcloud_custom_URL/remote.php/dav/files/<registered_user>/<Inject_here>`
3.2. As an information, one of those URL will works if we know the registered user at the application (noted with <registered_user>) in the sub point #3.1.
3.3. Both of those URL need the different "convince word" to gaining the "user's trust".
.

IV. Proof of Concept
---------------------
The proof of concept isn't that hard. The victim just need to visit one of those 2 (two) URL with "convince" word. For example:
4.1. `http://nextcloud_custom_URL/remote.php/dav/files/nxtgrpone2/The%20location%20of%20the%20files%20are%20moved%20to%20another%20url%20that%20could%20be%20found%20at%20fakenextcloud.com%20domain.%20Please%20visit%20the%20file%20at%20those%20new%20location%20with%20%22sample%20fake%20file.txt%22` --> please see the **"1st URL.png"** as reference.

4.2. `http://localhost/nextcloud/remote.php/dav/files/of%20yoko%20is%20removed%20in%20this%20old%20server.%20Please%20kindly%20visit%20the%20the%20new%20server%20with%20the%20same%20username%20at%20fakenextcloud.com%20domain.%20Please%20contact%20us%20again%20in%20yoko@fakedomain.com%20if%20you%20get%20the%20same%20error%20again,%20which%20is%20files`  --> please see the **"2nd URL.png"** as reference.
.

V. Recommendation
---------------------
5.1. Well, even it will be a classic looks and sounds, giving the validation of the input at those affected URL will minimize the risk. In this case, every invalid input should be redirected to custom URL;
5.2. The second one, related the URL that affected "if" Attacker knows the registered user, then it would be good if  the user enumeration is disable.
.

Best Regard,

YoKo

## Attachments
- 1st_URL.png
- 2nd_URL.png
