from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edc_microbiology.fieldsets import get_urine_culture_fieldset


class UrineCultureModelAdminMixin:

    fieldsets = (
        get_urine_culture_fieldset(),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "urine_culture_performed": admin.VERTICAL,
        "urine_culture_results": admin.VERTICAL,
        "urine_culture_organism": admin.VERTICAL,
    }
