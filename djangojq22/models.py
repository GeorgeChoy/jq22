from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from PIL import Image

# Create your models here.
#save the profile picture to dynamically created category id directory in media/images
def upload_to( filename):
    return 'images/category/%s' % ( filename)

class Category(models.Model):
    name=models.CharField(max_length=128,unique=True)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    slug=models.SlugField(unique=True)
    picture = models.ImageField( default='images/default.jpg')
#    picture = models.ImageField()
    def get_absolute_url(self):
        #return "/jqapp/category/%s/" %(self.slug)
        return reverse('djangojq22:index', kwargs={'cslug': self.slug})

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Thumbnail(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    thumbpic=models.ImageField( default='images/default.jpg')
    def __str__(self):
        return (self.category.name)

###Abstract base class example
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=False)
    class Meta:
        abstract = True
        ordering = ['name']
    def __str__(self):
        return self.name

##Inherits from CommonInfo parent class but over loads the Meta class so it orders by dob instead of name
class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
    class Meta(CommonInfo.Meta):
        ordering = ['dob']

class FinalStudent(Student):
    class Meta:
        proxy=True
    def __str__(self):
        return self.home_group