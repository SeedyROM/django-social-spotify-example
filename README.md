# django-social-spotify-example

## Files of interest:
* `spotify_test/settings.py`
  * This is where most of the configation has occured, copy this if need be.
  * All `TODO: *` blocks are places where the initial configuration has been altered! Search for them with your favorite text editors.
* `spotify_test/urls.py`
  * Where we create our OAuth callback urls and some test routes.
* `core/decorators.py`
  * The `@spotify_view` decorator is defined here which refreshes an instance of an OAuth token and passes it to the view.
  * It also checks if the user is authenticated!
* `info/views.py`
  * 2 Views to display how it works.
  * Super simple!

## Installation Instructions:

* Create a .env file in the root project directory and include your spotify keys.
  * Follow the .env.example template for more information.
* Run `python manage.py migrate`
* Run `python manage.py runserver`
