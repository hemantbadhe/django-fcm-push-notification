from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from fcm_django.api.rest_framework import FCMDeviceViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'devices', FCMDeviceViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='FCM django web demo')),
    url(r'^api/', include(router.urls)),
    url(r'^$', index),
    url(r'^api/send_notification/', send_notification),
    url(r'^firebase-messaging-sw.js',
        TemplateView.as_view(template_name="firebase-messaging-sw.js", content_type='application/javascript', )),
    url(r'^manifest.json',
        TemplateView.as_view(template_name="manifest.json", content_type='application/json', )),
]
