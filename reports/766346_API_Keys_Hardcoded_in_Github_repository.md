# API Keys Hardcoded in Github repository

## Report Details
- **Report ID**: 766346
- **URL**: https://hackerone.com/reports/766346
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-31T07:33:46.350Z
- **Disclosed**: 2020-04-01T13:49:25.364Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** API Keys is hard coded in one of the GitHub repository

**Description:** Key and google-services.json file is publically available in the RocketChat Android repository. 

## Releases Affected:

 * Latest Github Code

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)

**Fabric API Key**
 
  1. Go to this URL https://github.com/RocketChat/Rocket.Chat.Android/blob/638759d7b77375fd681f429d2e2d7ba59e602c45/app/src/main/AndroidManifest.xml
  2. Scroll down to the bottom
  3. You will see fabric APIKey hardcoded there

**google-services.json**

 1. Go to https://github.com/RocketChat/Rocket.Chat.Android/blob/30e95cc97d2fbec6c1d5f6fdad7350fbf60688d5/app/google-services.json
 2. You can see the complete google services config file


## Supporting Material/References:

  * Screenshot in attachment

## Suggested mitigation

  * Keys should not be pushed to the public repository

## Impact

1. Using Fabric key some attacker can mess up the complete analytics of the RocketChat Android App 
2. google-services.json can be used to access google services of RocketChats google account

## Attachments
- Screen_Shot_2019-12-31_at_12.52.17_PM.png
- Screen_Shot_2019-12-31_at_1.01.50_PM.png
