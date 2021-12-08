from django.contrib.sitemaps import Sitemap
from .models import Post

# A class for sitemaps to help make page ranking high
class PostSitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.9

	def items(self):
		return Post.published.all()

	def lastmod(self, obj):
		return obj.updated