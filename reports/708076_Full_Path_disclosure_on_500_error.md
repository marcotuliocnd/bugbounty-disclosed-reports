# Full Path disclosure on 500 error

## Report Details
- **Report ID**: 708076
- **URL**: https://hackerone.com/reports/708076
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-05T06:35:49.716Z
- **Disclosed**: 2019-10-05T12:58:47.835Z

## Reporter
- **Username**: rajauzairabdullah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
On manipulating cookie 
+ **parameter:** `gitHub_<anything>` 500 error returned with path disclosing of **Python** Files.

##Error Below:
> Traceback (most recent call last):
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/state_chain.py", line 328, in loop
    new_state = function(**deps.as_kwargs)
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/pando/state_chain.py", line 128, in render_response
    output = resource.render(context, state['dispatch_result'], state['accept_header'])
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/aspen/http/resource.py", line 129, in render
    return self.render_for_type(available[0], context)
  File "/opt/python/run/venv/local/lib/python3.6/site-packages/aspen/simplates/simplate.py", line 140, in render_for_type
    exec(self.page_two, context)
  File "/opt/python/bundle/4/app/www/on/%platform/associate.spt", line 36, in <module>
    cookie_obj = json.loads(b64decode_s(cookie_value))
  File "/usr/lib64/python3.6/json/__init__.py", line 354, in loads
    return _default_decoder.decode(s)
  File "/usr/lib64/python3.6/json/decoder.py", line 339, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib64/python3.6/json/decoder.py", line 355, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 98 (char 97)

## Impact

Information is being disclosed about internal files.

## Attachments
No attachments
