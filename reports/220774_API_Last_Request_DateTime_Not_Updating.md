# API Last Request Date/Time Not Updating

## Report Details
- **Report ID**: 220774
- **URL**: https://hackerone.com/reports/220774
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-13T13:52:36.188Z
- **Disclosed**: 2019-05-19T18:14:52.827Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi All,
I believe I've found a minor vulnerability with regards to your API last request date/time. However, I could not find any documentation on what this value is supposed to represent / when it should be relied on so I debated reporting this but figured it might in fact be an issue.

##Description
After creating an API token, on the API administration page, there is a field, ```Last request```. When I created the token, the value was ```Never```. However, after playing with the API, making GET, POST and PUT requests, the last request time never gets updated, it appears to be permanently ```Never```.

In the POC here, you can see that I've received notifications that my API user has performed actions via my notifications popup but the last request remains ```Never```. {F175636}

I should also note that my program is still in sandbox in the event that has some impact on the functionality though I think that would be an odd cause for this. I also have two tokens, one of which I used yesterday just for reading but still says never.

##Vulnerability
While I believe this is minor, I'm reporting because I would think this value was created on the administration page as an added security feature to let administrators know when the API token has last been used. If I'm correct, never updating it would undermine that purpose and create a false sense of security for any administrators relying on the value.

##Steps to reproduce
1. Create a new sandbox program
2. Go to the program settings --> API, the url will be https://hackerone.com/PROGRAM_HANDLE/api
3. Create a token and assign the API user to standard user and admin (or at least I did)
4. Perform some API curl requests -- I used read report, assign report and program details
5. Come back to the H1 UI and confirm you got the notifications for the API assigning a report and creating a comment
6. Reload the /PROGRAM_HANDLE/api page and you'll notice that the last request value has not been updated.

Please let me know if you have any questions and I apologize in advance if I've misunderstood what the last request field is supposed to denote.

Pete



## Attachments
No attachments
