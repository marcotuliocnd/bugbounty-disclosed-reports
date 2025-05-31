# Stored XSS in Elastic App Search

## Report Details
- **Report ID**: 846905
- **URL**: https://hackerone.com/reports/846905
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-10T21:47:48.472Z
- **Disclosed**: 2020-07-28T18:26:29.596Z

## Reporter
- **Username**: iamnoooob
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
**Summary:** 
There exists a stored XSS via reference_ui in "URL" Parameter in the latest Elastic App Search v7.6.2 (Tested both on cloud and local instance)

**Description:** 
Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-I XSS.

## Steps To Reproduce:
1. Go To https://cloud.elastic.co/ and login

2. Create a Deployment by visiting https://cloud.elastic.co/deployments/create

3. Fill & Select all necessary details but under **"Optimize your deployment"** section select **"App Search"** & Click Create Deployment

4. Now go to your deployment and click "launch" on your App Search instance and you would be taken to something like `https://069c551087be451bb8d1aecb3cf64341.app-search.us-east-1.aws.found.io/login`

5. Now Login with the provided credentials and Click **"Create an Engine"**

6. On the next screen, Click **"Paste JSON"** and put this 
```
{
"url":"javascript://test%0aalert(document.domain)"
}
```
7. Next, Go to "Reference UI" tab on the menu at the left and under "Title field (optional)" field select "url" and also under "URL field (optional)" field select "url" and finally click "Generate Preview" and you would be take to something like `https://069c551087be451bb8d1aecb3cf64341.app-search.us-east-1.aws.found.io/as/engines/test/reference_application/preview?titleField=url&urlField=url`
{F783219}

8. Press **"CTRL + CLICK"** or **middle mouse button** on the Title and XSS will be executed.
{F783213}

9. The Generated link `https://069c551087be451bb8d1aecb3cf64341.app-search.us-east-1.aws.found.io/as/engines/test/reference_application/preview?titleField=url&urlField=url` can directly be shared with High privileged users etc.

## Impact

A low privileged user with only access to create/index documents can create a document with such evil JSON and can send a link of Reference UI to Admin/Owner which when clicked would lead to Stored XSS

## Attachments
- Screenshot_105.png
- Screenshot_106.png
