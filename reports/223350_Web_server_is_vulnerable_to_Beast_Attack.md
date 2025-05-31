# Web server is vulnerable to Beast Attack

## Report Details
- **Report ID**: 223350
- **URL**: https://hackerone.com/reports/223350
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T09:56:12.052Z
- **Disclosed**: 2017-04-24T20:37:00.595Z

## Reporter
- **Username**: mrnull1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Supported versions:                                                      
 TLSv1.0 TLSv1.1 TLSv1.2                                                 
Deflate compression: no                                                  
Supported cipher suites (ORDER IS NOT SIGNIFICANT):                      
  TLSv1.0                                                                
     RSA_WITH_AES_128_CBC_SHA                                            
     DHE_RSA_WITH_AES_128_CBC_SHA                                        
     RSA_WITH_AES_256_CBC_SHA                                            
     DHE_RSA_WITH_AES_256_CBC_SHA                                        
  (TLSv1.1: idem)                                                        
  TLSv1.2                                                                
     RSA_WITH_AES_128_CBC_SHA                                            
     DHE_RSA_WITH_AES_128_CBC_SHA                                        
     RSA_WITH_AES_256_CBC_SHA                                            
     DHE_RSA_WITH_AES_256_CBC_SHA                                        
     RSA_WITH_AES_128_CBC_SHA256                                         
     RSA_WITH_AES_256_CBC_SHA256                                         
     DHE_RSA_WITH_AES_128_CBC_SHA256                                     
     DHE_RSA_WITH_AES_256_CBC_SHA256                                     
     TLS_RSA_WITH_AES_128_GCM_SHA256                                     
     TLS_RSA_WITH_AES_256_GCM_SHA384                                     
     TLS_DHE_RSA_WITH_AES_128_GCM_SHA256                                 
     TLS_DHE_RSA_WITH_AES_256_GCM_SHA384                                 
     TLS_RSA_WITH_AES_128_CCM                                            
     TLS_RSA_WITH_AES_256_CCM                                            
     TLS_DHE_RSA_WITH_AES_128_CCM                                        
     TLS_DHE_RSA_WITH_AES_256_CCM                                        
     TLS_RSA_WITH_AES_128_CCM_8                                          
     TLS_RSA_WITH_AES_256_CCM_8                                          
     TLS_DHE_RSA_WITH_AES_128_CCM_8                                      
     TLS_DHE_RSA_WITH_AES_256_CCM_8                                      
----------------------                                                   
Server certificate(s):                                                   
  a2bdec95cbd59ce1f45b5ff03ca15a849f446c2d: CN=avatar.cihar.com          
----------------------                                                   
Minimal encryption strength:     strong encryption (96-bit or more)      
Achievable encryption strength:  strong encryption (96-bit or more)      
BEAST status: vulnerable                                                 
CRIME status: protected                                                

## Attachments
No attachments
