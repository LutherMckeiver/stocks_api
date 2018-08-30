from pyramid_restful.routers import ViewSetRouter
from .views import CompanyAPIViewset, StockAPIViewset
from .views.auth import AuthAPIViewSet


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config, trailing_slash=False)
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/stocks', StockAPIViewset, 'stocks')
    router.register('api/v1/auth{auth}', AuthAPIViewSet, 'auth')
