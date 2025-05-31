# Reflected xss on theacademy.upserve.com

## Report Details
- **Report ID**: 415139
- **URL**: https://hackerone.com/reports/415139
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-27T00:21:31.207Z
- **Disclosed**: 2018-09-28T22:14:13.144Z

## Reporter
- **Username**: base_64
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upserve

## Vulnerability Information
**Vulnerabilty**
*Reflected xss* in (https://theacademy.upserve.com).

**STEPS TO REPRODUCE**
1. Go to (https://theacademy.upserve.com/playlists/all-videos/).
2. Click on any video to watch from the playlist and capture the request in burp.
3. you have to capture the request to (https://theacademy.upserve.com/wp-admin/admin-ajax.php?action=load_player&video_id=5742677405001&player_id=B14h0D4OM&type=pc&post_id=2712)
4. then replace the video_id with this payload = r"><BODY%20ONLOAD=alert(1)>.
5. Then see the response in browser and the popup will appear.

**NOTE**: *I also attached a video POC*

## Impact

With the help of *xss* a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their *cookies* and download a **malware** on their system, and there are many more attacking scenarios a skilled attacker can perform with **xss**.

## Attachments
- 20180926_165036_(2).mp4
