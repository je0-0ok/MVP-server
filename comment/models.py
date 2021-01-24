from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length = 50, null = False)
    contents = models.CharField(max_length = 200, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "user_comment"