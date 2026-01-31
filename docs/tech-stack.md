# QueryForge - Tech Stack Documentation
## Optimized for Free Tier (10 Users, Zero Cost, Zero Downtime)

---

## Executive Summary

This tech stack is carefully selected to support **10 concurrent users** with:
- ✅ **Zero monthly costs**
- ✅ **Zero downtime** (99.9%+ uptime)
- ✅ **Production-ready** performance
- ✅ **Scalable** architecture (easy to upgrade when needed)

All services selected have generous free tiers that will comfortably handle 10 users without hitting limits.

---

## 1. Frontend Stack

### **Framework: Next.js 14+ (App Router)**
- **Cost**: Free (open source)
- **Why**: 
  - Server-side rendering for better SEO
  - Built-in API routes (reduces backend complexity)
  - Excellent performance with React Server Components
  - Strong TypeScript support
  - Easy deployment to free hosting platforms

### **Language: TypeScript**
- **Cost**: Free
- **Why**: Type safety, better developer experience, fewer runtime errors

### **Styling: Tailwind CSS**
- **Cost**: Free (open source)
- **Why**: 
  - Utility-first CSS framework
  - Perfect for dark/light mode theming
  - Smaller bundle sizes than component libraries
  - Highly customizable
  - No runtime cost
- **Alternative Considered**: Vanilla CSS (also free, but slower development)

### **UI Components: shadcn/ui**
- **Cost**: Free (copy-paste components)
- **Why**:
  - Not a dependency (you own the code)
  - Built on Radix UI (accessible primitives)
  - Fully customizable
  - Dark mode support out of the box
  - Modern, production-ready components
- **Components to Use**:
  - Button, Input, Card, Table, Modal, Toast, Dropdown, Tabs
  - All components support dark/light themes

### **Icons: Lucide React**
- **Cost**: Free (open source)
- **Why**: Lightweight, tree-shakeable, modern icon set

### **Charts & Visualizations: Recharts**
- **Cost**: Free (open source)
- **Why**: 
  - React-based charting library
  - Good for analytics dashboards
  - Responsive and customizable
  - Works well with dark/light themes

### **State Management: Zustand**
- **Cost**: Free (open source)
- **Why**: 
  - Lightweight (1kb)
  - Simple API
  - Perfect for theme state, user preferences
  - No boilerplate like Redux

### **Form Handling: React Hook Form**
- **Cost**: Free (open source)
- **Why**: Performant, easy validation, minimal re-renders

### **Validation: Zod**
- **Cost**: Free (open source)
- **Why**: TypeScript-first schema validation, works great with React Hook Form

---

## 2. Backend Stack

### **Runtime: Node.js (v20 LTS)**
- **Cost**: Free
- **Why**: JavaScript everywhere, huge ecosystem, excellent for I/O operations

### **API Framework: Next.js API Routes**
- **Cost**: Free (built into Next.js)
- **Why**: 
  - No separate backend needed
  - Serverless functions (scales to zero)
  - Easy to deploy
  - Built-in middleware support

### **ORM: Prisma**
- **Cost**: Free (open source)
- **Why**:
  - Type-safe database access
  - Excellent TypeScript support
  - Auto-generated types
  - Database migrations
  - Works with PostgreSQL, MySQL, SQLite

### **API Documentation: TypeScript + JSDoc**
- **Cost**: Free
- **Why**: Self-documenting code, no need for Swagger/OpenAPI initially

---

## 3. Database Stack

### **Primary Database: Neon (PostgreSQL)**
- **Cost**: **FREE TIER**
  - 0.5 GB storage (enough for 10 users)
  - Unlimited compute hours
  - 1 project
  - Serverless PostgreSQL
- **Why**:
  - True PostgreSQL (not limited like some free tiers)
  - Serverless (scales to zero, no idle costs)
  - Auto-scaling
  - Built-in connection pooling
  - 99.95% uptime SLA
  - Branching for dev/staging environments
