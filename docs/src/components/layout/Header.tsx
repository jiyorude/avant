import React from 'react';
import Link from 'next/link';
import { IoLogoGithub, IoLogoPython } from 'react-icons/io';
import { MdDownload } from 'react-icons/md';

const Header: React.FC = () => {
    return (
        <header className='fixed left-0 top-0 w-full lg:w-20 shadow-xl'>
            <section className='flex lg:flex-col flex-row'>
                <div className='w-2/5 lg:w-full h-14 lg:h-20 bg-avaBlack select-none'>
                    <Link href="/">
                        <h1 className='text-avaWhite h-full flex justify-center items-center mt-0.5 lg:mt-0 lg:block lg:leading-normal text-center font-avaValorant text-4xl lg:text-6xl'>A</h1>
                    </Link>
                </div>
                <button className='w-1/5 lg:w-full h-14 lg:h-20 mxFlexCenter bg-avaTeal'>
                    <Link href='https://github.com/jiyorude/avant' target='_blank'>
                        <IoLogoGithub size={45} className='fill-avaWhite size-9 lg:size-100' title='GitHub Repository' />
                    </Link>
                </button>
                <button className='h-14 lg:h-20 w-1/5 lg:w-full mxFlexCenter bg-avaRed'>
                    <Link href='https://pypi.org/project/q3avant' target='_blank'>
                        <IoLogoPython size={45} className='fill-avaBlack mr-1.5 size-9 lg:size-100' title='PyPi package' />
                    </Link>
                </button>
                <button className='h-14 lg:h-20 w-1/5 lg:w-full mxFlexCenter bg-avaWhite'>
                    <Link href='https://github.com/jiyorude/avant/releases' target='_blank'>
                        <MdDownload size={45} className='fill-avaGrey size-9 lg:size-100' title='Download latest release' />
                    </Link>
                </button>
            </section>
        </header>
    )
}

export default Header;