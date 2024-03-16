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
    <Head>
      <title>Hamilton County Health Dashboard</title>
      <link rel="icon" href='/hc_logo.svg'/>
    </Head>
      <main>{children}</main>
    </div>
  </>
)
}