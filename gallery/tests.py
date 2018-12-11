from django.test import TestCase
from .models import Image, Category, Location


# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category = Category(name = 'sports')
        self.location = Location(place = 'USA')
        self.photo = Image(name = 'danmark',description ='The best sports Events of all time',location = self.location,category = self.category,photoimage = 'galleryimages/images1.jpeg')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Image))


    # Testing Save Method
    def test_save_method(self):
        self.photo.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0 )


    #Testing delete method
    def test_delete_method(self):
        self.photo.save_image()
        self.photo.delete_image()


    #Testing update
    def test_update_method(self):
        self.photo.save_image()
        new_photo = Image.objects.filter().update()
        photos = Image.objects.get()
        self.assertTrue(photos)



    # Testing getting image by id
    def test_get_image_by_id(self):
        self.photo.save_image()
        picture =self.photoimage.get_image_by_id(self.photoimage.id)
        photoimage = Image.objects.get(id =self.photoimage.id)
        self.assertTrue(picture,photoimage)


    #Test filter
    def test_filter_by_location(self):
        self.photo.save_image()
        picture = self.photoimage.filter_by_location(self.Image.location)
        photo = Image.objects.filter(location = self.Image.location)
        self.assertTrue(picture,photo)

