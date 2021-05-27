from django.shortcuts import render
import numpy as np
import joblib


def home(request):

    return render(request, 'AIModel/home2.html')


def about(request):

    return render(request, 'AIModel/index.html')


def result(request):

    rf = joblib.load('AIModel/final.sav')

    arr = []
    if request.method == 'POST':
        data1 = request.POST["a"]
        if data1 == "Parks,Restaraunts ,Grocery Stores":
            data1 = 14
        if data1 == "Grocery Stores,Mosques,Recreational Clubs":
            data1 = 2
        if data1 == "Parks,Restaraunts,Grocery Stores":
            data1 = 12
        if data1 == "Parks,Grocery Stores,Recreational Clubs":
            data1 = 6
        if data1 == "Parks,Mosques,Recreational Clubs":
            data1 = 9
        if data1 == "Restaraunts,Grocery Stores,Recreational Clubs":
            data1 = 16
        if data1 == "Parks,Grocery Stores,Mosques":
            data1 = 5
        if data1 == "Restaraunts,Grocery Stores,Mosques":
            data1 = 17
        if data1 == "Parks,Restaraunts,Recreational Clubs":
            data1 = 15
        else:
            data1 = 13
        arr.append(data1)
        data2 = request.POST['b']

        if data2 == "Social, Noisy, Public":
            data2 = 1
        elif data2 == "Social, Quiet, Private":
            data2 = 2
        else:
            data2 = 0
        arr.append(data2)

        data3 = request.POST['c']
        arr.append(data3)
        # data3 means Nature

        data4 = request.POST['d']
        if data4 == "Extrovert":
            data4 = 1
        elif data4 == "Introvert":
            data4 = 2
        else:
            data4 = 0
        arr.append(data4)

        # data5 means Mental Peace
        data5 = request.POST['e']
        if data5 == "Yes":
            data5 = 1
        else:
            data5 = 0
        arr.append(data5)

        # data6 means Reaction on lack  of something
        data6 = request.POST['f']
        if data6 == "Pursue something else":
            data6 = 1
        else:
            data6 = 0
        arr.append(data6)

        data7 = request.POST['g']
        if data7 == "Socialize":
            data7 = 2
        elif data7 == "Kill time":
            data7 = 0
        elif data7 == "Pursue hobbies (Sports, Reading, Painting etc)":
            data7 = 1
        else:
            data7 = 3
        arr.append(data7)
        data8 = request.POST['h']
        if data8 == "Once or twice a week":
            data8 = 2
        elif data8 == "Once or twice a month":
            data8 = 1
        elif data8 == "Rarely":
            data8 = 3
        else:
            data8 = 0
        arr.append(data8)
        data9 = request.POST['i']
        if data9 == "Never talk about that topic":
            data9 = 1
        elif data9 == "Try to change the other person's view":
            data9 = 3
        elif data9 == "Talk about the topic respecting eachother's views":
            data9 = 2
        else:
            data9 = 0
        arr.append(data9)
        data10 = request.POST['j']
        if data10 == "Desi":
            data10 = 1
        elif data10 == "Ginsoy":
            data10 = 3
        elif data10 == "KFC":
            data10 = 4
        elif data10 == "Dominos":
            data10 = 2
        else:
            data10 = 0
        arr.append(data10)

        arr1 = np.array([arr])
        pred = rf.predict(arr1)
        data = pred

        context = {
            'data': data
        }

    return render(request, 'AIModel/results.html', context)