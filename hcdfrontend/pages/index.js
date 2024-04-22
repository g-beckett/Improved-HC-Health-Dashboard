import Link from 'next/link';

const HomePage = () => {
  return (
    <div className="bg-gray-100 min-h-screen">
      <div className="max-w-6xl mx-auto px-4 py-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {/* Site Description Section */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden lg:col-span-2">
          <div className="p-6">
            <h2 className="text-2xl font-semibold mb-4 text-TN-blue">Improved Hamilton County Health Dashboard</h2>
            <p className="text-gray-700">
              This improved health dashboard was created in partnership with Hamilton County Health for CPSC 4910 UTC Spring 2024 Capstone Project by Lindsay Easterwood, Gabrielle Beckett, Cody Major, Brady Moore, Victoria Martino, and Cody Whitt. <br/> <br/>
              
              The motivation for this project was to create a health dashboard that makes navigating health and disease data and information easier to consume and more accessible for the citizens and health professionals of Hamilton County. <br/> <br/>

              Choose a disease category to view detailed information about reported cases, deaths, and more.
            </p>
          </div>
        </div>

        {/* Left Section */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden transform transition duration-300 hover:scale-105">
          <div className="mb-4">
            <img
              src="/covid.jpg"
              alt="COVID-19"
              className="object-cover w-full h-64"
            />
          </div>
          <Link href="/covid">
            <div className="bg-TN-blue text-white text-center py-2 px-4 hover:bg-gray-700 transition duration-300 cursor-pointer">
              <span className="text-lg font-semibold">View COVID-19 Disease Data</span>
            </div>
          </Link>
        </div>

        {/* Right Section */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden transform transition duration-300 hover:scale-105">
          <div className="mb-4">
            <img
              src="/flu_home.jpg"
              alt="Influenza-like Illness"
              className="object-cover w-full h-64"
            />
          </div>
          <Link href="/influenza-like-illness">
            <div className="bg-TN-blue text-white text-center py-2 px-4 hover:bg-gray-700 transition duration-300 cursor-pointer">
              <span className="text-lg font-semibold">View Influenza-like Illness Data</span>
            </div>
          </Link>
        </div>

        {/* Left Section */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden transform transition duration-300 hover:scale-105">
          <div className="mb-4">
            <img
              src="/foodborne.jpg"
              alt="Foodborne Illness"
              className="object-cover w-full h-64"
            />
          </div>
          <Link href="/foodborne-illness">
            <div className="bg-TN-blue text-white text-center py-2 px-4 hover:bg-gray-700 transition duration-300 cursor-pointer">
              <span className="text-lg font-semibold">View Foodborne Illness Data</span>
            </div>
          </Link>
        </div>

        {/* Right Section */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden transform transition duration-300 hover:scale-105">
          <div className="mb-4">
            <img
              src="/std.png"
              alt="Sexually Transmitted Diseases"
              className="object-cover w-full h-64"
            />
          </div>
          <Link href="/sexually-transmitted-diseases">
            <div className="bg-TN-blue text-white text-center py-2 px-4 hover:bg-gray-700 transition duration-300 cursor-pointer">
              <span className="text-lg font-semibold">View STI Data</span>
            </div>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
