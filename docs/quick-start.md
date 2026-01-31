# QueryForge - Quick Start Tech Stack

## 🎯 One-Page Reference for 10 Users (Free Tier)

---

## Core Stack (Copy-Paste Ready)

### Frontend
```json
{
  "framework": "Next.js 14+ (App Router)",
  "language": "TypeScript",
  "styling": "Tailwind CSS",
  "components": "shadcn/ui",
  "state": "Zustand",
  "forms": "React Hook Form + Zod",
  "charts": "Recharts",
  "icons": "Lucide React"
}
```

### Backend
```json
{
  "runtime": "Node.js v20",
  "api": "Next.js API Routes",
  "orm": "Prisma",
  "validation": "Zod"
}
```

### Database & Storage
```json
{
  "database": "Neon (PostgreSQL) - Free 0.5GB",
  "cache": "Upstash Redis - Free 10K commands/day",
  "files": "Vercel Blob - Free 1GB"
}
```

### Services
```json
{
  "auth": "Clerk - Free 10K MAUs",
  "ai": "Google Gemini Flash - Free 1,500 req/day",
  "email": "Resend - Free 3K emails/month",
  "hosting": "Vercel - Free 100GB bandwidth",
  "errors": "Sentry - Free 5K errors/month",
  "uptime": "UptimeRobot - Free"
}
```

---

## 📦 Package.json Dependencies

```json
{
  "dependencies": {
    "next": "^14.2.0",
    "react": "^18.3.0",
    "react-dom": "^18.3.0",
    "@clerk/nextjs": "^5.0.0",
    "@prisma/client": "^5.18.0",
    "@upstash/redis": "^1.34.0",
    "@google/generative-ai": "^0.17.0",
    "resend": "^4.0.0",
    "zod": "^3.23.0",
    "zustand": "^4.5.0",
    "react-hook-form": "^7.53.0",
    "@hookform/resolvers": "^3.9.0",
    "recharts": "^2.12.0",
    "lucide-react": "^0.441.0",
    "tailwindcss": "^3.4.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.5.0"
  },
  "devDependencies": {
    "typescript": "^5.5.0",
    "@types/node": "^22.0.0",
    "@types/react": "^18.3.0",
    "prisma": "^5.18.0",
    "eslint": "^8.57.0",
    "prettier": "^3.3.0"
  }
}
```

---

## 🚀 Setup Commands

### 1. Create Next.js Project
```bash
npx create-next-app@latest queryforge --typescript --tailwind --app --src-dir --import-alias "@/*"
cd queryforge
```

### 2. Install Dependencies
```bash
npm install @clerk/nextjs @prisma/client @upstash/redis @google/generative-ai resend zod zustand react-hook-form @hookform/resolvers recharts lucide-react class-variance-authority clsx tailwind-merge

npm install -D prisma @types/node
```

### 3. Initialize Prisma
```bash
npx prisma init
```

### 4. Install shadcn/ui
```bash
npx shadcn-ui@latest init
```

### 5. Add shadcn Components
```bash
npx shadcn-ui@latest add button input card table dialog toast dropdown-menu tabs accordion badge avatar tooltip
```

---

## 🔑 Environment Variables

Create `.env.local`:
```env
# Database (Neon)
DATABASE_URL="postgresql://user:password@host.neon.tech/dbname?sslmode=require"

# Redis (Upstash)
UPSTASH_REDIS_REST_URL="https://your-redis.upstash.io"
UPSTASH_REDIS_REST_TOKEN="your-token"

# Auth (Clerk)
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="pk_test_..."
CLERK_SECRET_KEY="sk_test_..."
NEXT_PUBLIC_CLERK_SIGN_IN_URL="/sign-in"
NEXT_PUBLIC_CLERK_SIGN_UP_URL="/sign-up"

# AI (Gemini)
GEMINI_API_KEY="AIza..."

# Email (Resend)
RESEND_API_KEY="re_..."

# Error Tracking (Sentry)
SENTRY_DSN="https://...@sentry.io/..."

# App
NEXT_PUBLIC_APP_URL="http://localhost:3000"
```

---

## 🗄️ Prisma Schema (Starter)

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id            String    @id @default(cuid())
  clerkId       String    @unique
  email         String    @unique
  name          String?
  role          Role      @default(USER)
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  queries       Query[]
  feedback      Feedback[]
}

enum Role {
  USER
  ADMIN
}

model Query {
  id                String    @id @default(cuid())
  userId            String
  user              User      @relation(fields: [userId], references: [id], onDelete: Cascade)
  naturalLanguage   String
  generatedSQL      String
  tablesUsed        String[]
  responseTime      Int       // milliseconds
  rowsReturned      Int?
  status            QueryStatus
  errorMessage      String?
  createdAt         DateTime  @default(now())
  feedback          Feedback?
}

enum QueryStatus {
  SUCCESS
  FAILED
  WARNING
}

model Feedback {
  id        String   @id @default(cuid())
  queryId   String   @unique
  query     Query    @relation(fields: [queryId], references: [id], onDelete: Cascade)
  userId    String
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  rating    Int      // 1-5 or thumbs up/down
  comment   String?
  createdAt DateTime @default(now())
}

model DatabaseConnection {
  id          String   @id @default(cuid())
  name        String
  dialect     String   // postgresql, mysql, sqlserver
  host        String
  port        Int
  database    String
  username    String
  password    String   // Encrypted
  isPrimary   Boolean  @default(false)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}
