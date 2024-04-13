import Dashboard from '../components/GetAll'
import Link from 'next/link';

const HomePage = () => {
  return (
    <div>
      {/* <div className="flex justify-center"> */}
      <div className="grid grid-cols-2 gap-0 justify-center items-center">
        <div className="flex justify-center items-center p-2">
          <Link href="/covid">
            <div className="bg-TN-blue p-6 m-4 text-white text-center cursor-pointer flex rounded-md w-7/8">
              <div className="flex-shrink-0">
                <img
                  src="/covid.jpg"
                  alt="Image"
                  className="object-cover rounded-md"
                  width={300} height={25}
                />
                <div className="flex-grow ml-2 text-center">
                  <div className="mb-3 text-lg font-bold"><b>COVID Disease Data</b></div>
                </div>
              </div>
              {/*<div className="flex-grow ml-4 align-text-bottom">
                <div className="mb-4 text-lg"><b>COVID Disease Data</b></div>
                <div>Click me to see COVID Disease Data</div>
              </div> */}
            </div>
          </Link>
        </div>

        <div className="flex justify-center items-center p-2 w-1/2">
          <Link href="/influenza-like-illness">
            <div className="bg-TN-blue p-6 m-4 text-white text-center cursor-pointer flex rounded-md w-7/8">
              <div className="flex-shrink-0">
                <img
                  src="/Flu banner.png"
                  alt="Image"
                  className="object-cover rounded-md"
                  width={300} height={25}
                />
                <div className="flex-grow ml-2 align-text-bottom">
                  <div className="mb-3 text-lg font-bold"><b>Influenza-like Illness Data</b></div>
                </div>
              </div>
              {/*<div className="flex-grow ml-4 align-text-bottom">
                <div className="mb-4 text-lg"><b>Influenza-like Illness Data</b></div>
                <div>Click me to see Influenza-like Illness Data</div> 
              </div> */}
            </div>
          </Link>
        </div>
      


        <div className="flex justify-center items-center p-2">
          <Link href="/foodborne-illness">
            <div className="bg-TN-blue p-6 m-4 text-white text-center cursor-pointer flex rounded-md w-7/8" >
              <div className="flex-shrink-0">
                <img
                  src="/foodborne.jpg" 
                  alt="Image"
                  className="object-cover rounded-md"
                  width={300} height={25}
                />
                <div className="flex-grow ml-2 text-center">
                  <div className="mb-3 text-lg font-bold"><b>Foodborne Illness Data</b></div>
                </div>
              </div>
              {/*<div className="flex-grow ml-4 text-center">
                <div className="mb-4 text-lg"><b>Foodborne Illness Data</b></div>
                <div>Click me to see Foodborne Illness Data</div>
            </div> */}
            </div>
          </Link>
        </div>

        <div className="flex justify-center items-center p-2 w-1/2">
          <Link href="/sexually-transmitted-diseases">
            <div className="bg-TN-blue p-6 m-4 text-white text-center cursor-pointer flex rounded-md w-7/8" >
              <div className="flex-shrink-0">
                <img
                  src="/std.png" 
                  alt="Image"
                  className="object-cover rounded-md"
                  width={300} height={25}
                />
                <div className="flex-grow ml-2 text-center">
                  <div className="mb-3 text-lg font-bold"><b>Sexually Transmitted Disease Data</b></div>
                </div>
              </div>
              {/* <div className="flex-grow ml-4 text-center">
                <div className="mb-4 text-lg"><b>Sexually Transmitted Disease Data</b></div>
                <div>Click me to see Sexually Transmitted Disease Data</div>
              </div> */}
            </div>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
