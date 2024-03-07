from .index import index
from .disease_category import DiseaseCategoryListView, DiseaseCategoryDetailView, DiseaseCategoryCreateView, DiseaseCategoryUpdateView, DiseaseCategoryDeleteView
from .disease import DiseaseListView, DiseaseDetailView, DiseaseCreateView, DiseaseUpdateView, DiseaseDeleteView
from .case_report import CaseReportListView, CaseReportDetailView, CaseReportCreateView, CaseReportUpdateView, CaseReportDeleteView
from .hospitalized_report import HospitalizedReportListView, HospitalizedReportDetailView, HospitalizedReportCreateView, HospitalizedReportUpdateView, HospitalizedReportDeleteView
from .death_report import DeathReportListView, DeathReportDetailView, DeathReportCreateView, DeathReportUpdateView, DeathReportDeleteView
from .icu_report import ICUReportListView, ICUReportDetailView, ICUReportCreateView, ICUReportUpdateView, ICUReportDeleteView
from .vaccination_report import VaccinationReportListView, VaccinationReportDetailView, VaccinationReportCreateView, VaccinationReportUpdateView, VaccinationReportDeleteView
from .api import data_portal_api2