```

---

## 📁 Project Structure

```
queryforge/
├── app/
│   ├── (auth)/
│   │   ├── sign-in/[[...sign-in]]/page.tsx
│   │   └── sign-up/[[...sign-up]]/page.tsx
│   ├── (dashboard)/
│   │   ├── layout.tsx
│   │   ├── page.tsx                    # Dashboard home
│   │   ├── sandbox/page.tsx            # Query sandbox
│   │   ├── history/page.tsx            # Query history
│   │   ├── settings/page.tsx           # User settings
│   │   └── admin/
│   │       ├── users/page.tsx
│   │       ├── logs/page.tsx
│   │       └── feedback/page.tsx
│   ├── api/
│   │   ├── query/route.ts              # Execute NL query
│   │   ├── feedback/route.ts
│   │   └── webhooks/clerk/route.ts
│   ├── layout.tsx
│   └── page.tsx                        # Landing page
├── components/
│   ├── ui/                             # shadcn components
│   ├── dashboard/
│   │   ├── query-input.tsx
│   │   ├── results-table.tsx
│   │   └── stats-card.tsx
│   ├── theme-provider.tsx
│   └── theme-toggle.tsx
├── lib/
│   ├── db.ts                           # Prisma client
│   ├── redis.ts                        # Upstash client
│   ├── ai.ts                           # Gemini AI
│   ├── email.ts                        # Resend
│   └── utils.ts
├── prisma/
│   └── schema.prisma
├── public/
├── styles/
│   └── globals.css
└── types/
    └── index.ts
```

---

## 🎨 Tailwind Config (Dark Mode)

```javascript
// tailwind.config.js
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        // Dark mode colors
        background: "hsl(222.2 84% 4.9%)",      // #0F172A
        foreground: "hsl(210 40% 98%)",         // #F8FAFC
        card: "hsl(217.2 32.6% 17.5%)",         // #1E293B
        "card-foreground": "hsl(210 40% 98%)",
        primary: "hsl(217.2 91.2% 59.8%)",      // #3B82F6
        "primary-foreground": "hsl(222.2 47.4% 11.2%)",
        // ... add more colors from design-system
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
```

---

## 🔌 Service Setup Links

| Service | Setup URL | Free Tier |
|---------|-----------|-----------|
| **Neon** | https://neon.tech | 0.5 GB database |
| **Upstash** | https://upstash.com | 10K commands/day |
| **Clerk** | https://clerk.com | 10K MAUs |
| **Gemini** | https://ai.google.dev | 1,500 req/day |
| **Resend** | https://resend.com | 3K emails/month |
| **Vercel** | https://vercel.com | 100 GB bandwidth |
| **Sentry** | https://sentry.io | 5K errors/month |
| **UptimeRobot** | https://uptimerobot.com | 50 monitors |

---

## ⚡ Quick Deploy to Vercel

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/queryforge.git
git push -u origin main

# 2. Deploy to Vercel (one command)
npx vercel

# 3. Add environment variables in Vercel dashboard
# 4. Done! Your app is live
```

---

## 🧪 Development Workflow

```bash
# Start dev server
npm run dev

# Run database migrations
npx prisma migrate dev

# Generate Prisma client
npx prisma generate

# Open Prisma Studio (database GUI)
npx prisma studio

# Lint code
npm run lint

# Format code
npm run format

# Build for production
npm run build
```

---

## 📊 Free Tier Limits Summary

| Resource | Limit | Per User (10) | Status |
|----------|-------|---------------|--------|
| Database | 0.5 GB | 50 MB | ✅ |
| Bandwidth | 100 GB/mo | 10 GB | ✅ |
| Redis | 10K cmd/day | 1K | ✅ |
| AI Queries | 1,500/day | 150 | ✅ |
| Emails | 3K/month | 300 | ✅ |
| Errors | 5K/month | 500 | ✅ |

**Total Monthly Cost: $0** 🎉

---

## 🚨 Important Notes

1. **Never commit `.env.local`** - Add to `.gitignore`
2. **Use environment variables in Vercel** - Don't hardcode secrets
3. **Enable Prisma Data Proxy** - For serverless (Neon handles this)
4. **Monitor usage** - Check dashboards weekly
5. **Backup database** - Export weekly as safety measure

---

## 📚 Essential Documentation

- Next.js: https://nextjs.org/docs
- Tailwind: https://tailwindcss.com/docs
- shadcn/ui: https://ui.shadcn.com
- Prisma: https://www.prisma.io/docs
- Clerk: https://clerk.com/docs
- Gemini: https://ai.google.dev/docs

---

## 🎯 Next Steps

1. ✅ Set up all services (30 minutes)
2. ✅ Clone starter template or create from scratch (1 hour)
3. ✅ Configure environment variables (15 minutes)
4. ✅ Deploy to Vercel (10 minutes)
5. ✅ Test with sample queries (30 minutes)
6. ✅ Invite first users (5 minutes)

**Total setup time: ~2-3 hours** ⚡

---

## 💡 Pro Tips

- Use Vercel's preview deployments for testing
- Set up GitHub Actions for automated testing
- Use Prisma Studio for database management
- Monitor Sentry daily for errors
- Check UptimeRobot for downtime alerts
- Keep dependencies updated monthly

---

**Ready to build? Start with:**
```bash
npx create-next-app@latest queryforge
```

🚀 **Let's go!**
