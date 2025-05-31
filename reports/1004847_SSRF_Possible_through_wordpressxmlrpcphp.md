# SSRF Possible through /wordpress/xmlrpc.php

## Report Details
- **Report ID**: 1004847
- **URL**: https://hackerone.com/reports/1004847
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-10-10T21:40:46.247Z
- **Disclosed**: 2020-10-12T15:24:54.410Z

## Reporter
- **Username**: azzassin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hello, 

I have found a SSRF in iandunn.name through the xmlrpc.php API.

I understood you've said about this endpoint in the past making up junk reports, but this is on a function which isn't disabled by disabling the endpoint, as I can prove with a Proof-Of-Concept.

There is a function using pingbacks which can be used when someone has linked your blog post, this makes a request to the website and scans for your post URL and adds it to a database on the site.

It is possible to [disable pingbacks](https://www.wpbeginner.com/wp-tutorials/how-to-disable-trackbacks-and-pings-on-existing-wordpress-posts/) and there is articles on [why you should.](https://www.securityweek.com/pingback-function-wordpress-vulnerable-malicious-use-serves-attack-tool)

I have been using a [grabify link](https://grabify.link) to debug how this works, the Proof-Of-Concept calls for a link to be used where you can review the IPs which have interacted with it, although you could probably use a link on your own domain if you can access the logs, if you are going to use grabify then you will have to set up a redirect URL, I used `http://youtube.com`. You will be given a link like grabify.link/XXXXXX, this is required for the Proof-Of-Concept to function correctly, just click the copy button and move on to the next step.

Execute the Proof-Of-Concept and input the URL you copied, you will then be asked for an amount of seconds to wait between each request, I personally would choose 5, since it's only proving it (There will be more time between each request because the server has to send the request, process and send it back before the code will continue).

The Proof-Of-Concept will print out any error codes the system sends back, there should be none. If there is a message, stop the code and make sure you have copied the URL and pasted it correctly, including the protocol and no slash at the end of the URL. (When the code says `Fault string returned: ` followed by a blank string, it means there is no error)

After it has printed a few links, go the grabify tracking page in your browser, scroll down and see the logged IPs, you may need to refresh your browser and ensure you didn't enable the toggle to stop bots showing up.

I have attacked a Proof-Of-Concept on how this can be abused and screenshots.

## Impact

An attacker can use this to get some idea of the internal network infrastructure or use it in co-ordination with other WordPress web sites to conduct a DDoS on a target

## Attachments
- iandunn.py
- Grabify_Proof_Of_Concept.PNG
- Python_Proof_Of_Concept.PNG
