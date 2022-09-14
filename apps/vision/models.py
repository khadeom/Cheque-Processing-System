from django.db import models
import uuid


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255,blank=True)
    email = models.EmailField(max_length=255,blank=True)
    test = models.BooleanField(default=False)
    

class Cheque(models.Model):
    uuid = models.UUIDField(
        max_length=36, primary_key=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=255,    blank=True)
    bank = models.CharField( max_length=50, blank=True)
    cheque_image = models.ImageField(upload_to='cheques/',blank=True)

    def __str__(self):
        return self.title

class ChequeDetail(models.Model):
    uuid = models.UUIDField(
        max_length=36, primary_key=True, default=uuid.uuid4, editable=False
    )
    test= models.CharField(max_length=50, blank=True)
    cheque_id = models.CharField(max_length=255,default=None)
    cheque_image = models.ImageField(upload_to='cheques/',blank=True)
    language = models.CharField(max_length=50, blank=True)
    bank_name = models.CharField(max_length=50, blank=True)
# AC/NO	IFSC	Amount	Cheque MICR Number	Signature

    PayeeName = models.CharField(max_length=50, blank=True)
    accNo = models.CharField(max_length=50,blank=True)
    amount = models.CharField(max_length=50,blank=True)   
    micr = models.CharField(max_length=50, blank=True)  
    ifsc = models.CharField(max_length=50, blank=True)

    payee_img = models.ImageField(upload_to='cheques/payee',blank=True)
    accNo_img = models.ImageField(upload_to='cheques/accNo',blank=True)
    ifsc_img = models.ImageField(upload_to='cheques/ifsc',blank=True)
    amount_img = models.ImageField(upload_to='cheques/ammount',blank=True)
    micr_img = models.ImageField(upload_to='cheques/micr',blank=True)
    signature = models.ImageField(upload_to='cheques/signature',blank=True)




    def __str__(self):
        # return self.bank_name
        return 'self.bank_name'