- **Alternative**: **Supabase** (also has generous free tier with 500MB database)

### **Caching: Upstash Redis**
- **Cost**: **FREE TIER**
  - 10,000 commands/day (plenty for 10 users)
  - 256 MB storage
  - Serverless Redis
- **Why**:
  - Query result caching
  - Session storage
  - Rate limiting
  - No idle costs
  - Global replication

### **File Storage: Vercel Blob (or Cloudflare R2)**
- **Cost**: **FREE TIER**
  - Vercel Blob: 1 GB storage (free on Hobby plan)
  - Cloudflare R2: 10 GB storage, 1M requests/month
- **Why**: For storing user avatars, exported reports, etc.

---

## 4. Authentication & Authorization

### **Auth Provider: Clerk**
- **Cost**: **FREE TIER**
  - Up to 10,000 monthly active users (MAUs)
  - Unlimited sign-ups
  - Email/password + OAuth (Google, GitHub, etc.)
  - Session management
  - User management UI
- **Why**:
  - Drop-in authentication
  - Beautiful pre-built UI components
  - Dark mode support
  - 2FA included
  - Role-based access control (RBAC)
  - Webhooks for user events
  - No backend auth code needed
- **Alternative**: **Supabase Auth** (also free, but less polished UI)

### **Authorization: CASL**
- **Cost**: Free (open source)
- **Why**: Isomorphic authorization, works on frontend and backend

---

## 5. AI/LLM Integration (Natural Language to SQL)

### **Primary LLM: OpenAI GPT-4o-mini**
- **Cost**: **PAY-AS-YOU-GO** (Very affordable for 10 users)
  - $0.150 per 1M input tokens
  - $0.600 per 1M output tokens
  - Estimated cost for 10 users: **$5-15/month** (assuming 1000 queries/month)
- **Why**:
  - Best-in-class for SQL generation
  - Function calling support
  - Reliable and accurate
  - Fast response times

### **Alternative: Google Gemini 1.5 Flash**
- **Cost**: **FREE TIER**
  - 15 requests per minute
  - 1 million tokens per minute
  - 1,500 requests per day
  - **This is enough for 10 users!**
- **Why**:
  - Completely free for low usage
  - Good SQL generation capabilities
  - Fast inference
  - 1M token context window
- **Recommendation**: Start with Gemini Flash (free), upgrade to GPT-4o-mini if needed

### **Prompt Management: Custom JSON Files**
- **Cost**: Free
- **Why**: Simple, version-controlled, no need for LangChain initially

### **Vector Database (for semantic search): Upstash Vector**
- **Cost**: **FREE TIER**
  - 10,000 queries/day
  - 10,000 vectors
- **Why**: Store table/column descriptions for better context retrieval
- **Alternative**: Skip initially, add later if needed

---

## 6. Deployment & Hosting

### **Frontend & API Hosting: Vercel**
- **Cost**: **FREE TIER (Hobby Plan)**
  - Unlimited deployments
  - 100 GB bandwidth/month (plenty for 10 users)
  - Automatic HTTPS
  - Global CDN
  - Preview deployments
  - Serverless functions (100 GB-hours/month)
  - 99.99% uptime SLA
- **Why**:
  - Built for Next.js (same company)
  - Zero-config deployment
  - Automatic scaling
  - Edge functions
  - Built-in analytics
  - Custom domains (free)

### **Alternative: Cloudflare Pages**
- **Cost**: **FREE TIER**
  - Unlimited requests
  - Unlimited bandwidth
  - 500 builds/month
- **Why**: Even more generous, but Vercel has better Next.js integration

---

## 7. Monitoring & Analytics

### **Error Tracking: Sentry**
- **Cost**: **FREE TIER**
  - 5,000 errors/month
  - 1 project
  - 30-day retention
- **Why**: 
  - Catch and fix bugs quickly
  - Source maps support
  - Performance monitoring
  - User feedback

