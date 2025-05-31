# firebase credentials leaks @ ███████

## Report Details
- **Report ID**: 1351326
- **URL**: https://hackerone.com/reports/1351326
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-26T08:37:48.619Z
- **Disclosed**: 2022-09-05T22:59:23.270Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello.
I found firebase credentials leaks at ████.


## Steps To Reproduce:
Visit █████ >> Right click >> view source code.



## Supporting Material/References:

 <script>
      // Your web app's Firebase configuration
      // For Firebase JS SDK v7.20.0 and later, measurementId is optional
      var firebaseConfig = {
        apiKey: "AIzaSyBZtK5_-J1DFWLBFpLBIOkeK9D8ZDfqJ3g",
        authDomain: "██████",
        databaseURL: "█████",
        projectId: "quizgame-4f2e3",
        storageBucket: "██████",
        messagingSenderId: "██████████",
        appId: "1:████████:web:923994d50811422213a052",
        measurementId: "G-N94D6VRGVG"
      };
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);
      firebase.analytics();
    </script>

## Impact

Un authorize access to firebase database.

Kind regard
@█████████

## Attachments
No attachments
