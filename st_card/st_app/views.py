from django.shortcuts import redirect, render
from .models import StudentDetails

# Create your views here.

#Load addStudent.html Page........
def addStudent(request):
    return render(request,'addStudent.html')

#Enter Product Details...
def add_student_details(request):
    if request.method=='POST':
    	sname=request.POST['student_name']
    	course=request.POST['course']
    	email=request.POST['email']
    	mob=request.POST['mob']
    	gender=request.POST['gender']
    	adress=request.POST['adress']
    	student=StudentDetails(student_name=sname,
    		course=course,
    		email=email,
    		mob=mob,
    		gender=gender,
    		adress=adress)
    	student.save()
    	print("hii")
    	# return redirect('/')
    	return redirect('show_students') 


#Show Products Detsils...
def show_students(request):
    students=StudentDetails.objects.all()
    return render(request,'showPimg.html',{'students':students})

#Load Edit Page....
def editpage(request,pk):
    students=StudentDetails.objects.get(id=pk)
    return render(request,'edit.html',{'students':students})

#Editing..
def edit_student_details(request,pk):
    if request.method=='POST':
        students = StudentDetails.objects.get(id=pk)
        students.student_name = request.POST.get('student_name')
        students.course = request.POST.get('course')
        students.email = request.POST.get('email')
        students.mob = request.POST.get('mob')
        students.gender = request.POST.get('gender')
        students.adress = request.POST.get('adress')
        students.save()
        return redirect('show_students')
    return render(request, 'edit.html',)


#Load delete Page...
def deletepage(request,pk):
    students=StudentDetails.objects.get(id=pk)
    return render(request,'delete.html',{'students':students})

#Deleting Product Element..
def delete_student(request,pk):
    students=StudentDetails.objects.get(id=pk)
    students.delete()
    return redirect('show_students')

def indi(request,pk):
    students=StudentDetails.objects.get(id=pk)
    return render(request,'card.html',{'students':students})