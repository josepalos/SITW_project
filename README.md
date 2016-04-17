# SITW_project

Github public address: https://github.com/josepalos/SITW_project/

For use the REST API (inside djangostack if used):
 - pip install djangorestframework
 - pip install markdown       # Markdown support for the browsable API.
 - pip install django-filter  # Filtering support
 
Database models: 

![model-diagram](https://github.com/josepalos/SITW_project/blob/master/diagram.png)

 The application has the following links:
 - utd/artists --> lists the artists in the database
 - utd/artist/{id} --> shows the artist details stored in the database
 - utd/artists/{id}/albums --> lists the albums of the artist
 - utd/artist/{id}/follow and /unfollow --> when the user is registered, going to this link adds or removes the artist from the list of artists followed by the user
 - utd/albums/{id}/ --> shows the details of the album stored in the database
 - utd/albums/{id}/songs --> lists the songs of the album
 - utd/albums/{id}/providers --> lists the providers of an album
 - utd/songs/{id} --> shows the details of a song from the database
 - utd/user/{username} --> shows the profile information of the user
 - utd/user/{username}/following --> lists the artists followed by the user
 - utd/user/{username}/playlist --> lists the songs of the playlist of the user

To access the REST API the entry point is:
- /utd/api

To access the admin interface (develop mode):
- username: josep
- password: josepalos
