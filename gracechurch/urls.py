from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^gracechurch/', include('gracechurch.foo.urls')),
    (r'^admin/treemenus/', include('treemenus.admin_urls')),
    # Uncomment this for admin:
     (r'^admin/', include('django.contrib.admin.urls')),
)
