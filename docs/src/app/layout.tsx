import type { Metadata } from "next";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import "./globals.css";

export const metadata: Metadata = {
  title: "Avant | Experimental Quake III Machinima Algorithm",
  description: "Random-data generating algorithm for experimental Quake III machinima (post-)production.",
  keywords: "avant, avant-garde, game art, videogame art, algorithm, python, software, mit license, experiment, experimental, experimental film, game movie, in-game film, in-game, game engine, videogames, meaning-making videogames, machinima, quake modding, quake mod, quake 3 modding, quake 3 mod, machinima production, rng, random data generator, quake 3 arena, quake, quake 3, quake iii arena, tool",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Header />
        <main className="pt-20 lg:pt-12">
          {children}
        </main>
        <Footer />  
      </body>
    </html>
  );
}
