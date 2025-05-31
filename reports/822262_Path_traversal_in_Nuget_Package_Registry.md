# Path traversal in Nuget Package Registry

## Report Details
- **Report ID**: 822262
- **URL**: https://hackerone.com/reports/822262
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-17T15:51:58.636Z
- **Disclosed**: 2022-06-07T14:16:20.534Z

## Reporter
- **Username**: saltyyolk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
There's a path traversal issue in Nuget package registry which was released to GitLab-EE recently. The issue allows an attacker to create any file with an extension “.nupkg” in the filesystem. By combining the bug with a race condition in Gitaly which I used several times before (#762421, #732330). It could finally be used to read sensitive files in a GitLab instance.

For some context, a large part of the exploit were explained in #762421, the npm registry issue. Here I will focus on the simple path traversal part which makes a little bit difference.

The root cause of the path traversal lies at `ee/app/services/packages/nuget/metadata_extraction_service.rb`
```
      XPATHS = {                                                               
        package_name: '//xmlns:package/xmlns:metadata/xmlns:id',               
        package_version: '//xmlns:package/xmlns:metadata/xmlns:version'        
      }.freeze 
...
      def extract_metadata(file)                                               
        doc = Nokogiri::XML(file)                                              
                                                                               
        XPATHS.map do |key, query|                                             
          [key, doc.xpath(query).text]                                         
        end.to_h 
```
It extracts the uploaded nupkg (which is in zip format) for the contained nuspec file (which is an XML). And then looks for attribute `id` and `version`. Then the extracted package_name(id), and package_version(version) will be concatenated into a new filename in `ee/app/services/packages/nuget/update_package_from_metadata_service.rb`
```                                                                      
        @package_file.transaction do                                           
          @package_file.update!(                                               
            file_name: package_filename,                                       
            file: @package_file.file                                           
          )      
...
      def package_filename                                                     
        "#{package_name.downcase}.#{package_version.downcase}.nupkg"           
      end    
```
So my payload is:
```                                                                  
  <?xml version="1.0" encoding="utf-8"?>                                       
  <package xmlns="http://schemas.microsoft.com/packaging/2013/05/nuspec.xsd">  
    <metadata>                                                                 
      <id>DummyProject.DummyPackage</id>                                       
      <version>../../../../../nyangawa</version>                                            
    </metadata>                                                                
  </package>                                                                   
```
name the file above as `dummy.nuspec` and zip it into `dummy.nupkg` and upload it through `PUT /api/v4/projects/#{id}/packages/nuget/` endpoint  will make GitLab to create a `nyangawa.nupkg` somewhere in the filesystem.

Then I wrote a script (I used in #762421) to combine this issue and the race in Gitaly. I could finally read any file I want in my GitLab instance.

### Steps to reproduce

1. Download the attached exploit.tar.gz and extract it.
2. Install some requirements by gem install faraday and gem install rubyzip
3. Edit exp.rb to update some url and credentials
4. Execute the exp.rb to watch the result of .gitlab_shell_secret of target GitLab instance.

### Examples
{F750878}

#### Results of GitLab environment info
```
root@localhost:/# gitlab-rake gitlab:env:info

System information
System:		
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.6.5p114
Gem Version:	2.7.10
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	5.0.7
Git Version:	2.24.1
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.8.7-ee
Revision:	2643fd87200
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.12
URL:		http://10.26.0.5
HTTP Clone URL:	http://10.26.0.5/some-group/some-project.git
SSH Clone URL:	git@10.26.0.5:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	11.0.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

ps. I changed my username because of a lost bet, don't be strange :p

Best regards,
SaltyYolk

## Impact

Common arbitrary file read issue caused by path traversal similar to my previous reports.

## Attachments
- 2020-03-17-234802_649x700_scrot.png
