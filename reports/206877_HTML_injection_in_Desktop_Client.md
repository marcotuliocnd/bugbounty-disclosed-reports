# HTML injection in Desktop Client

## Report Details
- **Report ID**: 206877
- **URL**: https://hackerone.com/reports/206877
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-16T13:01:16.695Z
- **Disclosed**: 2017-05-23T07:29:33.250Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
#Problem

There are HTML injections throughout the ownCloud desktop client. A good example of this can be seen in [accountsettings.cpp line 641 to 705](https://github.com/owncloud/client/blob/172689d35cfae5137a316dfdee7dacc9667e1dcc/src/gui/accountsettings.cpp#L641-L705). For reference purposes this is a trimmed down and slightly commented version of the code:

```cpp
void AccountSettings::refreshSelectiveSyncStatus()
{
    QString msg;
    int cnt = 0;
    foreach (Folder *folder, FolderMan::instance()->map().values()) {
    ...
        foreach(const auto &it, undecidedList) {
            ...
            QString myFolder = (it);
            ...
            QModelIndex theIndx = _model->indexForPath(folder, myFolder);
            if(theIndx.isValid()) {
                // User supplied content is appended to msg
                msg += QString::fromLatin1("<a href=\"%1?folder=%2\">%1</a>").arg(myFolder).arg(folder->alias());
            } else {
                msg += myFolder; // no link because we do not know the index yet.
            }
        }
    }

    if (msg.isEmpty()) {
       ...
    } else {
        ConfigFile cfg;
        QString info =
            !cfg.confirmExternalStorage() ? tr("There are folders that were not synchronized because they are too big: ") :
            !cfg.newBigFolderSizeLimit().first ? tr("There are folders that were not synchronized because they are external storages: ") :
            tr("There are folders that were not synchronized because they are too big or external storages: ");

        ui->selectiveSyncNotification->setText(info + msg);
        ui->selectiveSyncButtons->setVisible(false);
        ui->bigFolderUi->setVisible(true);
        shouldBeVisible = true;
    }
   ...
}
```

`msg` is assigned `QString::fromLatin1("<a href=\"%1?folder=%2\">%1</a>").arg(myFolder).arg(folder->alias());` whereas `myFolder` and `folder->alias()` are user-controlled content.

If an adversary on the instance now shares a folder with someone else that exceeds the "ask for confirmation before synchronising limit" (default: 500MB) this will lead into above execution path.  An example malicious folder name would be:

> `"><&#x2f;a><p><center><h1><strong>Important!<&#x2f;strong> Please go to nextcloud.com and relogin!<&#x2f;center><&#x2f;h1><&#x2f;p><!-- ` 

In the user interface this will lead to following view in the 2.3.x client:

{F161217}

*Note that this is also exploitable on 2.2.x. For simplicity, I went with the 2.3.x client as this is the currently developed branch. Exploit has been tested on OS X and may need adjustments for other operating systems.*

#Patch proposal

This kind of vulnerability can be addressed by escaping user-supplied content, in this case one approach to patch it would be:

```diff
diff --git src/gui/accountsettings.cpp src/gui/accountsettings.cpp
index 0fb32cfbf..9c46ce9c1 100644
--- src/gui/accountsettings.cpp
+++ src/gui/accountsettings.cpp
@@ -664,7 +664,7 @@ void AccountSettings::refreshSelectiveSyncStatus()
             }
             QModelIndex theIndx = _model->indexForPath(folder, myFolder);
             if(theIndx.isValid()) {
-                msg += QString::fromLatin1("<a href=\"%1?folder=%2\">%1</a>").arg(myFolder).arg(folder->alias());
+                msg += QString::fromLatin1("<a href=\"%1?folder=%2\">%1</a>").arg(myFolder.toHtmlEscaped()).arg(folder->alias().toHtmlEscaped());
             } else {
                 msg += myFolder; // no link because we do not know the index yet.
             }
```

#General recommendation

A quick research on the client application shows that similar vulnerabilities can be found throughout the application. For example when hovering file names as can be seen in F161223. 

I'd highly recommend thus to review the whole codebase for similar vulnerabilities.

## Attachments
- spoofed-error-message.png
- font-exploit.png
