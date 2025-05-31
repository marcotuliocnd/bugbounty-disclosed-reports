# profile-picture name parameter with large value lead to DoS for other users and programs on the platform

## Report Details
- **Report ID**: 764434
- **URL**: https://hackerone.com/reports/764434
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-25T14:24:53.824Z
- **Disclosed**: 2020-03-25T02:28:31.250Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
# Summary:

The issue persists as there are no text limitations for profile-picture name while uploading the profile-picture, these heavy text names can cause denial of service on different pages of hackerone.

# Description:

I was checking the profile picture upload feature of  hackerone and found out that there is no text limitation for image name, You can provide as much long image name as you want.
{F668357}

At first it didn’t look like a serious issue so I played with it a little and tried to add some special characters to make it throw a 500 response but didn’t work out.

The next thing I noticed that there are many places where a graphql query is getting executed to fetch the info of the user and the json response is also containing the Image url along with the filename which was provided at the time of upload.

So the first thought that came into my mind is to provide a humongous long string at the place of the image name so I created the payload(attached with the report **payload.txt**) and paste the entire payload in front of the filename, the size of the payload is approx 3MB and it took a little bit of time to execute the request. Account used - @d3f4ul7_m4n

{F668360}

{F668358}

Then I created a dummy report #654270 using my main account(@red_assassin) and invited @d3f4ul7_m4n into that report and found out that a request has been made to the endpoint `/reports/<report-id>/participants/` and as the response contains a humongous text payload it took a long amount of time to load, enough for a timeout and to crash the browser, to create more impact I did the same trick with my another account @fossnow27 and invited it to the same report so that when the endpoint `/reports/<report-id>/participants/` starts loading huge amount of junk gets returned inside the response to crash the report.
> I can also invite you to the dummy report for POC.

{F668359}

As you can see the amount of data loaded is so huge that even burp can't handle it.

Next thing I did was to load all the pages which were displaying my profile pictures in it e.g. profile page, reports page, invited reports page and I noticed that all the pages are taking significantly much more amount of time to load as they were taking before and some were even failing to load and crashing my browser.

{F668371}

# Steps To Reproduce

* Go to https://hackerone.com/settings/profile/edit
* Upload new profile picture and Intercept the request using Burp
{F668357}
* Add the payload text (attached with report payload.txt) at the starting of the filename in the above request e.g `<payload>abcd.png` 


# Security Impact/How an attacker can exploit such behavior

## Scenario - #1

Few months back I reported an issue on hackerone as it was a duplicate issue I got invited as a participant in the original report by the program. Report link - https://hackerone.com/reports/442522
Now suppose if I act as an attacker I can restrict the access to that report for all the participants by doing the above mentioned trick.

An attacker can restrict access of the report if the attacker is an external participant to the report.

## Scenario - #2

> I didn't tried this scenario as I didn't want to affect anything in Production/Live environment.

**Program Pages**
As you can see program pages have top hacker images and the thank you page has hundreds of hacker images. GraphQL queries are used to load the image URLs of the hacker profiles.

{F668378}

{F668379}

In this scenario, a **DDoS** attack is possible if more than one hacker tries to do the same trick as discussed previously, the amount of data needed to load will be huge which can easily crash the web page and the browser of the victim because of this lot of hackerone pages including Program pages can get affected.

## Impact

*  Blocking or Slowing Down of Hackerone pages containing the Payload Image
*  Crashing of Web browser.

## Attachments
- filenameh1.png
- payloadinresponse.png
- h1failurereport.png
- payloadinrequest.png
- h1reportfailure.PNG
- payload.txt
- thankspage.PNG
- h1thankspage.png
