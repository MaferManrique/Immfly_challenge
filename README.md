# Immfly_challenge

Hey! I'm Mafer Manrique! I'm python developer
This project offers you an API to solve the Immfly challenge.

# Installation 
## Without Docker
To run this project locally without docker follows this process:

Create your own virtual environment and make sure to install django and django rest framework:

```pip3 install -r requirements.txt```

Make sure to run all the migrations and seed the database with testing data

```python3 manage.py migrate && python3 manage.py seed```

Finally, run the project

```python3 manage.py runserver```

Now you can go to `localhost:8000/api`and you will see the API endpoints!

## With Docker 

With docker, you only need to run on your shell this:

```docker-compose up -d```

And now you can go to `localhost:8000/api` to see your endpoints

# How calculate average

To get a .csv file with all the channels a their rating average, you only need to run this command

```python3 manage.py getratings```

With this command you gonna have a .csv file on your project root

# Models
## Channels
Considering that a channel has a hierarchical structure in the form of a tree, and each channel can have subchannels that in turn are channels, I decided to create a single channel model that saves a reference to its parent in case it has one. If a channel does not have a parent channel (parent_channel=None), then it is one of the parent channels

## Content
For this model, consider content as the group of all files to give the user content that they can enjoy. For example: if the content is the chapter of a tv series, it will have several associated files that could be the video without audio, the audio in Spanish, the audio in English and the available subtitles.

Considering also that a content has an arbitrary amount of metadata, I also decided to create the metadata as a separate model associated with a content and with a key:value format.

# Endpoints
## `/api/channels`
This endpoint returns a list of then main channels and their subchannels,  to access a subchannel I decide to use HyperLinked, i did this thinking on performance, since in this way the entire channel hierarchy is not returned, but it can be obtained dynamically.

### Filtering by group
You can use this endpoint also with filtering, if you add to the end the query param `?group={id}` returns all the filter channels

## `/api/channels/{id}`
This endpoint returns the detail info about a channel, using HyperLikend.

## `/api/content/{id}`
This endpoint returns the detail info about a content, in this case i decide all the file info and metadata, in the same endpoint, to avoid many requests.
