from django.contrib import admin
from .models import Newman,Oldmen,SHB
# Register your models here.
class NewmanInline(admin.TabularInline):
	model = SHB.newman_list.through
	verbose_name = "Newman That Attended"
	verbose_name_plural = "Newmen That Attended"
	extra = 3
class SHBInline(admin.TabularInline):
	model = SHB.newman_list.through
	verbose_name = "SHB Attended"
	verbose_name_plural = "SHB's Attended"
	extra = 3
class SHBAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['shb_name']}),
		('Date', {'fields': ['shb_time'], 'classes': ['collapse']}),
		(None, {'fields': ['limited']}),
	]
	inlines = [NewmanInline]
	verbose_name = "SHB"
	verbose_name_plural = "SHB's"
class NewmanAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['newman_name']}),
		(None, {'fields': ['newman_instrument']}),
		(None, {'fields': ['owner']}),
		(None, {'fields': ['points']}),
		('Image File Name', {'fields': ['imgFileName']}),
	]
	inlines = [SHBInline]
	list_display = ('newman_name', 'newman_instrument', 'calc_points')
class OldmenAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['team_name']}),
		(None, {'fields': ['team_owner']}),
		(None, {'fields': ['team_points']}),
	]
	list_display = ('team_name', 'team_owner', 'team_total')

admin.site.register(Newman,NewmanAdmin)
admin.site.register(Oldmen, OldmenAdmin)
admin.site.register(SHB,SHBAdmin)