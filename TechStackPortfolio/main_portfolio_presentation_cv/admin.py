from django.contrib import admin
from main_portfolio_presentation_cv.models import UserData, JobTitle, Technologies, WorkExperience, \
    SocialLinkConnect, Projects, Portfolio

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    pass

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    pass

@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialLinkConnect)
class SocialLinkConnectAdmin(admin.ModelAdmin):
    pass

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass

