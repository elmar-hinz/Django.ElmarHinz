from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

import base.views

urlpatterns = [path('admin/', admin.site.urls),
               path('', base.views.index, name='index'),
               re_path(r'^docs/(?P<path>.*)', serve,
                       {'document_root': settings.DOCS_ROOT}),
               path('<name>', base.views.site, name='site'),
               ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.DOCS_URL, document_root=settings.DOCS_ROOT)
