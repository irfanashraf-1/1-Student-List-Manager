from django.shortcuts import render ,redirect
from projectapp.models import Student_data

# Create your views here.
def Indexpage(request) :
    return render(request,'index.html')

def Table(request) :
    all_data = Student_data.objects.all()
    return render (request, 'table.html', {'student_data' : all_data})

def Edit_data_page(request,pk):
    selected = Student_data.objects.get(id=pk)
    return render(request,'edit_data_page.html',{'selected_student':selected})



def Savedata(request):
    if request.method == 'POST' :
        fullname = request.POST.get('fullname')
        grade = request.POST.get('grade')
        phone_number = request.POST.get('phone_number')

        student_details = Student_data(
                                        Fullname = fullname,
                                        Grade = grade,
                                        Phone_number = phone_number
        )
        student_details.save()

        return redirect('Table')

def Edit_data(request,pk):
    if request.method == 'POST':
        modified = Student_data.objects.get(id=pk)

        modified.Fullname = request.POST.get('fullname')
        modified.Grade = request.POST.get('grade')
        modified.Phone_number = request.POST.get('phone_number')

        modified.save()
        return redirect('Table')
    
def Delete_data(request,pk):
    delete = Student_data.objects.get(id=pk)
    delete.delete()

    return redirect('Table')