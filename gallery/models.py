from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Location(models.Model):
    place = models.TextField()

    def __str__(self):
        return self.place
 
class Image(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    photoimage = models.ImageField(upload_to ="galleryimages/")

    def __str__(self):
        return self.name 

    def save_image(self):
        self.save()

    def delete_image():
        self.delete()

    def update_image():
        self.update()

    def get_image_by_id(id):
        self.get()

    def search_image(category):
        self.search()
   
    def filter_by_location(location):
        self.filter()

    @classmethod
    def search_category(cls,category):
        found_category = Category.objects.filter(name__icontains = category)[0]
        return cls.objects.filter(category_id = found_category.id)