"""Utility functions for user-related operations."""
from functools import lru_cache

from user.models import User


@lru_cache(maxsize=1)
def get_deleted_user():
    """
    Get or create the special 'Deleted User' account.
    
    This user is used as a placeholder when a user account is deleted
    but their content (reviews, etc.) should be preserved.
    
    Cached to avoid repeated database queries.
    """
    user, _ = User.objects.get_or_create(
        email='deleted@truthfood.system',
        defaults={
            'name': 'Deleted User',
            'is_active': False,
        }
    )
    return user


def get_deleted_user_id():
    """Return the ID of the deleted user account."""
    return get_deleted_user().pk
