from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CompanyRegisterForm, FreelancerRegisterForm, CompanyJobsForm, RecruiterRegisterForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Jobs, Company, Freelancer
from django.urls import reverse
from .forms import UserForm, CandidateProfileForm
from .models import User
# from .forms import SearchForm


def home(request):
    job_list = Jobs.objects.order_by('date_posted')
    # form = SearchForm(request.POST)
    job_title = 'abcd'
    company = 'abcd'
    job_type = 'abcd'
    Location = 'abcd'
    Qualification = 'abcd'
    min_exp = 'abcd'
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company = request.POST.get('company')
        job_type = request.POST.get('job_type')
        Location = request.POST.get('Location')
        Qualification = request.POST.get('Qualification')
        min_exp = request.POST.get('min_exp')
    job_filter1 = []
    job_filter2 = []
    job_filter3 = []
    job_filter4 = []
    job_filter5 = []
    job_filter6 = []
    if job_title != '':
        job_filter1 = Jobs.objects.filter(job_title__iexact = job_title)
    if company != '':
        job_filter2 = Jobs.objects.filter(company__iexact = company)
    if job_type != '':
        job_filter3 = Jobs.objects.filter(job_type__iexact = job_type)
    if Location != '':
        job_filter4 = Jobs.objects.filter(Location__iexact = Location)
    if Qualification  != '':
        job_filter5 = Jobs.objects.filter(Qualification__iexact = Qualification )
    if min_exp != '':
        job_filter6 = Jobs.objects.filter(min_exp__iexact = min_exp)

    l = []
    job_filter = []

    for i in job_filter1:
        if(i.id not in l):
            job_filter.append(i)
            l.append(i.id)
    for i in job_filter2:
        if(i.id not in l):
            job_filter.append(i)
            l.append(i.id)
    for i in job_filter3:
        if(i.id not in l):
            job_filter.append(i)
            l.append(i.id)
    for i in job_filter4:
        if(i.id not in l):
            job_filter.append(i)
            l.append(i.id)
    for i in job_filter5:
        if(i.id not in l):
            job_filter.append(i)
            l.append(i.id)
    for i in job_filter6:
        if(i.id not in l):
            job_filter.append(i)
            l.append(i.id)

    return render(request, 'accounts/home.html', {'jobs': job_list, 'job_filter1' : job_filter1, 'job_filter2' : job_filter2, 'job_filter3' : job_filter3, 'job_filter4' : job_filter4, 'job_filter5' : job_filter5, 'job_filter6' : job_filter6, 'job_filter' : job_filter})


def company_home(request):
    return render(request, 'accounts/company_home.html', {})


def companyjobs(request):
    #job_list = Jobs.objects.order_by('id')
    if request.method == 'POST':
        form = CompanyJobsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Job is posted Successfully!')
            return redirect('companyjobs')
    else:
        form = CompanyJobsForm()
    #context = {'job_list': job_list, 'form': form}
    return render(request, 'accounts/companyjobs.html', {'form': form})


def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_company:
            login(request, user)
            return redirect('companyjobs')
        else:
            return HttpResponse("Invalid login details given")

    return render(request, 'accounts/company_login.html', {})


def company_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        profile_form = CompanyRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit = False)
            user.is_company = True
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = CompanyRegisterForm()
    return render(request, 'accounts/company_register.html',
                  {'user_form': user_form,
                  'profile_form': profile_form,
                  'registered': registered})


@login_required
def company_profile(request):
    return render(request, 'accounts/company_profile.html', {})


def company_forgetpassword(request):
    return render(request, 'accounts/company_forgetpassword.html', {})


def freelancer_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        profile_form = FreelancerRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_freelancer = True
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = FreelancerRegisterForm()
    return render(request, 'accounts/company_register.html',
                  {'user_form': user_form,
                  'profile_form': profile_form,
                  'registered': registered})


def recruiter_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        profile_form = RecruiterRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit = False)
            user.is_recruiter = True
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = RecruiterRegisterForm()
    return render(request, 'accounts/recruiter_register.html',
                  {'user_form': user_form,
                  'profile_form': profile_form,
                  'registered': registered})


@login_required
def recruiter_profile(request):
    return render(request, 'accounts/recruiter_profile.html', {})


@login_required
def freelancer_profile(request):
    curr_user = request.user
    user_object = User.objects.get(email=curr_user.email)
    Name = user_object.freelancer.Name
    Phone = user_object.freelancer.Phone
    Qualification = user_object.freelancer.Qualification
    PAN = user_object.freelancer.PAN
    Location = user_object.freelancer.Location
    return render(request, 'accounts/freelancer_profile.html', {'curr_user':curr_user, 'Name':Name, 'Phone' : Phone, 'Qualification' : Qualification, 'Location':Location, 'PAN':PAN})


def freelancer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_freelancer:
            login(request, user)
            return redirect('freelancer_profile')
        else:
            return HttpResponse("Invalid login details given")

    return render(request, 'accounts/freelancer_login.html', {})


def recruiter_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_recruiter:
            login(request, user)
            return redirect('app_home')
        else:
            return HttpResponse("Invalid login details given")

    return render(request, 'accounts/recruiter_login.html', {})


def freelancer_home(request):
    return render(request, 'accounts/freelancer_home.html', {})


def recruiter_home(request):
    return render(request, 'accounts/recruiter_home.html', {})


def freelancer_forgetpassword(request):
    return render(request, 'accounts/freelancer_forgetpassword.html', {})


def recruiter_forgetpassword(request):
    return render(request, 'accounts/recruiter_forgetpassword.html', {})


def candidate(request):
    return render(request, 'accounts/candidate.html')


def cand_register(request):
    return render(request, 'accounts/cand_register.html')


def register(request):
    registered = False
    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(request.POST, request.FILES)
        profile_form = CandidateProfileForm(request.POST, request.FILES)
        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save User Form to Database
            user = user_form.save(commit = False)
            user.is_candidate = True
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # Now we deal with the extra info!
            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            # Check if they provided a resume
            if 'resume' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.resume = request.FILES['resume']
            # Now save model
            profile.save()
            # Registration Successful!
            registered = True
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors, profile_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = CandidateProfileForm()
    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'accounts/register.html',
                  {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    #context = {}
    form = UserForm(request.POST)
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_candidate:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('cand_register'))
            else:
                return HttpResponse("Account Is Not Active!")
        else:
            print("Someone Tried To login and Failed!")
            print("Username : {}  Password : {}".format(username, password))
            return HttpResponse("Invalid Credentials!")
    return render(request, 'accounts/candidate.html', {'form': form})


def success(request):
    pass


@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('candidate'))

def candidate_home(request):
    curr_user = request.user
    return render(request, 'accounts/candidate_profile.html', {'curr_user' : curr_user})
