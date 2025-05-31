# [dubsmash] Long String in 'shoutout' Parameter Leading Internal server Error on Popular hastags , Community and User Profile

## Report Details
- **Report ID**: 1237428
- **URL**: https://hackerone.com/reports/1237428
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-18T05:37:20.276Z
- **Disclosed**: 2021-12-13T22:48:03.944Z

## Reporter
- **Username**: sandeep_rj49
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
If the user input a long string in the 'shoutout' parameter of the 'CreateVideo' API then all the APIs where this video is supposed to appear (eg: hashtag API, community API, and user profile API) will throw 'internal server error' in the response. This will cause a denial of service attack for the hashtag API (if hashtags are used in the video), community API (if the video is uploaded in the community), and user profile API.

So, if the attacker uses all trending hashtags in the video then all other videos from the trending hashtags will disappear and API will respond with 200 OK HTTP status code but 'INTERNAL_SERVER_ERROR' in the response body. The hashtag activity tab will not display any other videos.

## Steps To Reproduce:
1. Open dubsmash ios app. 
2. Record any video. 
3. Use any hashtag in the description (use trending hashtags to cause a denial of service on the trending hashtags).
4. Click on the post button and intercept the vulnerable request in the burp suite.
5. Input any long string in the 'shoutout' parameter value. Example- 74692d5f38a34cb4b355cef784fe46aa
6. Forward the request to the server and turn off the intercept.
7. On the screen, if it is showing video not uploaded then click. on upload again. 
8. Wait for few minutes to reflect the video in the hashtag. 
9. Search for the used hashtag. 
10. You'll see your video thumbnail is appearing for the searched hashtag. But when you open a hashtag for accessing all the videos, it is not reflecting any API. 
11. Capture the TagUGC API, it will reflect "INTERNAL SERVER ERROR" in the response. 


