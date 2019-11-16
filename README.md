# Census

Census is a web microservice which provides persistent enumeration as a service. That is to say: it counts. The web service was created as a supplementary service for use with Quatrics.

A need arose for service, similar to the [Random Number Generator Service](http://reporting.qualtrics.com/projects/randomNumGen.php) but instead for generating a series of sequential numbers. I.e, a Serial Number Generator as it were.

```bash
curl -X GET \
  http://127.0.0.1:8000/count/gMW2xO1q2VZF \
  -H 'token: SB5wnG#eUObS8FDJVp*WKnNB5t4**WIc1hdeLGTwtJgN%kb7m3VRS!$d4x2l1*i!'
```

```json
{
    "id": 1,
    "origin_ip": "172.19.0.1",
    "reference": "gMW2xO1q2VZF"
}
```

Calling the service a second time will increment the ID.

```bash
curl -X GET \
  http://127.0.0.1:8000/count/gMW2xO1q2VZF \
  -H 'token: SB5wnG#eUObS8FDJVp*WKnNB5t4**WIc1hdeLGTwtJgN%kb7m3VRS!$d4x2l1*i!'
```

```json
{
    "id": 2,
    "origin_ip": "172.19.0.1",
    "reference": "gMW2xO1q2VZF"
}
```

## Features

Auth - Preshared secret key which must be provided
Origin IP - Audit trail of IP addresses requesting service
Reference - Requestor may provide a reference number which may be used to correlate requests to requestors.
