from django.db import models


class Timestamps(models.Model):
    """
    Base model for timestamp fields
    """

    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedBy(models.Model):
    """
    Base model for created_by field
    """

    created_by = models.ForeignKey(
        "user.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        abstract = True
