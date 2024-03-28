// components/NavBar.js
import Link from 'next/link'
import React, {useState} from 'react';


const NavigationBar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="bg-TN-blue p-4 flex flex-wrap relative  justify-between">
      <div className="flex w-1/5 items-center">
        <Link href ='/'>
        <img
          src="/hc_logo.svg"  
          alt="Logo"
          className="h-40 w-full" 
          />
          </Link>
      </div>

      <span className=" flex w-1/3 items-center text-center text-white text-base sm:text-sm md:text-lg xl:text-4xl font-semibold p-4">Hamilton County Public Health Dashboard</span>

      <div className="flex w-1/3 items-center">
        <input
          type="text"
          placeholder="Search"
          className="border border-gray-300 p-2 rounded-md text-black"
        />
      </div>
      
    <div className = "flex flex-col w-1/3 items-center"></div>
      {/* <div className = "flex w-1/3 items-center"></div> */}
        <div className = "flex flex-col w-1/3 items-center absoulte bottom-6 right-0 mt-0 mr-20 overflow-y-auto max-h-[80vh]"style={{ marginTop: '-40px' }}>
          <button
            id="dropdownDefaultButton"
            onClick={toggleDropdown}
            className="text-white bg-TN-blue hover:bg-TN-blue focus:ring-4 focus:outline-none focus:bg-TN-blue font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-TN-blue dark:hoverbg-TN-blue dark:focus:bg-TN-blue"
            type="button" > Dashboard
              <svg
              className="w-2.5 h-2.5 ms-3"
              aria-hidden="true"
              fill="none"
              viewBox="0 0 10 6"
              > <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m1 1 4 4 4-4"
              />
            </svg>
          </button>

          {isOpen && (
            <div
              id="dropdown"
              className="z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700"
            > <ul
                className="py-2 text-sm text-gray-700 dark:text-gray-200"
                aria-labelledby="dropdownDefaultButton"
              > <li>
                <a href="/"
                    className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  > Main
                  </a>
                </li> <li>
                  <a href="/covid"
                    className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  > COVID
                  </a>
                </li> <li>
                  <a href="/influenza-like-illness"
                    className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  > Influenza Like Illnesses
                  </a>
                </li> <li>
                  <a href="/foodborne-illness"
                    className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  > Foodborne Illnesses
                  </a>
                </li> <li>
                  <a href="/sexually-transmitted-diseases"
                    className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  > STDs
                  </a>
                </li>
              </ul>
            </div>
          )}
      </div>
    </nav>
  );
};

export default NavigationBar;
