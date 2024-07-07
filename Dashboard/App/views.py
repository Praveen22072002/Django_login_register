from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Signup, DocSignup
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signin(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.info(request, 'Both fields are required.')
            return HttpResponseRedirect(reverse('Login'))

        try:
            user = Signup.objects.get(email=email, password=password)
            request.session['user_id'] = user.id  # Store user ID in session
            return HttpResponseRedirect(reverse('dashboard'))
        except Signup.DoesNotExist:
            messages.info(request, 'Invalid Credentials')
            return HttpResponseRedirect(reverse('Login'))
    else:
        return HttpResponseRedirect(reverse('Login'))

def register(request):
    template = loader.get_template('Register.html')
    return HttpResponse(template.render({}, request))

def signrecord(request):
    if request.method == 'POST':
        name = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        repass = request.POST['repassword']
        username = request.POST['username']
        profile = request.FILES.get('profile_picture')
        address_line_1 = request.POST['address_line_1']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']


        if Signup.objects.filter(username=username).exists():
            messages.info(request, "Username already present!!!")
            return HttpResponseRedirect(reverse('register'))

        if password == repass:
            mysign = Signup(
                first_name=name,
                last_name=last,
                email=email,
                password=password,
                repassword=repass,
                username=username,
                profile_picture=profile,
                address_line_1=address_line_1,
                city=city,
                state=state,
                pincode=pincode,
            )
            mysign.save()
            return HttpResponseRedirect(reverse('Login'))
        else:
            messages.info(request, "Passwords do not match!!!")
            return HttpResponseRedirect(reverse('register'))

    return render(request, 'register.html')

@login_required
def dash(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return HttpResponseRedirect(reverse('Login'))

    try:
        user_info = Signup.objects.get(id=user_id)
    except Signup.DoesNotExist:
        user_info = None

    context = {
        'user_info': user_info
    }
    return render(request, 'Dashboard.html', context)




# Login for doctor

def docsignin(request):
    template = loader.get_template('doc_login.html')
    return HttpResponse(template.render({}, request))


def doclogin(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        password = request.POST.get('password')


        if not empid or not password:
            messages.info(request, 'Both fields are required.')
            return HttpResponseRedirect(reverse('docsignin'))

        try:
            user = DocSignup.objects.get(empid=empid, password=password)
            request.session['user_id'] = user.id  # Store user ID in session
            return HttpResponseRedirect(reverse('docdash'))
        except DocSignup.DoesNotExist:
            messages.info(request, 'Invalid Credentials')
            return HttpResponseRedirect(reverse('docsignin'))
    else:
        return HttpResponseRedirect(reverse('docsignin'))


def docregister(request):
    template = loader.get_template('doctor_register.html')
    return HttpResponse(template.render({}, request))

def docsignrecord(request):
    if request.method == 'POST':
        name = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        empid = request.POST['empid']
        password = request.POST['password']
        repass = request.POST['repassword']
        username = request.POST['username']
        profile = request.FILES.get('profile_picture')
        address_line_1 = request.POST['address_line_1']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        if DocSignup.objects.filter(username=username).exists():
            messages.info(request, "Username already present!!!")
            return HttpResponseRedirect(reverse('docregister'))

        if password == repass:
            mysign = DocSignup(
                first_name=name,
                last_name=last,
                email=email,
                empid=empid,
                password=password,
                repassword=repass,
                username=username,
                profile_picture=profile,
                address_line_1=address_line_1,
                city=city,
                state=state,
                pincode=pincode,
            )
            mysign.save()
            return HttpResponseRedirect(reverse('docsignin'))
        else:
            messages.info(request, "Passwords do not match!!!")
            return HttpResponseRedirect(reverse('doc_register'))

    return render(request, 'doctor_register.html')

@login_required
def docdash(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return HttpResponseRedirect(reverse('docsignin'))

    try:
        user_info = DocSignup.objects.get(id=user_id)
    except DocSignup.DoesNotExist:
        user_info = None

    context = {
        'user_info': user_info
    }
    return render(request, 'doc_dash.html', context)