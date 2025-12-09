from django.db import models

from user.utils import get_deleted_user_id


class Review(models.Model):
    """
    Model representing a review for a food item.
    """
    user = models.ForeignKey(
        'user.User',
        on_delete=models.SET_DEFAULT,
        default=get_deleted_user_id,
        related_name='reviews'
    )
