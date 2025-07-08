from django.db import models
from django.utils import timezone
from typing import Optional


class SoftDeleteQuerySet(models.QuerySet):
    """
    Custom QuerySet for handling soft-deleted records.
    """

    def deleted(self) -> models.QuerySet:
        """
        Return only the soft-deleted records.

        Returns
        -------
        QuerySet
            A queryset containing only the soft-deleted records.
        """
        return self.filter(is_deleted=True)

    def restore_all(self) -> int:
        """
        Restore all soft-deleted records.

        Returns
        -------
        int
            The number of records restored.
        """
        return self.update(is_deleted=False, deleted_at=None)


class SoftDeleteManager(models.Manager):
    """
    Custom Manager for handling soft-deleted records.
    """

    def get_queryset(self) -> SoftDeleteQuerySet:
        """
        Return only non-deleted records by default.

        Returns
        -------
        SoftDeleteQuerySet
            A queryset containing only the non-deleted records.
        """
        return SoftDeleteQuerySet(self.model, using=self._db).filter(
            is_deleted=False
        )


class SoftDeleteModel(models.Model):
    """
    Abstract base model for implementing soft delete functionality.

    Attributes
    ----------
    is_deleted : bool
        Indicates whether the record is soft-deleted.
    deleted_at : datetime
        The timestamp when the record was soft-deleted.
    """

    is_deleted: bool = models.BooleanField(default=False)
    deleted_at: Optional[timezone.datetime] = models.DateTimeField(
        null=True, blank=True
    )

    # Manager for active (non-deleted) records
    active_objects: SoftDeleteManager = SoftDeleteManager()
    # Manager to access all records, including soft-deleted ones
    all_including_deleted_objects: models.Manager = models.Manager()

    def delete(
        self, using: Optional[str] = None, keep_parents: bool = False
    ) -> None:
        """
        Override the default delete method to implement soft delete.

        Parameters
        ----------
        using : Optional[str], optional
            The database alias to use.
        keep_parents : bool, optional
            Whether to keep parent records.
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self) -> None:
        """
        Restore the soft-deleted record.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = (
            True  # This model will not be used to create any database table
        )


# Example Concrete Model
class MyModel(SoftDeleteModel):
    """
    Example model that inherits from SoftDeleteModel.

    Attributes
    ----------
    name : str
        The name of the model instance.
    description : str
        A description of the model instance.
    """

    name: str = models.CharField(max_length=100)
    description: str = models.TextField()

    def __str__(self) -> str:
        """
        Return the string representation of the model instance.

        Returns
        -------
        str
            The name of the model instance.
        """
        return self.name
