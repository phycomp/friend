from django.db.models import ForeignKey, ManyToManyField, CASCADE, Model, DateTimeField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
AUTH_USER_MODEL=settings.AUTH_USER_MODEL

class Friendship(Model):
	user=ForeignKey(AUTH_USER_MODEL, related_name='user_friendship', on_delete=CASCADE)
	invoker=ForeignKey(AUTH_USER_MODEL, related_name='invoker_friendship', on_delete=CASCADE, null=True)
	friend=ForeignKey(AUTH_USER_MODEL, related_name='friend_friendship', on_delete=CASCADE, null=True)
	blocker=ForeignKey(AUTH_USER_MODEL, related_name='blocker_friendship', on_delete=CASCADE, null=True)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	class Meta:
		db_table='friendship'

'''
class Invoker(Model):
	user=ForeignKey(settings.AUTH_USER_MODEL, related_name='user_friend', on_delete=CASCADE)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	class Meta:
		db_table='friend'

class Blocker(Model):
	user=ForeignKey(settings.AUTH_USER_MODEL, related_name='user_blocker', on_delete=CASCADE)
	class Meta:
		db_table='blocker'
'''
