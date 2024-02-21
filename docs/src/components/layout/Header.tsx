import React from 'react';

const Header: React.FC = () => {
    return (
        <header className=' bg-[#f5f5f5] flex flex-row shadow-lg'>
            <section className='w-20 h-20 bg-[#131313] select-none'>
                <h1 className='text-avaWhite h-full leading-normal w-full text-center font-avaValorant text-6xl'>A</h1>
            </section>
            <section className='border-4 h-20 container flex justify-end items-center border-red-500'>
                <button className='p-1 px-4 rounded mr-6 bg-avaRed'>Download</button>
            </section>
           
            
        </header>
    )
}

export default Header;