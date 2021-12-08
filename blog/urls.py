from django.urls import path
from . import views
from .feeds import LatestPostsFeed
# from django.contrib import admin


# All urls will be saved here

app_name = 'blog'  # name of blog

# A list of all urls
urlpatterns = [
	# post views
	path('', views.post_list, name='post_list'),
	# path('', views.PostListView.as_view(), name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
		views.post_detail, name='post_detail'),
	path('<int:post_id>/share/', views.post_share, name='post_share'),
	# to list posts by tag
	path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
	# to get recent feeds
	path('feed/', LatestPostsFeed(), name='post_feed'),
	path('search/', views.post_search, name='post_search'),
	path('contact', views.contact_form, name='contact'),
]