from django.conf.urls import url
from .jabin_view import JabinView,JabinView2,JabinView3

urlpatterns = [
    url(r'^jabin/$', JabinView.as_view(), name='jabin'),
    url(r'^jabin2/$', JabinView2.as_view(), name='jabin2'),
    url(r'^jabin3/$', JabinView3.as_view(), name='jabin3'),
 ]