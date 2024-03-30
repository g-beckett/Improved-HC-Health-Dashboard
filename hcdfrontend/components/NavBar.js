// components/NavBar.js
import Link from 'next/link';
import React, { useState } from 'react';

const NavigationBar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="relative">
      <div className="absolute inset-0 z-0">
        <img
          src="/chattanooga.jpg"
          alt="Background"
          className="w-full h-full object-cover filter blur-sm"
        />
      </div>

      <div className="relative z-10 bg-opacity-50 bg-gray-700 p-4 flex flex-wrap justify-between">
        <div className="flex w-1/3 items-center">
          <Link href='/'>
            <img
              src="/hc_logo.svg"
              alt="Logo"
              className="h-40 w-full"
            />
          </Link>
        </div>
        <span className="flex w-1/3 items-center justify-center text-center text-white text-base sm:text-md md:text-xl xl:text-4xl font-semibold p-4">Hamilton County Public Health Dashboard</span>
        <div className="flex w-1/3 items-center justify-end relative">
          <button
            id="dropdownDefaultButton"
            onClick={toggleDropdown}
            className="mr-5 text-gray-300 bg-gray-700 hover:bg-gray-600 focus:ring-4 focus:outline-none focus:bg-gray-600 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center"
            type="button" > Navigation
            <svg
              className="w-2.5 h-2.5 ms-3 text-gray-300"
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
              className="z-10 absolute top-24 mt-1 bg-gray-700 divide-y divide-gray-800 rounded-lg shadow"
            >
              <ul
                className="py-2 text-sm text-gray-300"
                aria-labelledby="dropdownDefaultButton"
              >
                <li>
                  <a href="/"
                    className="block px-4 py-2 hover:bg-gray-600 dark:hover:text-white"
                  > Home
                  </a>
                </li>
                <li>
                  <a href="/covid"
                    className="block px-4 py-2 hover:bg-gray-600 dark:hover:text-white"
                  > COVID-19
                  </a>
                </li>
                <li>
                  <a href="/influenza-like-illness"
                    className="block px-4 py-2 hover:bg-gray-600 dark:hover:text-white"
                  > Influenza Like Illnesses
                  </a>
                </li>
                <li>
                  <a href="/foodborne-illness"
                    className="block px-4 py-2 hover:bg-gray-600 dark:hover:text-white"
                  > Foodborne Illnesses
                  </a>
                </li>
                <li>
                  <a href="/sexually-transmitted-diseases"
                    className="block px-4 py-2 hover:bg-gray-600 dark:hover:text-white"
                  > STDs
                  </a>
                </li>
              </ul>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default NavigationBar;
