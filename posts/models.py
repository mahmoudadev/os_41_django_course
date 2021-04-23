from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Metric(models.Model):
    visits = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    ratio = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)


    def __str__(self):
        return f"{self.visits} visits | {self.likes} likes | ratio {self.ratio}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    author = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE, related_name="posts")
    categories = models.ManyToManyField(Category)
    metrics = models.OneToOneField(Metric, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)




    def __str__(self):
        return self.title