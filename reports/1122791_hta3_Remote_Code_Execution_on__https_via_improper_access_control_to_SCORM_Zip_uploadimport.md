# [hta3] Remote Code Execution on  https://███ via improper access control to SCORM Zip upload/import

## Report Details
- **Report ID**: 1122791
- **URL**: https://hackerone.com/reports/1122791
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-03-11T05:59:47.432Z
- **Disclosed**: 2022-09-15T13:28:18.119Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary:
There is a Remote Code Execution vulnerability at https://█████████/Kview/CustomCodeBehind/base/courseware/scorm/management/scorm2004uploadcourse.aspx which allows any user to upload a SCORM course package. Furthermore, an attacker can add an ASPX shell to the SCORM package which will then get extracted onto the server, where the attacker can then execute commands.

## Steps To Reproduce:

  1. Visit `https://███████/` and log in with the credentials: `██████████`
  2. Now download this "malicious" SCORM course package: █████
  3. If you `unzip scorm.zip`, you will notice this is a valid SCORM [package](https://scorm.com/scorm-explained/technical-scorm/content-packaging/), and you will also notice that I've included an ASPX file in `shared/cdlcdlcdl.aspx` which runs the `whoami` command. Notice I also included that file reference in the Scorm Manifest (`imsmanifest.xml`)
4. Visit https://████████/Kview/CustomCodeBehind/base/courseware/scorm/management/scorm2004uploadcourse.aspx, select the ██████ file. Start **intercepting** in Burp Suite Repeater. 
5. Forward the POST request to `/Kview/CustomCodeBehind/base/courseware/scorm/management/scorm2004uploadcourse.aspx`
6. Now intercept the request to `/Kview/CustomCodeBehind/base/courseware/scorm/management/scorm2004editmetadata.aspx`
7. Right-Click on it, Hover down to "Do intercept" and click "response to this request" then forward it.  (In your web-browser you might be able to just right-click, inspect-element, and search for strCourseId in there but my browser was being funky).
8. Once you've received the response, search for "strCourseId" and grab it.

For example, you would grab `F6BAC72B45D64B34ACB662BB001D8523` out of the following response:

```html
<a onclick="return&#32;ConfirmBeforeNavigateAway(&#39;Are&#32;you&#32;sure&#32;you&#32;want&#32;to&#32;navigate&#32;away&#32;from&#32;this&#32;page?&#32;\n\nYou&#32;made&#32;changes&#32;that&#32;will&#32;not&#32;be&#32;saved&#32;if&#32;you&#32;continue.&#32;\n\nClick&#32;OK&#32;to&#32;proceed&#32;or&#32;Cancel&#32;to&#32;return&#32;to&#32;the&#32;page.&#39;);" id="ML.BASE.WF.ReuploadCourse" class="WorkflowButton" NavigatingURL="Courseware/SCORM/Management/SCORM2004ReuploadCourse.aspx" ItemId="&lt;IDTable&gt;&lt;strCourseId&gt;F6BAC72B45D64B34ACB662BB001D8523&lt;/strCourseId&gt;&lt;strVersionId&gt;F6BAC72B45D64B34ACB662BB001D8523&lt;/strVersionId&gt;&lt;/IDTable&gt;" href="javascript:__doPostBack(&#39;ML.BASE.WF.ReuploadCourse&#39;,&#39;&#39;)"><span>Course Files</span></a>
```
9. Now, visit `https://█████/CServer/Courseware/<YOUR_COURSE_ID>/shared/cdlcdlcdl.aspx` and you will see the shell executes:

███

## Supporting Material/References:
- https://█████/CServer/Courseware/F6BAC72B45D64B34ACB662BB001D8523/shared/cdlcdlcdl.aspx

## Proof-of-Concept Video
█████████

## Impact

Critical, an attacker can execute commands on this military server, steal sensitive information, pivot to internal systems, etc.

Best,
@cdcl

## Attachments
No attachments
