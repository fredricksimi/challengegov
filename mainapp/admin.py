from django.contrib import admin
from .models import Challenges, ChallengeAudience, Preapproved_challenge, ChallengeTag


class ChallengesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.site_header = "Research Administration"
admin.site.site_title = "Research"

admin.site.register(Challenges, ChallengesAdmin)
admin.site.register(ChallengeAudience)
admin.site.register(Preapproved_challenge)
admin.site.register(ChallengeTag)
