from django.urls import path, re_path
from .views import UnFriend, FriendBlock, FriendReject, FriendInvoke, FriendAdd#, Friends, Profile, MePagination, ProfilePagination, ME, Login, Logout, editProfile, passwordForgot, passwordReset, SignUp, Members, checkEmail#, checkUsername

urlpatterns = [
    path(r'add/', FriendAdd.as_view(), name='friend-add'),
    path(r'reject/', FriendReject.as_view(), name='friend-reject'),
    path(r'invoke/', FriendInvoke.as_view(), name='friend-invoke'),
    path(r'block/', FriendBlock.as_view(), name='friend-block'),
    path(r'unfriend/', UnFriend.as_view(), name='friend-unfriend'),
]
'''
    path('friends/', Friends, name='friends'), 
    #path(r'users/', all_users, name='friendship_view_users'),
    re_path('accept/(?P<friendship_request_id>\d+)/', friendship_accept, name='friendship_accept'),
    re_path('reject/(?P<friendship_request_id>\d+)/', friendship_reject, name='friendship_reject'),
    re_path('cancel/(?P<friendship_request_id>\d+)/', friendship_cancel, name='friendship_cancel'),
    path('requests/', friendship_request_list, name='friendship_request_list'),
    path('requests/rejected/', friendship_request_list_rejected, name='friendship_requests_rejected'),
    re_path('request/(?P<friendship_request_id>\d+)/', friendship_requests_detail, name='friendship_requests_detail'),
    re_path('followers/(?P<username>[\w-]+)/', followers, name='friendship_followers'),
    re_path('following/(?P<username>[\w-]+)/', following, name='friendship_following'),
    re_path('follower/add/(?P<followee_username>[\w-]+)/', follower_add, name='follower_add'),
    re_path('follower/remove/(?P<followee_username>[\w-]+)/', follower_remove, name='follower_remove'),
    re_path('blockers/(?P<username>[\w-]+)/', blockers, name='friendship_blockers'),
    re_path('blocking/(?P<username>[\w-]+)/', blocking, name='friendship_blocking'),
    re_path('block/add/(?P<blocked_username>[\w-]+)/', block_add, name='block_add'),
    re_path('block/remove/(?P<blocked_username>[\w-]+)/', block_remove, name='block_remove'),
try:
    from django.urls import path, re_path
except ImportError:
    from django.conf.urls.defaults import url
from .views import friends, friendship_add_friend, friendship_accept, \
    friendship_reject, friendship_cancel, friendship_request_list, \
    friendship_request_list_rejected, friendship_requests_detail, followers,\
    following, follower_add, follower_remove, all_users,block_add,block_remove,blockers,blocking
'''
