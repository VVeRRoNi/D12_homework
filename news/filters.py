from django_filters import FilterSet
from .models import Post


class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            "dateCreation": ["gt"],
            "author": ["gt"],
            "title": ["icontains"],
        }
