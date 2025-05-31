# SafeParamsHelper::safe_params is not so safe

## Report Details
- **Report ID**: 946728
- **URL**: https://hackerone.com/reports/946728
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-29T13:31:45.285Z
- **Disclosed**: 2020-11-02T21:19:01.556Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

GitLab uses [SafeParamsHelper](https://gitlab.com/gitlab-org/gitlab/-/blob/682a3c0134f2cfec9e5743aa97fbaf2a7d89e65f/app/helpers/safe_params_helper.rb#L8) to filter out some keys before passing them to `url_for`: 

```ruby
  def safe_params
    if params.respond_to?(:permit!)
      params.except(:host, :port, :protocol).permit!
    else
      params
    end
  end
```

The issue is that there are a [lot more dangerous keys](https://github.com/rails/rails/blob/12f3f11f61eccc5d9423b288a08cb1fc7e60999b/actionpack/lib/action_dispatch/routing/route_set.rb#L781):

```ruby
RESERVED_OPTIONS = [:host, :protocol, :port, :subdomain, :domain, :tld_length,
                          :trailing_slash, :anchor, :params, :only_path, :script_name,
                          :original_script_name, :relative_url_root]
```

This means that anywhere `safe_params` is used, the domain could be changed using the `domain` query. Most of the `build_canonical_path` methods call `url_for(safe_params)` which then gets used by [RoutableActions](https://gitlab.com/gitlab-org/gitlab/-/blob/682a3c0134f2cfec9e5743aa97fbaf2a7d89e65f/app/controllers/concerns/routable_actions.rb#L54):

```ruby
def ensure_canonical_path(routable, requested_full_path)
    return unless request.get?

    canonical_path = routable.full_path
    if canonical_path != requested_full_path
      if !request.xhr? && request.format.html? && canonical_path.casecmp(requested_full_path) != 0
        flash[:notice] = "#{routable.class.to_s.titleize} '#{requested_full_path}' was moved to '#{canonical_path}'. Please update any links and bookmarks that may still have the old path."
      end

      redirect_to build_canonical_path(routable)
    end
  end
```

This creates an open redirect in all of the `RoutableActions` routes by making `canonical_path != requested_full_path` (eg using a capital letter) and adding the `domain` param:

1. Visit https://gitlab.com/vakzz-h1/Redirect1?domain=aw.rs
1. You will be redirected to https://aw.rs/

The other key that can be abused is `script_name`, as this is appended to the start of the url and can be used to fake a protocol such as javascript:

1. Visit https://gitlab.com/vakzz-h1/redirect1/-/issues?script_name=javascript:alert(1)//
1. Look at the RSS Feed link

    ```html
<a class="btn btn-svg has-tooltip" data-container="body" title=""  href="javascript:alert(1)//vakzz-h1/redirect1/-/issues.atom?feed_token=XXXX&amp;state=opened" data-original-title="Subscribe to RSS feed">
  <svg class="s16 qa-rss-icon" data-testid="rss-icon">
    <use xlink:href="https://gitlab.com/assets/icons-37f758fe6359f04ae912169432d8ddd9dd45a1316d8fa634996c10bd033e9726.svg#rss"></use>
  </svg>
</a>
   ```
1. On gitlab.com this is blocked by the CSP

There are a bunch of other places that use `safe_params` that could be exploited such as the [_viewer.html.haml](https://gitlab.com/gitlab-org/gitlab/-/blob/682a3c0134f2cfec9e5743aa97fbaf2a7d89e65fapp/views/projects/blob/_viewer.html.haml#L7)

```haml
- viewer_url = local_assigns.fetch(:viewer_url) { url_for(safe_params.merge(viewer: viewer.type, format: :json)) } if load_async
.blob-viewer{ data: { type: viewer.type, rich_type: rich_type, url: viewer_url, path: viewer.blob.path }, class: ('hidden' if hidden) }
```

This allows an attacker to specify the `viewer_url` for the blob url. Since the json returned by the url has an `html` attributes it allows arbitrary html to be inserted. The below uses https://gitlab.com/-/snippets/1999965 as the viewer url and 1 click csp bypass (same as https://hackerone.com/reports/662287#activity-6026826) with https://gitlab.com/-/snippets/1999974/raw for the js payload:

1. Visit https://gitlab.com/vakzz-h1/redirect1/-/blob/master/test.txt?script_name=/-/snippets/1999965/raw%23
1. See the injected HTML:

    ```html
<form>any <b>html</b> can go <button>here<a data-remote="true" data-method="get" data-type="script" href="https://gitlab.com/-/snippets/1999974/raw" class="atwho-view select2-drop-mask pika-select">
  <img width="10000" height="10000">
</a></button></form>
    ```
1. Clicking anywhere will trigger an alert

I've only skimmed the other locations that use `safe_params` but it looks like there are a few more that load data via javascript or could be turned into open redirects. I also haven't looked into the impact of the open redirects to see if they could be escalated to leak sensitive information, I'll update the report if I find anything else.

I've put all of these in a single report as the mitigation is the same for all of them, but if you would like me to split them into separate reports I can do that as well. I've also set the severity to high due to the number of places that this is used and relative ease of trigger it, but the individual issues are probably less so might need to be adjusted. 

### What is the current *bug* behavior?

`SafeParamsHelper.safe_params` only filters out the keys `:host, :port, :protocol` but there are other dangerous ones

### What is the expected *correct* behavior?
`SafeParamsHelper.safe_params` should filter out all of the reserved options:

```ruby
RESERVED_OPTIONS = [:host, :protocol, :port, :subdomain, :domain, :tld_length,
                          :trailing_slash, :anchor, :params, :only_path, :script_name,
                          :original_script_name, :relative_url_root]
```


### Output of checks
This bug happens on GitLab.com

## Impact

* open redirect on quire a few routes
* reflected xss using the `javascript` protocol
* reflected xss with csp bypass using the blob viewer

## Attachments
No attachments
