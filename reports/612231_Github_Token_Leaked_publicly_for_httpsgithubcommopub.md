# Github Token Leaked publicly for https://github.com/mopub

## Report Details
- **Report ID**: 612231
- **URL**: https://hackerone.com/reports/612231
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-13T18:05:27.945Z
- **Disclosed**: 2019-08-15T23:05:07.900Z

## Reporter
- **Username**: moro139
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
##Description :

GitHub is a truly awesome service but it is unwise to put any sensitive data in code that is hosted on GitHub and similar services as i was able to find github token indexed 4 days Ago by user
Dravya Nataraj 

##Issue & POC :

You can find the leak in this link :
https://github.com/dravyan/Sample/blob/725ac6be32530197aa5cb29239d6d6fb5c3ef8f2/android-automate-release.sh
> #!/usr/bin/env bash
# ==================================================== #
### Set up gitsubmodules to run gradle build ###
#git submodule update --recursive --remote
#git add submodules https://github.com/mopub/mopub-android-sdk.git
#git add submodules https://github.com/mopub/mopub-android.git
#git add submodules https://github.com/mopub/mopub-pso-tools.git
#export FIREBASE_TOKEN=█████
echo "running script testing"
USER_NAME=dravyan
API_KEY=████████
# Networks this script checks for
NETWORKS=( 
    AdColony
    AdMob
    AppLovin 
    Chartboost
    FacebookAudienceNetwork
    Flurry 
    IronSource
    OnebyAOL
    Tapjoy
    UnityAds
    Verizon
    Vungle
)
### Function to get display name for Firebase update ###
function get_display_name {
    key=$1
    out=$2
    name=$key
    case "$key" in
        AdMob ) name="Google (AdMob)";;
        FacebookAudienceNetwork ) name="Facebook Audience Network";;
        Flurry ) name="Yahoo! Flurry";;
        IronSource ) name="ironSource";;
        OnebyAOL ) name="One by AOL";;
        UnityAds ) name="Unity Ads";;
    esac
    eval "$out='$name'"
}
### Function to read Adapter version from AdapterConfiguration ###
function read_networkAdapter_version
{
 versionnumber=`grep -r "project.version = " ./$1/ | awk '{print $3}' | sed s/\'//g | sed s/\;//g`
 echo $versionnumber
 sdkverion=`echo $versionnumber | cut -d'.' -f 1-3`
 echo $sdkverion
 lowercaseselection=$(echo "$1" | tr '[:upper:]' '[:lower:]')
 mv ./libs/mopub-$lowercaseselection-adapters-*.aar ./libs/$lowercaseselection-$versionnumber.aar
 ### Generate pom file for adapter version ###
echo '<?xml version="1.0" encoding="UTF-8"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.mopub.mediation</groupId>
  <artifactId>'"$lowercaseselection"'</artifactId>
  <version>'"$versionnumber"'</version>
  <packaging>aar</packaging>
</project>' >> ./libs/sample.pom
  ls ./libs
  echo $lowercaseselection
  echo $versionnumber
  mv ./libs/*.pom ./libs/$lowercaseselection-$versionnumber.pom
  ### CREATING TAG RELEASE IN GITHUB ###
  commitId= git rev-parse HEAD
  echo $commitId
  tagname="$lowercaseselection-$versionnumber"
  echo $tagname
  #git tag -a $lowercaseselection-$versionnumber -m "new tag" $commitId
  #git push origin $versionnumber
  ### Publish release in Github [TO_DO]
  #curl -H "Authorization: token ██████████" --data '{"tag_name": "$lowercaseselection-$versionnumber","target_commitish": "$commitId","name": "$versionnumber","body": "Release of version $versionnumber. Refer https://github.com/mopub/mopub-android-mediation/blob/master/$1/CHANGELOG.md.", "draft": false, "prerelease": false}' https://api.github.com/repos/mopub/mopub-android-mediation/releases
  #curl -H "Authorization: token ████████" --data '{"tag_name": "'"$tagname"'","target_commitish": "'"$commitId"'","name": "'"$versionnumber"'","body": "Refer https://github.com/mopub/mopub-android-mediation/blob/master/$1/CHANGELOG.md.","draft": false,"prerelease": false}' https://api.github.com/repos/mopub/mopub-android-mediation/releases
  ### RELEASING aar AND pom TO BINTRAY ###
  ##curl -T <FILE.EXT> -udravyan:<API_KEY> https://api.bintray.com/content/mopub/mopub-android-mediation/<YOUR_COOL_PACKAGE_NAME>/<VERSION_NAME>/<FILE_TARGET_PATH>
  #curl -T ./libs/$lowercaseselection-$versionnumber.aar -u$USER_NAME:$API_KEY https://api.bintray.com/content/mopub/mopub-android-mediation/com.mopub.mediation.$lowercaseselection/$versionnumber/com/mopub/mediation/$lowercaseselection/$versionnumber/
  #curl -T ./libs/$lowercaseselection-$versionnumber.pom -u$USER_NAME:$API_KEY https://api.bintray.com/content/mopub/mopub-android-mediation/com.mopub.mediation.$lowercaseselection/$versionnumber/com/mopub/mediation/$lowercaseselection/$versionnumber/
  if [ $? -eq 0 ]; then
    ### UPDATE FIREBASE ###
    echo "Updating firebase JSON..."
    firebase_project="mopub-mediation"
    FIREBASE_TOKEN="██████████"
    get_display_name $i name
    json_path="/releaseInfo/$name/Android/version"
    echo $i
    echo $versionnumber
    if [ -z "$FIREBASE_TOKEN" ]; then
        print_red_line "\$FIREBASE_TOKEN environment variable not set!"
    else
        #firebase database:set --confirm "/releaseInfo/$name/Android/version/adapter/" --data "\"$versionnumber\"" --project $firebase_project --token $FIREBASE_TOKEN
        #firebase database:set --confirm "/releaseInfo/$name/Android/version/sdk/" --data "\"$sdkverion\"" --project $firebase_project --token $FIREBASE_TOKEN
        if [[ $? -ne 0 ]]; then
            echo "ERROR: Failed to run firebase commands; please follow instructions at: https://firebase.google.com/docs/cli/"
        else
            echo "Done updating firebase JSON"
        fi
      fi
else
    echo Failed to Push to bintray. Please update bintray before updating Firebase.
fi
### CLEAN UP /LIBS FOLDER ###
 rm -r ./libs/*.pom
}
for i in "${NETWORKS[@]}"
do
    changed=$(git log --name-status -1 --oneline ./ | grep $i)
    if [[ ! -z "$changed" ]]; then
        echo "$changed"
        read_networkAdapter_version  $i
    fi  
done

## Impact

I didn't try anything with the token, and dont know what access it has, and i know that in order to login to https://github.com/mopub/mopub-android.git 
https://github.com/mopub/mopub-pso-tools.git

## Attachments
No attachments
