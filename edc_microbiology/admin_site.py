from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

edc_microbiology_admin = EdcAdminSite(name="edc_microbiology_admin", app_label=AppConfig.name)
