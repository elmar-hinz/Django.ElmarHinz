import django_challenges_adapter.urls
import django_education_certificates.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import base.views

urlpatterns = [path('admin/', admin.site.urls),
               path('challenges/', include(django_challenges_adapter.urls)),
               path('', base.views.index, name='index'),
               path('certificates/',
                    include(django_education_certificates.urls)),
               path('<name>.html', base.views.site, name='site'),
               ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.DOCS_URL, document_root=settings.DOCS_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