## AFFECTED API:
hashtag API:
```
POST /graphql?build_number=52430&platform=ios HTTP/2
Host: gateway-production.dubsmash.com
Content-Type: application/json
X-Device-Country: IN
Accept: application/json
Authorization: Bearer xxxxxx
X-Dubsmash-Device-Id: 8F15E960-B1C5-4C30-A100-CA0527827502
X-Accept-Content-Language: en_IN
Accept-Language: en-IN;q=1.0, hi-IN;q=0.9
Accept-Encoding: gzip, deflate
If-None-Match: W/"697-EM383iY/+yqkrvx/lSeRoGMBjWM"
X-Device-Language: en
X-Build-Number: 52430
X-Device-Timezone: 19800
X-App-Version: 6.3.0
X-Remote-Config-Values: []
User-Agent: Dopesmash/6.3.0 (com.mobilemotion.dubsmash; build:52430; iOS 14.0.1) Alamofire/5.4.1
Content-Length: 4737
Connection: close

{"query":"query TagUGC($name: String!, $page: String, $ranking: ContentRankingMethod) {\n  tag(name: $name) {\n    __typename\n    num_objects\n    objects(object_type: VIDEO, page_size: 9, offset: $page, ranking: $ranking) {\n      __typename\n      results {\n        __typename\n        ... on Video {\n          ...VideoFragment\n        }\n      }\n      next\n    }\n  }\n}\nfragment VideoFragment on Video {\n  __typename\n  uuid\n  created_at\n  creator {\n    __typename\n    ...PublicUserFragment\n  }\n  video_type\n  item_type\n  video_data {\n    __typename\n    mobile {\n      __typename\n      video\n      thumbnail\n    }\n    animated_thumbnail {\n      __typename\n      video\n      thumbnail\n    }\n  }\n  updated_at\n  status\n  liked\n  caption: title\n  original_sound: sound {\n    __typename\n    ...SoundFragment\n  }\n  num_views\n  num_likes\n  num_comments\n  comments_allowed\n  share_link\n  width\n  height\n  duet_allowed\n  privacy_level\n  is_featured\n  is_live\n  community {\n    __typename\n    ...CommunityFragment\n  }\n  duet_with {\n    __typename\n    uuid\n    title\n    creator {\n      __typename\n      uuid\n      username\n    }\n  }\n  top_comments {\n    __typename\n    ...BasicCommentFragment\n  }\n  prompt {\n    __typename\n    ...PromptFragment\n  }\n  poll {\n    __typename\n    ...PollFragment\n  }\n  mentions {\n    __typename\n    ...MentionFragment\n  }\n  shoutout {\n    __typename\n    ...BasicShoutoutFragment\n  }\n}\nfragment PublicUserFragment on User {\n  __typename\n  username\n  uuid\n  display_name\n  blocked\n  followed\n  num_public_post_plays\n  followsCount: num_follows\n  followingsCount: num_followings\n  share_link\n  date_joined\n  has_invite_badge\n  badges\n  profile_picture\n  allow_video_download\n  bio\n  ... on User {\n    gifts_offered: products_offered(product_type: GIFT) {\n      __typename\n      results {\n        __typename\n        product {\n          __typename\n          uuid\n        }\n      }\n    }\n    shoutouts_offered: products_offered(product_type: SHOUTOUT) {\n      __typename\n      results {\n        __typename\n        product {\n          __typename\n          uuid\n        }\n      }\n    }\n  }\n}\nfragment SoundFragment on Sound {\n  __typename\n  uuid\n  created_at\n  sound\n  name\n  waveform_raw_data\n  liked\n  soundStatus: status\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n  share_link\n  num_likes\n  num_videos\n}\nfragment ContentCreatorFragment on User {\n  __typename\n  username\n  uuid\n  date_joined\n  followed\n  has_invite_badge\n  badges\n  profile_picture\n}\nfragment CommunityFragment on Community {\n  __typename\n  uuid\n  created_at\n  updated_at\n  name\n  description\n  member_count\n  online_members\n  post_count\n  is_subscribed\n  icon\n  banner_image\n}\nfragment BasicCommentFragment on Comment {\n  __typename\n  uuid\n  text\n  likesCount: num_likes\n  created_at\n  liked\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n}\nfragment PromptFragment on Prompt {\n  __typename\n  uuid\n  created_at\n  name\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n  liked\n}\nfragment PollFragment on Poll {\n  __typename\n  uuid\n  title\n  num_total_votes\n  choices {\n    __typename\n    ...PollChoiceFragment\n  }\n  positioning {\n    __typename\n    ...StickerPositioningFragment\n  }\n  voted_for {\n    __typename\n    ...PollChoiceFragment\n  }\n}\nfragment PollChoiceFragment on PollChoice {\n  __typename\n  uuid\n  name\n  num_votes\n  index\n}\nfragment StickerPositioningFragment on StickerPositioning {\n  __typename\n  x\n  y\n  width\n  height\n  rotation\n}\nfragment MentionFragment on Mention {\n  __typename\n  object {\n    __typename\n    ... on User {\n      ...PublicUserFragment\n    }\n    ... on Tag {\n      ...TagFragment\n    }\n  }\n  content_type\n  positioning {\n    __typename\n    ...StickerPositioningFragment\n  }\n  interval {\n    __typename\n    start_time\n    end_time\n  }\n}\nfragment TagFragment on Tag {\n  __typename\n  uuid\n  name\n  num_objects\n  num_plays\n  subscribed\n  top_videos {\n    __typename\n    ...TopVideoFragment\n  }\n}\nfragment TopVideoFragment on Video {\n  __typename\n  uuid\n  video_data {\n    __typename\n    mobile {\n      __typename\n      thumbnail\n    }\n  }\n  creator {\n    __typename\n    uuid\n    username\n  }\n}\nfragment BasicShoutoutFragment on Shoutout {\n  __typename\n  uuid\n  created_at\n  updated_at\n  requestor {\n    __typename\n    ...PublicUserFragment\n  }\n  status\n  creator {\n    __typename\n    ...PublicUserFragment\n  }\n}","variables":{"page":null,"ranking":"POPULARITY_HASHTAGS","name":"hexagonalprism"}}
```

