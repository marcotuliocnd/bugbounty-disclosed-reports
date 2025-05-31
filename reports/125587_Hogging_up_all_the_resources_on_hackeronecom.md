# Hogging up all the resources on hackerone.com

## Report Details
- **Report ID**: 125587
- **URL**: https://hackerone.com/reports/125587
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-03-24T01:38:59.232Z
- **Disclosed**: 2019-04-10T07:35:47.784Z

## Reporter
- **Username**: kirils
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
***Please note.*** *I believe that some of the issues described below can also be used on their own and/or combined in other configurations to achieve different results, e.g. "paying" a bounty of zero or team avoiding to resolve and unpleasant issue. I am however describing the (very likely) doomsday scenario.*

The following report IDs were used in testing: 125555, 125556. After you're done with this bug, please remove those. **DO NOT OPEN BEFORE READING THE FULL REPORT**

To reproduce the problem immediately, just skip to **Bug5**.

**Bug1. It is possible to award bounties of size zero.** *(not required for doomsday)*
hackerone has implemented a filter on minimal bounty amount. It is impossible to award negative bounty, zero bounty or "0.00" bounty. This is checked by JavaScript and furthermore on the server side. However, it is possible to award "0.001" bounty, effectively awarding zero amount. This allows a team to risk no money when executing next steps.

**Bug2. POST to `bulk` is susceptible to a replay attack .** *(not required for doomsday)*
This of course only makes the following attack easier, but POST to https://hackerone.com/reports/bulk can be replayed without changing a thing in the request. A dynamic use-once token is strongly advised.

**Bug3. Many `Activities::BountyAwarded` on a bug report hog up server resources because of unoptimized codebase.** 
*Note. Other types of activities may also be affected. This was not further clarified due to severe impact on hackerone infrastructure.*
It was measured that with each new activity added https://hackerone.com/reports/NNNNNN.json became slower and slower.
Please see the following table where cnt is the count of Activities::BountyAwarded in a bug report and spd is the time (in seconds) it took for the json to load.
```
cnt		spd
335		13
380		15
440		19
485		23
555		24
680		26
750		28
```
This already makes the specific bug report quite unusable.

**Bug4. Cloudflare is configured to disconnect the HTTP session if the response takes longer than 30 seconds.** *(not required for doomsday)*
This is generally a good thing, but considering the previous bug this means that at some amount of `Activities::BountyAwarded` we effectively make report inaccessible to anyone. I reached this point in my testing with approx 800 activities per report. Note that I did not try to find the specific limit due to the severe impact of this bug on hackerone infrastructure. Additionally the specific number is probably dependant on the server load anyway.
*Please see the attached screenshot "offline.png".*

Still I am quite sure that a report can only have less than a thousand activities of this type.
After Cloudflare has disconnected a HTTP session, it does not automatically reconnect, so this can be further used to make the user believe that he is logged out. Probably some other nefarious purposes.
*Please see the attached screenshot "logged-out.png", I am infact logged-in at that moment.*

**Bug5. Just 10 parallel requests to the json file is enough to paralyse hackerone.com for everyone.**
```
for((x=0;x<10;x++)); do (curl https://hackerone.com/reports/NNNNNN.json & ); done
```
This was tested on the report ID ending with 6. I ran the attack only twice. Second time to confirm that the unavailability was not a coincidence.
*Please see the attached file "DoS-impact-measurments.txt" for attack impact measurement.*

I am able to effectively permanently take down hackerone.com by sending just **14 thousand requests per day**. You state that you treat confidentiality bugs as "severe". This is an availability (+small part integrity) bug, but the impact is massive. I therefore urge that you consider this bug of the highest severity.


**Attack plan**
1. Get a vulnerability report
2. Fix it, agree on disclosure. It is now publicly available and visible on the front page.
3. Submit a 1000 rewards of 0.001 to the report.
4. Anyone who requests the json file (by opening the report on the front page for example) will get disconnected by Cloudflare.
5. If this is not enough to create a DDoS on the actual infrastructure hidden behind Cloudflare, you can just launch 10 parallel requests to the json file yourself every minute for a simple and elegant DoS.
6. ~~Profit.~~ Watch the world burn.

**Suggested fixes**
Bug1: round the value first, validate against >0 later.
Bug2: apply non-reusable tokens to your POST forms.
Bug3: hell if I know! you're not open source, right? take a look at your damn code. ;)
Bug4: might want to adjust the thresholds or reimplement your client-side (JavaScript) algorithms for detecting if a user is logged in or not.
Bug5: pre-generating actual json files for different audiences would surely reduce the load and eliminate this vector.

## Attachments
- offline.png
- logged-out.png
- DoS-impact-measurments.txt
