# QueryForge Frontend

Next.js 14 frontend for QueryForge - Natural Language to SQL SaaS application.

## Setup

1. **Install dependencies:**
```bash
npm install
```

2. **Configure environment variables:**
```bash
cp .env.example .env.local
# Edit .env.local and add your API keys
```

3. **Run development server:**
```bash
npm run dev
```

4. **Open browser:**
```
http://localhost:3000
```

## Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx      # Root layout
│   │   ├── page.tsx        # Landing page
│   │   └── globals.css     # Global styles
│   ├── components/
│   │   └── ui/             # shadcn/ui components
│   ├── lib/                # Utilities
│   └── types/              # TypeScript types
├── public/                 # Static assets
├── package.json
├── tsconfig.json
├── tailwind.config.ts
├── next.config.mjs
└── .env.example
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Check TypeScript types

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **State Management**: Zustand
- **Forms**: React Hook Form + Zod
- **Charts**: Recharts
- **Icons**: Lucide React
- **Auth**: Clerk
- **HTTP Client**: Axios

## Adding shadcn/ui Components

```bash
npx shadcn-ui@latest init
npx shadcn-ui@latest add button
npx shadcn-ui@latest add input
npx shadcn-ui@latest add card
# etc.
```

## Deployment

See main project documentation for deployment instructions.
