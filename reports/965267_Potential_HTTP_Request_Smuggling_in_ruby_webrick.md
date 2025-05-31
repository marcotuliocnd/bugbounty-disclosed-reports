# Potential HTTP Request Smuggling in ruby webrick

## Report Details
- **Report ID**: 965267
- **URL**: https://hackerone.com/reports/965267
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-23T13:25:24.087Z
- **Disclosed**: 2020-10-29T07:08:50.517Z

## Reporter
- **Username**: piao
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
function read_body in file /lib/webrick/httprequest.rb use  expression ```/chunked/io``` to decide ```transfer-encoding``` whether or not.
that is not rigorous. When using webrick as a http server, a attacker may use  a ```Transfer-Encoding: AAAchunkedBBB``` header to fake a legal header. than can make a HTTP Request Smuggling attack.
```
def read_body(socket, block)
      return unless socket
      if tc = self['transfer-encoding']
        case tc
        when /chunked/io then read_chunked(socket, block)
        else raise HTTPStatus::NotImplemented, "Transfer-Encoding: #{tc}."
        end
      elsif self['content-length'] || @remaining_size
        @remaining_size ||= self['content-length'].to_i
        while @remaining_size > 0
          sz = [@buffer_size, @remaining_size].min
          break unless buf = read_data(socket, sz)
          @remaining_size -= buf.bytesize
          block.call(buf)
        end
        if @remaining_size > 0 && @socket.eof?
          raise HTTPStatus::BadRequest, "invalid body size."
        end
      elsif BODY_CONTAINABLE_METHODS.member?(@request_method)
        raise HTTPStatus::LengthRequired
      end
      return @body
    end
```

## Impact

It is possible to smuggle the request and disrupt the user experience.

## Attachments
No attachments
