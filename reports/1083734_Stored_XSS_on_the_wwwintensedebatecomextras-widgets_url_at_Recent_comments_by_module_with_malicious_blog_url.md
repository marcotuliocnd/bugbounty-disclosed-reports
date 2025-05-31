# Stored XSS on the "www.intensedebate.com/extras-widgets" url at "Recent comments by" module with malicious blog url

## Report Details
- **Report ID**: 1083734
- **URL**: https://hackerone.com/reports/1083734
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-21T22:39:03.620Z
- **Disclosed**: 2022-04-13T18:04:24.185Z

## Reporter
- **Username**: superpan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hello team. I have found a place where filtration/encoding for special symbols used in blog/site url  is not set which leads to Stored XSS on the user page who posted a comment on malicious blog/site.

## Platform(s) Affected:
Affected page www.intensedebate.com/extras-widgets block "Recent comments by". After loading, this page makes a request to https://www.intensedebate.com/widgets/userComment/27205148 - (where 27205148 is userID) to receive additional javascript logic and list of user's comments with html  pre set.

Here are Payloads for malicious blog / site.
For context of "a" tag a malicious url must be like this ``` http://████.herokuapp.com/"onmousemove=console.log(`Happy-hack!`);>.html```
For context of "html" document a malicious url must be like this ```http://██████████.herokuapp.com/"><img+src=z+onerror=console.log(`Happy-hack!`);>.html```
You can encode this url as URI to hide these special symbols from users eyes or load this page in some iframe.
I used Heroku service to demonstrate this case. I used this console.log (...) payload so as not to bother real users because I don't know where else it might appear.

Here are some pieces of code from this https://www.intensedebate.com/widgets/userComment/27205148 request.
Line #2 contains generated html with comments where two links are not filtered / escaped "Jump to" and "Document", but 3th link is escaped!
```javascript
var theHTML = '... <a href=\"http://████.herokuapp.com/\"><img src=z onerror=console.log(`Happy-hack!`);>.html#IDComment1096880652\" class=\"idw-jump\"><span>Jump to</span></a> </p> <p><a href=\"http://█████.herokuapp.com/&quot;&gt;&lt;img+src=z+onerror=console.log(`happy-hack!`);&gt;.html\">http://████████.herokuapp.com/&amp;quot;&amp;gt;&amp;lt;img+src=z+onerror=console.log(`happy-hack!`);&amp;gt;.html/</a> / <a href=\"http://████.herokuapp.com/\"><img src=z onerror=console.log(`Happy-hack!`);>.html\">Document</a></p> ...
```
and line #20 (in my case) where `theHTML` code is written into html document
```javascript
 document.write('<style>....</style><div class="idw-container" id="IDWidget1">' + theHTML + '</div> ...');
```

## Steps To Reproduce:
First of all we need to have two accounts to test this case. e.g the first is an Attacker who is the owner of malicious blog/site and the second is victim user. Let's say we have two accounts "Attacker" (set "I want to install IntenseDebate on my blog or website" while registration) and "Victim"

**Attacker steps:**
  1. Create a page on the Attacker's blog/site and set the name of route or static file (in my case) as 
```"onmousemove=console.log(`Happy-hack!`);>.html``` or ```"><img+src=z+onerror=console.log(`Happy-hack!`);>.html``` 
  2. Login into https://www.intensedebate.com
  3. Navigate to https://intensedebate.com/install and add blog/site with payload e.g ```http://██████.herokuapp.com/"><img+src=z+onerror=console.log(`Happy-hack!`);>.html```
  4. Then go next to *"Step: 2"* and choose platform (in my case it's "Generic Install"). I think this works for every platform.
  5. Then do JavaScript installation on the Attacker's blog/site *"Copy and paste the following code into the area where you would like Intense Debate comments to appear:"*
  6. You can use this functionality to trigger users to visit your blog / site *"Let people know that you have installed IntenseDebate"*

**Victim steps:**
  1. Login into https://www.intensedebate.com
  2. Visit  the Attacker's blog/site and login there
  3. Post a comment
  4. Then navigate to this page https://intensedebate.com/extras-widgets
  5. Pay attention to "Recent comments by" block

## Supporting Material/References:
{F1167118}

{F1167119}

{F1167120}

{F1167124}

## Impact

In this case an attacker can use his own blog / site to inject and run arbitrary code on the "intensedebate.com" users page. It's possible to make malicious request from users account to somewhere or to someone or interact with user's personal data by injection more complex payload and so on.

You need to filter/escape these "Jump to" and "Document" affected places before rendering on the front-end.

## Attachments
- affected_html_code.png
- theHTML_variable.png
- loaded_script_this_html.png
- stored_xss_example.mov
