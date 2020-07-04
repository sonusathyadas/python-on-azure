from django.db import models
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=10, null=False)
    fax = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        """Return the string representation """
        return f"""Name={self.name}\n
                Email={self.email}\n
                Mobile={self.mobile}\n
                Fax={self.fax}"""

    # save(self, *args, **kwargs):
    #     if(settings.DEBUG):
    #         storage_helper = StorageHelper(settings.STORAGE_CONNECTION_STRING)
    #         storage_helper.create_container(settings.STORAGE_CONTAINER)
    #         storage_helper.upload_blob(self.image)
    #     super(Contact,self).save(*args, **kwargs)