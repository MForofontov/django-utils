from typing import Any
from django.db import models

class VersionedModel(models.Model):
    """
    Abstract base model that includes fields for tracking creation and update timestamps,
    as well as a version number that increments on each update.
    
    Attributes
    ----------
    created_at : DateTimeField
        The timestamp when the record was created.
    updated_at : DateTimeField
        The timestamp when the record was last updated.
    version : PositiveIntegerField
        The version number of the record, which increments on each update.
    """
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    version: models.PositiveIntegerField = models.PositiveIntegerField(default=1)

    class Meta:
        abstract = True  # This model will not be used to create any database table

# Example Concrete Model
class MyModel(VersionedModel):
    """
    Concrete model that inherits from VersionedModel and adds additional fields.
    
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
        Override the save method to increment the version number on each update.
        
        Parameters
        ----------
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        # Increment version on update
        if self.pk:
            self.version += 1
        super().save(*args, **kwargs)
