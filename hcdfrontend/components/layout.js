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
    <div className="relative h-screen bg-gray-300 -z-1">
    <Head>
      <title>Hamilton County Health Dashboard</title>
      <link rel="icon" href='/tn.png'/>
    </Head>
      <main>{children}</main>
    </div>
  </>
)
}