# python-django-backend
my python django restfull api backend

Django settings for static assets can be a bit difficult to configure and debug. However, if you just add the following settings to your settings.py, everything should work exactly as expected:

settings.py

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
See a full version of our example settings.py on GitHub.

Django won’t automatically create the target directory (STATIC_ROOT) that collectstatic uses, if it isn’t available. You may need to create this directory in your codebase, so it will be available when collectstatic is run. Git does not support empty file directories, so you will have to create a file inside that directory as well.

Whitenoise
Django does not support serving static files in production. However, the fantastic WhiteNoise project can integrate into your Django application, and was designed with exactly this purpose in mind.

See the WhiteNoise documentation for more details.

Installing Whitenoise

First, install WhiteNoise with pipenv:

pipenv install whitenoise
Adding whitenoise to Pipfile's [packages]...
Next, install WhiteNoise into your Django application. This is done in settings.py’s middleware section (at the top):

settings.py

MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
Finally, if you’d like gzip functionality enabled, also add the following setting to settings.py.

settings.py

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
Your application will now serve static assets directly from Gunicorn in production. This will be perfectly adequate for most applications, but top-tier applications may want to explore using a CDN with Django-Storages.

Collectstatic during builds
When a Django application is deployed to Heroku, $ python manage.py collectstatic --noinput is run automatically during the build. A build will fail if the collectstatic step is not successful.

Debugging
If collectstatic failed during a build, a traceback was provided that will be helpful in diagnosing the problem. If you need additional information about the environment collectstatic was run in, use the DEBUG_COLLECTSTATIC configuration.

heroku config:set DEBUG_COLLECTSTATIC=1
This will display in your build output all of the environment variables that were available to Python when the collectstatic command was executed.

Disabling Collectstatic
Sometimes, you may not want Heroku to run collectstatic on your behalf. You can disable the collectstatic build step with the DISABLE_COLLECTSTATIC configuration:

heroku config:set DISABLE_COLLECTSTATIC=1
This will fully disable the collectstatic step of the build.
