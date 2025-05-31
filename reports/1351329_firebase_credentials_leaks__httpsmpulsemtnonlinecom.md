# firebase credentials leaks @ https://mpulse.mtnonline.com 

## Report Details
- **Report ID**: 1351329
- **URL**: https://hackerone.com/reports/1351329
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-26T08:43:07.812Z
- **Disclosed**: 2022-09-05T22:59:06.455Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello.
I found firebase credentials leaks at https://mpulse.mtnonline.com

## Steps To Reproduce:
Visit https://mpulse.mtnonline.com >> right click >> view source code

## Supporting Material/References:
<!-- Firebase -->
    
    



    <!-- <script>
    // Initialize Firebase
    var config = {
    apiKey: "████",
    authDomain: "████████",
    databaseURL: "https://mpulse-25c68.firebaseio.com",
    projectId: "mpulse-25c68",
    storageBucket: "mpulse-25c68.appspot.com",
    messagingSenderId: "295133444438"
    };
    firebase.initializeApp(config);
    </script> -->

## Impact

Un authorize access to firebase database.


Kind regard
@aliyugombe

## Attachments
No attachments
