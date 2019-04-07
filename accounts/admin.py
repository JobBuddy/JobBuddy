from django.contrib import admin

from .models import Company, Freelancer, Jobs, Recruiter, CandidateProfile

admin.site.register(Company)
admin.site.register(Freelancer)
admin.site.register(Jobs)
admin.site.register(Recruiter)
admin.site.register(CandidateProfile)
