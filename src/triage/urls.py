from django.urls import path
from django.views.generic import TemplateView
from triage.views import findings, filters, home, cases

# pylint: disable=C0103
urlpatterns = [
    path('cases/', cases.show_cases),
    path('api/findings/add', findings.api_add),
    path('api/findings/get_files', findings.api_get_files),
    path('api/findings/get_source_code', findings.api_get_source_code),
    path('api/findings/get_file_list', findings.api_get_file_list),
    path('api/findings/get_blob_list', findings.api_get_blob_list),
    path('findings/<uuid:finding_uuid>', findings.show_finding_by_uuid),
    path('findings/', findings.show_findings),
    path('filters/new', filters.new_filter),
    path('filters', filters.index),
    path('', home.home),
]