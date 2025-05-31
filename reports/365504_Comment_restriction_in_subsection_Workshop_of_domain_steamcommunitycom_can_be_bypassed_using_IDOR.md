# Comment restriction in subsection "Workshop" of domain "steamcommunity.com" can be bypassed using IDOR

## Report Details
- **Report ID**: 365504
- **URL**: https://hackerone.com/reports/365504
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-13T10:16:17.886Z
- **Disclosed**: 2019-01-07T20:16:03.063Z

## Reporter
- **Username**: ronak_9889
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
Summary -

 While testing Domain "steamcommunity.com", i found subsection "workshop" which has restriction to comment on workshop items of the game which i do now own in my account. This access control can be bypassed using IDOR  and user can post comment though comment section is disabled on workshop page.

Description:-
  
- Steam community contains various subsection among that while testing i found that comment has been disabled for workshop items. Upon finding through below links i found that this is the feature restriction which do not allow to comment on workshop items to users who do not own that game on the account. 

"https://steamcommunity.com/discussions/forum/1/2381701715711036208/"
"https://www.reddit.com/r/Steam/comments/73u13i/cant_comment_on_workshop_items/"

 According to above links users who own the game only can comment on the workshop items that belongs to that app or game. however note that same users can comment on the artwork or create the discussion on the workshop. 

I found IDOR vulnerability using that user can bypass this access control or comment restriction and post comment on same workshop item.

Browsers Verified in:-
This issue is not Browser-dependent but i used Firefox Quantum 59.0.2 while testing for this Vulnerability.

Steps to Reproduce:-
	Login to the "steamcommunity.com" using your account and navigate to https://steamcommunity.com/?subsection=workshop

	Select any workshop item and navigate to the comment section Tab. make sure that you do not own the app of workshop item you have explored. You would find that comments from the other users are displayed but  section to post comment is not available on the page and you are unable to comment on that workshop item. That means if you do not own the app on the account through which you are navigating to workshop item then you have on read access of the comment section tab but not write.

	However, this restriction can be bypassed using the IDOR vulnerability. Users are able to comment on the "Artwork" subsection for the same any app or game  and this subsection has no such restriction. select any artwork and while posting comment on the Artwork intercept the request using Burp or any proxy.

	On intercepted request, change the contributor id of URL to workshop item contributor on which you want to post comment, change file id of URL to workshop item file id. There is post parameter on same request "extended _data" change the contributor id and app id that belong to the workshop item. Set the count parameter to number of comments currently on workshop item.

	Now forward the edited request and you would find that comment was successfully posted on the workshop item.


Proof of Concept:-

	 I have reproduced this vulnerability using my profile named "King Kong" and has profile id 76561198039572190. This account is at level for and not have limited access.

	I logged in using the above mentioned profile and navigated to the steam community subsection "Workshop" through below link

https://steamcommunity.com/?subsection=workshop

	From, listed workshop items on this section,i selected particular workshop item available on below link
" https://steamcommunity.com/sharedfiles/filedetails/?id=1404861377"

On the comment section of this workshop as visible on the attached screenshot "comentdisabled_workshop" ,comments are disabled and there is no section to post comment due the fact that app that belongs to this workshop item do not have in my account.

	Now, I opened source of this webpage and noted contributor id,app id and file id as highlighted on the attached screenshot "source_workshop"

	As mentioned on the "steps to reproduce" comments are allowed for any artwork section. so I went to the artwork available at below link

" https://steamcommunity.com/sharedfiles/filedetails/?id=1406988713"
In comment option of this artwork i posted comment "testrestriction"  and intercepted request using Burp proxy.
This intercepted request is visible on the attached screenshot "artwork_comment_originalrequest"

	As highlighted on the screenshot "artwork_edited_request",  i edited profile id and file id on the URL. Replaced profile id and file id are of the workshop item which we noted from the source of the webpage of workshop item as mentioned on the third step of this POC. In the POST parameter of the request, i set count to the number of comments currently existing on the workshop item. edited the app id and contributor id of the extended_data parameter as 
well.  

	I forwarded the edited request now and comment was successfully posted on the workshop item as visible on the screenshot "success_response" and "comment_added_workshop".


References:- 
Below report is mentioned for the reference purpose. It may have different impact functionality-wise and has been reported for the different endpoint but same vulnerability IDOR has been found which violated read access control.
https://hackerone.com/reports/308610

## Impact

Attacker can post comment on the restricted section "workshop" for which he/she do not have write access as he/she do not own that game on the account. So this restriction can bypassed by the attacker.

## Attachments
- artwork_comment_edited_request.png
- artwork_comment_originalrequest.png
- comentdisabled_workshop.png
- source_workshop.png
- commment_added_workshop.png
- success_response.png
