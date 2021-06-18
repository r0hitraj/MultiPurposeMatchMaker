from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile, indexdata, passionlist,purposedata
from django.contrib.auth.models import User, auth
from django.contrib import messages
#for sendding mail
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def index(request):
    data=indexdata.objects.all() #this line will show all the dynamic content of the index page
    return render(request,'index.html',{'data': data})


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')      




def profile(request):
    passion=passionlist.objects.all()

    if request.method == 'POST':
        phone = request.POST['phone_no']
        gender = request.POST['gender']
        dob = request.POST['dob']
        passion1 = request.POST['passion1']
        passion2 = request.POST['passion2']
        passion3 = request.POST['passion3']
        passion4 = request.POST['passion4']
        passion5 = request.POST['passion5']
        passion6 = request.POST['passion6']
        passion7 = request.POST['passion7']
        passion8 = request.POST['passion8']
        passion9 = request.POST['passion9']
        passion10 = request.POST['passion10']
        pic1=request.POST['profile_pic1']
        pic2=request.POST['profile_pic2']
        Height = request.POST['Height']
        Nationality = request.POST['Nationality']
        Ethnicity = request.POST['Ethnicity']
        Employment = request.POST['Employment']
        author =request.user
        if pic1 == "" or pic2=="":
            messages.info(request,"Uplode Your Profile Pic")
            return redirect('profile')
        if not  Height == "" or not Nationality == "" or not Ethnicity == "" or not Employment == "":
            if phone =="" or gender =="" or dob=="" or  passion1 == "" or passion2=="" or  passion3 == ""or passion4=="" or  passion5 == ""or passion6=="" or  passion7 == ""or passion8=="" or  passion9 == "" or  passion10 == "" or pic1 == "" or pic2== "":
                messages.info(request,"there is one or more fields are empty!")
                return redirect('profile')

            else:
                profile =  Profile(
                            author=author,
                            phone=phone,
                            date_of_birth=dob,
                        gender=gender,
                        passionid1=passion1,
                        passionid2=passion2,
                        passionid3=passion3,
                        passionid4=passion4,
                        passionid5=passion5,
                        passionid6=passion6,
                        passionid7=passion7,
                        passionid8=passion8,
                        passionid9=passion9,
                        passionid10=passion10,
                        profilepic1=pic1,
                        profilepic2=pic2,
                        height= Height,
                        nationality=Nationality,
                        employment=Employment,
                        ethnicity=Ethnicity)
                profile.save()
                return redirect('purpose')
            
        elif  phone == "" or gender == "" or dob =="" or  passion1 == "" or passion2=="" or  passion3 == ""or passion4=="" or  passion5 == ""or passion6=="" or  passion7 == ""or passion8=="" or  passion9 == "" or  passion10 == "" or pic1 =="" or pic2=="" :
            messages.info(request,"there is one or more fields are empty!")
            return redirect('profile')
        else:
            profile =  Profile(
                            author=author,
                            phone=phone,
                            date_of_birth=dob,
                        gender=gender,
                        passionid1=passion1,
                        passionid2=passion2,
                        passionid3=passion3,
                        passionid4=passion4,
                        passionid5=passion5,
                        passionid6=passion6,
                        passionid7=passion7,
                        passionid8=passion8,
                        passionid9=passion9,
                        passionid10=passion10)
            profile.save()
            return redirect('purpose')


    return render(request,'profile.html',{'passion':passion})

def matches(request):

    profile=Profile.objects.get(author=request.user)
    lmatch=Profile.objects.all().filter(purposeid=profile.purposeid)
    match=lmatch.exclude(author=request.user)
    if request.method =='POST':
        to=User.objects.get(username=request.POST['matchto'])
        html_content =render_to_string("email.html" )
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(

            "Amazing You Got A Match",  #subject
            text_content, #email containt
            settings.EMAIL_HOST_USER, #from Email
             [to.email],    #add list of Recipents Here

        )
        email.attach_alternative(html_content,"text/html")
        email.send()

    

    return render(request,'card2.html',{'match':match} )

    





def purpose(request): 
    purpose_object=purposedata.objects.all()  #this line will show all the dynamic content of the purpose page
    if request.method == 'POST':
        purpose_data= request.POST['purposeid']
        entry=Profile.objects.get(author=request.user)
        entry.purposeid=purpose_data
        entry.save()
        return redirect('/card2')

    return render(request,'purpose.html',{'purpose_object':purpose_object})

def delt(request):
    user=User.objects.get(username=request.user)
    user.delete()

    return redirect('/del')