User profile API:
```
POST /graphql?build_number=52430&platform=ios HTTP/2
Host: gateway-production.dubsmash.com
Content-Type: application/json
X-Device-Country: IN
Accept: application/json
Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoxLjYyMzk1NDg2NGUrMDksImV4cCI6MTYyNDA0MTI2NCwiaGFzX3B1YmxpY19wcm9maWxlIjp0cnVlLCJwZXJtaXNzaW9uX2dyb3VwcyI6W10sInJlcXVlc3RfaWQiOiJkYjNhNWIxZi01ZWNlLTQ5YTctYWQwOS1kYjEyYmZlMTQ5ODUiLCJ1c2VybmFtZSI6IjMwNTIzZmEwYzE3MzQ3MDNiNzM4N2E1NjliZTA2MmNkIn0.aWVynW42kALTw18Z6IAfVuUFJmUS7lGW_1F7I2SjJUXsrH2HHsnw3R-gKSiTnW-U5kc11BZnGO3nqoAZwtqPJA
X-Dubsmash-Device-Id: 8F15E960-B1C5-4C30-A100-CA0527827502
X-Accept-Content-Language: en_IN
Accept-Language: en-IN;q=1.0, hi-IN;q=0.9
Accept-Encoding: gzip, deflate
If-None-Match: W/"52-sxSZbTm01+no7htgkLGYqCFOwFk"
X-Device-Language: en
X-Build-Number: 52430
X-Device-Timezone: 19800
X-App-Version: 6.3.0
X-Remote-Config-Values: []
User-Agent: Dopesmash/6.3.0 (com.mobilemotion.dubsmash; build:52430; iOS 14.0.1) Alamofire/5.4.1
Content-Length: 4707
Connection: close

{"variables":{"next":null,"username":"test123458","itemType":"POST","pageSize":9},"query":"query UserUGC($username: String!, $itemType: VideoItemType!, $next: String, $pageSize: Int!) {\n  user(username: $username) {\n    __typename\n    videos(next: $next, page_size: $pageSize, item_type: $itemType) {\n      __typename\n      results {\n        __typename\n        ...VideoFragment\n      }\n      next: next_page\n    }\n  }\n}\nfragment VideoFragment on Video {\n  __typename\n  uuid\n  created_at\n  creator {\n    __typename\n    ...PublicUserFragment\n  }\n  video_type\n  item_type\n  video_data {\n    __typename\n    mobile {\n      __typename\n      video\n      thumbnail\n    }\n    animated_thumbnail {\n      __typename\n      video\n      thumbnail\n    }\n  }\n  updated_at\n  status\n  liked\n  caption: title\n  original_sound: sound {\n    __typename\n    ...SoundFragment\n  }\n  num_views\n  num_likes\n  num_comments\n  comments_allowed\n  share_link\n  width\n  height\n  duet_allowed\n  privacy_level\n  is_featured\n  is_live\n  community {\n    __typename\n    ...CommunityFragment\n  }\n  duet_with {\n    __typename\n    uuid\n    title\n    creator {\n      __typename\n      uuid\n      username\n    }\n  }\n  top_comments {\n    __typename\n    ...BasicCommentFragment\n  }\n  prompt {\n    __typename\n    ...PromptFragment\n  }\n  poll {\n    __typename\n    ...PollFragment\n  }\n  mentions {\n    __typename\n    ...MentionFragment\n  }\n  shoutout {\n    __typename\n    ...BasicShoutoutFragment\n  }\n}\nfragment PublicUserFragment on User {\n  __typename\n  username\n  uuid\n  display_name\n  blocked\n  followed\n  num_public_post_plays\n  followsCount: num_follows\n  followingsCount: num_followings\n  share_link\n  date_joined\n  has_invite_badge\n  badges\n  profile_picture\n  allow_video_download\n  bio\n  ... on User {\n    gifts_offered: products_offered(product_type: GIFT) {\n      __typename\n      results {\n        __typename\n        product {\n          __typename\n          uuid\n        }\n      }\n    }\n    shoutouts_offered: products_offered(product_type: SHOUTOUT) {\n      __typename\n      results {\n        __typename\n        product {\n          __typename\n          uuid\n        }\n      }\n    }\n  }\n}\nfragment SoundFragment on Sound {\n  __typename\n  uuid\n  created_at\n  sound\n  name\n  waveform_raw_data\n  liked\n  soundStatus: status\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n  share_link\n  num_likes\n  num_videos\n}\nfragment ContentCreatorFragment on User {\n  __typename\n  username\n  uuid\n  date_joined\n  followed\n  has_invite_badge\n  badges\n  profile_picture\n}\nfragment CommunityFragment on Community {\n  __typename\n  uuid\n  created_at\n  updated_at\n  name\n  description\n  member_count\n  online_members\n  post_count\n  is_subscribed\n  icon\n  banner_image\n}\nfragment BasicCommentFragment on Comment {\n  __typename\n  uuid\n  text\n  likesCount: num_likes\n  created_at\n  liked\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n}\nfragment PromptFragment on Prompt {\n  __typename\n  uuid\n  created_at\n  name\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n  liked\n}\nfragment PollFragment on Poll {\n  __typename\n  uuid\n  title\n  num_total_votes\n  choices {\n    __typename\n    ...PollChoiceFragment\n  }\n  positioning {\n    __typename\n    ...StickerPositioningFragment\n  }\n  voted_for {\n    __typename\n    ...PollChoiceFragment\n  }\n}\nfragment PollChoiceFragment on PollChoice {\n  __typename\n  uuid\n  name\n  num_votes\n  index\n}\nfragment StickerPositioningFragment on StickerPositioning {\n  __typename\n  x\n  y\n  width\n  height\n  rotation\n}\nfragment MentionFragment on Mention {\n  __typename\n  object {\n    __typename\n    ... on User {\n      ...PublicUserFragment\n    }\n    ... on Tag {\n      ...TagFragment\n    }\n  }\n  content_type\n  positioning {\n    __typename\n    ...StickerPositioningFragment\n  }\n  interval {\n    __typename\n    start_time\n    end_time\n  }\n}\nfragment TagFragment on Tag {\n  __typename\n  uuid\n  name\n  num_objects\n  num_plays\n  subscribed\n  top_videos {\n    __typename\n    ...TopVideoFragment\n  }\n}\nfragment TopVideoFragment on Video {\n  __typename\n  uuid\n  video_data {\n    __typename\n    mobile {\n      __typename\n      thumbnail\n    }\n  }\n  creator {\n    __typename\n    uuid\n    username\n  }\n}\nfragment BasicShoutoutFragment on Shoutout {\n  __typename\n  uuid\n  created_at\n  updated_at\n  requestor {\n    __typename\n    ...PublicUserFragment\n  }\n  status\n  creator {\n    __typename\n    ...PublicUserFragment\n  }\n}"}
```

