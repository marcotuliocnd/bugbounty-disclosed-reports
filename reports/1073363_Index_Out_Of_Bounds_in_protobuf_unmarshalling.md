# Index Out Of Bounds in protobuf unmarshalling

## Report Details
- **Report ID**: 1073363
- **URL**: https://hackerone.com/reports/1073363
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-01-07T10:23:45.000Z
- **Disclosed**: 2021-08-30T19:06:19.305Z

## Reporter
- **Username**: pulpkk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:

I have recently discovered a bug in the gogo/protobuf code generator.  This bug allows for an index out of bounds when unmarshalling certain protobuf objects. The bug is that a check is lacking when skipping certain bytes. There are numerous occurrences of this bug (too many to count easily) the following is one such case.

In `staging/src/k8s.io/api/certificates/v1beta1/generated.pb.go`
```
1686:					skippy, err := skipGenerated(dAtA[iNdEx:])
1690:					if skippy < 0 {
1693:					if (iNdEx + skippy) > postIndex {
1696:					iNdEx += skippy
```

Here the issue may occur since `iNdEx` is an int the following `iNdEx += skippy` may overflow causing a negative value. Next time the `dAtA[iNdEx]` occurs it will cause an index out of bounds and the program will panic.

Since the bug is so wide spread I have not fully analysed the different impacts but since this appears in many APIs it would likely lead to crashing nodes.

Patch:

The code should have the checks to match the following as seen in the same file `staging/src/k8s.io/api/certificates/v1beta1/generated.pb.go`
```
1736:			skippy, err := skipGenerated(dAtA[iNdEx:])
1740:			if skippy < 0 {
1743:			if (iNdEx + skippy) < 0 {
1746:			if (iNdEx + skippy) > l {
1749:			iNdEx += skippy
```

Specifically the check `if (iNdEx + skippy) < 0`

Note: I have contracted the maintainers of gogo/protobuf and they have a patch and will make a release soon. After that it is recommended to re-generate all of the existing protobuf code. Alternatively if waiting for a release is too long then the patch may be applied manually OR I can create a patched version of gogo/protobuf.

## Kubernetes Version:

v1.20.2

## Component Version:

n/a

## Steps To Reproduce:

I have not generated a PoC as the bug was very simple to explain but happy to do so upon request.

## Supporting Material/References:

n/a

## Impact

Attackers will be able to crash nodes which use the affected protobuf code arbitrarily.

## Attachments
No attachments
