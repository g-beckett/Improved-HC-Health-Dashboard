 /**
  * layout.js -- sets layout for pages
  * allows for consistent topnav and footer
  */
 
 import NavBar from '../components/NavBar';
 
 export default function Layout({ children }) {
  return (
    <>
      <NavBar />
        <main>{children}</main>
    </>
  )
}