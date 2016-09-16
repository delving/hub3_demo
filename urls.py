from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from nave.search.urls import router
from .views import NarthexRedirectView

urlpatterns = patterns(
    '',
    # static homepage - remove if CMS active
    url(r'^$', 'views.index'),
    # api is loaded here so custom api can be added at the settings level
    url(r'api/', include(router.urls)),
    url(r'narthex/', NarthexRedirectView.as_view()),
    #url(r'search', FacettedSearchView.as_view()),
)
