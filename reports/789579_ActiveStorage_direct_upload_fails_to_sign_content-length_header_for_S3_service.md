# ActiveStorage direct upload fails to sign content-length header for S3 service

## Report Details
- **Report ID**: 789579
- **URL**: https://hackerone.com/reports/789579
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-05T22:24:41.310Z
- **Disclosed**: 2020-05-18T20:43:36.685Z

## Reporter
- **Username**: travispew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
When a user makes a direct upload using ActiveStorage, the browser makes a request to the DirectUploadsController containing the direct_upload parameters filename, content_type, byte_size, and checksum. These are used to generate a presigned url that is then passed back to the browser, allowing the user to upload directly to S3.

In particular, the byte_size parameter is intended to be encoded in the url for content-length, preventing the user from uploading a file of a different size. Although Rails does not currently provide any built in validations, developers have been encouraged to modify the controller or provide their own controller if they want to create a validation. For example, a developer might decide to prohibit uploads greater than 10MB in size.

in all current version of Rails with ActiveStorage and direct uploads `active_storage/lib/active_storage/service/s3_service.rb`, the code generates the presigned_url as follows:

```ruby
    def url_for_direct_upload(key, expires_in:, content_type:, content_length:, checksum:)
      instrument :url, key: key do |payload|
        generated_url = object_for(key).presigned_url :put, expires_in: expires_in.to_i,
          content_type: content_type, content_length: content_length, content_md5: checksum

        payload[:url] = generated_url

        generated_url
      end
    end
```

However, the aws-sdk-s3 gem *silently blacklists* the "content-length" header:

https://github.com/aws/aws-sdk-ruby/blob/master/gems/aws-sdk-s3/lib/aws-sdk-s3/presigner.rb#L22

This issue is also raised here: https://github.com/aws/aws-sdk-ruby/issues/2098

As a result, the content-length header is never actually part of the presigned url. As a result, a malicious user can select a file of arbitrary size, tell the direct uploads controller that the file is a different size, and then proceed to upload the file, bypassing the intended protection of the signed url.

The solution is to add the whitelist_headers argument:

```ruby
    def url_for_direct_upload(key, expires_in:, content_type:, content_length:, checksum:)
      instrument :url, key: key do |payload|
        generated_url = object_for(key).presigned_url :put, expires_in: expires_in.to_i,
          content_type: content_type, content_length: content_length, content_md5: checksum,
          whitelist_headers: ['content-length']

        payload[:url] = generated_url

        generated_url
      end
    end
```
After this is added, the content-length will be included in the presigned url and the client will be unable to upload a file of arbitrary size.

## Impact

The attacker could upload a file of any size, unless the S3 service is configured separately to prevent this, whereas the developer believes they have protected themselves against this. This could allow an attacker to upload a very large file to S3, incurring additional costs to the website owner or causing other harm.

## Attachments
No attachments
