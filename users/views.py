from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from jobs.models import Jobs
from .forms import UserForm, CandidateProfileForm
# Create your views here.

def home(request):
    context = {
        'jobs': Jobs.objects.all()
	}
    return render(request, 'jobs/home.html',context )


def candidate(request):
    return render(request, 'users/candidate.html')

def cand_register(request):
    return render(request, 'users/cand_register.html')



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
            user = user_form.save()

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
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = CandidateProfileForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'users/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    context = {}
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active():
                login(request, user)
                return HttpResponseRedirect(reverse('cand_register'))
            else:
                return HttpResponse("Account Is Not Active!")
        else:
            print("Someone Tried To login and Failed!")
            print("Username : {}  Password : {}".format(username, password))
            return HttpResponse("Invalid Credentials!")
    else:
        return render(request, 'candidate.html', {})

def success(request):
    pass

@login_required
def user_logout(request):
    if request.method == "POST" :
        logout(request)
        return  HttpResponseRedirect(reverse('candidate'))
