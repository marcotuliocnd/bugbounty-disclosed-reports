# Stored XSS on team.slack.com using new Markdown editor of posts inside the Editing mode and using javascript-URIs

## Report Details
- **Report ID**: 132104
- **URL**: https://hackerone.com/reports/132104
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-18T19:29:54.692Z
- **Disclosed**: 2016-09-01T01:47:40.659Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi,

I noticed while looking at an old article I made a while ago that some links were actually inserted as `javascript:`-links. Doing some modifications to these actually revealed that inside editing mode, no protection is added for getting arbitrary scripts to run. This means that by catching the modifications for the Web Socket, I was able to create a payload that would trigger on click (only inside Editing mode for some reason).

Here's the vulnerable socket-request I modified to get the payload in:

As you see in my post, I delete a link, then do a Ctrl+Z to undo it, putting back the link. I then capture that request and modify the request to insert the payload inside the `links` part:
```
{"type":"rocket","event":"rocket","payload":{"mm":[["fi",[],3,{"type":"unfurl","originalFragment":{"_bindings":{"attach":[[]],"mutation:post":[[]],"attached":[[]],"detach":[[]],"detached":[[]]},"_bindingLock":0,"_customData":[],"_data":{"type":"p","text":"javascript:alert(document.domain%29","tabbing":0,"links":{"javascript:alert(\"XSS\"%29":[0,22]},"formats":[]},"_dom":null,"_mutable":{"_lock":0},"_mutableGuard":{"_lock":0},"_parent":null,"_text":"javascript:alert(\"XSS\"%29","_tabbing":0,"_links":{"javascript:alert(\"XSS\"":{"_ranges":[{"_s":0,"_e":22}]}},"pendingUnfurls":[],"_formats":{"b":{"_ranges":[]},"i":{"_ranges":[]},"u":{"_ranges":[]},"strike":{"_ranges":[]},"code":{"_ranges":[]}}},"url":"javascript:alert(\"XSS\"%29"}]],"r":19,"$":15,"type":"mm","sel":[[3],0,[3],0]},"id":25}
```

Here's a PoC-image when clicking the link when I'm editing the post in my team:
{F87107}

Also, since you're able to get other people to edit it as well, by enabling "Let others edit this Post" you can get other people affected in your team. What's also interesting is that when creating a public link, that will be hosted on slack-files.com, there's a catcher for links that does not begin with `^http(s)?:` which is awesome, however, this is not the case when editing a post on the team domain, which is a bit worse, since it's not sandboxed at all.

This is the link to my team's post:
https://marqueexss.slack.com/files/marqueexss/F0283AA4K/__hello__a_name__n____href__javascript_alert__xss_____you___a_

Also, here's a link to the public post:
https://slack-files.com/T025M9QPZ-F0283AA4K-2989c27641
to show you that the link has indeed the `javascript:` uri, however, this little snippet is triggered, which is great:
```
if (protocol && /^https?:$/.test(protocol) === false) {
     e.preventDefault();
     if (console && typeof console.warn === "function") {
         console.warn("not following bad link from a post preview")
     }
}
```
(This code is not present in the Edit-mode on the team URL as mentioned above)

PoC-movie is attached showing the complete flow from editing to triggering the XSS. I've also verified that it will trigger for other users in the team if they edit the post. 

Regards,
Frans

## Attachments
No attachments
