# Remote Unrestricted file Creation/Deletion and Possible RCE.

## Report Details
- **Report ID**: 191884
- **URL**: https://hackerone.com/reports/191884
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-17T06:45:02.720Z
- **Disclosed**: 2017-02-26T21:13:08.032Z

## Reporter
- **Username**: zigoo0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hello Gents,

During my research on Twitter BBP, I found below domain name: **Reverb.twitter.com**

###Background:
>We worked with Twitter to develop TwitterReverb, an application that reveals how conversations arise and reverberate across the entire Twitter landscape. The custom application allows visitors to reveal patterns in Twitter activities related to keywords, hashtags, topics, people, and individual tweets through the use of a backend administrative tool that dynamically generates a custom data visualization.
>"TheRealPeriscopic" -> https://www.youtube.com/watch?v=bm5eyTeBBDE

###Description:
Reverb.twitter.com (also uses **reverb.guru**) is vulnerable to unauthenticated remote file Creation/Deletion and Possible RCE vulnerability.
Below URL is an API file used to generate png images based on 3 given inputs:
https://reverb.twitter.com/api/actions/saveImage.php

The 3 given inputs are: **image**=SomeContent&**filename**=test&**extension**=png

It was found that the file doesn't require authentication or authorization in order to be able to initiate the API call to generate a new png file. it doesn't even validate the created file name.

In normal scenario, to use the file you have to send a POST request as below:
https://reverb.twitter.com/api/actions/saveImage.php
**POST:**
image=SomeContent&filename=test&extension=png

the a/m example should create a png file named as "preview-test.png" in below directory:
/var/www/html/view/data/image/preview-test.png

**Example of normal file operation output:**
https://go.reverb.guru/view/data/image/preview-069772811858678284.png

Since I've the ability to choose the file name & ext, i've manipulated the file ext to be php and the file name to be /../../zigo (Directory Traversal) which allowed me escape the "preview-" added to the filename and to escape the uploads directory to create a file as below:

https://reverb.twitter.com/api/actions/saveImage.php
**POST:**
image=SomeContent&filename=/../../zigoo&extension=php

**POC:** https://reverb.twitter.com/view/data/zigoo.php
**PATH:** /var/www/html/view/data/zigoo.php

It is noticed that user input under the parameter "image" is passed to some function that would treat it as image stream and convert it as well to a png image. I imagine that backend code that handles the input of parameter "image" looks like:

><?php
 $data = $_POST['image'];
 $im = imagecreatefromstring($data);
 if ($im !== false) {
    imagepng($im);
    imagedestroy($im);
 }
 else {
    exit;
 }
> ?>

I've wrote a python script (Attached as: F144335) to simulate the same scenario, unfortunately i couldn't trigger the RCE. BUT ......

**Vulnerability Consequences:**
1. Since i can control the filename, ext, and file content, the RCE is still possible if given enough time to research and try, but i always thought that FileDescriptor would have reported it if i delayed :D
2. An attacker can submit the same request over and over with large file size, even if the files contents are not understood, it is still consuming the server space which would cause the server to go down (Space Exhaustion, refer to function **DDOS()** in the attached python file)
3. File deletion and defacement is also possible since Directory traversal were found. for example, an attacker can submit the file name as: **../../../../index.php** which will replace the main page of the vulnerable site!
4. The above mentioned scenario could also be used to cause the **TwitterReverb** application to stop working permanently by overwriting the file **"api/twitter/twitterLogin.php"** which is responsible for the authentication of application users.
5. Also directory traversal scenario could be used to create ".htaccess" file at any directory which would cause all the pages inside that directory to stop working!

**How to Fix:**
1. Set proper authentication/authorization on the affected file.
2. Filename, ext & input content should be validated before being submitted to the backend server. for example the file ext should be restricted to '.png' only & filename should never contain dots or other special characters.
3. A filesize limit must be applied on the created files to avoid DDOS attacks via exhausting the server disk space.

Kindly note that the affected server holds large amount of Twitter users authentication tokens for the TwitterRiverb application.

And finally, below is a POC video to demonstrate the vulnerability and how to reproduce it.

**POC:** https://youtu.be/OPlexp-1XxU

Thank you and have a nice day.


## Attachments
- RCE-Tester.py
- Screen_Shot_2016-12-17_at_8.09.12_AM.png
