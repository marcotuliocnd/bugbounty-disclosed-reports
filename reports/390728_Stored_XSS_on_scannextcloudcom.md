# Stored XSS on scan.nextcloud.com

## Report Details
- **Report ID**: 390728
- **URL**: https://hackerone.com/reports/390728
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-05T16:34:39.000Z
- **Disclosed**: 2020-03-01T13:57:00.351Z

## Reporter
- **Username**: 5b66c571
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The scan.nextcloud.com engine fetches a 'status.php' content in order to extract some version number as well as installed flavors.

While scanning a website, the following API-wise cinematic happens :

    POST https://scan.nextcloud.com/api/queue (twice, gives the UUID)
    GET https://scan.nextcloud.com/api/result/<UUID>

The first POST to /queue triggers a scan (/requeue works similarly), and the second request (GET) fetches a JSON describing the scan results.

While all the data fetched in the attacker-controlled "status.php" file are safely escaped with escapeHTML (stripping a lot of unwanted characters, - you might want to double check that \ is escaped as well.), the `data.url` isn't escaped, and is placed in a HTML DOM element as innerHTML

{F328696}

This means that if an URL contains valid HTML, it will be interpreted upon loading the XHR answer. A poc has been done, scanning for `hack.pirate-server.com/heh<script>alert(1)`

    $ mkdir 'heh<script>alert(1)'
    $ ln -s ../status.php heh\<script\>alert\(1\)/

POC : https://scan.nextcloud.com/results/166b377c-a24d-41b3-bcec-1ae57dd651c8

When loading the results, the <script> element is inserted, and an alert(1) pops :
{F328697}

poc demo :
{F328698}
end

## Impact

An attacker - having tricked an user into accessing a trapped scan report - could gain arbitrary javascript execution in the context of `scan.nextcloud.com`, which is a subdomain of nextcloud.com.

While this might not be critical, maybe a Content-Security-Policy of another nextcloud.com domain blindly trusts *.nextcloud.com.

Which could mean the standard XSS consequences : impersonation, secret stealing, proxying traffic, drive-by malware download, etc. etc.

## Attachments
- Screenshot_from_2018-08-05_18-11-25.png
- Screenshot_from_2018-08-05_18-10-58.png
- Screenshot_from_2018-08-05_18-10-20.png
