// components/Dashboard.js

import { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [diseaseCategories, setDiseaseCategories] = useState([]);
  const [diseases, setDiseases] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://hcdbackend.fly.dev/dataportal/_query');
        const { DiseaseCategories, Diseases } = response.data;
    
        setDiseaseCategories(DiseaseCategories);
        setDiseases(Diseases);
      } catch (error) {
        console.error('Error fetching data:', error);
        console.error('Response status:', error.response?.status);
        console.error('Response data:', error.response?.data);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="container mx-auto text-black p-4">
      <h2 className="text-2xl text-black font-semibold mb-4">Disease Categories</h2>
      <table className="table-auto border-collapse w-full mb-8">
        <thead>
          <tr>
            <th className="border px-4 py-2">Category</th>
            <th className="border px-4 py-2">Description</th>
          </tr>
        </thead>
        <tbody>
          {diseaseCategories.map((category, index) => (
            <tr key={index}>
              <td className="border px-4 py-2">{category.name}</td>
              <td className="border px-4 py-2">{category.description}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2 className="text-2xl text-black font-semibold mb-4">Diseases</h2>
      {diseases.length > 0 ? (
        <div>
          {diseaseCategories.map((category, index) => (
            <div key={index} className="mb-4">
              <h3 className="text-xl text-black font-semibold">{category.name}</h3>
              <table className="table-auto border-collapse w-full">
                <thead>
                  <tr>
                    <th className="border px-4 py-2">Name</th>
                    <th className="border px-4 py-2">Description</th>
                  </tr>
                </thead>
                <tbody>
                  {diseases
                    .filter((disease) => disease.diseaseCategory === category.name)
                    .map((disease, index) => (
                      <tr key={index}>
                        <td className="border px-4 py-2">{disease.name}</td>
                        <td className="border px-4 py-2">{disease.description}</td>
                      </tr>
                    ))}
                </tbody>
              </table>
            </div>
          ))}
        </div>
      ) : (
        <p>Loading diseases...</p>
      )}
    </div>
  );
};

export default Dashboard;
