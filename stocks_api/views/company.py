from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIViewset(APIViewSet):
    def retrieve(self, request, id=None):
        """
        This will show the endpoint for this API, and then send a message back to the client.
        """
        return Response(
            json={'message': 'Provided a single resource'},
            status=200
        )
