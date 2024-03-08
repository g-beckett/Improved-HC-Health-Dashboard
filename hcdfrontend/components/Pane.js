import Link from 'next/link'

const Pane = () => {
    <Link href="/covid">
        <div className="bg-TN-blue p-8 m-4 text-white text-center cursor-pointer flex rounded-md">

        <div className="flex-shrink-0">
            <img
            src="/chattanooga.jpg" 
            alt="Image"
            className="h-full object-cover rounded-md"
            />
        </div>


        <div className="flex-grow ml-4 text-left">
            <div className="mb-4">Information Title</div>
            <div>Click me for Destination Page</div>
        </div>
        </div>
    </Link>
}

export default Pane;