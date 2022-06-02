from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(DomainEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userProfile')
    name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    board = models.CharField(max_length=100, blank=True, null=True)
    ssc_passing_year = models.DateField(blank=True, null=True)
    hsc_passing_year = models.DateField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)

    def __str__(self):
        return self.user.email


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)
        return profile


post_save.connect(create_user_profile, sender=User)
