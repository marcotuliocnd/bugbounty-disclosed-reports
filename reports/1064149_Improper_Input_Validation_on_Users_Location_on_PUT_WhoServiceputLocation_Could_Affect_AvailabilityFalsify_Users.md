# Improper Input Validation on User's Location on PUT /WhoService/putLocation Could Affect Availability/Falsify Users

## Report Details
- **Report ID**: 1064149
- **URL**: https://hackerone.com/reports/1064149
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-22T07:03:10.150Z
- **Disclosed**: 2021-01-12T05:55:52.416Z

## Reporter
- **Username**: humayunalikhan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: who-covid-19-mobile-app

## Vulnerability Information
Summary:
Note: I noticed that that the team has fixed issues like an XSS that's caused only from a header value (typically OOS since it's not directly exploitable) https://github.com/WorldHealthOrganization/app/pull/855, so in the spirit of this I'm also reporting another "good-to-fix" issue.

On the WHO app, users send approximate location data to the WhoService API:

/app/client/flutter/lib/pages/onboarding/location_sharing_page.dart:

  Future<void> _allowLocationSharing() async {
    try {
      await Location().requestPermission();
      if (await Location().hasPermission() == PermissionStatus.granted) {
        if (await Location().requestService()) {
          LocationData location = await Location().getLocation();
          Map jitteredLocationData = JitterLocation().jitter(
              location.latitude, location.longitude,
              5 /*kms refers to kilometers*/);

          await WhoService.putLocation(
              latitude: jitteredLocationData['lat'],
              longitude: jitteredLocationData['lng']);
        }
      }
    } catch(_) {
      // ignore for now.
    } finally {
      _complete();
    }
  }
Which in turn translates to a call to https://staging.whocoronavirus.org/WhoService/putDeviceToken:

curl --request POST \
  --url 'https://hackerone.whocoronavirus.org/WhoService/putLocation' \
  --header 'content-type: application/json' \
  --header 'who-client-id: ██████████' \
  --header 'who-platform: ios' \
  --data '{
    "latitude": 22222222,
    "longitude": "9999999"
}'
This returns a 200 OK response. On the server side, we see that it uses the following logic:

  [@Override](/override) public Void putLocation(PutLocationRequest request) throws IOException {
    Client client = Client.current();
    client.latitude = request.latitude;
    client.longitude = request.longitude;
    S2LatLng coordinates = S2LatLng.fromDegrees(request.latitude, request.longitude);
    client.location = S2CellId.fromLatLng(coordinates).id();
    ofy().save().entities(client);
    return new Void();
  }
There is no validation on request.latitude, request.longitude before it is stored into the Google App Engine datastore. This is because the S2LatLng.fromDegrees (which transforms the values into a S2LatLng object) from the s2-geometry-library-java library specifically does not validate these values because, according to their comments at https://github.com/google/s2-geometry-library-java/blob/master/src/com/google/common/geometry/S2LatLng.java:

Like the rest of the "geometry" package, the
intent is to represent spherical geometry as a mathematical abstraction, so
functions that are specifically related to the Earth's geometry (e.g.
easting/northing conversions) should be put elsewhere.
Thus, even these values:

    "latitude": 22222222,
    "longitude": "9999999"
Are accepted and stored in the database even though they are technically non-existent coordinates on earth.

To reproduce, just run this request with different who-client-id UUID you generated yourself and impossible latitude and longitude.

curl --request POST \
  --url 'https://hackerone.whocoronavirus.org/WhoService/putLocation' \
  --header 'content-type: application/json' \
  --header 'who-client-id: ████████' \
  --header 'who-platform: ios' \
  --data '{
    "latitude": 22222222,
    "longitude": "9999999"
}'

## Impact

An attacker can exploit this to affect the Availability or Integrity of the analytics data by injecting false location values and falsifying user data. A fix for this would be to implement a quick lat lng validator that is specifically meant to validate Earth geometry, instead of the S2LatLng class.

## Attachments
No attachments