### **Analytics: Vercel Analytics**
- **Cost**: **FREE** (included in Vercel Hobby plan)
  - Web Vitals tracking
  - Page views
  - No cookie banners needed (privacy-friendly)
- **Why**: Built-in, zero config, privacy-focused

### **Uptime Monitoring: UptimeRobot**
- **Cost**: **FREE TIER**
  - 50 monitors
  - 5-minute checks
  - Email alerts
- **Why**: Get notified if your app goes down

### **Logging: Axiom**
- **Cost**: **FREE TIER**
  - 500 MB/month
  - 30-day retention
- **Why**: Centralized logging for debugging
- **Alternative**: Vercel Logs (built-in, but limited retention)

---

## 8. Email Service

### **Transactional Emails: Resend**
- **Cost**: **FREE TIER**
  - 3,000 emails/month
  - 1 custom domain
- **Why**:
  - Modern API
  - React email templates
  - Built-in analytics
  - Great deliverability
- **Alternative**: **SendGrid** (100 emails/day free)

---

## 9. Development Tools

### **Version Control: GitHub**
- **Cost**: Free (public/private repos)
- **Why**: Industry standard, integrates with everything

### **CI/CD: GitHub Actions**
- **Cost**: **FREE TIER**
  - 2,000 minutes/month
- **Why**: Automated testing, linting, deployment

### **Code Quality: ESLint + Prettier**
- **Cost**: Free (open source)
- **Why**: Consistent code style, catch errors early

### **Testing: Vitest + React Testing Library**
- **Cost**: Free (open source)
- **Why**: Fast, modern testing framework

---

## 10. Additional Services

### **Domain Name: Namecheap or Cloudflare**
- **Cost**: ~$10-15/year (one-time annual cost)
- **Why**: Professional custom domain
- **Alternative**: Use Vercel's free subdomain (e.g., queryforge.vercel.app)

### **SSL Certificate: Let's Encrypt (via Vercel)**
- **Cost**: Free
- **Why**: Automatic HTTPS, handled by Vercel

### **CDN: Vercel Edge Network**
- **Cost**: Free (included)
- **Why**: Global content delivery, faster load times

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         USER (Browser)                       │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Vercel (Next.js App + API Routes)               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Frontend   │  │  API Routes  │  │  Middleware  │      │
│  │  (React/TS)  │  │ (Serverless) │  │    (Auth)    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────┬───────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┬─────────────┐
        │             │             │             │
        ▼             ▼             ▼             ▼
