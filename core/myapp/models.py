# Python code
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

class Like(models.Model):

    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Listed below are the mandatory fields for a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

class Post(models.Model):
    
    likes = GenericRelation(Like)

class Page(models.Model):
    
    likes = GenericRelation(Like)

class Comment(models.Model):
    
    likes = GenericRelation(Like)




# class Post(models.Model):
#     posted_by = models.ForeignKey(User ,on_delete=models.CASCADE)
#    # likes = GenericRelation(Like, related_query_name='post'))

# >>> import os;
# >>> os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings';
# >>> import django;
# >>> django.setup();
# >>> from app.models import MyClass;