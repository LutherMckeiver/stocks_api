from pyramid_restful.routers import ViewSetRouter
from .views.portfolio import StockAPIViewset
from .views.company import CompanyAPIViewset
from .views.auth import AuthAPIViewset


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('lookup', 'api/v1/lookup/{symbol}')

    router = ViewSetRouter(config)
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/stock', StockAPIViewset, 'stock')
    router.register('api/v1/auth/{auth}', AuthAPIViewset, 'auth')

