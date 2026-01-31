import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Dark mode colors (default)
        background: "hsl(222.2 84% 4.9%)", // #0F172A
        foreground: "hsl(210 40% 98%)", // #F8FAFC
        card: "hsl(217.2 32.6% 17.5%)", // #1E293B
        "card-foreground": "hsl(210 40% 98%)",
        popover: "hsl(217.2 32.6% 17.5%)",
        "popover-foreground": "hsl(210 40% 98%)",
        primary: "hsl(217.2 91.2% 59.8%)", // #3B82F6
        "primary-foreground": "hsl(222.2 47.4% 11.2%)",
        secondary: "hsl(217.2 32.6% 17.5%)",
        "secondary-foreground": "hsl(210 40% 98%)",
        muted: "hsl(217.2 32.6% 17.5%)",
        "muted-foreground": "hsl(215 20.2% 65.1%)",
        accent: "hsl(217.2 32.6% 17.5%)",
        "accent-foreground": "hsl(210 40% 98%)",
        destructive: "hsl(0 62.8% 30.6%)",
        "destructive-foreground": "hsl(210 40% 98%)",
        border: "hsl(217.2 32.6% 17.5%)",
        input: "hsl(217.2 32.6% 17.5%)",
        ring: "hsl(217.2 91.2% 59.8%)",
      },
      borderRadius: {
        lg: "0.5rem",
        md: "calc(0.5rem - 2px)",
        sm: "calc(0.5rem - 4px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
};

export default config;
