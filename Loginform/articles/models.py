from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later
    # char поменьше
    # text текс больше

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
        # делается что бы были покороче предложения при обзоре