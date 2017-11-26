### A thin wrapper around oepnalpr api

### Build
```
docker build . sepehrv/openalpr
docker run -it -p 8080:80 -v /home/ubuntu/:/data sepehrv/openalpr bash
```
then run the app.

#### Usage
Just a personal experiment. Don't expect the server to be up all the time.
replace the url with any image link. then see what openalpr would respond.
returns json.

```curl -H "Content-Type: application/json" -X POST -d '{"image_url":"https://www.roadtrafficsigns.com/blog/wp-content/uploads/2013/06/Calif-license-plate.jpg"}' http://199.116.235.173:8080/get```
