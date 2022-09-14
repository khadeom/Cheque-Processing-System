from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import ChequeForm,CrispForm,VerifyForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Cheque,ChequeDetail
import time
from django.core.files import File
import json
from core.settings import get_BASE_DIR
from django.core import serializers


baseDir= get_BASE_DIR()

class Home(TemplateView):
    template_name = 'vision/home.html'

# Create your views here.
def base(request):
    return render(request, 'vision/base.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'vision/upload.html', context)


def home(request):
    cheques = Cheque.objects.all()
    return render(request, 'vision/home.html', {
        'cheques': cheques
    })

def upload_cheque(request):
    if request.method == 'POST':
        

        form = ChequeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = ChequeForm()

        return render(request, 'vision/uploadcheque.html',{"form":form})


def upload_cheque2(request):
    if request.method == 'POST':
        form = ChequeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            cheque = Cheque.objects.last()
            print("printting Cheque")
            print(cheque.title)
            print(cheque.cheque_image)
            # form2=ChequeForm()
            return render(request, 'vision/uploadcheque2.html',{"form":form,"cheque":cheque})

    else:
        form = ChequeForm()
        cheque = []
        return render(request, 'vision/uploadcheque2.html',{"form":form,"cheque":cheque})


def viewCheque(request):
    z=ChequeDetail()
    if request.method == 'POST':
        UCheque = CrispForm(request.POST, request.FILES)
        if UCheque.is_valid():
            z.cheque_image = UCheque.cleaned_data.get("cheque_image")
            print(request.POST.get('bank_name'))


            z.cheque_id = "chq_" + str(int(time.time()))

            request.sessions["cheque_id"] = z.cheque_id
            z.save()

        return render(request, "vision/uploadcheque3.html",{"cheque_image":z.cheque_image})
    return render(request, "vision/uploadcheque3.html",{"cheque_image":z.cheque_image})
    



def upload_cheque3(request):
    print("this is it and uploadcheque2")
    z=ChequeDetail()
    


    if request.method == "POST":
        UCheque = CrispForm(request.POST, request.FILES)
        if UCheque.is_valid():
            z.cheque_image = UCheque.cleaned_data.get("cheque_image")
            print(request.POST.get('bank_name'))

            z.cheque_id = "chq_" + str(int(time.time()))
            request.session["cheque_id"] = z.cheque_id
            z.bank_name = request.POST.get("bank_name")
            print(z.bank_name)
            z.language = request.POST.get("language")

            print(z.cheque_image.url)
            # print("****************************777777777778888888889999999999999**************************")
            # print(z.choosescript)
            z.save()

            return render(request, "vision/chequeProcess.html",{"cheque":z})


            # return render(request, "vision/showcheque.html",{'chequedetails':z})

        return render(request, 'vision/uploadcheque3.html')
        
    else:

        return render(request, 'vision/uploadcheque3.html')
from .ChequeOCR.scripts import OCR
# from chequeocr.ChequeOCR.scripts import OCR
from pprint import pprint
def chequeProcessing(request):
    print("this is it")
    cheque_image_url=request.GET['cheque_image']

    #sending cheque id through $ajx as a get request
    cheque_id= request.GET['cheque_id']
    print("cheque imae",cheque_image_url)

    try:
        print("type of image is",type(cheque_image_url))
        z={"cheque_id":cheque_id,'cheque_image_url':cheque_image_url,"bank_name":"ok","language":"English"}
        print(cheque_id)
        chequedetails = ChequeDetail.objects.get(cheque_id=cheque_id)

        print(chequedetails,'as before')
        


        cheque_url =chequedetails.cheque_image.url

        print(chequedetails.cheque_image.url)
        print("cheque image is",chequedetails.cheque_image)
        
        print("path of image is",str(baseDir) + cheque_url)
        image_path=str(baseDir) + cheque_url
        print("path of image is",image_path)


        # print(baseDir,"it is")
        print("doneee")
        cheque_details=OCR.cheque_ocr(image_path)
        # cheque_details={'PayeeName': 'PadabaD . Pradeep Kumar', 'AC/NO': '1130002010108841', 'IFSC': 'SYNB0003011', 'Amount': '8800000', 'Cheque MICR Number': 'DDD683651DDD 5666 D5633D 29666 2U'}

        pprint(cheque_details)

# AC/NO	IFSC	Amount	Cheque MICR Number	Signature

        chequedetails.PayeeName = cheque_details["PayeeName"]
        chequedetails.accNo = cheque_details["AC/NO"]
        chequedetails.ifsc = cheque_details["IFSC"]
        chequedetails.amount = cheque_details["Amount"]
        chequedetails.micr = cheque_details["Cheque MICR Number"]

        with open('/home/omkhade/chequeOCR/Bank-Cheque-OCR/ChequeProcessing/vision/ChequeOCR/feilds/signature.jpg', 'rb') as f:   # use 'rb' mode for python3
            data = File(f)
            chequedetails.signature.save(cheque_id+"signature.jpg", data,True)


        with open('/home/omkhade/chequeOCR/Bank-Cheque-OCR/ChequeProcessing/vision/ChequeOCR/feilds/payee.jpg', 'rb') as f:   # use 'rb' mode for python3
            data = File(f)
            chequedetails.payee_img.save(cheque_id+"payee.jpg", data,True)
        with open('/home/omkhade/chequeOCR/Bank-Cheque-OCR/ChequeProcessing/vision/ChequeOCR/feilds/ac_no.jpg', 'rb') as f:   # use 'rb' mode for python3
            data = File(f)
            chequedetails.accNo_img.save(cheque_id+"ac_no.jpg", data,True)
        with open('/home/omkhade/chequeOCR/Bank-Cheque-OCR/ChequeProcessing/vision/ChequeOCR/feilds/ifsc.jpg', 'rb') as f:   # use 'rb' mode for python3
            data = File(f)
            chequedetails.ifsc_img.save(cheque_id+"ifsc.jpg", data,True)

        with open('/home/omkhade/chequeOCR/Bank-Cheque-OCR/ChequeProcessing/vision/ChequeOCR/feilds/Amount/padded_amount.jpg', 'rb') as f:   # use 'rb' mode for python3
            data = File(f)
            chequedetails.amount_img.save(cheque_id+"amount.jpg", data,True)
        with open('/home/omkhade/chequeOCR/Bank-Cheque-OCR/ChequeProcessing/bottom.jpg', 'rb') as f:   # use 'rb' mode for python3
            data = File(f)
            chequedetails.micr_img.save(cheque_id+"micr.jpg", data,True)
        
        


        chequedetails.save()

        chequeinfo = serializers.serialize('json',[chequedetails]) # pass as a list to serialize
        # =serializers.serialize("json", Person.objects.all())

        context = {
                    "status": "success",
                    
                    
                }
        return JsonResponse(context)
    except Exception as e:
        print(e)
        context={"status": "Error"}

        return JsonResponse({},status=500)

    # return render(request, "vision/showcheque.html",{'chequedetails':z})
def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})
def done(request):
    cheque_details=ChequeDetail.objects.get(cheque_id=request.session.get('cheque_id'))
    form = VerifyForm(instance=cheque_details)
    if request.method == 'POST':
        form= VerifyForm(request.POST,instance=cheque_details)
        if form.is_valid():
            form.save()
            return redirect('cheque_upload3')
        else:
            form= VerifyForm(instance=cheque_details)


    return render(request,"vision/checkverify.html",{'form':form, 'cheque_details':cheque_details})



    
    





    return render(request, "vision/showcheque.html",{'chequedetails':cheque_details})
    



def viewAll(request):

    pass




def chequeProcessingBACKUP(request):
    print("this is it")
    cheque_image_url=request.GET['cheque_image']
    print("cheque imae",cheque_image)

    

    try:
        print("type of image is",type(cheque_image))
        z={'cheque_image_url':cheque_image_url,"bank_name":"ok","language":"English"}

        
        context = {
                    "status": "success",
                }
        return JsonResponse(context)
    except Exception as e:
        print(e)
        context={"status": "Error"}

        return JsonResponse({},status=500)

    return render(request, "vision/showcheque.html",{'chequedetails':z})




    
# /home/omkhade/chequeOCR/Bank-Cheque-OCR/ChequeProcessing/vision/templates/vision/uploadcheque.html



