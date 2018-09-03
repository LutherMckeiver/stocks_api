from pyramid.response import Response
from pyramid.view import forbidden_view_config, notfound_view_config


@forbidden_view_config()
def forbidden(request):
    """
    If a user is not recognized by the system, sends a 403 error message.
    """
    return Response(json='Forbidden', status=403)


@notfound_view_config()
def not_found(request):
    """
    If the user is not found in the database, sends out a 404 error message.
    """
    return Response(json='Not Found', status=404)