┌──────────────┐ ┌─────────┐ ┌──────────┐ ┌─────────────┐
│    Clerk     │ │  Neon   │ │ Upstash  │ │   Gemini    │
│    (Auth)    │ │  (DB)   │ │ (Redis)  │ │  Flash AI   │
└──────────────┘ └─────────┘ └──────────┘ └─────────────┘
```

---

## Cost Breakdown (Monthly)

| Service | Free Tier Limit | Estimated Usage (10 Users) | Cost |
|---------|----------------|---------------------------|------|
| Vercel | 100 GB bandwidth | ~10-20 GB | **$0** |
| Neon (PostgreSQL) | 0.5 GB storage | ~100-200 MB | **$0** |
| Upstash Redis | 10K commands/day | ~1-2K/day | **$0** |
| Clerk Auth | 10K MAUs | 10 users | **$0** |
| Gemini Flash | 1,500 req/day | ~50-100/day | **$0** |
| Sentry | 5K errors/month | ~100-500/month | **$0** |
| Resend | 3K emails/month | ~100-300/month | **$0** |
| UptimeRobot | 50 monitors | 1 monitor | **$0** |
| Domain (optional) | N/A | 1 domain | **$1.25/month** |
| **TOTAL** | | | **$0-1.25/month** |

**Note**: If using OpenAI GPT-4o-mini instead of Gemini, add ~$5-15/month.

---

## Removed/Simplified Design Features (Due to Free Tier Constraints)

### ❌ Removed Features:
1. **Advanced Analytics Dashboards**: Simplified to basic metrics only (no need for paid analytics tools)
2. **Real-time Collaboration**: Removed (would require WebSocket infrastructure)
3. **Video Tutorials**: Replaced with text documentation (no video hosting costs)
4. **Advanced AI Training**: Removed custom model fine-tuning (use prompt engineering instead)
5. **Multi-region Deployment**: Single region only (Vercel auto-routes to nearest edge)
6. **Advanced Monitoring**: Basic monitoring only (no APM tools like DataDog)
7. **Custom Email Templates**: Use simple HTML emails (no fancy email builders)

### ✅ Kept Features (Fully Functional):
1. ✅ **Dark/Light Mode**: Fully implemented with Tailwind CSS
2. ✅ **Modern UI Components**: Using shadcn/ui (free, production-ready)
3. ✅ **User Authentication**: Full OAuth + email/password via Clerk
4. ✅ **Natural Language to SQL**: Using Gemini Flash (free tier)
5. ✅ **Query History**: Stored in Neon PostgreSQL
6. ✅ **Usage Analytics**: Basic user metrics and dashboards
7. ✅ **Role-based Access**: Admin vs User roles via Clerk
8. ✅ **Responsive Design**: Mobile, tablet, desktop support
9. ✅ **Error Handling**: Comprehensive error tracking with Sentry
10. ✅ **Email Notifications**: Transactional emails via Resend
11. ✅ **Caching**: Redis caching for query results
12. ✅ **Database Connection**: Support for PostgreSQL, MySQL, SQL Server
13. ✅ **Export Functionality**: CSV, Excel, JSON exports
14. ✅ **Feedback System**: User feedback on queries
15. ✅ **Sandbox Environment**: Test queries before production

---

## Scaling Path (When You Exceed 10 Users)

### **At 50 Users** (~$20-50/month):
- Upgrade Vercel to Pro ($20/month) for more bandwidth
- Upgrade Neon to paid tier ($19/month) for more storage
- Consider switching to OpenAI GPT-4o-mini for better accuracy

### **At 100 Users** (~$50-100/month):
- Upgrade Clerk to paid tier ($25/month) for advanced features
- Add Upstash Redis paid tier for more cache capacity
- Consider dedicated database instance

### **At 500+ Users** (~$200-500/month):
- Move to dedicated infrastructure (AWS/GCP)
- Implement load balancing
- Add CDN caching
- Consider self-hosting some services

---

## Development Workflow

### **Local Development**:
```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local

# Run database migrations
npx prisma migrate dev

# Start dev server
npm run dev
```

### **Environment Variables** (`.env.local`):
```env
# Database
DATABASE_URL="postgresql://..."

# Redis
UPSTASH_REDIS_REST_URL="https://..."
UPSTASH_REDIS_REST_TOKEN="..."

# Auth
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="pk_..."
CLERK_SECRET_KEY="sk_..."

# AI
GEMINI_API_KEY="..."

# Email
RESEND_API_KEY="re_..."
```

### **Deployment**:
```bash
# Push to GitHub
git push origin main

