from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    """
    Model representing a subscription for a user.
    
    Attributes
    ----------
    user : ForeignKey
        The user who owns the subscription.
    start_date : DateTimeField
        The date and time when the subscription starts.
    end_date : DateTimeField
        The date and time when the subscription ends.
    is_active : BooleanField
        Indicates whether the subscription is currently active.
    """
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    end_date: models.DateTimeField = models.DateTimeField()
    is_active: models.BooleanField = models.BooleanField(default=True)

    def __str__(self) -> str:
        """
        Return a string representation of the subscription.
        
        Returns
        -------
        str
            The username of the user and the subscription status.
        """
        return f"{self.user.username} - {'Active' if self.is_active else 'Inactive'}"
