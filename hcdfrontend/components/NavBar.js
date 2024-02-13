// components/Navbar.js
import Link from 'next/link'

const NavigationBar = () => {
  return (
    <nav className="bg-TN-blue p-4 flex items-center justify-between">
      <div className="flex items-center">
        <Link href ='/'>
        <img
          src="/tndh.svg"  
          alt="Logo"
          className="h-24 w-full" 
          />
          </Link>
        {/* <span className="text-white text-lg font-semibold">Hamilton County Health</span> */}
      </div>

      <span className="text-TN-font text-3xl font-semibold">Public Health Dashboard</span>

      <div className="flex items-center">
        <input
          type="text"
          placeholder="Search"
          className="border border-gray-300 p-2 rounded-md"
        />
      </div>
    </nav>
  );
};

export default NavigationBar;
