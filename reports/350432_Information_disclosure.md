# Information disclosure

## Report Details
- **Report ID**: 350432
- **URL**: https://hackerone.com/reports/350432
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-11T12:42:47.317Z
- **Disclosed**: 2018-12-27T12:27:16.167Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Chaining few simple informative issues on HackerOne platform and applying new method of timing attack, exploiting interesting feature in HTML5  https://developer.mozilla.org/en-US/docs/Web/API/Resource_Timing_API/Using_the_Resource_Timing_API more precise `Copy with CORS`we can perform low cost, precise and effective CSRF attacks against GrapQL json endpoints (not html, more in the description) on HackerOne platform in order to retrieve valuable information regarding victim (program or researcher).  


**Description:**
Informative issues:
1. report ID on the platform is incremental. => We can measure the number of reports submitted towards platform from one known report ID towards another. Very valuable info for later stages.
2. When user is not logged in and loads some json endpoint that requires user authentication, http 400 code will be returned. That causes attacking `<img>` tag not to be loaded e.g. timing attack to make it impossible => we can remote determine if user is logged in on HackerOne or not. Very valuable info for later stages.
3. Even if this "issue" is solved e.g. api returns http 200, there are always handy http 500 status codes e.g. if we know some endpoint that returns http 500 for request where user need to be logged in, then we have our marker. Try adding `%00` as value in `subject` parameter.
    
New timing attack technique towards JSON endpoints - current connection speed towards not CSRF protected json endpoint

Why only JSON endpoints - HTML tags will add extra noice to the response and will add extra deviation towards final approximation of the final results. JSON holds adds minimum noise in the results.

How timing attack works
On the attacker end - offline
1. Need to have HackerOne profile in order to find vulnerable endpoints
2. Need to find 3 interesting endpoints with the following characteristics:
     2.1 Endpoint that holds valuable data as number of triaged + critical reports where report id nolds XYZTRA numbers ( you can determine time of the report via report id ) (https://hackerone.com/bugs.json?text_query=4&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged)
     2.2 Endpoint that returns minimal response and could be considered equal with empty response (https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged)
     2.3 Endpoint that will hold decent amount of data (~10KB) and that data is not changed very often in order to eliminate/lower server side processing difference from the equation (https://hackerone.com/programs/search.json?query=IBB&sort=published_at%3Adescending&page=1)
3. Minimal 2.2 and targeted 2.1 endpoints need to have same/similar server side complexity ( 2.1 with empty `text_query` is much faster than 2.2. with `text_query = 999999999` )
4. On stable and descent internet connection calculate the following:
    4.1 Average time of loading 2.2 and 2.3
    4.2 AVG_TIME(2.3) - AVG_TIME(2.2) = AVG_TIME_DATA_ONLY(2.3)
    4.3 SPEED_ME (B per ms) = (SIZE(2.3) - SIZE(2.2))/AVG_TIME_DATA_ONLY(2.3) is the speed towards HackerOne infrastructure
    4.4 Monitoring many different responses with the same form as 2.1 we can calculate each json record average size - we can call it ONE_JSON ~ 850B ( this calculation must be based from the response side perspective due the fact it is traveling gzip-ed )
    4.5 Calculate the average time of loading 2.1 AVG_TIME(2.1) and AVG_TIME(2.1) - AVG_TIME(2.2) = AVG_TIME_DATA_ONLY(2.1)
    4.6  SPEED_ME * AVG_TIME_DATA_ONLY(2.1)  = SIZE_DATA_ONLY(2.1) and if you divide with ONE_JSON it will give number of records.

On the attacking web server:
1. Victim need to be measured only towards 2 endpoints:
 1.1 Towards 2.3 endpoint (no need of 2.1, but those bonus info would make calculations more precise)
 1.2 Towards attacking endpoint
2. Results of measurement will be then send towards attacker server for later processing
3. Attack could start after attacker will make sure victim is already logged in on H1.
4. With dumped results we can measure victim speed ( simple proportion in this case or repeating above procedure ) and based on the speed we can derive conclusions regarding endpoint that is under attack.
5. All of this could be performed offline (clean up results even by hand due the fact 25+ requests per endpoint give perfect insight).

### Steps To Reproduce

1. Use scripts from 348168 report in order to harvest the data for calculations
2. Use only 1.php and 3.php to collect victims benchmarks 
3. Proportion between 2.3 average load time ( you - attacker and victim ) will give you insight regarding his speed. Then jump towards calculations above

### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 *

## Impact

Counting number of reports with any property from `search filters` on HackerOne in certain time interval (report id)

## Attachments
No attachments
