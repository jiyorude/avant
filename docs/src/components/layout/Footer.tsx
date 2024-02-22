import React from 'react';

const Footer: React.FC = () => {
    const now = new Date().getFullYear();
    
    return (
    <footer className="w-full bg-avaBlack fixed bottom-0 left-0 right-0 shadow-inner h-8 flex items-center">
        <section className='flex mx-auto container h-full justify-center flex-row pb-0.5'>
        <div className='flex items-center px-4 text-avaWhite font-avaSemiBold text-[10px] lg:text-xs'>
                <p>&copy; Jordy Veenstra {now}</p>
            </div>
            <div className='flex items-center px-4 text-avaWhite font-avaLight text-[10px] lg:text-xs'>
                <p>V0.2.0</p>
            </div>
            <div className='flex items-center px-4 text-avaWhite font-avaLight text-[10px] lg:text-xs'>
                <p>Licensed under MIT</p>
            </div>
        </section>
    </footer>
    )
};

export default Footer;