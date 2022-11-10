from django.shortcuts import render
from .forms import UserCrudForm
from .models import User
from django.http import JsonResponse
# Create your views here.
def Home(request):
    form = UserCrudForm()
    studentData = User.objects.all()
    context = {'form':form,'studentData':studentData}
    return render(request,'crud/index.html',context)

def saveData(request):
    if request.method == "POST":
        form = UserCrudForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (sid == ''):
                user = User(name=name, email=email, password=password)
            else:
                user = User(id=sid, name=name, email=email, password=password)
            user.save()
            student_data = User.objects.values()
            stu_data = list(student_data)
            dic = {'status':'Save','stu_data':stu_data}
            return JsonResponse(dic)
        else:
            return JsonResponse({'status':0})

def DeleteData(request):
    if request.method == "POST":
        id = request.POST.get('sid');
        data = User.objects.get(pk=id)
        data.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def EditData(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        stu_data = User.objects.get(pk=id)
        student = {'id':stu_data.id,'name':stu_data.name,'email':stu_data.email,'password':stu_data.password}
        return JsonResponse(student)