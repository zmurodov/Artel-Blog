from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ACCOUNT_STATUS = (
        ('active', 'Active'),
        ('blocked', 'Blocked')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    account_status = models.CharField(max_length=10, choices=ACCOUNT_STATUS, blank=True)
    about = models.TextField(max_length=254, blank=True)
    follows = models.ManyToManyField('self', related_name='profile_follows', symmetrical=False)

    # birth_date = models.DateField(blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

#
# class Follower(models.Model):
#     follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)  # who follows
#     following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)  # who is followed
#     follow_time = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('follower', 'following')
#
#     def __unicode__(self):
#         return u'%s follows %s' % (self.follower, self.following)
#

# User.add_to_class('following',
#                   models.ManyToManyField('self', through=Follower, related_name='followers', symmetrical=False))