# Vercel auto-deploys from main branch
# No manual deployment needed!
```

---

## Security Considerations

### **Implemented Security**:
1. ✅ **HTTPS Everywhere**: Automatic via Vercel
2. ✅ **Authentication**: Clerk handles all auth securely
3. ✅ **SQL Injection Prevention**: Prisma ORM prevents SQL injection
4. ✅ **Rate Limiting**: Upstash Redis for API rate limiting
5. ✅ **Environment Variables**: Secrets never committed to Git
6. ✅ **CORS**: Configured in Next.js middleware
7. ✅ **CSP Headers**: Content Security Policy headers
8. ✅ **Input Validation**: Zod schemas for all inputs

### **Database Security**:
1. ✅ **Connection Pooling**: Neon handles this automatically
2. ✅ **Read-only Connections**: For user queries (prevent data modification)
3. ✅ **Query Timeouts**: Prevent long-running queries
4. ✅ **Audit Logging**: Track all database queries

---

## Performance Optimizations

### **Frontend**:
1. ✅ **Code Splitting**: Next.js automatic code splitting
2. ✅ **Image Optimization**: Next.js Image component
3. ✅ **Font Optimization**: Next.js Font optimization
4. ✅ **Lazy Loading**: React.lazy for heavy components
5. ✅ **Memoization**: React.memo for expensive renders

### **Backend**:
1. ✅ **Query Caching**: Redis cache for repeated queries
2. ✅ **Database Indexing**: Proper indexes on frequently queried columns
3. ✅ **Connection Pooling**: Neon serverless pooling
4. ✅ **Serverless Functions**: Auto-scaling with Vercel

### **AI/LLM**:
1. ✅ **Prompt Caching**: Cache similar prompts
2. ✅ **Response Streaming**: Stream AI responses for better UX
3. ✅ **Fallback Handling**: Graceful degradation if AI fails

---

## Recommended Project Structure

```
queryforge/
├── app/                      # Next.js App Router
│   ├── (auth)/              # Auth pages (login, signup)
│   ├── (dashboard)/         # Protected dashboard pages
│   ├── api/                 # API routes
│   ├── layout.tsx           # Root layout
│   └── page.tsx             # Landing page
├── components/              # React components
│   ├── ui/                  # shadcn/ui components
│   ├── dashboard/           # Dashboard-specific components
│   └── shared/              # Shared components
├── lib/                     # Utility functions
│   ├── db.ts               # Prisma client
│   ├── redis.ts            # Redis client
│   ├── ai.ts               # AI/LLM functions
│   └── utils.ts            # Helper functions
├── prisma/                  # Database schema
│   └── schema.prisma
├── public/                  # Static assets
├── styles/                  # Global styles
├── types/                   # TypeScript types
├── .env.local              # Environment variables (gitignored)
├── next.config.js          # Next.js config
├── tailwind.config.js      # Tailwind config
├── tsconfig.json           # TypeScript config
└── package.json            # Dependencies
```

---

## Getting Started Checklist

- [ ] Set up GitHub repository
- [ ] Create Vercel account and connect GitHub
- [ ] Create Neon database
- [ ] Create Upstash Redis instance
- [ ] Create Clerk account and configure auth
- [ ] Get Gemini API key from Google AI Studio
- [ ] Create Resend account for emails
- [ ] Set up Sentry for error tracking
- [ ] Configure environment variables in Vercel
- [ ] Deploy to Vercel
- [ ] Set up custom domain (optional)
- [ ] Configure UptimeRobot monitoring
- [ ] Test with 2-3 users before full rollout

---

## Support & Maintenance

### **Monitoring**:
- Check Sentry daily for errors
- Review Vercel analytics weekly
- Monitor UptimeRobot alerts
- Check database usage monthly

### **Updates**:
- Update dependencies monthly (npm update)
- Review security advisories (GitHub Dependabot)
- Test new features in preview deployments
- Keep documentation up to date

### **Backup**:
- Neon provides automatic backups (point-in-time recovery)
- Export database weekly as additional backup
- Version control all code in GitHub

---

## Conclusion

This tech stack provides a **production-ready, zero-cost solution** for 10 users with:
- ✅ Modern, fast, and responsive UI
- ✅ Secure authentication and authorization
- ✅ AI-powered natural language to SQL
- ✅ Reliable database and caching
- ✅ Comprehensive monitoring and error tracking
- ✅ Easy deployment and scaling
- ✅ **Total cost: $0-1.25/month** (domain optional)

**Estimated Development Time**: 4-6 weeks for MVP with 1-2 developers.

**Ready to scale**: When you grow beyond 10 users, you can easily upgrade individual services without major refactoring.
