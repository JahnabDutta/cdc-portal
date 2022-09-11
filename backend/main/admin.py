from django.contrib import admin
from main.models import OfficeMails, PastRecruiters, News,\
    AlumniTestimonial, HomeImageCarousel, DesignationChoices,\
    VolunteersYearChoices, CareerCommittee, CoreTeamContacts,\
    Volunteers, NavBarSubOptions, AboutUs, DirectorMessage,\
    Achievements, WhyRecruit, CareerDevelopmentActivity, PlacementCalendar,\
    CourseHighlights, SheetsPlacementCalendar
from import_export.admin import ImportExportActionModelAdmin


admin.site.register(OfficeMails)


admin.site.register(AboutUs)


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):
    list_display = ['order_no', 'title', 'active', ]
    list_filter = ['active', ]
    ordering = ['order_no']

    class Meta:
        model = News


@admin.register(CareerDevelopmentActivity)
class CareerDevelopmentActivityAdmin(ImportExportActionModelAdmin):
    list_display = ['ranking', 'title', 'active', ]
    list_filter = ['active', ]
    ordering = ['ranking']

    class Meta:
        model = CareerDevelopmentActivity


@admin.register(DirectorMessage)
class DirectorMessageAdmin(ImportExportActionModelAdmin):
    class Meta:
        model = DirectorMessage


@admin.register(PastRecruiters)
class PastRecruitersAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_order_no', 'active', ]
    list_filter = ['active', ]

    class Meta:
        model = PastRecruiters
        fields = '__all__'


@admin.register(AlumniTestimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['ranking', 'alumni_name', 'active', ]
    list_filter = ['active', ]
    ordering = ['ranking', ]

    class Meta:
        model = AlumniTestimonial
        fields = '__all__'


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ['ranking', 'title', 'active', ]
    list_filter = ['active', ]
    ordering = ['ranking', ]

    class Meta:
        model = Achievements
        fields = '__all__'


@admin.register(HomeImageCarousel)
class HomeImageCarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'ordering', 'active', ]
    ordering = ['ordering', ]

    class Meta:
        model = HomeImageCarousel
        fields = '__all__'


@admin.register(DesignationChoices)
class DesignationChoicesAdmin(admin.ModelAdmin):
    class Meta:
        model = DesignationChoices
        fields = '__all__'


@admin.register(VolunteersYearChoices)
class VolunteersYearChoicesAdmin(admin.ModelAdmin):
    class Meta:
        model = VolunteersYearChoices
        fields = '__all__'


@admin.register(CoreTeamContacts)
class CoreTeamContactsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'designation', 'active', ]
    list_filter = ['active', 'designation', ]
    ordering = ['order_no', ]

    class Meta:
        model = CoreTeamContacts
        fields = '__all__'


@admin.register(CareerCommittee)
class CareerCommitteeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'designation', 'active', ]
    list_filter = ['active', 'designation', ]
    ordering = ['order_no', ]

    class Meta:
        model = CareerCommittee
        fields = '__all__'


@admin.register(Volunteers)
class VolunteersAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'active', ]
    list_filter = ['active', ]

    class Meta:
        model = Volunteers
        fields = '__all__'


@admin.register(NavBarSubOptions)
class NavBarSubOptionsAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]

    class Meta:
        model = NavBarSubOptions
        fields = '__all__'


@admin.register(WhyRecruit)
class WhyRecruitAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    list_filter = ['active', ]
    search_fields = ['title', ]

    class Meta:
        model = WhyRecruit
        fields = '__all__'


@admin.register(PlacementCalendar)
class PlacementCalendarAdmin(admin.ModelAdmin):
    list_display = ['start', 'end', 'title', 'description']
    search_fields = ['title', ]

    class Meta:
        model = PlacementCalendar
        fields = '__all__'


@admin.register(SheetsPlacementCalendar)
class SheetsPlacementCalendarAdmin(admin.ModelAdmin):
    list_display = ['type', 'calendar_publish_link', 'applicable_years']
    list_filter = ['type', ]

    class Meta:
        model = SheetsPlacementCalendar
        fields = '__all__'


@admin.register(CourseHighlights)
class CourseHighlightsAdmin(admin.ModelAdmin):
    list_display = ['program', 'title']
    list_filter = ['program', 'title']
    search_fields = ['program', 'title']

    class Meta:
        model = CourseHighlights
        fields = '__all__'
