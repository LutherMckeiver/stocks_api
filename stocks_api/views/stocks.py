from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StockAPIViewset(APIViewSet):

    def retrieve(self, request, id):
        return Response(json={'message': 'Provided a single resource for id'})

    def list(self, request):  # GET?
        return Response(json={'message': 'Provided a lists of stocks'}, status=200)

    def create(self, request):  # POST
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request):  # DELETE
        return Response(json={'message': 'Deleted the record'}, status=204)
