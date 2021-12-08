# import django libraries
from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

# to display the total number of posts in the side bar
@register.simple_tag
def total_posts():
	return Post.published.count()

# to display all recent posts at the side bar
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = Post.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}

# to display most commented posts
@register.simple_tag
def get_most_commented_posts(count=5):
	return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

# make markdowns to convert texts to HTMLs tags
@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))