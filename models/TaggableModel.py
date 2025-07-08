from django.db import models


class Tag(models.Model):
    """
    Model representing a tag that can be associated with other models.

    Attributes
    ----------
    name : CharField
        The name of the tag, which must be unique.
    """

    name: models.CharField = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        """
        Return a string representation of the tag.

        Returns
        -------
        str
            The name of the tag.
        """
        return self.name


class TaggableModel(models.Model):
    """
    Abstract base model that provides tagging functionality.

    Attributes
    ----------
    tags : ManyToManyField
        A many-to-many relationship to the Tag model.
    """

    tags: models.ManyToManyField = models.ManyToManyField(
        Tag, related_name="tagged_items"
    )

    class Meta:
        abstract = (
            True  # This model will not be used to create any database table
        )


# Example Concrete Model
class MyModel(TaggableModel):
    """
    Concrete model that inherits from TaggableModel and adds additional fields.

    Attributes
    ----------
    name : CharField
        The name of the model instance.
    description : TextField
        A description of the model instance.
    """

    name: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField()
