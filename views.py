from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model
from django.template import loader
from random import choice
from friend.models import Friendship
User=get_user_model()

class UnFriend(View):
	def post(self, request):
		userInfo=eval(request.body)
		me, fid=request.user, userInfo['fid']
		meQueryset=me.user_friendship.exclude(friend_id=fid).filter(friend_id__isnull=False)
		Friendship.objects.get(user=me, friend_id=fid).delete()
		Friendship.objects.get(user_id=fid, friend=me).delete()
		if meQueryset.exists():
			fid=meQueryset[0].friend_id
			tmpl=loader.get_template('friend-template.html')
			ctx=tmpl.render({'fid':fid})
			return JsonResponse({'unFriended':True, 'friendTemplate':ctx})
		return JsonResponse({'unFriended':True})

class FriendBlock(View):
	def post(self, request):
		me, fid=request.user, eval(request.body)['fid']
		meQueryset=me.user_friendship.exclude(friend_id=fid)
		meFS=me.user_friendship.get(friend_id=fid)
		meFS.friend_id, meFS.blocker_id=None, fid
		meFS.save()
		if meQueryset.exists():
			friends=meQueryset.filter(friend_id__isnull=False)
			friend=friends[0]
			tmpl=loader.get_template('friend-template.html')
			ctx=tmpl.render({'fid':friend.id})
			return JsonResponse({'UnFriended':True, 'friendTemplate':ctx})
		return JsonResponse({'friendBlocked':True})

class FriendReject(View):
	def post(self, request):
		userInfo=eval(request.body)
		me, iid, iids=request.user, userInfo['iid'], userInfo['iids']
		meFS=me.user_friendship.get(invoker_id=iid)
		meFS.delete()
		meQueryset=me.user_friendship.exclude(invoker_id__in=iids).filter(invoker_id__isnull=False)
		if meQueryset.exists():
			iid=meQueryset[0].invoker_id
			tmpl=loader.get_template('invoker-template.html')
			ctx=tmpl.render({'iid':iid})
			return JsonResponse({'friendRejected':True, 'invokerTemplate':ctx})
		return JsonResponse({'friendRejected':True})

class FriendAdd(View):
	def post(self, request):
		userInfo=eval(request.body)
		me, iid, iids=request.user, userInfo['iid'], userInfo['iids']
		meFS=me.user_friendship.get(invoker_id=iid)
		meFS.friend_id, meFS.invoker_id=iid, None
		meFS.save()
		Friendship.objects.create(user_id=iid, friend=me)
		meQueryset=me.user_friendship.exclude(invoker_id__in=iids).filter(invoker_id__isnull=False)
		if meQueryset.exists():
			invoker=meQueryset[0].invoker
			tmpl=loader.get_template('invoker-template.html')
			ctx=tmpl.render({'iid':invoker.id})
			return JsonResponse({'friendAdded':True, 'invokerTemplate':ctx})
		return JsonResponse({'friendAdded':True})

class FriendInvoke(View):
	def post(self, request):
		me, oid=request.user, eval(request.body)['oid']
		meFS=me.invoker_friendship.create(user_id=oid)
		#invoker, status=other.user_friendship.get_or_create(invoker=me)
		#me.user_friendship.filter(friend__isnull=False)
		OIDs=[fs.invoker_id for fs in me.user_friendship.filter(invoker__isnull=False)]
		OIDs+=[fs.friend_id for fs in me.user_friendship.filter(friend__isnull=False)]
		othersQueryset=User.objects.exclude(id__in=OIDs)
		if othersQueryset.exists():
			oid=othersQueryset[0].id
			tmpl=loader.get_template('other-template.html')
			ctx=tmpl.render({'oid':oid})
			return JsonResponse({'friendInvoked':True, 'otherTemplate':ctx})
		return JsonResponse({'friendInvoked':True})

'''
		friend=other.invoker_friend.create()
		me.friend_friend.add(friend)
		User.objects.exclude(id__in=ids)
		#invoker.invoker.add(me)
		#invoker.invoker.add(other)
		#other.invoker_friend.add(me)
class FriendBlock(View):
	def post(self, request):
		userInfo=eval(request.body)
		me, fid=request.user, userInfo['fid']
		meFS=me.user_friendship.get(friend_id=fid)
		meFS.blocker_id=fid
		meFS.friend_id=None
		meFS.save()
		return JsonResponse({'friendBlocked':True})

class UnFriend(View):
	def post(self, request):
		me, fid=request.user, eval(request.body)['fid']
		meFS=me.user_friendship.get(friend_id=fid)
		meFS.delete()
		return JsonResponse({'unFriended':True})
		#invokerFS, status=invoker.user_friendship.filter(friend=me).get_or_create()

class FriendReject(View):
	def post(self, request):
		userInfo=eval(request.body)
		me, iid, iids=request.user, userInfo['iid'], userInfo['iids']
		#invoker=User.objects.get(id=iid)
		meQueryset=me.user_friendship
		meFS=meQueryset.filter(invoker_id=iid).get()
		meFS.invoker_id=None
		meFS.save()
		#for iid in iids:
		#	invoker=User.objects.get(id=iid)
		#	meQueryset.exclude(invoker_id=iid)
		meQueryset.exclude(invoker_id__in=iids)
		invoker=choice(meQueryset.all())
		tmpl=loader.get_template('invoker-template.html')
		ctx=tmpl.render({'iid':invoker.id})
		return JsonResponse({'friendRejected':True, 'invokerTemplate':ctx})
		invokers=me.user_friendship.filter(invoker__isnull=False)
		meFS=me.user_friendship.get(friend_id=fid)
		meFS.friend_id, meFS.blocker_id=None, fid
		meQueryset=me.user_friendship
		other=User.objects.get(id=oid)
		friend=other.invoker_friend.create()
		me=request.user
		me.friend_friend.add(friend)
'''
