from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserImpersonationMiddleware:
    """
    Middleware to allow user impersonation based on a cookie.
    
    This middleware allows an admin to impersonate another user by setting a cookie
    with the user's ID. The request's user object is replaced with the impersonated user.
    """
    
    def __init__(self, get_response):
        """
        Initialize the middleware with the given get_response callable.
        
        Parameters
        ----------
        get_response : callable
            The next middleware or view in the chain.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Handle the incoming request and replace the user object if impersonation is enabled.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the impersonate_user_id from the cookies
        impersonate_user_id = request.COOKIES.get('impersonate_user_id')
        if impersonate_user_id:
            # Replace the request's user object with the impersonated user
            request.user = get_object_or_404(User, id=impersonate_user_id)
        # Get the response from the next middleware or view
        response = self.get_response(request)
        return response
