from django.db import models

# Create your models here.
class Category(models.Model):

    # CharField, a field for storing character data (e.g. strings). 
    # Specify max_length to provide a maximum number of characters that a CharField field can store.
    name = models.CharField(max_length=128, unique=True)

    # For each field, you can specify the unique attribute. 
    # If set to True, the given field’s value must be unique 
    # throughout the underlying database table that is mapped to the associated model.

    # typo within the admin interface (Categorys, not Categories). This typo can be fixed
    class Meta:
        verbose_name_plural = 'Categories'

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    # CASCADE instructs Django to delete the pages associated with the category when the category is deleted.

    title = models.CharField(max_length=128)

    # URLField, much like a CharField, but designed for storing resource URLs. 
    # You may also specify a max_length parameter.
    url = models.URLField()

    # IntegerField, which stores integers.
    views = models.IntegerField(default=0)

    def __str__(self): 
        return self.title