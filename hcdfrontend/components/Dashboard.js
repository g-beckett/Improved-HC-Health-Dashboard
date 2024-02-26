import { useState, useEffect } from 'react';
import axios from 'axios';
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/react/outline';

const Dashboard = () => {
  const [diseaseCategories, setDiseaseCategories] = useState([]);
  const [diseases, setDiseases] = useState([]);
  const [caseReports, setCaseReports] = useState([]);
  const [hospitalizedReports, setHospitalizedReports] = useState([]);
  const [icuReports, setICUReports] = useState([]);
  const [deathReports, setDeathReports] = useState([]);
  const [vaccinationReports, setVaccinationReports] = useState([]);

  const [isDiseaseCategoriesOpen, setIsDiseaseCategoriesOpen] = useState(true);
  const [isDiseasesOpen, setIsDiseasesOpen] = useState(true);
  const [isCaseReportsOpen, setIsCaseReportsOpen] = useState(false); 
  const [isHospitalizedReportsOpen, setIsHospitalizedReportsOpen] = useState(false);
  const [isICUReportsOpen, setIsICUReportsOpen] = useState(false);
  const [isDeathReportsOpen, setIsDeathReportsOpen] = useState(false);
  const [isVaccinationReportsOpen, setIsVaccinationReportsOpen] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://hcdbackend.fly.dev/dataportal/_query');
        const { DiseaseCategories, Diseases, CaseReports, HospitalizedReports, ICUReports, DeathReports, VaccinationReports } = response.data;

        setDiseaseCategories(DiseaseCategories);
        setDiseases(Diseases);
        setCaseReports(CaseReports);
        setHospitalizedReports(HospitalizedReports);
        setICUReports(ICUReports);
        setDeathReports(DeathReports);
        setVaccinationReports(VaccinationReports);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const toggleSection = (section) => {
    switch (section) {
      case 'diseaseCategories':
        setIsDiseaseCategoriesOpen(!isDiseaseCategoriesOpen);
        break;
      case 'diseases':
        setIsDiseasesOpen(!isDiseasesOpen);
        break;
      case 'caseReports':
        setIsCaseReportsOpen(!isCaseReportsOpen);
        break;
      case 'hospitalizedReports':
        setIsHospitalizedReportsOpen(!isHospitalizedReportsOpen);
        break;
      case 'icuReports':
        setIsICUReportsOpen(!isICUReportsOpen);
        break;
      case 'deathReports':
        setIsDeathReportsOpen(!isDeathReportsOpen);
        break;
      case 'vaccinationReports':
        setIsVaccinationReportsOpen(!isVaccinationReportsOpen);
        break;
      default:
        break;
    }
  };

  return (
    <div className="container mx-auto p-4 text-black">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-2xl font-semibold">Disease Categories ({diseaseCategories.length})</h2>
        <button onClick={() => toggleSection('diseaseCategories')}>
          {isDiseaseCategoriesOpen ? (
            <ChevronUpIcon className="h-6 w-6" />
          ) : (
            <ChevronDownIcon className="h-6 w-6" />
          )}
        </button>
      </div>
      {isDiseaseCategoriesOpen && (
        <div className="mb-4">
          <ul>
            {diseaseCategories.map((category, index) => (
              <li key={index}>
                <strong>{category.name}</strong>: {category.description}
              </li>
            ))}
          </ul>
        </div>
      )}

      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-2xl font-semibold">Diseases ({diseases.length})</h2>
        <button onClick={() => toggleSection('diseases')}>
          {isDiseasesOpen ? <ChevronUpIcon className="h-6 w-6" /> : <ChevronDownIcon className="h-6 w-6" />}
        </button>
      </div>
      {isDiseasesOpen && (
        <div className="mb-4">
          <table className="table-auto border-collapse w-full">
            <thead>
              <tr>
                <th className="border px-4 py-2">Disease</th>
                <th className="border px-4 py-2">Description</th>
                <th className="border px-4 py-2">Category</th>
              </tr>
            </thead>
            <tbody>
              {diseases.map((disease, index) => (
                <tr key={index}>
                  <td className="border px-4 py-2">{disease.name}</td>
                  <td className="border px-4 py-2">{disease.description}</td>
                  <td className="border px-4 py-2">{disease.diseaseCategory}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-2xl font-semibold">Case Reports ({caseReports.length})</h2>
        <button onClick={() => toggleSection('caseReports')}>
          {isCaseReportsOpen ? <ChevronUpIcon className="h-6 w-6" /> : <ChevronDownIcon className="h-6 w-6" />}
        </button>
      </div>
      {isCaseReportsOpen && (
        <div className="mb-4">
          <table className="table-auto border-collapse w-full">
            <thead>
              <tr>
                <th className="border px-4 py-2">Date</th>
                <th className="border px-4 py-2">Disease</th>
                <th className="border px-4 py-2">Category</th>
                <th className="border px-4 py-2">New Cases</th>
              </tr>
            </thead>
            <tbody>
              {caseReports.map((report, index) => (
                <tr key={index}>
                  <td className="border px-4 py-2">{report.AnalyticsDate}</td>
                  <td className="border px-4 py-2">{report.Disease}</td>
                  <td className="border px-4 py-2">{report.DiseaseCategory}</td>
                  <td className="border px-4 py-2">{report.NumberOfNewCases}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <div className="mb-4 flex items-center justify-between">
              <h2 className="text-2xl font-semibold">Hospitalized Reports ({hospitalizedReports.length})</h2>
              <button onClick={() => toggleSection('hospitalizedReports')}>
                {isHospitalizedReportsOpen ? (
                  <ChevronUpIcon className="h-6 w-6" />
                ) : (
                  <ChevronDownIcon className="h-6 w-6" />
                )}
              </button>
            </div>
            {isHospitalizedReportsOpen && (
              <div className="mb-4">
                <table className="table-auto border-collapse w-full">
                  <thead>
                    <tr>
                      <th className="border px-4 py-2">Date</th>
                      <th className="border px-4 py-2">Disease</th>
                      <th className="border px-4 py-2">Category</th>
                      <th className="border px-4 py-2">Inpatients</th>
                      <th className="border px-4 py-2">People Under Investigation</th>
                    </tr>
                  </thead>
                  <tbody>
                    {hospitalizedReports.map((report, index) => (
                      <tr key={index}>
                        <td className="border px-4 py-2">{report.AnalyticsDate}</td>
                        <td className="border px-4 py-2">{report.Disease}</td>
                        <td className="border px-4 py-2">{report.DiseaseCategory}</td>
                        <td className="border px-4 py-2">{report.HospitalizedInpatientsInHamiltonCounty}</td>
                        <td className="border px-4 py-2">{report.HospitalizedPeopleUnderInvestigationInHamiltonCounty}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
          )}
          
      <div className="mb-4 flex items-center justify-between">
      <h2 className="text-2xl font-semibold">ICU Reports ({icuReports.length})</h2>
        <button onClick={() => toggleSection('icuReports')}>
          {isICUReportsOpen ? (
            <ChevronUpIcon className="h-6 w-6" />
          ) : (
            <ChevronDownIcon className="h-6 w-6" />
          )}
        </button>
      </div>
      {isICUReportsOpen && (
        <div className="mb-4">
          <table className="table-auto border-collapse w-full">
            <thead>
              <tr>
                <th className="border px-4 py-2">Date</th>
                <th className="border px-4 py-2">Disease</th>
                <th className="border px-4 py-2">Category</th>
                <th className="border px-4 py-2">Patients in ICU</th>
              </tr>
            </thead>
            <tbody>
              {icuReports.map((report, index) => (
                <tr key={index}>
                  <td className="border px-4 py-2">{report.AnalyticsDate}</td>
                  <td className="border px-4 py-2">{report.Disease}</td>
                  <td className="border px-4 py-2">{report.DiseaseCategory}</td>
                  <td className="border px-4 py-2">{report.PatientsInICUInCountyHospitals}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <div className="mb-4 flex items-center justify-between">
      <h2 className="text-2xl font-semibold">Death Reports ({deathReports.length})</h2>
        <button onClick={() => toggleSection('deathReports')}>
          {isDeathReportsOpen ? (
            <ChevronUpIcon className="h-6 w-6" />
          ) : (
            <ChevronDownIcon className="h-6 w-6" />
          )}
        </button>
      </div>
      {isDeathReportsOpen && (
        <div className="mb-4">
          <table className="table-auto border-collapse w-full">
            <thead>
              <tr>
                <th className="border px-4 py-2">Date</th>
                <th className="border px-4 py-2">Disease</th>
                <th className="border px-4 py-2">Category</th>
                <th className="border px-4 py-2">Deaths</th>
              </tr>
            </thead>
            <tbody>
              {deathReports.map((report, index) => (
                <tr key={index}>
                  <td className="border px-4 py-2">{report.AnalyticsDate}</td>
                  <td className="border px-4 py-2">{report.Disease}</td>
                  <td className="border px-4 py-2">{report.DiseaseCategory}</td>
                  <td className="border px-4 py-2">{report.Deaths}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <div className="mb-4 flex items-center justify-between">
      <h2 className="text-2xl font-semibold">Vaccination Reports ({vaccinationReports.length})</h2>
        <button onClick={() => toggleSection('vaccinationReports')}>
          {isVaccinationReportsOpen ? (
            <ChevronUpIcon className="h-6 w-6" />
          ) : (
            <ChevronDownIcon className="h-6 w-6" />
          )}
        </button>
      </div>
      {isVaccinationReportsOpen && (
        <div className="mb-4">
          <table className="table-auto border-collapse w-full">
            <thead>
              <tr>
                <th className="border px-4 py-2">Date</th>
                <th className="border px-4 py-2">Disease</th>
                <th className="border px-4 py-2">Category</th>
                <th className="border px-4 py-2">Deaths</th>
              </tr>
            </thead>
            <tbody>
              {vaccinationReports.map((report, index) => (
                <tr key={index}>
                  <td className="border px-4 py-2">{report.AnalyticsDate}</td>
                  <td className="border px-4 py-2">{report.Disease}</td>
                  <td className="border px-4 py-2">{report.DiseaseCategory}</td>
                  <td className="border px-4 py-2">{report.VaccinationCount}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

    </div>
  );
};

export default Dashboard;
