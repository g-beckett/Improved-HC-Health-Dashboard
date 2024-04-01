 /**
  * layout.js -- sets layout for pages
  * allows for consistent topnav and footer
  */
import Head from 'next/head';
import NavBar from '../components/NavBar';
 
export default function Layout({ children }) {
return (
  <>
    <NavBar />
    <div className="relative h-full bg-gray-300 z-1">
    <div className="relative top-0 left-0 right-0 h-4 bg-TN-blue"></div>

    <Head>
      <title>Hamilton County Health Dashboard</title>
      <link rel="icon" href='/hc_logo.svg'/>
    </Head>
      <main>{children}</main>
    </div>
  </>
)
}