from django.conf.urls import url
from .noyon_view import NoyonView
from .noyon_view import Noyon2View
from .noyon_view import Noyon3View
from .noyon_view import Noyon4View

urlpatterns = [
    url(r'^noyon/$', NoyonView.as_view(), name='noyon'),
    url(r'^noyon2/$', Noyon2View.as_view(), name='noyon2'),
    url(r'^noyon3/$', Noyon3View.as_view(), name='noyon3'),
    url(r'^noyon4/$', Noyon4View.as_view(), name='noyon4'),
]