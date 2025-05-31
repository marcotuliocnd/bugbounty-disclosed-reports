# csi-snapshot-controller crashes when processing VolumeSnapshot with non-existing PVC

## Report Details
- **Report ID**: 995699
- **URL**: https://hackerone.com/reports/995699
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-01T09:23:55.600Z
- **Disclosed**: 2021-01-07T19:00:41.829Z

## Reporter
- **Username**: jsafrane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
csi-snapshot-controller crashes when processing VolumeSnapshot with non-existing PVC

## Kubernetes Version:
1.19


## Component Version:
snapshot-controller from external-snapshotter repo ver 3.0.0
https://github.com/kubernetes-csi/external-snapshotter/releases/tag/v3.0.0

## Steps To Reproduce:

  1. Install Kubernetes 1.19 with snapshot-controller v3.0.0
  1. Create VolumeSnapshot object with empty spec.volumeSnapshotClass and spec.source.persistentVolumeClaimName = <non-existing PVC name>
    ```
    apiVersion: snapshot.storage.k8s.io/v1beta1
    kind: VolumeSnapshot
    metadata:
      name: new-snapshot
    spec:
      source:
        persistentVolumeClaimName: blabla
    ```

  1. watch snapshot-controller die

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

snapshot-controller log:
```
E0929 06:42:38.147021       1 snapshot_controller_base.go:338] checkAndUpdateSnapshotClass failed to setDefaultClass the snapshot source PVC name is not specified
E0929 06:42:38.147118       1 runtime.go:78] Observed a panic: "invalid memory address or nil pointer dereference" (runtime error: invalid memory address or nil pointer dereference)
goroutine 161 [running]:
k8s.io/apimachinery/pkg/util/runtime.logPanic(0x1446fc0, 0x201e670)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/runtime/runtime.go:74 +0xa6
k8s.io/apimachinery/pkg/util/runtime.HandleCrash(0x0, 0x0, 0x0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/runtime/runtime.go:48 +0x89
panic(0x1446fcit sh0, 0x201e670)
        /usr/lib/golang/src/runtime/panic.go:969 +0x175
github.com/kubernetes-csi/external-snapshotter/v3/pkg/common-controller.(*csiSnapshotCommonController).syncSnapshotByKey(0xc0001f8e00, 0xc0006a6ae0, 0x19, 0x0, 0xbc)
        /go/src/github.com/kubernetes-csi/external-snapshotter/pkg/common-controller/snapshot_controller_base.go:215 +0x9d7
github.com/kubernetes-csi/external-snapshotter/v3/pkg/common-controller.(*csiSnapshotCommonController).snapshotWorker(0xc0001f8e00)
        /go/src/github.com/kubernetes-csi/external-snapshotter/pkg/common-controller/snapshot_controller_base.go:188 +0xed
k8s.io/apimachinery/pkg/util/wait.BackoffUntil.func1(0xc0006ba8b0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:155 +0x5f
k8s.io/apimachinery/pkg/util/wait.BackoffUntil(0xc0006ba8b0, 0x1774260, 0xc0001f0030, 0x1, 0xc00002a1e0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:156 +0xad
k8s.io/apimachinery/pkg/util/wait.JitterUntil(0xc0006ba8b0, 0x0, 0x0, 0x1, 0xc00002a1e0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:133 +0x98
k8s.io/apimachinery/pkg/util/wait.Until(0xc0006ba8b0, 0x0, 0xc00002a1e0)
        /go/src/github.com/kubernetes-csi/external-snapshotter/vendor/k8s.io/apimachinery/pkg/util/wait/wait.go:90 +0x4d
created by it shgithub.com/kubernetes-csi/external-snapshotter/v3/pkg/common-controller.(*csiSnapshotCommonController).Run
        /go/src/github.com/kubernetes-csi/external-snapshotter/pkg/common-controller/snapshot_controller_base.go:139 +0x2ae
panic: runtime error: invalid memory address or nil pointer dereference [recovered]
        panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0xa0 pc=0x12b1d97]
```


Note:

* This has been already **publicly reported** by Qin Ping, piqin@redhat.com at https://bugzilla.redhat.com/show_bug.cgi?id=1883421. She should get credit for discovering the issue and bounty if possible. China has national holiday until Oct 8th, so I'm filling the report.
  * I already fixed it upstream ( https://github.com/kubernetes-csi/external-snapshotter/issues/380,  https://github.com/kubernetes-csi/external-snapshotter/pull/381) and only later realized its security impacts.

* Volume snapshots are Beta feature of Kubernetes 1.19 / external-snapshotter 3.0.0.
* external-snapshotter 3.0.0 has been released ~14 days ago and it's probably not widely installed yet.

## Impact

DoS of snapshot-controller. It's restarted by Kubernetes, but it dies processing the same VolumeSnapshot again and again.

* Users can't create snapshots of their volumes.
* Kubernetes (snapshot-controller) does not clean up VolumeSnapshotContent objects when user deletes a VolumeSnapshot and its Retain policy is Delete.

All other Kubernetes functionality is not impacted.

## Attachments
No attachments
