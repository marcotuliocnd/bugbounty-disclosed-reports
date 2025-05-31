# Persistent XSS in Note objects

## Report Details
- **Report ID**: 508184
- **URL**: https://hackerone.com/reports/508184
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-12T04:17:55.553Z
- **Disclosed**: 2019-07-19T00:03:17.197Z

## Reporter
- **Username**: saltyyolk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
Some cache invalidation and project import logic issues enable an attacker to import a project with XSS payloads in places like MR discussions and similar places where a Note object exists.

**Description:**
There are basically 3 issues causing the XSS here:
All attributes of Note objects are controllable in `project.json`, for example `note_html` and `cached_markdown_version`.

Now I can control the value of `note_html` to contain my XSS payload, but the problem is that the value of this field is a `CacheMarkdownField`, it's regenerated from the value of `note` during new object creation (when `note_object.note_html_invalidated?` returns true). The next question is how to trick GitLab that the field does not need to be regenerated.

in `app/models/concerns/cache_markdown_field.rb`
```
      define_method(invalidation_method) do
        changed_fields = changed_attributes.keys
        invalidations  = changed_fields & [markdown_field.to_s, *INVALIDATED_BY]
        invalidations.delete(markdown_field.to_s) if changed_fields.include?("#{markdown_field}_html")

        !invalidations.empty? || !cached_html_up_to_date?(markdown_field)
      end
```

There are 2 checks here (also the last 2 issues):
the first one is:
```
        INVALIDATED_BY = %w[author project].freeze
...
        invalidations  = changed_fields & [markdown_field.to_s, *INVALIDATED_BY]
        invalidations.delete(markdown_field.to_s) if changed_fields.include?("#{markdown_field}_html")
```

```
note_object.changed_attributes.keys
=> ["note", "noteable_type", "author_id", "created_at", "updated_at", "project_id", "line_code", "position", "original_position", "note_html", "cached_markdown_version", "change_position", "attachment"]
```

This check is, unfortunately, voided because
+ Neither `author` nor `project` is in the changed_attributes list, but `author_id` and `project_id`
+ `note` is deleted from `invalidations` because `note_html` is also changed
So invalidations is empty.

and the other one is:
```
!cached_html_up_to_date?(markdown_field)
```
It basically checks whether attribute `cached_markdown_version` equals to `latest_cached_markdown_version`
This is really interesting, because I found that `latest_cached_markdown_version` is always 917504 in my GitLab instance (also gitlab.com). Looks like `local_version` is always 0 for at least Notes in MR.

```
  def latest_cached_markdown_version
    @latest_cached_markdown_version ||= (CacheMarkdownField::CACHE_COMMONMARK_VERSION << 16) | local_version
  end

  def local_version
    return local_markdown_version if has_attribute?(:local_markdown_version)

    settings = Gitlab::CurrentSettings.current_application_settings

    if settings.respond_to?(:local_markdown_version)
      settings.local_markdown_version
    else
      0
    end
  end
```

Finally, I could set `note_html` to the XSS payload, and `cached_markdown_version` to the magic number to avoid my payload being overwritten by GitLab. :P


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Create an export of a project with at least 1 discussion in at least 1 merge request.
  1. Modify the project.json, add field `note_html` and `cached_markdown_version`

```
      "notes": [
        {
          "id": 1,
          "note": "interesting note here",
          "note_html": "<img src=\"test\" onerror=\"alert(document.domain)\"></img>html overwritten",
          "cached_markdown_version": 917504,
```

  1. Import the modified project
  1. View the only discussion of the imported project.

## Supporting Material/References:

Check `https://gitlab.com/Nyangawa/xss/merge_requests/1`, you should be able to see a pop-up.

## Impact

This is a typical persistent XSS issue and the link I mentioned above is accessible publicly, so all GitLab users are vulnerable theoretically.

## Attachments
- Screen_Shot_2019-03-12_at_11.45.35_AM.png
