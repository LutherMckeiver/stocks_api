from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIViewset(APIViewSet):
    def retrieve(self, request, id=None):

        return Response(json={'message': 'Provided a single resource for id'})
