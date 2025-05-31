# [node-red] Stored XSS within Flow's - "Name" field 

## Report Details
- **Report ID**: 681986
- **URL**: https://hackerone.com/reports/681986
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-26T09:17:03.178Z
- **Disclosed**: 2020-01-11T16:11:38.868Z

## Reporter
- **Username**: vineetpandey
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report Stored XSS in node-red.
It allows to steal session cookies, deface web applications, etc.

# Module

**module name:** node-red
**version:** 0.20.7
**npm page:** `https://www.npmjs.com/package/node-red`

## Module Description

A visual tool for wiring the Internet of Things.

## Module Stats

> Replace stats below with numbers from npm’s module page:

Weekly downloads - 23,557 


# Vulnerability

## Vulnerability Description

npm-red has flows to demonstrate the Inject, Debug and Function nodes, etc and you can define multiple flows. 
For your customization, when renaming the flow - malicious javascript can be inserted into the "Name" field and Click "Done". Then after clicking the "Deploy" button, changes will take effect. Then Everytime you double-click the flow, inserted malicious code will be executed.

## Steps To Reproduce:
1.
install node-red: sudo npm install -g --unsafe-perm node-red
start node-red: node-red
& 
Open http://localhost:1880

2. Now Edit the flow (refer img_1.png)
3. Insert malicious javascript code and click "Done" (refer img_2.png) 
4. Click Deploy and changes will take place.
5. Double click on flow and you'll observe a pop-up executing the malicious content (refer img_3.png) 

## Patch
Deploy input sanitization/validation around the input fields.

> If you're able to provide a patch with the fix please post it in this section

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Kali linux
- Node.js v12.8.0
- NPM v6.10.2
- Firefox 60.8.0esr
- Burpsuite, if there would have been client side validation

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

This vulnerability will allow the attacker to steal session cookies, deface web applications, etc.

## Attachments
- img_2.PNG
- img_1.PNG
- img_3.PNG
