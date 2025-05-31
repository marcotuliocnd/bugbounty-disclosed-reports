# File System Monitoring Queue Overflow

## Report Details
- **Report ID**: 881891
- **URL**: https://hackerone.com/reports/881891
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-24T18:37:13.000Z
- **Disclosed**: 2021-12-03T14:01:05.136Z

## Reporter
- **Username**: ihsinme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
in the source code "owncloud/client" in the file "src/gui/folderwatcher_linux.cpp" in the function "void FolderWatcherPrivate :: inotifyRegisterPath (const QString & path)" by calling "inotify_add_watch" the file paths are set for monitoring

```cpp
 int wd = inotify_add_watch(_fd, path.toUtf8().constData(),
        IN_CLOSE_WRITE | IN_ATTRIB | IN_MOVE | IN_CREATE | IN_DELETE | IN_DELETE_SELF | IN_MOVE_SELF | IN_UNMOUNT | IN_ONLYDIR);
```
But in the specified call, the flag "IN_Q_OVERFLOW" is omitted, which allows an attacker to influence the operation of the software.
The essence of the impact is to form a large number of events overflowing the monitoring queue.
In my opinion, the most effective and not noticeable will be creating a hidden file, writing data to it, closing and deleting.

It is worth noting that the function code "void FolderWatcherPrivate :: slotReceivedNotification (int fd)"

```cpp
  do {
        len = read(fd, buffer.data(), buffer.size());
        error = errno;
        /**
          * From inotify documentation:
          *
          * The behavior when the buffer given to read(2) is too
          * small to return information about the next event
          * depends on the kernel version: in kernels  before 2.6.21,
          * read(2) returns 0; since kernel 2.6.21, read(2) fails with
          * the error EINVAL.
          */
        if (len < 0 && error == EINVAL) {
            // double the buffer size
            buffer.resize(buffer.size() * 2);
            /* and try again ... */
            continue;
        }
    } while (false);
``` 

As my tests showed, it does not provide an increase in the buffer, which could offset the impact.
The function reads part of the data from the queue, since the minimum buffer necessary for reading is much less than 2048.

```
Specifying a buffer of size
sizeof(struct inotify_event) + NAME_MAX + 1
will be sufficient to read at least one event.
```

## Impact

Thus, the essence of the impact will consist in overflowing the monitoring queue.
What will force the system to discard incoming events and the program will skip them.
Skipping program monitoring events will lead to incorrect display of files and directories in the program, and will also affect the synchronization with the server.

## Attachments
No attachments
