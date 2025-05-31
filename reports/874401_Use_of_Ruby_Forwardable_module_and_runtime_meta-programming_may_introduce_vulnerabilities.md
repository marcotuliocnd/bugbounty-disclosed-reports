# Use of Ruby Forwardable module and runtime meta-programming may introduce vulnerabilities

## Report Details
- **Report ID**: 874401
- **URL**: https://hackerone.com/reports/874401
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-14T18:46:29.801Z
- **Disclosed**: 2021-11-15T16:24:12.617Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
I was digging through the `gitlab-foss`  repository and noticed an interested pattern that seems to be adopted in a few places: the use of `Forwardable` with meta-programming over delegators, explicit `attr_reader` methods or `method_missing`. Heads up: the arbitrary file read vulnerability I demonstrate in this report isn't currently exploitable. I was somewhat hesitant to submit this, but I think it'd be a good refactor nonetheless. Before diving into the vulnerability, I'd like to start by describing Ruby's `Forwardable` module behavior in combination with `def_delegators`.

Before Ruby 2.5.1, delegators could be implemented using the `delegate` or `method_missing` methods. It would look something like this:

```ruby
class HelloWorld
  def initialize(attributes)
    @options = OpenStruct.new(attributes)
  end

  def say_it
    "Hello world"
  end

  def method_missing(method, *args)
    @options.send(method, *args)
  end
end
```

When a method would be called on a `HelloWorld` instance that wouldn't exist, it would pass it along to the `@options` instance variable.

```ruby
HelloWorld.new({}).say_it
# => "Hello world"

HelloWorld.new(hello: "world").hello
# => "world"

HelloWorld.new(say_it: "Not hello world").say_it
# => "Hello world"
```

Because the `say_it` method is already defined on the class, its behavior won't be overridden when passing `say_it` to the initializer.

This class can be refactored to use the `Forwardable` method and `def_delegators`:

```ruby
class HelloWorld
  extend Forwardable

  def initialize(attributes)
    @options = OpenStruct.new(attributes)

    self.class.instance_eval do
      def_delegators :@options, *attributes.keys
    end
  end

  def say_it
    "Hello world"
  end
end
```

At first glance, this seems like it has the same behavior as the first code example; but there's one crucial difference: **because the delegators are meta-programmed after the class was loaded, it can overwrite existing methods**:

```ruby
HelloWorld.new({}).say_it
# => "Hello world"

HelloWorld.new(hello: "world").hello
# => "world"

HelloWorld.new(say_it: "Not hello world").say_it
# => "Not hello world"
#        ^------------------ The method is overwritten
```

As can be seen in the above example, the `say_it` method is overwritten when passing it to the initializer.

Going back to GitLab's main Ruby repository, there are a number of places where the `Forwardable` module is used. One place in particular stands out: `Gitlab::ImportExport::AfterExportStrategies::BaseAfterExportStrategy`. This class is a base class used for:

* `Gitlab::ImportExport::AfterExportStrategies::MoveFileStrategy`
* `Gitlab::ImportExport::AfterExportStrategies::DownloadNotificationStrategy`
* `Gitlab::ImportExport::AfterExportStrategies::WebUploadStrategy`

```ruby
# frozen_string_literal: true

module Gitlab
  module ImportExport
    module AfterExportStrategies
      class BaseAfterExportStrategy
        extend Gitlab::ImportExport::CommandLineUtil
        include ActiveModel::Validations
        extend Forwardable

        # ...

        def initialize(attributes = {})
          @options = OpenStruct.new(attributes)

          self.class.instance_eval do
            def_delegators :@options, *attributes.keys
          end
        end

        # ...

        def archive_path
          project.import_export_shared.archive_path
        end

        # ...
      end
    end
  end
end
```

The `MoveFileStrategy` and `WebUploadStrategy` classes overwrite the initializer method or declare its arguments, so these don't meta-program the arguments on the class or limit what can be delegated. My worry, and the potential security vulnerabilities, is that if a new strategy would be declared that inherits from the `BaseAfterExportStrategy` without overwriting the initializer, it may give attackers the ability to change the behavior of existing methods.

