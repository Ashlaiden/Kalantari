# from django.db import models
# from django.core.files.storage import FileSystemStorage
#
# # Define a custom storage system that can save files in a specific directory
# fs = FileSystemStorage(location='my_project/my_app')
#
# # Define a model that has a file field and a code field
# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     file = models.FileField(storage=fs)  # uses the custom storage system
#     code = models.TextField()  # or models.JSONField()
#
#     def save(self, *args, **kwargs):
#         # Override the save method to write the code to the file
#         with open(self.file.path, "w") as f:
#             f.write(self.code)
#         super().save(*args, **kwargs)
