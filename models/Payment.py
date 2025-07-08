from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    """
    Model representing a payment made by a user.
    
    Attributes
    ----------
    user : ForeignKey
        The user who made the payment.
    amount : DecimalField
        The amount of the payment.
    payment_date : DateTimeField
        The date and time when the payment was made.
    payment_method : CharField
        The method used for the payment.
    """
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    amount: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    payment_method: models.CharField = models.CharField(max_length=50)

    def __str__(self) -> str:
        """
        Return a string representation of the payment.
        
        Returns
        -------
        str
            A string describing the payment details.
        """
        return f"Payment of {self.amount} by {self.user.username} on {self.payment_date}"
