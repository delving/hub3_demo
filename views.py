from django.conf import settings
from django.shortcuts import render
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework_jsonp.renderers import JSONPRenderer

from nave.search.renderers import XMLRenderer
from nave.search.serializers import NaveQueryResponseWrapperSerializer
from nave.search.views import SearchListAPIView
from nave.base_settings import FacetConfig


def index(request):
    return render(template_name='index.html', request=request)


class DefaultSearchListAPIView(SearchListAPIView):
    """
    An APIView that for returning ES search results.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = NaveQueryResponseWrapperSerializer
    renderer_classes = (TemplateHTMLRenderer, BrowsableAPIRenderer, JSONRenderer, JSONPRenderer, XMLRenderer,
                        # rdf renders
                        # N3Renderer, JSONLDRenderer, RDFRenderer, NTRIPLESRenderer, TURTLERenderer
                        )

    index_name = settings.SITE_NAME
    doc_types = []
    template_name = "search/search-results.html"
    facets = [
        FacetConfig('dc_subject.raw', _("Subject")),
        FacetConfig('nave_technique.raw', _("Technique")),
        FacetConfig('nave_material.raw', _("Material")),
        FacetConfig('nave_collectionPart.raw', _("Collection")),
        FacetConfig('dc_type.raw', _("Object type")),
        ]
    filters = []


class NarthexRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        resolve_url = self.request.META["HTTP_HOST"].split(':')[0]
        return "http://{}/narthex".format(resolve_url)
