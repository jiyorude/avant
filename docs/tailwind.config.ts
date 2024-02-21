import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        'avaBlack': '#131313',
        'avaRed': '#990404',
        'avaWhite': '#f5f5f0',
      },
      fontFamily: {
        'avaValorant': 'Valorant',
        'avaLight': 'Gantari-Light',
        'avaRegular': 'Gantari-Regular',
        'avaItalic': 'Gantari-Italic',
        'avaSemiBold': 'Gantari-SemiBold',
        'avaBold': 'Gantari-Bold',
      },
    },
  },
  plugins: [],
};
export default config;
