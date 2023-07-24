from django import template
from blog.models import Post

register = template.Library()
@register.inclusion_tag('blog/lasts_post.html')
def lastest_post():
    context = {
        'l_posts': Post.objects.all().order_by("?")[0:6]
    }
    return context
