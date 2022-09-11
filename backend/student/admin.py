from django.contrib import admin
from student.models import StudentProfile, Resume, ProgramAndBranch, BranchChangers
from .resources import StudentProfileResource
from import_export.admin import ImportExportActionModelAdmin
import csv
from django.http import HttpResponse
from zipfile import ZipFile
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from os.path import basename


class ResumeInline(admin.StackedInline):
    model = Resume


def approve_resumes(modeladmin, request, queryset):
    queryset.update(is_verified=True)


def unapprove_resumes(modeladmin, request, queryset):
    queryset.update(is_verified=False)


def ban(modeladmin, request, queryset):
    queryset.update(banned=True)


def mark_placed(modeladmin, request, queryset):
    queryset.update(placed=True)


def mark_unplaced(modeladmin, request, queryset):
    queryset.update(placed=False)


def export_as_csv(modeladmin, request, queryset):

    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        _ = writer.writerow([getattr(obj, field) for field in field_names])

    return response


def get_zipped_resumes(modeladmin, request, queryset):
    if modeladmin.model is Resume:
        resumes = queryset
    if not resumes.count():
        messages.warning(request, "Select atleast 1 resume to download")
        return

    zip_path = "assets/media/resume/zipped/" + \
        resumes[0].student.roll_no.replace(" ", "_") + '_to_' + resumes[len(resumes)-1].student.roll_no.replace(" ", "_") + ".zip"

    missing = []
    for resume in resumes:
        if not resume.file:
            missing.append(resume.student.user.first_name.replace(" ", "_")+"("+resume.student.roll_no.replace(" ", "_")+")")

    if missing:
        messages.error(request, 'Missing Resume of '+', '.join(missing)+" .")
        return
    else:
        zip = ZipFile(zip_path, 'w')
        for resume in resumes:
            try:
                zip.write(resume.file.path, basename(resume.file.path))
            except Exception as e:
                print(e)
                print(resume.student.user.first_name)
        zip.close()
        url = "/media/resume/zipped/" + resumes[0].student.roll_no.replace(" ", "_") + \
            '_to_' + resumes[len(resumes)-1].student.roll_no.replace(" ", "_") + ".zip"
        return HttpResponseRedirect(url)


@admin.register(ProgramAndBranch)
class ProgramAndBranchAdmin(admin.ModelAdmin):
    class Meta:
        model = ProgramAndBranch
        fields = '__all__'


@admin.register(StudentProfile)
class StudentProfileAdmin(ImportExportActionModelAdmin):
    readonly_fields = ['registration_timestamp', ]
    resource_class = StudentProfileResource
    inlines = (ResumeInline,)
    list_display = ['__str__', 'roll_no', 'program_branch', 'year', 'registration_timestamp']
    list_filter = ['program_branch', 'year', 'registration_timestamp', 'placed']
    ordering = ['roll_no', ]
    search_fields = ['roll_no', 'user__first_name', 'user__last_name']
    actions = ImportExportActionModelAdmin.actions + [ban, mark_placed, mark_unplaced, export_as_csv]

    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    readonly_fields = ['timestamp', ]
    ordering = ['student', ]
    list_display = ['get_roll_no', 'student', 'get_gpa', 'reference', 'file', 'is_verified', 'timestamp', ]
    search_fields = ['student__user__first_name', 'student__user__last_name', 'student__user__username']
    list_filter = ['is_verified', 'timestamp', 'student__program_branch', 'student__year']
    actions = [get_zipped_resumes, approve_resumes, unapprove_resumes, export_as_csv]

    def get_roll_no(self, instance):
        return instance.student.roll_no
    get_roll_no.admin_order_field = 'student__roll_no'

    def get_gpa(self, instance):
        return instance.student.gpa
    get_gpa.admin_order_field = 'student__gpa'

    class Meta:
        model = Resume
        fields = '__all__'


@admin.register(BranchChangers)
class BranchChangersAdmin(admin.ModelAdmin):
    class Meta:
        model = BranchChangers
        fields = '__all__'
