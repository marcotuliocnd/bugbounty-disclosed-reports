# HTTP Host injection in redirect_to function

## Report Details
- **Report ID**: 888176
- **URL**: https://hackerone.com/reports/888176
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-06-01T06:20:35.148Z
- **Disclosed**: 2021-06-15T17:44:27.821Z

## Reporter
- **Username**: komang4130
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Hi team,

Here is the sample vulnerable code 
```ruby
class TesttestController < ApplicationController
  def index
    redirect_to  "/demo/?your_reset_token=your_reset_token"
  end
end
```

The ** _compute_redirect_to_location** will take the input **"/demo/?your_reset_token=your_reset_token"** as **options** variables. 
File **File **action_controller\metal\redirecting.rb**** line 63
```ruby
    def redirect_to(options = {}, response_options = {})
      raise ActionControllerError.new("Cannot redirect to nil!") unless options
      raise AbstractController::DoubleRenderError if response_body

      self.status        = _extract_redirect_to_status(options, response_options)
      self.location      = _compute_redirect_to_location(request, options)
      self.response_body = "<html><body>You are being <a href=\"#{ERB::Util.unwrapped_html_escape(response.location)}\">redirected</a>.</body></html>"
    end
```

Then it will check if the **options**, because the input is **String**, so it will be the concatenate of **request.protocol + request.host_with_port + options**
File **action_controller\metal\redirecting.rb** line 96
```ruby
    def _compute_redirect_to_location(request, options) #:nodoc:
      case options
      # The scheme name consist of a letter followed by any combination of
      # letters, digits, and the plus ("+"), period ("."), or hyphen ("-")
      # characters; and is terminated by a colon (":").
      # See https://tools.ietf.org/html/rfc3986#section-3.1
      # The protocol relative scheme starts with a double slash "//".
      when /\A([a-z][a-z\d\-+\.]*:|\/\/).*/i
        options
      when String
        request.protocol + request.host_with_port + options
      when Proc
        _compute_redirect_to_location request, instance_eval(&options)
      else
        url_for(options)
      end.delete("\0\r\n")
    end
    module_function :_compute_redirect_to_location
    public :_compute_redirect_to_location
```

The **request.protocol** will be **http://** or **https://**
The **request.host_with_port**  will call **raw_host_with_port** to check if there is the **X_FORWARD_FOR** else, it will take the input from **HTTP_HOST** then continue the **_compute_redirect_to_location** process.
file **action_dispatch\http\url.rb** line 220
```ruby
      def raw_host_with_port
        if forwarded = x_forwarded_host.presence
          forwarded.split(/,\s?/).last
        else
          get_header("HTTP_HOST") || "#{server_name || server_addr}:#{get_header('SERVER_PORT')}"
        end
      end
```

So at the end, our input will be **request.protocol + request.host_with_port + options** and being set as **Header["location"]** value.

We cant change the HTTP_HOST to something else because the HTTP_HOST must be declare in the the **config.host** and raise 403 Status ( see the **img4.JPG** )


But if we use the IP, we can bypass this and here is the result, which 149.28.128.52 is the attacker IP, and there is no check for IP address but only the hostname.

The **img2.JPG** is the PoC request when use HTTP_HOST.
The **img3.JPG** is the PoC request when use HTTP_X_FORWARD_HOST.

Fix:
There should be a check for IP ADDRESS as well as the HOSTNAME in the enviroment config if user dont specific the host as parameter for **redirect_to** function.

## Impact

Password Reset Poisoning - which user use the HTTP_HOST as the input for the reset token.
Web-cache  - which user use the HTTP_HOST as the input

## Attachments
- img2.JPG
- img3.JPG
- img4.JPG
