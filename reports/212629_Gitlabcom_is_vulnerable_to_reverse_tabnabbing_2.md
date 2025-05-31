# Gitlab.com is vulnerable to reverse tabnabbing. (#2)

## Report Details
- **Report ID**: 212629
- **URL**: https://hackerone.com/reports/212629
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-11T18:45:39.677Z
- **Disclosed**: 2017-05-09T19:12:21.392Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Dear GitLab bug bounty team,

# Summary
---

Gitlab.com is vulnerable to reverse tabnabbing in issues, comments, etc. This is the same type of issue as https://hackerone.com/reports/211065, but far worse since in the previous report only a user with developer access to a project could view the "Environments" tab. In this case, the issue affects anywhere where HTML can be added.

# Why does this vulnerability exist?
---

By creating a link with `https://gitlab.com@example.com` the parser ignores it and does not add the usual `rel="nofollow noreferrer"` which is located on all other links. I discovered this, because I noticed that internal links are treated differently than external links. So in the example above the victim ends up on `example.com`, which is where the same scenario as https://hackerone.com/reports/211065 can be performed.

In order to demonstrate this issue the following payload can be used:

~~~
<a href="https://gitlab.com@example.com" target="_blank">Reverse Tabnabbing</a>
~~~

# Where does the issue lie?
---

The issue appears to lie in the following lines of code:

~~~
it 'skips internal links' do
    internal = Gitlab.config.gitlab.url
    exp = act = %Q(<a href="#{internal}/sign_in">Login</a>)
    expect(filter(act).to_html).to eq exp
  end
~~~

Link to source code: https://github.com/gitlabhq/gitlabhq/blob/master/spec/lib/banzai/filter/external_link_filter_spec.rb#L16-L20

If you require further information feel free to contact me.

Yours sincerely,
Ed

## Attachments
No attachments
