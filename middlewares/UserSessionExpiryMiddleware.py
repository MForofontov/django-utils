from django.utils import timezone
from django.contrib.auth import logout
from django.conf import settings

class UserSessionExpiryMiddleware:
    """
    Middleware to handle user session expiry based on inactivity.
    
    This middleware logs out users if they have been inactive for a period longer
    than the session timeout defined in the settings.
    """
    
    def __init__(self, get_response):
        """
        Initialize the middleware with the given get_response callable and session timeout.
        
        Parameters
        ----------
        get_response : callable
            The next middleware or view in the chain.
        """
        self.get_response = get_response
        self.session_timeout = settings.SESSION_COOKIE_AGE  # in seconds

    def __call__(self, request):
        """
        Handle the incoming request and log out the user if the session has expired.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        if request.user.is_authenticated:
            # Get the last activity time from the session
            last_activity = request.session.get('last_activity')
            if last_activity:
                # Check if the session has expired
                if (timezone.now() - last_activity).total_seconds() > self.session_timeout:
                    # Log out the user if the session has expired
                    logout(request)
            # Update the last activity time in the session
            request.session['last_activity'] = timezone.now()
        # Get the response from the next middleware or view
        response = self.get_response(request)
        return response
