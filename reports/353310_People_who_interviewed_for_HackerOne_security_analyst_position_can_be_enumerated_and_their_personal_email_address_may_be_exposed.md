# People who interviewed for HackerOne security analyst position can be enumerated and their personal email address may be exposed

## Report Details
- **Report ID**: 353310
- **URL**: https://hackerone.com/reports/353310
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-17T05:43:22.396Z
- **Disclosed**: 2018-06-25T21:38:12.769Z

## Reporter
- **Username**: testdefense
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
It's possible to gather basic information on potential employees (at the very least who interviewed) via old sample reports not being removed from the program
**Description:**
This report is meant to provide awareness of potentially private data being accessed by potential candidates.

When given access to the h1triage program as a potential candidate, I found that I was able to view prior candidate's answers to the interview questions/scenarios as well as non-hackerone email addresses.
### Steps To Reproduce potential private email disclosure

1. Sign in as a member of the h1triage team (mock triage interview)
2. Browse to https://hackerone.com/h1triage/groups/25396/members/edit
████

### Steps To Reproduce candidate disclosure

1. Gather all reports submitted to the interview program. For sake of time I have included a curl command to gather this information. The only thing required to duplicate is a valid cookie that has access to the h1triage program

`curl --silent --cookie '<COOKIE>' -H 'Accept: application/json, text/javascript, */*; q=0.01' 'https://hackerone.com/bugs.json?subject=h1triage&report_id=222368&view=all&substates%5B%5D=new&substates%5B%5D=triaged&substates%5B%5D=needs-more-info&substates%5B%5D=resolved&substates%5B%5D=informative&substates%5B%5D=not-applicable&substates%5B%5D=duplicate&substates%5B%5D=spam&reported_to_team=&text_query=&program_states%5B%5D=2&program_states%5B%5D=3&program_states%5B%5D=4&program_states%5B%5D=5&sort_type=latest_activity&sort_direction=descending&limit=1000&page=1' | tr ',' '\n' | grep -E '^\"id' | cut -d ':' -f 2 > ~/Desktop/reports.txt`

This will provide a list of reports that had been created for the interview process (130 in total):

... snippet ...
352430
302753
283278
273850
218861
224701
224703
224705
224737
224738
273847
283279
283285
302752
302751
302743
302756
302750
283280
283291
283284
283283
283282
273848
... snippet ...

2. Use this list to gather all triagers (potential employees). Again, a simple while loop using curl to gather said information.

`while read -r id; do curl --silent --cookie '<COOKIE>' -H 'Accept: application/json, text/javascript, */*; q=0.01' "https://hackerone.com/reports/$id.json" | tr ',' '\n' | grep -Eo 'username.*\"' | cut -d '"' -f 3 >> ~/Desktop/candidates.txt; done < ~/Desktop/reports.txt`

What you'll be left with is a list of all potential candidates in the past year (some are hackerone employees on interview team or the fake reporter):

███████
███
███
██████████
███████
██████████
███
████████
████████
██████████
█████████
██████
██████
██████
████████
█████
███████
██████████
████████
██████
r3naissance
███
█████
████
████████
████

This list can be used to gather information on the candidate (ie, see if they were accepted as a triager) by looking up their profile and identifying if they are a member of the HackerOne team.

3. Another while loop could be used to enumerate which candidates passed the interview process and were accepted as triagers but an exmaple request can be seen below to illustrate the point.
██████████

### Resolution
The wisest choice would be to dispose of candidate information and reports as soon as they are not needed to remove the risk of potential leakage.

## Impact

While the impact is limited to candidates that passed the first round of interviews, it's still plausible that a threat actor may pose as a candidate to gain access to this information and use it to illicit social engineering attacks.

## Attachments
No attachments
