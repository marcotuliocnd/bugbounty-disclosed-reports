# .git folder exposed [HtUS]

## Report Details
- **Report ID**: 1624157
- **URL**: https://hackerone.com/reports/1624157
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-04T14:02:15.551Z
- **Disclosed**: 2022-10-14T17:44:25.663Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Heyy there,
I have found a exposed .git folder on https://█████



https://████████/.git/config


```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://████
	fetch = +refs/heads/*:refs/remotes/origin/*

```


Using gitdumper (https://github.com/internetwache/GitTools) , I was able to dump the whole `.git` directory and later was able to get access to the whole source code of the ███ application.

```bash
code
├── 404.php
├── build
│ └── app.min.js.map
├── css
│ └── style.css
├── debug
│ ├── debug.css
│ ├── debug.js
│ └── debug.svg
├── dispatch.php
├── files
│ └── images
├── index.php
├── install.php
├── js
│ ├── config.development.js
│ └── config.production.js
├── manual
│ ├── css
│ │ └── manual.css
│ └── index.php
├── private
│ ├── Gruntfile.js
│ ├── bootstrap.php
│ ├── build.js
│ ├── classes
│ │ ├── Config.php
│ │ ├── Controller.php
│ │ ├── Database.php
│ │ ├── DatabaseResult.php
│ │ ├── DatabaseResultRow.php
│ │ ├── DebugLog.php
│ │ ├── Dictionary.php
│ │ ├── FileUploader.php
│ │ ├── ImageUploader.php
│ │ ├── Importer.php
│ │ ├── Installer.php
│ │ ├── ModelController.php
│ │ ├── Modeler.php
│ │ ├── ███████
│ │ │ ├── Controller.php
│ │ │ ├── ProblemFetcher.php
│ │ │ └── Status.php
│ │ ├── ███████Browser.php
│ │ ├── Perls
│ │ │ ├── Controller.php
│ │ │ └── UserManager.php
│ │ ├── Request.php
│ │ ├── Router.php
│ │ ├── UploadController.php
│ │ ├── UserLogin.php
│ │ ├── XmlImporter.php
│ │ └── xAPI
│ │     ├── Builder.php
│ │     ├── Controller.php
│ │     └── Logger.php
│ ├── config.json
│ ├── controllers
│ │ ├── Author
│ │ │ ├── Applications.php
│ │ │ ├── Categories.php
│ │ │ ├── DefaultParameters.php
│ │ │ ├── Globals.php
│ │ │ ├── Images.php
│ │ │ ├── Lists.php
│ │ │ ├── Modules.php
│ │ │ ├── ProblemLayouts.php
│ │ │ ├── ProblemTemplates.php
│ │ │ ├── Problems.php
│ │ │ ├── Publish.php
│ │ │ ├── Tags.php
│ │ │ ├── Unpublish.php
│ │ │ ├── UploadImage.php
│ │ │ └── Users.php
│ │ ├── Import
│ │ │ ├── Parse.php
│ │ │ └── Submit.php
│ │ ├── ███
│ │ │ ├── Browse.php
│ │ │ ├── Load.php
│ │ │ ├── Problem.php
│ │ │ ├── Reset.php
│ │ │ └── Sequence.php
│ │ ├── Perls
│ │ │ ├── ListModules.php
│ │ │ ├── ProbeProblems.php
│ │ │ ├── Request██████.php
│ │ │ ├── SampleProblems.php
│ │ │ └── UserStatus.php
│ │ ├── User
│ │ │ ├── ConfirmEmail.php
│ │ │ ├── Consent.php
│ │ │ ├── Login.php
│ │ │ ├── Logout.php
│ │ │ ├── Register.php
│ │ │ ├── ResetPassword.php
│ │ │ ├── Save.php
│ │ │ ├── Touch.php
│ │ │ ├── Unique.php
│ │ │ └── VerifyEmail.php
│ │ └── xAPI
│ │     ├── Categories.php
│ │     ├── Modules.php
│ │     ├── Problems.php
│ │     ├── Statements.php
│ │     └── Users.php
│ ├── install.xml
│ ├── models
│ │ ├── Applications.php
│ │ ├── Categories.php
│ │ ├── FileTags.php
│ │ ├── GlobalParameters.php
│ │ ├── ImageTypes.php
│ │ ├── Images.php
│ │ ├── Lists.php
│ │ ├── Modules.php
│ │ ├── ProblemLayouts.php
│ │ ├── ProblemTemplates.php
│ │ ├── Problems.php
│ │ └── Users.php
│ ├── package.json
│ ├── sql
│ │ ├── application_parameters.sql
│ │ ├── applications.sql
│ │ ├── categories.sql
│ │ ├── category_parameters.sql
│ │ ├── category_prerequisites.sql
│ │ ├── completed_modules.sql
│ │ ├── file_tags.sql
│ │ ├── global_parameters.sql
│ │ ├── image_tag_map.sql
│ │ ├── image_types.sql
│ │ ├── images.sql
│ │ ├── lists.sql
│ │ ├── module_parameters.sql
│ │ ├── modules.sql
│ │ ├── performances.sql
│ │ ├── priorities.sql
│ │ ├── problem_graph.sql
│ │ ├── problem_layouts.sql
│ │ ├── problem_parameters.sql
│ │ ├── problem_templates.sql
│ │ ├── problems.sql
│ │ ├── problems_logged.sql
│ │ ├── retired_categories.sql
│ │ ├── user_authentication.sql
│ │ ├── user_status.sql
│ │ ├── users.sql
│ │ └── xapi_statements.sql
│ └── vendor
│     └── TinCanPHP
│         ├── About.php
│         ├── Activity.php
│         ├── ActivityDefinition.php
│         ├── ActivityProfile.php
│         ├── Agent.php
│         ├── AgentAccount.php
│         ├── AgentProfile.php
│         ├── Attachment.php
│         ├── Context.php
│         ├── ContextActivities.php
│         ├── Document.php
│         ├── Extensions.php
│         ├── Group.php
│         ├── LRSInterface.php
│         ├── LRSResponse.php
│         ├── LanguageMap.php
│         ├── Map.php
│         ├── Object.php
│         ├── RemoteLRS.php
│         ├── Result.php
│         ├── Score.php
│         ├── State.php
│         ├── Statement.php
│         ├── StatementBase.php
│         ├── StatementRef.php
│         ├── StatementTargetInterface.php
│         ├── StatementsResult.php
│         ├── SubStatement.php
│         ├── Util.php
│         ├── Verb.php
│         ├── Version.php
│         └── VersionableInterface.php
├── source
│ ├── application
│ │ ├── app.js
│ │ ├── attributes
│ │ │ ├── image.js
│ │ │ ├── template.js
│ │ │ └── text.js
│ │ ├── author
│ │ │ ├── images
│ │ │ │ ├── browse.js
│ │ │ │ ├── image.js
│ │ │ │ └── multiselected.js
│ │ │ ├── images.js
│ │ │ ├── lists
│ │ │ │ ├── browse.js
│ │ │ │ ├── list.js
│ │ │ │ └── multiselected.js
│ │ │ ├── lists.js
│ │ │ ├── parameters
│ │ │ │ ├── application.js
│ │ │ │ ├── category.js
│ │ │ │ ├── global.js
│ │ │ │ ├── module.js
│ │ │ │ └── problem.js
│ │ │ ├── sets
│ │ │ │ ├── images.js
│ │ │ │ └── tags.js
│ │ │ ├── structure
│ │ │ │ ├── browse.js
│ │ │ │ ├── category
│ │ │ │ │ ├── details.js
│ │ │ │ │ ├── parameters.js
│ │ │ │ │ └── prereqs.js
│ │ │ │ ├── category.js
│ │ │ │ ├── module
│ │ │ │ │ ├── details.js
│ │ │ │ │ ├── parameters.js
│ │ │ │ │ └── perls.js
│ │ │ │ ├── module.js
│ │ │ │ ├── problem
│ │ │ │ │ ├── details.js
│ │ │ │ │ └── parameters.js
│ │ │ │ ├── problem.js
│ │ │ │ └── tree.js
│ │ │ ├── structure.js
│ │ │ ├── tabs.js
│ │ │ ├── tags
│ │ │ │ ├── browse.js
│ │ │ │ ├── multiselected.js
│ │ │ │ └── tag.js
│ │ │ ├── tags.js
│ │ │ ├── templates
│ │ │ │ ├── browse.js
│ │ │ │ ├── multiselected.js
│ │ │ │ ├── template
│ │ │ │ │ ├── details.js
│ │ │ │ │ └── parameters.js
│ │ │ │ └── template.js
│ │ │ └── templates.js
│ │ ├── author.js
│ │ ├── dashboard.js
│ │ ├── dropdowns
│ │ │ ├── layouts.js
│ │ │ └── templates.js
│ │ ├── embed.js
│ │ ├── eula.js
│ │ ├── footer.js
│ │ ├── functions
│ │ │ └── ajax.js
│ │ ├── menus
│ │ │ ├── app.js
│ │ │ ├── checkbox.js
│ │ │ ├── help.js
│ │ │ └── user.js
│ │ ├── modals
│ │ │ ├── delete-application.js
│ │ │ ├── delete-category.js
│ │ │ ├── delete-image.js
│ │ │ ├── delete-list.js
│ │ │ ├── delete-module.js
│ │ │ ├── delete-problem.js
│ │ │ ├── delete-tag.js
│ │ │ ├── delete-template.js
│ │ │ ├── delete-user.js
│ │ │ ├── duplicate-category.js
│ │ │ ├── duplicate-list.js
│ │ │ ├── duplicate-module.js
│ │ │ ├── duplicate-problem.js
│ │ │ ├── duplicate-tag.js
│ │ │ ├── duplicate-template.js
│ │ │ ├── edit-application.js
│ │ │ ├── edit-category.js
│ │ │ ├── edit-image.js
│ │ │ ├── edit-list.js
│ │ │ ├── edit-module.js
│ │ │ ├── edit-problem.js
│ │ │ ├── edit-profile.js
│ │ │ ├── edit-tag.js
│ │ │ ├── edit-template.js
│ │ │ ├── edit-user.js
│ │ │ ├── import-problems.js
│ │ │ ├── manage-image-tags.js
│ │ │ ├── manage-images.js
│ │ │ ├── manage-prereqs.js
│ │ │ ├── modify-application-params.js
│ │ │ ├── modify-category-params.js
│ │ │ ├── modify-global-params.js
│ │ │ ├── modify-module-params.js
│ │ │ ├── modify-perls.js
│ │ │ ├── modify-problem-params.js
│ │ │ ├── modify-template-params.js
│ │ │ ├── move-category.js
│ │ │ ├── move-problem.js
│ │ │ ├── new-application.js
│ │ │ ├── new-category.js
│ │ │ ├── new-list.js
│ │ │ ├── new-module.js
│ │ │ ├── new-problem.js
│ │ │ ├── new-tag.js
│ │ │ ├── new-template.js
│ │ │ ├── new-user.js
│ │ │ ├── publish-application.js
│ │ │ ├── reset-module.js
│ │ │ ├── select-image.js
│ │ │ ├── select-list.js
│ │ │ ├── select-tag.js
│ │ │ ├── unpublish-application.js
│ │ │ ├── upload-images.js
│ │ │ └── wizard
│ │ │     ├── what-are-distractors.js
│ │ │     ├── what-is-a-learning-point.js
│ │ │     ├── what-is-a-module.js
│ │ │     ├── what-is-a-problem.js
│ │ │     ├── what-is-a-prompt.js
│ │ │     ├── what-is-a-token.js
│ │ │     ├── what-is-an-app.js
│ │ │     ├── what-is-feedback.js
│ │ │     └── what-is-the-difference.js
│ │ ├── module.js
│ │ ├── not-found.js
│ │ ├── ███
│ │ │ ├── finale.js
│ │ │ ├── intro.js
│ │ │ ├── mastery.js
│ │ │ ├── passive.js
│ │ │ └── trial.js
│ │ ├── ████.js
│ │ ├── preview.js
│ │ ├── redux
│ │ │ ├── actions.js
│ │ │ ├── adapters.js
│ │ │ ├── reducers.js
│ │ │ └── store.js
│ │ ├── user
│ │ │ ├── authenticated.js
│ │ │ ├── authorized.js
│ │ │ ├── consent.js
│ │ │ ├── login.js
│ │ │ ├── register.js
│ │ │ └── verify.js
│ │ ├── user-management.js
│ │ ├── wizard
│ │ │ ├── apps
│ │ │ │ ├── create.js
│ │ │ │ ├── index.js
│ │ │ │ └── select.js
│ │ │ ├── attributes
│ │ │ │ ├── answer
│ │ │ │ │ ├── image
│ │ │ │ │ │ ├── choose.js
│ │ │ │ │ │ ├── preview.js
│ │ │ │ │ │ ├── specify.js
│ │ │ │ │ │ ├── tag
│ │ │ │ │ │ │ ├── create
│ │ │ │ │ │ │ │ ├── images.js
│ │ │ │ │ │ │ │ └── name.js
│ │ │ │ │ │ │ ├── create.js
│ │ │ │ │ │ │ └── select.js
│ │ │ │ │ │ └── tag.js
│ │ │ │ │ ├── image.js
│ │ │ │ │ └── text.js
│ │ │ │ ├── answer.js
│ │ │ │ ├── continue.js
│ │ │ │ ├── distractors
│ │ │ │ │ ├── index
│ │ │ │ │ │ ├── edit.js
│ │ │ │ │ │ └── preview.js
│ │ │ │ │ ├── index.js
│ │ │ │ │ ├── lists
│ │ │ │ │ │ ├── create.js
│ │ │ │ │ │ ├── index.js
│ │ │ │ │ │ └── select.js
│ │ │ │ │ ├── specify
│ │ │ │ │ │ ├── image
│ │ │ │ │ │ │ ├── edit.js
│ │ │ │ │ │ │ └── preview.js
│ │ │ │ │ │ ├── image.js
│ │ │ │ │ │ └── text.js
│ │ │ │ │ ├── specify.js
│ │ │ │ │ ├── summary.js
│ │ │ │ │ └── tags
│ │ │ │ │     ├── create
│ │ │ │ │     │ ├── images.js
│ │ │ │ │     │ └── name.js
│ │ │ │ │     ├── create.js
│ │ │ │ │     ├── index.js
│ │ │ │ │     └── select.js
│ │ │ │ ├── edit.js
│ │ │ │ ├── feedback.js
│ │ │ │ ├── image
│ │ │ │ │ ├── choose.js
│ │ │ │ │ ├── preview.js
│ │ │ │ │ ├── specify.js
│ │ │ │ │ ├── tag
│ │ │ │ │ │ ├── create
│ │ │ │ │ │ │ ├── images.js
│ │ │ │ │ │ │ └── name.js
│ │ │ │ │ │ ├── create.js
│ │ │ │ │ │ └── select.js
│ │ │ │ │ └── tag.js
│ │ │ │ ├── image.js
│ │ │ │ ├── layout.js
│ │ │ │ ├── preview.js
│ │ │ │ └── question.js
│ │ │ ├── breadcrumbs.js
│ │ │ ├── categories
│ │ │ │ ├── create.js
│ │ │ │ ├── index.js
│ │ │ │ └── select.js
│ │ │ ├── modules
│ │ │ │ ├── create.js
│ │ │ │ ├── index.js
│ │ │ │ └── select.js
│ │ │ ├── problems
│ │ │ │ ├── create
│ │ │ │ │ ├── layout.js
│ │ │ │ │ └── name.js
│ │ │ │ ├── create.js
│ │ │ │ ├── index.js
│ │ │ │ └── select.js
│ │ │ └── samples.js
│ │ └── wizard.js
│ ├── application.js
│ ├── classes
│ │ ├── actions.js
│ │ ├── persistent.js
│ │ └── timer.js
│ ├── constants.js
│ ├── functions
│ │ ├── adapters.js
│ │ ├── ajax.js
│ │ ├── collection.js
│ │ ├── cookies.js
│ │ ├── enumerable.js
│ │ ├── preload.js
│ │ └── reducers.js
│ ├── main.js
│ ├── mixins
│ │  └── validatable.js
│ ├── vendor
│ │ ├── history
│ │ │ ├── history.js
│ │ │ └── history.min.js
│ │ ├── react
│ │ │ ├── react-dom-server.js
│ │ │ ├── react-dom-server.min.js
│ │ │ ├── react-dom.js
│ │ │ ├── react-dom.min.js
│ │ │ ├── react-with-addons.js
│ │ │ ├── react-with-addons.min.js
│ │ │ ├── react.js
│ │ │ └── react.min.js
│ │ ├── react-redux
│ │ │ ├── react-redux.js
│ │ │ └── react-redux.min.js
│ │ ├── react-router
│ │ │ ├── ReactRouter.js
│ │ │ └── ReactRouter.min.js
│ │ └── redux
│ │     ├── redux.js
│ │     └── redux.min.js
│ └── widgets
│     ├── alerts.js
│     ├── attribute-image.js
│     ├── button.js
│     ├── checkbox.js
│     ├── clickable.js
│     ├── content.js
│     ├── equalize.js
│     ├── file-browser.js
│     ├── form.js
│     ├── modals.js
│     ├── popover.js
│     ├── searchbox.js
│     └── unreact.js
├── style.css
├── tasks
│ └── xapi.php
└── vendor
    ├── animate.css
    ├── babel-core
    │ └── 5.8.23
    │     ├── browser-polyfill.js
    │     ├── browser-polyfill.min.js
    │     ├── browser.js
    │     └── browser.min.js
    ├── classList.min.js
    ├── es6-module-loader
    │ ├── es6-module-loader-dev.js
    │ ├── es6-module-loader-dev.js.map
    │ ├── es6-module-loader-dev.src.js
    │ ├── es6-module-loader.js
    │ ├── es6-module-loader.js.map
    │ └── es6-module-loader.src.js
    ├── fastclick.js
    ├── font-awesome
    │ ├── css
    │ │ ├── font-awesome.css
    │ │ └── font-awesome.min.css
    │ └── fonts
    │     ├── FontAwesome.otf
    │     ├── fontawesome-webfont.eot
    │     ├── fontawesome-webfont.svg
    │     ├── fontawesome-webfont.ttf
    │     ├── fontawesome-webfont.woff
    │     └── fontawesome-webfont.woff2
    ├── foundation
    │ ├── foundation
    │ │ ├── foundation.abide.js
    │ │ ├── foundation.accordion.js
    │ │ ├── foundation.alert.js
    │ │ ├── foundation.clearing.js
    │ │ ├── foundation.dropdown.js
    │ │ ├── foundation.equalizer.js
    │ │ ├── foundation.interchange.js
    │ │ ├── foundation.joyride.js
    │ │ ├── foundation.js
    │ │ ├── foundation.magellan.js
    │ │ ├── foundation.offcanvas.js
    │ │ ├── foundation.orbit.js
    │ │ ├── foundation.reveal.js
    │ │ ├── foundation.slider.js
    │ │ ├── foundation.tab.js
    │ │ ├── foundation.tooltip.js
    │ │ └── foundation.topbar.js
    │ ├── foundation.css
    │ ├── foundation.min.css
    │ ├── foundation.min.js
    │ └── foundation.modified.min.js
    ├── jquery
    │ └── jquery-2.1.3.min.js
    ├── modernizr.js
    └── systemjs
        ├── system-csp-production.js
        ├── system-csp-production.js.map
        ├── system-csp-production.src.js
        ├── system-polyfills.js
        ├── system-polyfills.js.map
        ├── system-polyfills.src.js
        ├── system-register-only.js
        ├── system-register-only.js.map
        ├── system-register-only.src.js
        ├── system.js
        ├── system.js.map
        └── system.src.js

370 directories, 3515 files
```

By just looking at some interesting files such as `config.js`, I found the credentials for the database:

`/private/config.json`

```json
{
	    // DATABASE_HOST
    // Database host to connect to
    
    "DATABASE_HOST":"localhost",
    
    // DATABASE_USER
    // Name of the database user to connect as
    
    "DATABASE_USER":"███",
    
    // DATABASE_PASSWORD
    // Password to connect with
    
    "DATABASE_PASSWORD":"█████████",
    
    // DATABASE_NAME
    // Name of the Authoring Tools database
    
    "DATABASE_NAME":"███████",
}
```

And another interesting file where I found user email addresses and password hashes: `/private/install.xml`

```xml
<user>
    <email>██████████</email>
    <password>█████</password>
    <name>██████</name>
    <superuser>1</superuser>
</user>
<user>
    <email>█████</email>
    <password>███████</password>
    <name>███████</name>
    <superuser>1</superuser>
</user>
<user>
    <email>████</email>
    <password>████</password>
    <name>█████</name>
    <superuser>1</superuser>
</user>
<user>
    <email>██████████</email>
    <password>███</password>
    <name>█████████</name>
    <superuser>1</superuser>
</user>
<user>
    <email>████████</email>
    <password>██████████</password>
    <name>█████████</name>
    <superuser>1</superuser>
</user>
<user>
    <email>██████</email>
    <password>████████</password>
    <name>████████</name>
    <superuser>1</superuser>
</user>
```


The information disclosed in above two files is really very sensitive, I haven't looked much into other files but I am pretty sure there will be much more things like this in the source code.

## Impact

An attacker by dumping the whole source code , can find credentials such as I have shown in my report (db creds, administrator creds) and also they will have full access to the source code of the application.

Thankyou
Regards
Sudhanshu

## Attachments
No attachments
