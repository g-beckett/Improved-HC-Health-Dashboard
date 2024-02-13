import styles from './_app.js';
import React, { useState, useEffect } from 'react';
import Head from 'next/head';
import Image from 'next/image';


export default function Home() {
  
  /** PAGE CONTENT */
  
  return (
    <div className="relative h-screen bg-gray-300">
      <Head>
        <title>Hamilton County Health Dashboard</title>
        <link rel="icon" src='tndh.svg'/>
      </Head>
      
      {/* <div className='flex-center text-center text-4xl justify-center w-full'>
        <Image src='/chatt.jpg' width={400} height={400} alt='Image of Chattanooga River'/>
      </div> */}

      </div>

  );
}