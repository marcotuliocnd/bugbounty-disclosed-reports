# HTML TAG INJECTION ON PROFILE NAME

## Report Details
- **Report ID**: 358001
- **URL**: https://hackerone.com/reports/358001
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-27T00:05:21.177Z
- **Disclosed**: 2018-07-27T20:29:54.770Z

## Reporter
- **Username**: rootbakar_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Allows me to change the profile name to an image tag <img src="........"/> and convert it into an html code and this tag appears perfectly on the "snippets" page.

Suppose I include an image tag with source <img src="http://progress28.web.id/abc.jpg"> and when another user sees it on the "https://gitlab.com/snippets/1718284" page it will appear an image of an anonymous.

I can also add a header tag in the profile name with the tag "<h1>HACKED BY TALAOHU28</h1>" and will look perfect on the same page "https://gitlab.com/snippets/1718284".

Other tags that run perfectly include:
</br>
<div></div>
<a href=""></a>
<b></b>


Here's the complete payload I've made as the profile name

</br><h1>HACKED BY TALAOHU28</h1><img src="http://progress28.web.id/abc.jpg"></br><h1>I WANT TO BACK FREE</h1></br>

## Impact

other users can see the page "https://gitlab.com/snippets/1718284" as if being hacked by hackers

## Attachments
- Screenshot_from_2018-05-27_07-02-58.png
- Screenshot_from_2018-05-27_07-03-20.png
- Screenshot_from_2018-05-27_07-04-57.png
