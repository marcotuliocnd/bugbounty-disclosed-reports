# Every user can delete public deploy keys

## Report Details
- **Report ID**: 195088
- **URL**: https://hackerone.com/reports/195088
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-01T18:10:30.371Z
- **Disclosed**: 2017-01-23T23:09:52.996Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability details
A GitLab instance can have public deploy keys that project admins can use for their project. An attacker can delete these public keys used by other users to deploy code.

# Impact
Deleting these shared deploy keys may stop users to deploy their code.

# Proof of concept
Make sure the GitLab instance has a public deploy key. Lets assume it has ID 1. Now sign in as a normal user and follow the steps below.

1. Create a new project called `test`
2. Go to http://gitlab-instance/user/test/deploy_keys
3. Go to the `Public deploy keys available to any project` section and click the `Enable` button for the public deploy key
4. Create an access token for the API for your own account
5. Request `/api/v3/projects`, get the ID number for the project `test`
6. Request `/api/v3/projects/:project_id/deploy_keys`, you'll see the public deploy key
7. Send a `DELETE` request to `/api/v3/projects/:project_id/deploy_keys/:id - this will delete the public (shared) deploy key, not the relationship between the project and the key. Below is a copy of the request and response.

**Request**
```
curl -X DELETE -H "Private-Token: AAAA" http://gitlab-instance/api/v3/projects/1/deploy_keys/1
```


**Response**
```
{"id":1,"user_id":null,"created_at":"<removed>","updated_at":"<removed>","key":"<key>","title":"<title>","fingerprint":"72:bb:e9:cc:04:dc:64:b9:a3:e7:c2:26:8f:f2:ed:df","public":true}
```

The root cause of this problem lies in the following lines of code:

**lib/api/deploy_keys.rb**
```ruby
delete ":id/#{path}/:key_id" do
  key = user_project.deploy_keys.find(params[:key_id])
  key.destroy
end
```

The `destroy` method will be called on the shared deploy key instead of on the relationship.

# Remediation advice
Instead of removing the entire object, remove the relationship instead when it's a public deploy key.

## Attachments
No attachments
