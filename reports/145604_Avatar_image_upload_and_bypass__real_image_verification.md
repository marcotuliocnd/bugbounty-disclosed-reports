# Avatar image upload and bypass  real image verification 

## Report Details
- **Report ID**: 145604
- **URL**: https://hackerone.com/reports/145604
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-18T01:50:10.608Z
- **Disclosed**: 2017-01-15T22:07:23.197Z

## Reporter
- **Username**: dremos
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi

We can bypass Avatar Upload image verification and extension  uploading a php file or any other extension binding a valide  jpeg image  , there is no risk for the moment because the avatar is renamed to avatar_upload on the remote server , but it ll be nice to secure this part of code .

Example  
---------------
here is the same file with two different extension : 

http://91.121.108.101/image1.jpg
http://91.121.108.101/image1.php      <== execute php code inside the image 

1) download image1.jpg

2) as you can see  if you open the file image1.jpg  file on notepad it hide php code ( phpinfo(); function in this case .

3) rename image1.jpg to image1.php  , and try to upload it on the avatar upload form , it pass the verification  .

This verification is not enought in this  file :  /core/controller/avatarcontroller.php  


	if ($image->valid()) {
				$mimeType = $image->mimeType();
				if ($mimeType !== 'image/jpeg' && $mimeType !== 'image/png') {
					return new DataResponse(
						['data' => ['message' => $this->l->t('Unknown filetype')]],
						Http::STATUS_OK,
						$headers
					);
				}




## Attachments
No attachments
