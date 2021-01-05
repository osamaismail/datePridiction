from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *
from datetime import datetime, timedelta
import pandas as pd




def index(request):
    qs = DataEntery.objects.all().values()
    data_df = pd.DataFrame(qs).rename({'infected':'No of Infected','infectedDate':'Infected Date'}, axis=1).drop(['id','created'], axis=1)
    # print(data_df)
    context = {'data': data_df.to_html()}
    template = 'analystic/index.html'
    return render(request, template, context)

def inputData(request):
    if request.method == 'POST':
        dataForm = DataInputForm(request.POST)
        if dataForm.is_valid():
            dataForm.save()
            messages.success(request,'Data has been added')
            return redirect('home')
    else:
        dataForm = DataInputForm()
    context = {'form': dataForm}
    template = 'analystic/enter_data.html'
    return render(request, template, context)

## Get Results

def is_valid_queryparam(param):
    return param != '' and param is not None

def searchResults(request):
    qs = DataEntery.objects.all()
    zeroDate= request.GET.get('date')
    numberOfDays = request.GET.get('days')
    resu = []
    res = {}
    if is_valid_queryparam(zeroDate) and is_valid_queryparam(numberOfDays):
        qs = qs.filter(Q(infectedDate__contains=zeroDate)).values()
        # print(type(zeroDate))
        # print(zeroDate)

        date_object = datetime.strptime(zeroDate, '%Y-%m-%d').date()
        print(type(date_object))
        print(date_object)
        newDate = date_object + timedelta(int(numberOfDays))
        print(newDate)
        for infec in qs:
            Nd=round(((1+1.15)**int(numberOfDays))*int(infec['infected']),0)
            res = {'newDate':newDate, 'Nd':Nd}
            resu.append(res)
            print(resu)
            #print(infec['infectedDate'])
    context = {'resu':resu}
    return render(request, 'analystic/search.html', context)
