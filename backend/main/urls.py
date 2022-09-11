from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('office_mails/', views.OfficeMailsSerializer.as_view(), name="office_mails"),
    path('news/', views.NewsSerializer.as_view(), name="news"),
    path('about_us/', views.AboutUsSerializer.as_view(), name="about_us"),
    path('director_message/', views.DirectorMessageSerializer.as_view(), name="director_message"),
    path('alumni_testimonial/', views.AlumniTestimonialSerializer.as_view(), name="alumni_testimonial"),
    path('career_development_activity/', views.CareerDevelopmentActivitySerializer.as_view(), name="career_development_activity"),
    path('achievements/', views.AchievementsSerializer.as_view(), name="achievements"),
    path('past_recruiters/', views.PastRecruitersSerializer.as_view(), name="past_recruiters"),
    path('designation_choices/', views.DesignationChoicesSerializer.as_view(), name="designation_choices"),
    path('home_image_carousel/', views.HomeImageCarouselSerializer.as_view(), name="home_image_carousel"),
    path('core_team_contacts/', views.CoreTeamContactsSerializer.as_view(), name="core_team_contacts"),
    path('career_committee/', views.CareerCommitteeSerializer.as_view(), name="career_committee"),
    path('volunteers_year_choices/', views.VolunteersYearChoicesSerializer.as_view(), name="volunteers_year_choices"),
    path('volunteers/', views.VolunteersSerializer.as_view(), name="volunteers"),
    path('navbar_suboptions/', views.NavBarSubOptionsSerializer.as_view(), name="navbar_suboptions"),
    path('whyrecruitdata/', views.WhyRecruitSerializer.as_view(), name="whyrecruitdata"),
    path('course_highlights/', views.CourseHighlightsSerializer.as_view(), name="course_highlights"),
    path('placement_calendar/', views.PlacementCalendarView.as_view(), name="placement_calendar"),
    path('sheets_placement_calendar/', views.SheetsPlacementCalendarView.as_view(), name="sheets_placement_calendar"),
    path('alerts/', views.Alerts.as_view(), name="alerts"),
]
