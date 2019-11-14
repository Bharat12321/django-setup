"""Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
"""

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from . import api_urls

admin.site.site_title = admin.site.site_header = 'Auth Admin'

# Top Level Pages
# ==============================================================================
urlpatterns = [
]

urlpatterns += [

    # Rest API
    url(r'^api/', include(api_urls)),

    # Django Admin
    url(r'^{}/'.format(settings.DJANGO_ADMIN_URL), admin.site.urls),

]