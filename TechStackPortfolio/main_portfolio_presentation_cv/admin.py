from django.contrib import admin
from main_portfolio_presentation_cv.models import MainUser, JobTitle, Technologies, WorkExperience, \
    SocialLinkConnect, Projects

@admin.register(MainUser)
class MainUserAdmin(admin.ModelAdmin):
    # Display fields directly from MainUser
    # list_display = ('first_name', 'middle_name', 'last_name', 'job_title',
    #                 'age', 'country')
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

# Register MainUser with custom admin class
# admin.site.register(MainUser, MainUserAdmin)
# admin.site.register(MainUser, JobTitleAdmin)
# admin.site.register(MainUser, TechnologiesAdmin)
# admin.site.register(MainUser, TechnologiesAdmin)
# admin.site.register(MainUser, TechnologiesAdmin)

