from fattwitter.apps.twitter.models import * 
from django.contrib import admin

class EquivalenceAdmin(admin.ModelAdmin):
	pass

admin.site.register(Equivalence, EquivalenceAdmin)