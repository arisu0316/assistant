from django.db import models

# Create your models here.
class Journal(model.Model):
    content = models.TextField("內容")
    created = models.DataField(auto_now_add=True)

    def __str__(self):
        return self.content
    