As an example, let's say the `DownloadNotificationStrategy` class would be initialized with a user-inputted hash: if the user would specify the `archive_path` argument, it could overwrite the method and point it to a different archive on the local system. Same for the `WebUploadStrategy`: if the `initialize` method would be removed today, specs would still pass, but suddenly a security vulnerability would be present if the user could give it arbitrary arguments (same thing, overwrite the `archive_path`).

I know that this isn't the security vulnerabilities you typically receive from me, but after reading the code, I felt it was the right thing to do to warn you about the potential security vulnerabilities that could be introduced in the future.

This is based on the `master` branch as of May 13, 2020.

# Recommendation
Given that there are only three classes inheriting from the base class, I'd rewrite the code like this to avoid trouble in the future (untested). Direct download: F828467.

```diff
diff --git a/lib/gitlab/import_export/after_export_strategies/base_after_export_strategy.rb b/lib/gitlab/import_export/after_export_strategies/base_after_export_strategy.rb
index b30258123d4..b52073978ee 100644
--- a/lib/gitlab/import_export/after_export_strategies/base_after_export_strategy.rb
+++ b/lib/gitlab/import_export/after_export_strategies/base_after_export_strategy.rb
@@ -6,7 +6,6 @@ module Gitlab
       class BaseAfterExportStrategy
         extend Gitlab::ImportExport::CommandLineUtil
         include ActiveModel::Validations
-        extend Forwardable
 
         StrategyError = Class.new(StandardError)
 
@@ -16,14 +15,6 @@ module Gitlab
 
         public
 
-        def initialize(attributes = {})
-          @options = OpenStruct.new(attributes)
-
-          self.class.instance_eval do
-            def_delegators :@options, *attributes.keys
-          end
-        end
-
         def execute(current_user, project)
           @project = project
 
@@ -67,10 +58,6 @@ module Gitlab
           project.import_export_shared.lock_files_path
         end
 
-        def archive_path
-          project.import_export_shared.archive_path
-        end
-
         def locks_present?
           project.import_export_shared.locks_present?
         end
diff --git a/lib/gitlab/import_export/after_export_strategies/download_notification_strategy.rb b/lib/gitlab/import_export/after_export_strategies/download_notification_strategy.rb
index 39a6090ad87..da0a593691c 100644
--- a/lib/gitlab/import_export/after_export_strategies/download_notification_strategy.rb
+++ b/lib/gitlab/import_export/after_export_strategies/download_notification_strategy.rb
@@ -10,6 +10,10 @@ module Gitlab
           false
         end
 
+        def archive_path
+          project.import_export_shared.archive_path
+        end
+
         private
 
         def strategy_execute
diff --git a/lib/gitlab/import_export/after_export_strategies/move_file_strategy.rb b/lib/gitlab/import_export/after_export_strategies/move_file_strategy.rb
index 2e3136936f8..8a58f0911e3 100644
--- a/lib/gitlab/import_export/after_export_strategies/move_file_strategy.rb
+++ b/lib/gitlab/import_export/after_export_strategies/move_file_strategy.rb
@@ -4,6 +4,8 @@ module Gitlab
   module ImportExport
     module AfterExportStrategies
       class MoveFileStrategy < BaseAfterExportStrategy
+        attr_reader :archive_path
+
         def initialize(archive_path:)
           @archive_path = archive_path
         end
diff --git a/lib/gitlab/import_export/after_export_strategies/web_upload_strategy.rb b/lib/gitlab/import_export/after_export_strategies/web_upload_strategy.rb
index e2dba831661..80b12a76d26 100644
--- a/lib/gitlab/import_export/after_export_strategies/web_upload_strategy.rb
+++ b/lib/gitlab/import_export/after_export_strategies/web_upload_strategy.rb
@@ -16,8 +16,11 @@ module Gitlab
           end
         end
 
+        attr_reader :url, :http_method
+
         def initialize(url:, http_method: PUT_METHOD)
-          super
+          @url = url
+          @http_method = http_method
         end
 
         protected
@@ -32,6 +35,10 @@ module Gitlab
           end
         end
 
+        def archive_path
+          project.import_export_shared.archive_path
+        end
+
         private
 
         def send_file
```

## Impact

Allowing an attacker to pass a hash to the initializer of a class inheriting from `BaseAfterExportStrategy` may lead to arbitrary file read, or potentially even to remote code execution.

## Attachments
- patch.diff
