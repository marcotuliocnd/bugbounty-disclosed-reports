# Leak of sensitive values to Airflow rendered template

## Report Details
- **Report ID**: 1773895
- **URL**: https://hackerone.com/reports/1773895
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-15T09:07:08.685Z
- **Disclosed**: 2022-12-27T18:54:38.372Z

## Reporter
- **Username**: jrs53
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I’m just getting started with Airflow, but seem to have got into a situation where sensitive values (e.g. connection passwords) end up in my task’s rendered template. Here’s how my DAG starts, having set up a connection called “secret” with a password specified: 

```
     t1 = BashOperator( 

        task_id="masked-in-rendered-template", 

        bash_command="echo {{ conn.secret.password }}", 

    ) 
        

    t2 = BashOperator( 

        task_id="not-masked-in-rendered-template", 

        depends_on_past=True, 

        bash_command="echo {{ conn.secret.password }}",         

        #bash_command="fail {{ conn.secret.password }}" 

    ) 


    t1 >> t2 
```
 

I manually trigger this DAG and it runs as expected - it succeeds, and both the rendered template and log output show the password masked. 

 

Next I swap t2's bash_command for the one intended to fail and manually trigger the DAG again. It also runs as expected, failing but with the password masked in both the rendered template and the log output. 

 

Next, I manually trigger the DAG again (no changes). This time, since depends_on_past is true for t2, t1 executes fine, but t2 is not scheduled (it shows not yet started in the UI). However, if I click on t2 in the graph view and look at the rendered template, it shows the password *unmasked*. 

 

Finally, if I swap the lines back again and manually trigger (so t2 succeeds), all the running DAGs complete and the output is masked, 

 

My guess is this is a race hazard - the third invocation of t2 won't run (since depends_on_past=True and it previously failed), but the masking code comes at some point later. 

 

I am running Airflow v2.2.4 on CentOS 7 & Python 3.9

## Impact

Learn sensitive values (e.g. database passwords, API keys etc) from rendered templates

## Attachments
No attachments
