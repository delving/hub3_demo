from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from nave.search.urls import router
from .views import NarthexRedirectView, index

urlpatterns = [
    # static homepage - remove if CMS active
    url(r'^$', index),
    # api is loaded here so custom api can be added at the settings level
    url(r'api/', include(router.urls)),
    url('', include('nave.diw.urls')),
    url(r'narthex/', NarthexRedirectView.as_view()),
    #url(r'search', FacettedSearchView.as_view()),
]
