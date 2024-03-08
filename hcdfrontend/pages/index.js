import Dashboard from '../components/GetAll'
import Link from 'next/link';

const HomePage = () => {
  return (
    <div className="flex justify-center items-center p-2 w-full">
      <Link href="/covid">
        <div className="bg-TN-blue p-8 m-4 text-white text-center cursor-pointer flex rounded-md">

        <div className="flex-shrink-0">
            <img
            src="/covid.jpg" 
            alt="Image"
            className="object-cover rounded-md"
            width={500} height={50}
            />
        </div>


        <div className="flex-grow ml-4 text-center">
            <div className="mb-4 text-lg"><b>COVID Disease Data</b></div>
            <div>Click me to see COVID Disease Data</div>
        </div>
        </div>
    </Link>
    </div>
  );
};

export default HomePage;
