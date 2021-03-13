from django.db import models

# Create your models here.



class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name # {Group.objects.get(id=self.group_id).name}

class Snippet(models.Model):
    body = models.TextField(max_length=1000)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.body
