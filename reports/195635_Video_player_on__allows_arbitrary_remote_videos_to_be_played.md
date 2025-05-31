# Video player on ███ allows arbitrary remote videos to be played

## Report Details
- **Report ID**: 195635
- **URL**: https://hackerone.com/reports/195635
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-04T01:53:28.404Z
- **Disclosed**: 2019-12-02T17:54:17.966Z

## Reporter
- **Username**: tomnomnom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:** A Flash video player hosted on ███████ can be provided with an arbitrary remote XML file via the `url` query string parameter.

**Description:**
The Flash video player (http://█████/shared/widgets/popup.asp) uses the `url` query string parameter as an address to fetch an RSS feed type XML document that specifies a video to play, and meta data about that video.

Although some restrictions are in place to prevent the use of arbitrary URLs (e.g. a request to `http://████/shared/widgets/popup.asp?url=http://█████████/rss.xml` results in a 403 response code), those restrictions are bypassable by replacing `http://` with `//` in the URL.

## Impact

1. An abitrary video can be played in the player, appearing as though the US Air Force is the source of that video
2. The title and description of that video are controllable, again appearing as though the US Air Force is the source of that content
3. The URL pointed to by the 'DOWNLOAD (WMV)' link in the lower left of the player is controllable, and as the download link is in a Flash object there is no 'hover-over' prompt telling the user where the file will be downloaded from. This could be used to trick users into downloading a malicious file under the assumption that it is provided by the US Air Force.

## Step-by-step Reproduction Instructions

A web server has been configured at http://████/ to aid in a proof of concept, and a working PoC can be seen at this URL: http://███████/shared/widgets/popup.asp?url=//████/rss.xml

Note that the video is of a mobility scooter race, the title is set to 'Any title you want', the description is set to 'Any description you want' and clicking the 'DOWNLOAD (WMV)' link downloads a file called `bad.bat` (which is actually harmless in this case).

The webroot of the server contains the following files:

* http://██████/crossdomain.xml - a permissive crossdomain settings file
* http://█████████/rss.xml - the XML file containing the video URL and meta data
* http://████████/video.flv - the video file itself
* http://████/bad.bat - a placeholder for a malicious file

These are the only files required for an attacker to exploit this vulnerability. Copies of the `crossdomain.xml` and `rss.xml` are attached, as is a screen recording of the problem being demonstrated.

## Suggested Mitigation/Remediation Actions

Without seeing the source code it's difficult to know how the `url` parameter is currently being checked, but the workaround's existence suggests some kind of substring checking. It's often a good idea to use a well-tested URL parsing library - which, in theory, should be immune to tricks like using `//` - and compare the domain of the URL to a whitelist instead.

## Attachments
No attachments
