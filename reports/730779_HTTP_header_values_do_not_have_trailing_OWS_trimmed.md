# HTTP header values do not have trailing OWS trimmed

## Report Details
- **Report ID**: 730779
- **URL**: https://hackerone.com/reports/730779
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-06T17:46:12.794Z
- **Disclosed**: 2020-02-24T17:48:42.993Z

## Reporter
- **Username**: alyssawilk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
[I suspect I may have tagged the wrong vulnerability type -I'm failing to find "insufficient validation of user input"]

According to the HTTP-spec, http values are
       field-value    = *( field-content | LWS )
http_parser does not appear to trim trailing LWS. This means if a user sends "Host: foo\r\n" the string literal "foo" is passed up, but if the user sends "Host: foo \r\n" the string literal "foo " is passed up, complete with trailing LWS.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

If one hands "GET / HTTP/1.1\r\nHost: foo.com \r\nHello: World\r\n\r\n"
to http_parser, http_parser sends on_header_value "foo.com " instead of "foo.com"

## Impact: [add why this issue matters]

We are trying to address an issue with Envoy, where if 
"GET / HTTP/1.1\r\nHost: my-super-private-domain.com \r\nHello: World\r\n\r\n"
is passed to Envoy, and Envoy is configured to block any requests to "my-super-private-domain.com", the matcher fails due the trailing whitespace, and external users can tunnel requests that should be blocked.

Originally we were going to address this by doing whitespace trimming in Envoy, but this should probably be fixed upstream in http_parser in case other users are affected, so we're reaching out to see what folks on your end think.

## Supporting Material/References:

My Envoy regression test verifies this lack of LWS trimming, but this is current under envoy security embargo, so please don't share

TEST_F(Http1ServerConnectionImplTest, LWS) {                                                         
  initialize();                                                                                      
                                                                                                     
  InSequence sequence;                                                                               
                                                                                                     
  Http::MockStreamDecoder decoder;                                                                   
  EXPECT_CALL(callbacks_, newStream(_, _)).WillOnce(ReturnRef(decoder));                             
                                                                                                     
  TestHeaderMapImpl expected_headers{                                                                
      {"Test", "value "},      // note the LWS after value is passed up from http_parser to Envoy :-(                                                                       
      {"Hello", "World"},                                                                            
      {":path", "/"},                                                                                
      {":method", "GET"},                                                                            
  };                                                                                                 
  EXPECT_CALL(decoder, decodeHeaders_(HeaderMapEqual(&expected_headers), true)).Times(1);            
                                                                                                     
  Buffer::OwnedImpl buffer("GET / HTTP/1.1\r\nTest: value \r\nHello: World\r\n\r\n");                
  codec_->dispatch(buffer);                                                                          
  EXPECT_EQ(0U, buffer.length());                                                                    
}

## Impact

As said above, this could allow privileged escalation, where if one uses an http_parser  enabled server configured to block specific domains, those blocks can be trivially bypassed using white-space. It's possible there are other attacks bypassing http_parser header value checks with whitespace, but I haven't investigated beyond the most obvious exploit

## Attachments
No attachments
