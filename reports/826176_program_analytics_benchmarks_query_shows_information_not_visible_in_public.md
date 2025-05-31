# program_analytics_benchmarks query shows information not visible in public

## Report Details
- **Report ID**: 826176
- **URL**: https://hackerone.com/reports/826176
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-22T00:26:00.520Z
- **Disclosed**: 2020-03-27T16:25:42.270Z

## Reporter
- **Username**: 0619
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
`program_analytics_benchmarks` is displaying information i don't see yet in public profile of a program.

**Description:**
I tried querying program_analytics_benchmarks for the program security and ██████ and it showing information i cannot find in public profile especially in ███████ 
### Steps To Reproduce
Please try the graphql for the the program security and ████████
```
{
  program_analytics_benchmarks(teams:"security" select:p50_time_to_bounty, from:response_targets, where:{severity:{is_null:true}},group:week_bounty_awarded_at, 
    start_date:"2019-10-01T00:00:00.000Z",end_date:"2020-10-01T00:00:00.000Z%00")
    {
      id
      x
      y
      
    }
}
```
Please see the attached file for the actual response



### Optional: Supporting Material/References (Screenshots)
███
███
 * 

I saved this graphql query and been trying to run this for a month now and i just noticed now that it's returning some information.

## Impact

Information disclosure

## Attachments
No attachments
