# fcm-django-web-demo

Quick demo to demonstrate the use of firebase web push notifications with the use of `javascript` on frontend, `django` on backend and push notifications via `fcm-django` pypi package for django.

## Quick start

### prerequisites
- in `fcm-django-web-demo`:
  - create virtual environment with `virtualenv -p python3 <venv name>` Python 3
  - activate virtual environment with `. env/bin/activate`
  - install necessary Python packages with `pip install -r updated_requirements.txt`
  - add the senderId, APIkey etc, in index.html
  - add senderId in manifest.json & firebase-messaging-sw.js file
  - add Server key as FCM_SERVER_KEY in settings file
### backend
- in `fcm-django-web-demo/mysite`:
  - run database migrations with `python manage.py migrate`
  - create Django administrator with `python manage.py createsuperuser`
  - collect static files with `python manage.py collectstatic`
  - run server with `python manage.py runserver 0.0.0.0:8000`.

### how to use
- open http://localhost:8000 in your browser of choice
- request token and allow firebase to send notifications to your browser (device)
- you should now be seeing your instance id token on the aforementioned URL
- if you go to django admin, http://localhost:8000/admin/fcm_django/fcmdevice/, you should be seeing a FCMDevice instance for your browser
- send yourself a test notification with django admin actions
  - shell example (run `python manage.py shell` from `fcm-django-web-demo/mysite`):
    ```python
	   from fcm_django.models import FCMDevice
	   device = FCMDevice.objects.all().first()
	   device.send_message(title='title', body='message')
    ```
- voila :)

### using Postman
- URL: https://fcm.googleapis.com/fcm/send
- Type: POST
- Header
	Authorization: key=<server key>
- Request Body:
	{
	  "notification": {
		"title": "<notification title>",
		"body": "<notifiction body>",
		"icon": "firebase-icon.png",
		"click_action": "http://localhost:8081"
	  },
	  "to": "<target device token>"
	}

### fcm-django DRF API URL docs demo

- available via `coreapi` and `djangorestframework` pypi packages, can be accessed at http://localhost:8000/docs
