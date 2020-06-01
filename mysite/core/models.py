from django.db import models


class Po(models.Model):
    order = models.CharField(max_length=100, null=True, blank=True)
    style = models.CharField(max_length=100,null=True, blank=True)
    quantity = models.CharField(max_length=100,null=True, blank=True)
    country =models.CharField( max_length=100,null=True, blank=True)

    XXS = models.CharField(max_length=100, null=True, blank=True)
    XS = models.CharField(max_length=100, null=True, blank=True)
    S = models.CharField(max_length=100, null=True, blank=True)
    M = models.CharField(max_length=100, null=True, blank=True)
    L = models.CharField(max_length=100, null=True, blank=True)
    XL = models.CharField(max_length=100, null=True, blank=True)
    XXL = models.CharField(max_length=100, null=True, blank=True)
    XXXL = models.CharField(max_length=100, null=True, blank=True)
    total = models.CharField(max_length=100, null=True, blank=True)
    
    
   

    #date =models.DateField(null=True, blank=True)
    pdf = models.FileField(upload_to='pos/pdfs/')
    #csv = models.FileField(upload_to='pos/csv/')
    choice =(('BestSeller','BestSeller'),
    ('TomTailor','TomTailor'),
    ('TomyHill', 'TomyHill'),
    ('Espirit', 'Espirit'))
    choose = models.CharField(max_length = 100, choices=choice)
    #cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.choose

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        #self.cover.delete()
        super().delete(*args, **kwargs)


    
# class Po_size(models.Model):
#     csv = models.FileField(upload_to='pos/csv/')
#     XXS = models.CharField(max_length=100, null=True, blank=True)
#     XS = models.CharField(max_length=100, null=True, blank=True)
#     S = models.CharField(max_length=100, null=True, blank=True)
#     M = models.CharField(max_length=100, null=True, blank=True)
#     L = models.CharField(max_length=100, null=True, blank=True)
#     XL = models.CharField(max_length=100, null=True, blank=True)
#     XXL = models.CharField(max_length=100, null=True, blank=True)
#     XXXL = models.CharField(max_length=100, null=True, blank=True)
#     total = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return self.total

