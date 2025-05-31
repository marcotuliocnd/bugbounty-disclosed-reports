# [OPEN S3 BUCKET] All uploaded files are public. 

## Report Details
- **Report ID**: 905641
- **URL**: https://hackerone.com/reports/905641
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-22T20:30:32.914Z
- **Disclosed**: 2021-04-01T06:14:37.585Z

## Reporter
- **Username**: n0x496n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trycourier

## Vulnerability Information
Hi I found open s3 bucket : backend-production-librarybucket-1izigk5lryla9 

Step to reproduce : 

1- Go to notification and click to create notification 
2- Add new image (also allows svg & xss) then copy image location 
https://s3.amazonaws.com/backend-production-librarybucket-1izigk5lryla9/85abcc94-a7db-4529-b0aa-826e3026c8c1/1592856757262_camion2.svg
Here is your bucket : backend-production-librarybucket-1izigk5lryla9

Configure your s3 command line tool..

Then run : 

$ aws s3 ls backend-production-librarybucket-1izigk5lryla9
```
                           PRE 07d11869-8744-4a59-a871-cf44a833f95d/
                           PRE 07dfd29d-7dee-4d7a-85b8-566d2d223799/
                           PRE 07f4ed3f-3bac-4ca2-bc99-51a51f738d25/
                           PRE 0a5c28b2-47e8-40df-9178-0603dba1c848/
                           PRE 0c34571a-f774-4ad9-b1d3-3e426c3a4327/
                           PRE 131f3727-3ef3-4470-9979-6868678c70a0/
                           PRE 15a5ce40-e45d-4f31-aed1-812187826100/
                           PRE 15cfcb49-fdd2-430c-99e2-cb4fa1ac5db7/
                           PRE 15e77f43-b14a-48ee-9f76-234263e207a7/
                           PRE 18bfd6aa-ae6e-4986-be70-f25fa17b0a3a/
                           PRE 198c03a4-ec81-47e1-8437-dfa3cf2dff40/
                           PRE 1ad057c7-64ea-4ae3-a901-fdbeee68f4c7/
                           PRE 1c9dac1f-d101-4204-95d6-d00dbd293e03/
                           PRE 1d1b07c5-0b6c-4975-8782-41ce5c73c833/
                           PRE 21ab53f9-7936-4ee5-ab0b-81688b3dc752/
                           PRE 24095203-0bb9-4d65-aa8a-84c0524b81e2/
                           PRE 2521ad05-bdc5-4c3b-9218-a08419179e2c/
                           PRE 27eed8e8-e23a-43f2-b778-5281bf0c28e8/
                           PRE 29ff4075-6b02-4d97-ae53-eb7de452381e/
                           PRE 2a0b1c26-64ef-4410-ae0b-a94b14c89806/
                           PRE 3dac5231-c152-45c5-b1ae-21416d8b31fa/
                           PRE 3ed7cd08-9487-4638-aadd-7ec481bf4dca/
                           PRE 3f2e34a1-c8c9-47a5-b4ab-8c5a80ae2d89/
                           PRE 3f40a128-de0c-4c1d-aeae-77457f4fef07/
                           PRE 424d5f83-6355-458d-a242-b2fde250d021/
                           PRE 42ba1e99-497d-484a-afe8-4fe071a3a9fc/
                           PRE 43692e6c-3e2d-4303-bc6c-b392f8d72483/
                           PRE 439b1bf1-a1a1-4429-b229-5ed3266721e4/
                           PRE 49a4f492-223c-4186-af87-36a8fadc6efc/
                           PRE 4bbb0473-a777-45ff-9129-befff793533b/
                           PRE 4cf0fb6f-e80a-4272-9201-4c2945ea8fa5/
                           PRE 4e9f0e7d-e21b-4c12-8983-a89c2561cc01/
                           PRE 50da822f-f8d0-47f0-9d43-266e21df4f62/
                           PRE 558bee9e-74c3-4d1d-ac8b-613491288b7d/
                           PRE 563b2f1e-9ca2-46c7-8b16-c6c2467c7091/
                           PRE 59321302-fda0-4859-952d-a485e4e09e80/
                           PRE 5c5ed4a7-b3b2-4b28-94a4-7eba76292899/
                           PRE 5dca9144-9850-4e2b-aff9-019901847e22/
                           PRE 614e95b9-0da2-457e-9053-a36cf392d573/
                           PRE 6313d7c4-3b50-47e7-a436-f343125f911c/
                           PRE 698ba47a-690b-4e5e-abbc-5bb94a7192e3/
                           PRE 6d13e62a-7fab-4f8b-ac20-e0cf0cd737c3/
                           PRE 7158a04b-a696-437f-b1e6-1c4d76a05d80/
                           PRE 71aa0dc6-bb0b-487d-abe3-402b3915dbbb/
                           PRE 742420bb-2d85-4d08-b158-d19a30208da3/
                           PRE 7592fa64-cc0a-4e73-919f-05c5250f14cb/
                           PRE 76a374c3-18a6-4fa8-900b-a34620603d72/
                           PRE 779663ff-b7ad-44c2-8b90-67a0b52e12d9/
                           PRE 79885c78-f12e-4ff2-97cc-5088508b0ce6/
                           PRE 7a77acca-ab89-4733-87b3-ddd99957a23a/
                           PRE 7aff2747-d1bb-4f47-9476-3eae1646ba02/
                           PRE 7caf8905-8dc7-4532-a7a5-1529b55aaeeb/
                           PRE 7cf9a885-cf48-4751-90c5-7fbff8b7cff1/
                           PRE 82035bdb-771d-471f-8a3b-e4d9756fde8d/
                           PRE 82f4b57c-0cef-40de-9e52-345582e4b560/
                           PRE 83b322fa-bc71-4610-8ff0-a593e08031dd/
                           PRE 85abcc94-a7db-4529-b0aa-826e3026c8c1/
                           PRE 866015e8-21b2-41b7-a86a-ffcf028b5e3d/
                           PRE 882ef568-7273-4ce3-9845-1fd0b7e01369/
                           PRE 89031384-35f1-427a-b1d1-83edf963a02f/
                           PRE 8a336f9d-0002-440f-b659-d29797c6569d/
                           PRE 8d0d857e-eac9-420f-8534-8f7107135e5c/
                           PRE 911c0243-587a-4398-8f5a-cc81ad2b83a2/
                           PRE 97397e63-c8f4-43ae-997e-22dfbd2fe28c/
                           PRE 9f8ce8c7-761b-4978-9b50-e437e85fa2b6/
                           PRE a3184125-9f01-43c2-a7c4-6f46b40fe31b/
                           PRE a4ae1cc9-1c59-42fb-8fee-873fd76c7c66/
                           PRE a6e39c2a-a74a-480c-a383-96c5abf2e576/
                           PRE a772727e-0e2e-42dd-949f-af181eedb842/
                           PRE ad917583-d303-47d2-8567-dcd5b425cd56/
                           PRE ae5b4e86-6902-4f42-b43e-7caea5930d8a/
                           PRE b263017b-15b3-4278-8731-504aa58b3e07/
                           PRE b487c33d-6e2d-4a0f-9496-3f9db78432a8/
                           PRE b71fabae-0350-4280-b5d9-085e337959e7/
                           PRE be9a1caf-0063-4433-8242-6965feea080e/
                           PRE bf78b406-a9d7-4314-b95c-785503dccd36/
                           PRE c281f2c8-2016-43a2-82e1-f8a3bf56a97a/
                           PRE c8526e90-368c-47e7-872f-61dc94bc44da/
                           PRE c8fa99b7-d0d8-4225-8825-5ef259542665/
                           PRE ce79b74a-caad-451c-9bd3-0fd95a2d4ea8/
                           PRE d38d2655-307b-42be-82d4-1619281e828c/
                           PRE d5353a0f-6553-42fd-9306-5ec8e0c56391/
                           PRE d620cc0a-1161-4d3d-803a-ec3c729801c3/
                           PRE d90cad3e-c4d3-4c24-95e8-d9e676dae2d7/
                           PRE dd7c62fe-cf52-41f8-bb94-b88b48515ffe/
                           PRE e0104de6-0f33-4f54-b823-5d86deb37812/
                           PRE e3766b5d-78b0-4351-b1c3-c194b3a4a72f/
                           PRE e4405c87-5649-4684-9678-b3b9a0e0c49b/
                           PRE ef019283-4126-4173-83cb-de1f70357584/
                           PRE f1e5cdbc-ff97-43ea-8b1a-84828abbd49e/
                           PRE f81d6ef0-260e-44a1-9138-e1ab46e56dde/
                           PRE static/
```

For example : 

```
C:\Users\gguze>aws s3 ls backend-production-librarybucket-1izigk5lryla9/f81d6ef0-260e-44a1-9138-e1ab46e56dde
                           PRE f81d6ef0-260e-44a1-9138-e1ab46e56dde/
```

```
C:\Users\gguze>aws s3 ls backend-production-librarybucket-1izigk5lryla9/f81d6ef0-260e-44a1-9138-e1ab46e56dde/1565682169629_lattice-logo.png
2019-08-13 10:42:51      37641 1565682169629_lattice-logo.png
```


Go to image : https://s3.amazonaws.com/backend-production-librarybucket-1izigk5lryla9/f81d6ef0-260e-44a1-9138-e1ab46e56dde/1565682169629_lattice-logo.png


Best regards, @gkhck_

## Impact

Information disclosure!!

## Attachments
No attachments
