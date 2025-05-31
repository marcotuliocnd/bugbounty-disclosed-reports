# Reflected XSS on www.bookfresh.com/index.html?view=upload_form

## Report Details
- **Report ID**: 31187
- **URL**: https://hackerone.com/reports/31187
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-10-13T01:52:44.576Z
- **Disclosed**: 2017-08-31T10:31:55.025Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bookfresh

## Vulnerability Information
The issue is in the view _upload_form_.

**Description**
When you show an upload form in the site you use an URL like this: https://www.bookfresh.com/index.html?standalone=1&e=0c551a759eb62ba457d017569617eaa8&bk=FFFFFF&view=upload_form
And you show the value of the parameter `bk` in the page: `<style>body{ background-color: #[VALUE_OF_BK]; }</style>`. 

You have protection for XSS because you encode or remove tags like `<script>`, etc.
But the problem is that you are only protecting the `GET` requests. So, if I do a `POST` request the value of `bk` is shown in the page without encoding or removing the tags.

Another problem is that when the file https://www.bookfresh.com/index.html is loaded from the server there is not `X-Frame-Options` header set in the response. So, it will be more easy to exploit the vulnerability.

**Steps to reproduce**:
1. Create a HTML file with this content:

        <form action="https://www.bookfresh.com/index.html" method="post">
         <input type="hidden" name="bk" value="</style><script>alert(document.domain);</script><style>">
         <input type="hidden" name="view" value="upload_form">
        </form>
        <script>
         document.forms[0].submit();
        </script>

2. Create a HTML file with this content:

        <iframe src="[path_of_the_file_from_step_1]"></iframe>

3. Put the files on a server or run a test server on the localhost with something like: `php -S localhost:8000`
4. Visit the file created in the step 2 and wait a few seconds.
5. You will see an `alert()` with the domain of the frame: www.bookfresh.com.

It works on the last version of Firefox and it doesn't work on the last version of Chrome.

## Attachments
No attachments
