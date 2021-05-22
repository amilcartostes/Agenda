'''
CONTACT FIELDS
name: STR * (Mandatory )
surname: STR (Optional)
telephone: STR * (Mandatory )
email: STR (Optional)
creation_date: DATETIME (Automatic)
description: TEXT
category: CATEGORY (outro model)

CATEGORY
name: STR * (Mandatory )
'''

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    # Changing the form of representation of the fields of the Category model
    def __str__(self):
        return self.name


class Contact(models.Model):  # models.Model - Inherits models from the Model class

    # Create the contact fields in the database.
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True)  # blank=True informs that the field is optional
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    creation_date = models.DateTimeField(auto_now_add=False)
    description = models.TextField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)  # What to do if a category is deleted
    show = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%d")  # Image field - By default it can be empty

    # Changing the form of representation of the fields of the Category model
    def __str__(self):
        return self.name