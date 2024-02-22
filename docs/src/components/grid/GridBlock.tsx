import React, { ReactElement } from 'react';
import Link from 'next/link';
import { IoIosArrowForward } from 'react-icons/io';

interface GridBlockProps {
  icon: ReactElement;
  header: string;
  subtext: string;
  linkTo: string;
}

const GridBlock: React.FC<GridBlockProps> = ({ icon, header, subtext, linkTo }) => {
  return (
    <Link href={linkTo} passHref>
        <button className="group mx-auto bg-avaWhite max-w-96 p-6 rounded-lg flex flex-col justify-between h-full hover:cursor-pointer mb-4">
        <header className="flex items-center space-x-6">
            <div className="fill-avaTeal">{icon}</div>
            <h2 className="text-xl leading-loose font-semibold text-avaTeal">{header}</h2>
        </header>
        <main className="mt-4 pr-8 text-left text-sm text-pretty">
            {subtext}
        </main>
        <footer className="flex justify-end">
            <figure className="flex justify-end items-center">
                <IoIosArrowForward className="text-lg group-hover:text-avaTeal group-hover:translate-x-2.5 duration-200 ease-in-out transition-all" />
            </figure>
        </footer>
        </button>
    </Link>
  );
};

export default GridBlock;
