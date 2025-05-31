# IE 11 Self-XSS on Jira Integration Preview Base Link

## Report Details
- **Report ID**: 212721
- **URL**: https://hackerone.com/reports/212721
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-12T06:34:08.144Z
- **Disclosed**: 2017-03-29T08:04:01.188Z

## Reporter
- **Username**: ziot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
I wasn't sure if you would accept this report due to it being Self-XSS, but I figured it might be useful information because it breaks one of the flows used to validate URLs.

Steps
====================

1. Launch IE 11
2. Log into a HackerOne account that has admin on a program.
3. Go to the Automation -> Integrations -> Jira page, e.g.
 * https://hackerone.com/buer_haus/integrations
 * -> https://hackerone.com/buer_haus/integrations/jira/edit
4. Set the Base URL input to the following:
 * `javascript://alert(document.domain);%2f%2f@`
{F168165}
5. Fill in the rest of the required inputs with any data.
6. After the AJAX request is sent to Preview, you'll have generated a `Test escalation URL` link under Section 2 Test Integration.
{F168164}
7. Click the `Test escalation URL` link.
8. ---> You executed a JavaScript alert in a new window displaying the context as hackerone.com
{F168166}


Info
====================

There's a Cross-Site Scripting vulnerability on the program Configure JIRA Integration page. When the user puts a URL into the Base URL input, it sends an AJAX request to `/jira_integrations/preview` and returns with a JSON response containing a URL in `example_escalation_url`. This JSON value gets placed into an <a href> element on the page. It's possible to break the URL validation in a way that it returns with a JavaScript data URI so that it executes JavaScript when a user clicks on the link.

This is relatively low impact because of the following:
 * The JavaScript link text is shown in a preview right above the URL. It's pretty obvious it's a JavaScript link at that point.
 * It breaks the URL validation on the POST preview and not on the actual PUT request to save the URL to the integration page. Maybe there's a way around this, but I couldn't find a way. This makes it a Self-XSS and not Stored.
 * Even if you could get it Stored, it's protected by CSRF so you can't attack other programs. You would have to invite people to your program or attack other users already in your program.
 * The HackerOne CSP rules prevent script-src at `self`. That means this will only execute in browsers that don't support CSP such as IE 11.

Request/Response
====================
URL https://hackerone.com/buer_haus/jira_integrations/preview
POST 
```
pid=123&issue_type=1&base_url=javascript://alert(1)%3B@&summary={{title}}&description={{details_truncated}}+{{1+1}}+#{1+1}&labels=HackerOne&assignee=&custom=test=1
```

Response:
```
{"preview":{"example_escalation_url":"javascript:alert(1);@/secure/CreateIssueDetails!init.jspa?assignee=\u0026description=%7B%7Bdetails_truncated%7D%7D+%7B%7B1+1%7D%7D+%23%7B1+1%7D\u0026issuetype=1\u0026labels=HackerOne\u0026pid=123\u0026summary=%7B%7Btitle%7D%7D\u0026test=1"}}
```

Source
====================
```<a href="javascript:alert(document.domain);%2f%2f@/secure/CreateIssueDetails!init.jspa?assignee=&amp;description=%7B%7Bdetails_truncated%7D%7D+%7B%7B1%2B1%7D%7D+%23%7B1%2B1%7D&amp;issuetype=1&amp;labels=HackerOne&amp;pid=123&amp;summary=%7B%7Btitle%7D%7D&amp;test=1" target="_blank"><!-- react-text: 82 -->Test escalation URL<!-- /react-text --><!-- react-text: 83 --> <!-- /react-text --><i class="icon-external-link"></i></a>```

## Attachments
- test_url.png
- base_url.png
- alert.png
