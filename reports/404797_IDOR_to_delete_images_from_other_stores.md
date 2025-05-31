# IDOR to delete images from other stores

## Report Details
- **Report ID**: 404797
- **URL**: https://hackerone.com/reports/404797
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-03T16:42:10.715Z
- **Disclosed**: 2018-09-05T17:01:23.798Z

## Reporter
- **Username**: emitrani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Summary:** The parameter `photo_ids` in below request is vulnerable to IDOR

/php/client_manage_handler?██████████&case=remove-active-photo

**Description:** Since there is no check for res_id or ownership I was able to delete Gerben's image by just using the photo_id from his store. This is a problem because it is a get request and I can try a bunch of ID's to randomly delete photos that don't belong to me or try to find a way to leak this ID from store page to do targeted deletes. 

I believe if you try to delete multiple photos there will be more ids in the request so that would allow to expand the attack by trying a lot of ids at once.

**Platform(s) Affected:** [website]


## Steps To Reproduce:


  1. Get 2 stores.
  2. With store 1 navigate to https://www.zomato.com/clients/manage_photos.php
  3. Start to delete a photo and capture the request that looks like :

```
GET /php/client_manage_handler?███&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
X-Requested-With: XMLHttpRequest
Cookie: _ga=GA1.2.2082511252.1535917423; _gid=GA1.2.1587734047.1535917423; PHPSESSID=4821c7caf69f3253db3be3d4c42a15b7b04d223a; fbcity=283; zl=en; fbtrack=a09417c27b7e98b4b3f2ad8357ef3903; __utmx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:NaN; __utmxx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1535944804:8035200; dpr=2; cto_lwid=82057293-9985-419b-a25b-4d8b6d89951b; G_ENABLED_IDPS=google; zhli=1; squeeze=cd186e1f53eee0d94e51ef00c9d4eb25; orange=2769113; al=1; session_id=null
Connection: close
X-Forwarded-For: 127.0.0.1

```

4 . Save the photo_ids parameter
5 . Go to your second restaurant account and capture the same request with a different res_id and cookies
6 . Replace the `photo_ids` with the id from step 4 and send request.
7 . Observe the photo is deleted.

## Impact

By using targeted or blind attacks it is possible to delete photos that don't belong to a restaurant because of this IDOR. My leading theory is that currently you are checking that the logged in user has permissions on the res_id in the request but not verifying that the res_id owns that photograph. There should be an additional check to ensure that the photo_id belongs to that restaurant before deleting it.

Regards,
Eray

## Attachments
No attachments
