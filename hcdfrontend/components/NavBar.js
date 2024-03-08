// components/NavBar.js
import Link from 'next/link'

const NavigationBar = () => {
  return (
    <nav className="bg-TN-blue p-4 flex items-center justify-between">
      <div className="flex items-center">
        <Link href ='/'>
        <img
          src="/tndhw.svg"  
          alt="Logo"
          className="h-24 w-full" 
          />
          </Link>
      </div>

      <span className="text-white text-base sm:text-sm md:text-lg xl:text-4xl font-semibold p-4">Hamilton County Public Health Dashboard</span>

      <div className="flex items-center">
        <input
          type="text"
          placeholder="Search"
          className="border border-gray-300 p-2 rounded-md text-black"
        />
      </div>
    </nav>
  );
};

export default NavigationBar;
