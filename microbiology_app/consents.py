from edc_consent.consent_definition import ConsentDefinition
from edc_constants.constants import FEMALE, MALE
from edc_protocol import Protocol

consent_v1 = ConsentDefinition(
    "microbiology_app.subjectconsent",
    version="1",
    start=Protocol().study_open_datetime,
    end=Protocol().study_close_datetime,
    age_min=18,
    age_is_adult=18,
    age_max=64,
    gender=[MALE, FEMALE],
)
