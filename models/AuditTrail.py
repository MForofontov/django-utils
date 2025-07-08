from typing import Any
from django.db import models


class AuditTrail(models.Model):
    """
    Model to keep track of actions performed on other models.

    Attributes
    ----------
    action : CharField
        The action performed (e.g., 'create', 'delete').
    model_name : CharField
        The name of the model on which the action was performed.
    object_id : PositiveIntegerField
        The ID of the object on which the action was performed.
    timestamp : DateTimeField
        The timestamp when the action was performed.
    """

    action: models.CharField = models.CharField(max_length=50)
    model_name: models.CharField = models.CharField(max_length=100)
    object_id: models.PositiveIntegerField = models.PositiveIntegerField()
    timestamp: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]  # Order by timestamp in descending order


class MyModel(models.Model):
    """
    Example model that uses the AuditTrail to track create and delete actions.

    Attributes
    ----------
    name : CharField
        The name of the model instance.
    description : TextField
        A description of the model instance.
    """

    name: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField()

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Override the save method to create an audit trail entry on creation.

        Parameters
        ----------
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        super().save(*args, **kwargs)
        # Create an audit trail entry for the 'create' action
        AuditTrail.objects.create(
            action="create",
            model_name=self.__class__.__name__,
            object_id=self.id,
        )

    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Override the delete method to create an audit trail entry on deletion.

        Parameters
        ----------
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        # Create an audit trail entry for the 'delete' action
        AuditTrail.objects.create(
            action="delete",
            model_name=self.__class__.__name__,
            object_id=self.id,
        )
        super().delete(*args, **kwargs)
