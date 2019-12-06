# Census

Census is a web microservice which provides persistent enumeration as a service. That is to say: it counts. The web service was created as a supplementary service for use with Quatrics.

A need arose for service, similar to the [Random Number Generator Service](http://reporting.qualtrics.com/projects/randomNumGen.php) but instead for generating a series of sequential numbers. I.e, a Serial Number Generator as it were.

## Up and running

1. Build the docker image
```bash
docker-compose build
```
2. Create a config file
```
cp local_env_settings.sh.example local_env_settings.sh
```
3. Edit `local_env_settings.sh` as per [Configurtion](#configurtion) section

4. Start a server
```bash
source env_setup && docker-compose up -d
```

To start a server for development with hot-reloading run the following instead.
```bash
source env_setup && docker-compose run -p 8000:8000 census --hot-reload
```

## Configuration

|Property|Description|
|---|---|
|`SECRET_TOKEN`|This is the token that must be provided for authorization. Should be a long, unique, random string containing letters, numbers and symbols|
|`SQLALCHEMY_DATABASE_URI`|Database connection URI in [SQAlchemy Connection URI Format](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format)|

## Contributing

 * Issues - https://github.com/iokiwi/census/issues
 * PRs - https://github.com/iokiwi/census/pulls

# API Reference

## Authorization

Authorization is done by passing a secret token as a header.

```http
GET count/1
token: SB5wnG#eUObS8FDJVp*WKnNB5t4**WIc1hdeLGTwtJgN%kb7m3VRS!$d4x2l1*i!
```

The value of the token is the value `SECRET_TOKEN` is configured as in `local_env_settings.sh`.

## Resources 

### Get next number in sequence
```http
GET /count/:reference HTTP/1.1
```

|Field|Location|Description|
|---|---|---|
|token|header|Authorization token|
|reference|path|A value to be stored in the database as a reference to associate the request with data on the client side|

**Example Request**
```bash
curl -X GET \
  http://127.0.0.1:8000/count/1 \
  -H 'token: SB5wnG#eUObS8FDJVp*WKnNB5t4**WIc1hdeLGTwtJgN%kb7m3VRS!$d4x2l1*i!'
```

**Example Response**
```
Content-Type: text/html; charset=utf-8

count=1
```

Calling the service a second time will increment the ID.

