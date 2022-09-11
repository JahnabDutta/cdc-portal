from cdc_portal.utils import get_config_value
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import StudentProfile

from main.models import (OfficeMails, AboutUs, Achievements, AlumniTestimonial,
                         CareerCommittee, CoreTeamContacts, DesignationChoices,
                         DirectorMessage, HomeImageCarousel, SheetsPlacementCalendar,
                         NavBarSubOptions, News, PastRecruiters, PlacementCalendar, Volunteers,
                         VolunteersYearChoices, WhyRecruit, CareerDevelopmentActivity, CourseHighlights)
from main.serializers import (OfficeMailsSerializer, AboutUsSerializer, AchievementsSerializer,
                              AlumniTestimonialSerializer,
                              CareerCommitteeSerializer,
                              CoreTeamContactsSerializer,
                              DesignationChoicesSerializer,
                              DirectorMessageSerializer,
                              HomeImageCarouselSerializer,
                              NavBarSubOptionsSerializer, NewsSerializer,
                              PastRecruitersSerializer, PlacementCalendarSerializer, VolunteersSerializer,
                              VolunteersYearChoicesSerializer, SheetsPlacementCalendarSerializer,
                              WhyRecruitSerializer, CareerDevelopmentActivitySerializer, CourseHighlightsSerializer)


class OfficeMailsSerializer(ListAPIView):
    queryset = OfficeMails.objects.filter(active=True)
    serializer_class = OfficeMailsSerializer


class NewsSerializer(ListAPIView):
    queryset = News.objects.filter(active=True).order_by('order_no')
    serializer_class = NewsSerializer


class AboutUsSerializer(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class DirectorMessageSerializer(ListAPIView):
    queryset = DirectorMessage.objects.all()
    serializer_class = DirectorMessageSerializer


class AlumniTestimonialSerializer(ListAPIView):
    queryset = AlumniTestimonial.objects.filter(active='True').order_by('ranking')
    serializer_class = AlumniTestimonialSerializer


class CareerDevelopmentActivitySerializer(ListAPIView):
    queryset = CareerDevelopmentActivity.objects.filter(active='True').order_by('ranking')
    serializer_class = CareerDevelopmentActivitySerializer


class AchievementsSerializer(ListAPIView):
    queryset = Achievements.objects.filter(active='True').order_by('ranking')
    serializer_class = AchievementsSerializer


class PastRecruitersSerializer(ListAPIView):
    queryset = PastRecruiters.objects.filter(active=True)
    serializer_class = PastRecruitersSerializer


class HomeImageCarouselSerializer(ListAPIView):
    queryset = HomeImageCarousel.objects.filter(active=True)
    serializer_class = HomeImageCarouselSerializer


class DesignationChoicesSerializer(ListAPIView):
    queryset = DesignationChoices.objects.all()
    serializer_class = DesignationChoicesSerializer


class VolunteersYearChoicesSerializer(ListAPIView):
    queryset = VolunteersYearChoices.objects.all()
    serializer_class = VolunteersYearChoicesSerializer


class CoreTeamContactsSerializer(ListAPIView):
    queryset = CoreTeamContacts.objects.filter(active=True).order_by('order_no')
    serializer_class = CoreTeamContactsSerializer
    search_fields = ['designation__designation']
    filter_backends = (SearchFilter,)


class CareerCommitteeSerializer(ListAPIView):
    queryset = CareerCommittee.objects.filter(active=True)
    serializer_class = CareerCommitteeSerializer
    search_fields = ['designation__designation']
    filter_backends = (SearchFilter,)


class VolunteersSerializer(ListAPIView):
    queryset = Volunteers.objects.filter(active=True)
    serializer_class = VolunteersSerializer


class NavBarSubOptionsSerializer(ListAPIView):
    queryset = NavBarSubOptions.objects.all()
    serializer_class = NavBarSubOptionsSerializer
    search_fields = ['title']
    filter_backends = (SearchFilter,)


class WhyRecruitSerializer(ListAPIView):
    queryset = WhyRecruit.objects.filter(active=True)
    serializer_class = WhyRecruitSerializer
    search_fields = ['title']
    filter_backends = (SearchFilter,)


class Alerts(APIView):
    def get(self, request,):
        return Response(get_config_value('Alerts'), status=status.HTTP_200_OK)


class Announcements(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request,):
        profile = get_object_or_404(StudentProfile, user=request.user)
        IntershipYears = get_config_value('IntershipYears')
        JobYears = get_config_value('JobYears')
        an = get_config_value('Annoucements')
        year_combo = profile.program_branch.getter.split('/')[0] + str(profile.year)
        data = {'Annoucements': an["All"]}
        if year_combo in IntershipYears:
            data['Annoucements'].append(an["Interships"])
        if year_combo in JobYears:
            data['Annoucements'].append(an["Jobs"])
        return Response(data, status.HTTP_200_OK)


class CourseHighlightsSerializer(ListAPIView):
    queryset = CourseHighlights.objects.all()
    serializer_class = CourseHighlightsSerializer
    search_fields = ['program', 'title']
    filter_backends = (SearchFilter,)


class PlacementCalendarView(ListAPIView):
    queryset = PlacementCalendar.objects.all()
    serializer_class = PlacementCalendarSerializer


class SheetsPlacementCalendarView(ListAPIView):
    queryset = SheetsPlacementCalendar.objects.all()
    serializer_class = SheetsPlacementCalendarSerializer
