from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from vnstock import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create your views here.

def calculate_macd_signals(data):
    # Định nghĩa các tham số
    r1 = 12
    r2 = 26
    r3 = 9
    r4 = 17
    r5 = 8

    # Đọc dữ liệu từ tệp CSV hoặc các nguồn dữ liệu khác và chuyển đổi thành DataFrame
    # Thực hiện các tính toán cho MACD và tín hiệu
    macd = pd.DataFrame()
    macd['m1'] = data['close'].ewm(span=r1).mean() - data['close'].ewm(span=r2).mean()
    macd['s1'] = macd['m1'].ewm(span=r3).mean()
    macd['m1w'] = data['close'].ewm(span=r4).mean() - data['close'].ewm(span=r5).mean()
    macd['s1w'] = macd['m1w'].ewm(span=r3).mean()
    macd['BuyIBD'] = macd['m1'].apply(lambda x: 'Buy' if x > 0 else '')
    macd['SellIBD'] = macd['m1'].apply(lambda x: 'Sell' if x < 0 else '')
    return macd

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if(form.is_valid()):
            print(form.cleaned_data)

            return HttpResponseRedirect('thank_you')
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/review.html', {
        'form': form
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')