Community API:
```
POST /graphql?build_number=52430&platform=ios HTTP/2
Host: gateway-production.dubsmash.com
Content-Type: application/json
X-Device-Country: IN
Accept: application/json
Authorization: Bearer xxxxxxx
X-Dubsmash-Device-Id: 8F15E960-B1C5-4C30-A100-CA0527827502
X-Accept-Content-Language: en_IN
Accept-Language: en-IN;q=1.0, hi-IN;q=0.9
Accept-Encoding: gzip, deflate
If-None-Match: W/"1c03-0+FK7TwWGvh/rKyVJ5n+lHkl05o"
X-Device-Language: en
X-Build-Number: 52430
X-Device-Timezone: 19800
X-App-Version: 6.3.0
X-Remote-Config-Values: []
User-Agent: Dopesmash/6.3.0 (com.mobilemotion.dubsmash; build:52430; iOS 14.0.1) Alamofire/5.4.1
Content-Length: 4682
Connection: close

{"variables":{"uuid":"db89458d693b49fdbdced90f3b5e2f90","next":null},"query":"query CommunityPosts($uuid: String!, $next: String) {\n  community(uuid: $uuid) {\n    __typename\n    ... on Community {\n      posts(next: $next) {\n        __typename\n        next\n        results {\n          __typename\n          ... on Video {\n            ...VideoFragment\n          }\n        }\n      }\n    }\n  }\n}\nfragment VideoFragment on Video {\n  __typename\n  uuid\n  created_at\n  creator {\n    __typename\n    ...PublicUserFragment\n  }\n  video_type\n  item_type\n  video_data {\n    __typename\n    mobile {\n      __typename\n      video\n      thumbnail\n    }\n    animated_thumbnail {\n      __typename\n      video\n      thumbnail\n    }\n  }\n  updated_at\n  status\n  liked\n  caption: title\n  original_sound: sound {\n    __typename\n    ...SoundFragment\n  }\n  num_views\n  num_likes\n  num_comments\n  comments_allowed\n  share_link\n  width\n  height\n  duet_allowed\n  privacy_level\n  is_featured\n  is_live\n  community {\n    __typename\n    ...CommunityFragment\n  }\n  duet_with {\n    __typename\n    uuid\n    title\n    creator {\n      __typename\n      uuid\n      username\n    }\n  }\n  top_comments {\n    __typename\n    ...BasicCommentFragment\n  }\n  prompt {\n    __typename\n    ...PromptFragment\n  }\n  poll {\n    __typename\n    ...PollFragment\n  }\n  mentions {\n    __typename\n    ...MentionFragment\n  }\n  shoutout {\n    __typename\n    ...BasicShoutoutFragment\n  }\n}\nfragment PublicUserFragment on User {\n  __typename\n  username\n  uuid\n  display_name\n  blocked\n  followed\n  num_public_post_plays\n  followsCount: num_follows\n  followingsCount: num_followings\n  share_link\n  date_joined\n  has_invite_badge\n  badges\n  profile_picture\n  allow_video_download\n  bio\n  ... on User {\n    gifts_offered: products_offered(product_type: GIFT) {\n      __typename\n      results {\n        __typename\n        product {\n          __typename\n          uuid\n        }\n      }\n    }\n    shoutouts_offered: products_offered(product_type: SHOUTOUT) {\n      __typename\n      results {\n        __typename\n        product {\n          __typename\n          uuid\n        }\n      }\n    }\n  }\n}\nfragment SoundFragment on Sound {\n  __typename\n  uuid\n  created_at\n  sound\n  name\n  waveform_raw_data\n  liked\n  soundStatus: status\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n  share_link\n  num_likes\n  num_videos\n}\nfragment ContentCreatorFragment on User {\n  __typename\n  username\n  uuid\n  date_joined\n  followed\n  has_invite_badge\n  badges\n  profile_picture\n}\nfragment CommunityFragment on Community {\n  __typename\n  uuid\n  created_at\n  updated_at\n  name\n  description\n  member_count\n  online_members\n  post_count\n  is_subscribed\n  icon\n  banner_image\n}\nfragment BasicCommentFragment on Comment {\n  __typename\n  uuid\n  text\n  likesCount: num_likes\n  created_at\n  liked\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n}\nfragment PromptFragment on Prompt {\n  __typename\n  uuid\n  created_at\n  name\n  creator {\n    __typename\n    ...ContentCreatorFragment\n  }\n  liked\n}\nfragment PollFragment on Poll {\n  __typename\n  uuid\n  title\n  num_total_votes\n  choices {\n    __typename\n    ...PollChoiceFragment\n  }\n  positioning {\n    __typename\n    ...StickerPositioningFragment\n  }\n  voted_for {\n    __typename\n    ...PollChoiceFragment\n  }\n}\nfragment PollChoiceFragment on PollChoice {\n  __typename\n  uuid\n  name\n  num_votes\n  index\n}\nfragment StickerPositioningFragment on StickerPositioning {\n  __typename\n  x\n  y\n  width\n  height\n  rotation\n}\nfragment MentionFragment on Mention {\n  __typename\n  object {\n    __typename\n    ... on User {\n      ...PublicUserFragment\n    }\n    ... on Tag {\n      ...TagFragment\n    }\n  }\n  content_type\n  positioning {\n    __typename\n    ...StickerPositioningFragment\n  }\n  interval {\n    __typename\n    start_time\n    end_time\n  }\n}\nfragment TagFragment on Tag {\n  __typename\n  uuid\n  name\n  num_objects\n  num_plays\n  subscribed\n  top_videos {\n    __typename\n    ...TopVideoFragment\n  }\n}\nfragment TopVideoFragment on Video {\n  __typename\n  uuid\n  video_data {\n    __typename\n    mobile {\n      __typename\n      thumbnail\n    }\n  }\n  creator {\n    __typename\n    uuid\n    username\n  }\n}\nfragment BasicShoutoutFragment on Shoutout {\n  __typename\n  uuid\n  created_at\n  updated_at\n  requestor {\n    __typename\n    ...PublicUserFragment\n  }\n  status\n  creator {\n    __typename\n    ...PublicUserFragment\n  }\n}"}
```

Exploit:
1. Serach for the #hexagonalprism in the hashtag search option. 
2. You'll observe 3/4 video's thumbnails in the hashtag search.
3. Click on the hashtag to view all videos, the hashtag API will throw "Internal Server Error" and will not display any video.

## Impact

The impact of this vulnerability is severe if the attackers use all trending hashtags in the description and upload the video then the other users will not be able to load the trending hashtags and view the videos. 

Also, if the video is uploaded in the community then all other videos will not appear in that particular community tab as the community API stops responding properly.

## Attachments
- Screenshot_2021-06-18_at_11.06.57_AM.png
