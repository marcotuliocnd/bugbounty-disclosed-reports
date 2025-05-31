# ██████ Authenticated User Data Disclosure

## Report Details
- **Report ID**: 587214
- **URL**: https://hackerone.com/reports/587214
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-21T17:52:47.504Z
- **Disclosed**: 2019-10-04T15:16:11.942Z

## Reporter
- **Username**: deputy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Background##
The Air Force’s ███ application is exposing members’ personal information to other users with access to the applocaton. We’ve identified two specific issues, but there may be other similar problems in the same vein as the ones described here. The underlying problem appears to be that users are not prevented from visiting the web addresses (URLs) that return others’ data.
███████ Home Page: https://███/█████
Version Number: 1.85.10

###Caveats###
1. Users must first be able to login to ██████ in order to exercise these issues. Members’ data is not being exposed to just any user on the web, as far as we know
2. All screenshots containing member data were taken with the consent of the member. Personal information has been redacted and replaced with placeholders (Person #1 and Person #2). Person #1 is the logged in user. Person #2 is another user whose data is being accessed by Person #1, with Person #2’s consent.

##Issue #1: Exposure of Members’ Vulnerable Mover List (VML) Status Information##
BLUF: Talent Marketplace exposes members’ bid/preference information along with the CC’s ranking and comments sent to the Air Force Personnel Center to any logged on user in the VML cycle.
When you visit the “My VML Status” page you are presented by the position preferences you’ve chosen, the bids you’ve received, your Losing Commander’s comments/ranking, and some other information about your VML cycle. See ███████

In order to present you with this information, your browser makes a request in the background for the information it uses to populate the webpage. This request is easily viewable using developer tools present in most modern browsers.

████████ shows the raw data sent to your browser in response to the request it sends. You can see all the preferences you put in, information on the bids you’ve received, and your Losing Commander’s ranking and comments for the member. Notice the redacted “personId” labeled “ID #1” at the very top of the screenshot. This is a unique ID tied to Person #1 (you). If you replace this ID with that of Person #2, and make the request again, the server will send you all the same information for Person #2, even though you (not Person #2) are making the request.

Taken to the nth degree, any user could iterate through all “personId” values to gather all bid/preference/CC comments for everyone in a VML cycle, but there’s also a way to determine the “personId” of any arbitrary user.

###Finding a Member’s PersonID###
On the “My Profile” page, there’s a button you can click to change your military supervisor. When you begin typing someone’s name in the dialog box, your browser makes another background request to search the server’s database for users with that name. Contained in the response is the user’s “personId.” This is not necessarily a problem in and of itself, but it can be used to determine the Person ID of the member whose VML Status you wish to see. See ██████████.

###Key URLs###
Note: You must first log in to the ████ application before visiting these URLs
**Access Arbitrary Member’s VML Cycle Info By Person ID (Replace XXXXXX with Person ID)**
https://█████/███/IndividualReport/GetVmlEligibleBidInfoData?personId=XXXXXX&vmlCycleId=4
**Determine Arbitrary Member’s Person ID By Name (Replace XXXXXX with Name)**
https://███/██████/SearchPersonUser/FindPerson?SearchTerm=XXXXXX

##Issue #2: Exposure of Other Members’ Career Brief##
BLUF: ███ exposes other members’ career brief to any logged on user.
When you view the “My Boards” section of ████, there’s a link that you can visit to see a PDF of your career brief as seen by the Board. The URL for this PDF uses another unique ID (not the same as PersonID from Issue #1) to determine whose career brief you see. If you replace your unique ID with someone else’s in the URL, you can see their Career Brief, which contains Privacy Act data. See ███.

###Finding a Member’s “Encrypted ID”###
The Career Brief page uses an “Encrypted ID,” to identify a member. It is much longer than a “Person ID,” making it difficult to just iterate over all possible IDs, but there is a way for you to find the Encrypted ID of a particular user if they have a mentor profile. When you view the members’ mentor profile in the “Mentoring Connections” section of ██████████, the URL contains their Encrypted ID. If you copy and paste that ID and replace your ID with theirs in the URL for your career brief, you will see their career brief, which is clearly marked as Privacy Act Data, and should not be visible to any member. See ████

###Key URLs###
Note: You must first log in to the ████ application before visiting this URL
**Access Arbitrary Members’ Career Brief By Encrypted ID (Replace XXXXXX with Encrypted ID)**
https://███████/███/Dashboard/CareerBrief/PrintOfficerCareerBrief?person=XXXXXX

##Suggested Mitigations##
We suggest that █████████ enforce access to user data based on the current logged in user, rather than just the PersonID or Encrypted ID the user presents in the request URL.

It’s likely that there are other API endpoints accessible to the user that have similar issues to the two presented above. We also recommend surveying all API endpoints to ensure they are properly validating that the logged in user is only requesting their own information rather than that of any other user.

## Impact

Any user logged into USAF ███████ can see data, including Privacy Act data, of other users through the application. The issue does not expose user data to the open Internet, but it does expose it to other legitimate users who should not be able to see it.

## Attachments
No attachments
