from django.core.files.storage import FileSystemStorage
from django.db import models


class FileStorageModel(models.Model):
    """
    Model for storing uploaded files using a custom file system storage.

    Attributes
    ----------
    uploaded_file : FileField
        The file that is uploaded by the user.
    """

    # Define a custom file system storage
    file_storage: FileSystemStorage = FileSystemStorage(
        location="/path/to/media"
    )

    # Use the custom file storage for the uploaded_file field
    uploaded_file: models.FileField = models.FileField(
        upload_to="uploads/", storage=file_storage
    )

    def get_file_url(self) -> str:
        """
        Get the URL of the uploaded file.

        Returns
        -------
        str
            The URL of the uploaded file.
        """
        return self.uploaded_file.url

    def __str__(self) -> str:
        """
        Return a string representation of the uploaded file.

        Returns
        -------
        str
            The name of the uploaded file.
        """
        return self.uploaded_file.name
