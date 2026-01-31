Product Name & Branding
Primary Name: QueryForge
Tagline: "Transform conversations into insights"
Alternative Names to Consider:

DataDialog
SQLSpeak
InsightQuery
ConversaData


## Global Design Requirements

### Component Standards
**CRITICAL**: All components must be modern, production-ready, and fully functional. No dummy/placeholder components are acceptable.

- **Modern UI/UX**: Every component must follow contemporary design patterns with:
  - Smooth animations and transitions
  - Micro-interactions for better user engagement
  - Glass morphism effects where appropriate
  - Gradient accents and modern color schemes
  - Responsive and adaptive layouts
  - Accessibility-first approach (WCAG 2.1 AA compliance)

- **No Placeholders**: All components must be:
  - Fully functional with real data handling
  - Production-ready with proper error states
  - Complete with loading states and skeleton screens
  - Equipped with proper validation and feedback mechanisms

### Theme & Appearance

**Dark Mode by Default**: The application launches in dark mode as the primary theme.

**Theme Switching**: 
- Global theme toggle accessible from user settings and main navigation
- Options: Dark Mode (default), Light Mode, System Preference
- Smooth transition animations between themes (200ms ease-in-out)
- Theme preference persisted in user settings
- All components must support both dark and light themes seamlessly

**Dark Mode Specifications**:
- Background: Deep charcoal (#0F172A) to pure black (#000000) gradients
- Surface: Elevated cards with subtle borders (#1E293B)
- Text: High contrast whites (#F8FAFC) and grays (#CBD5E1)
- Accents: Vibrant colors that pop against dark backgrounds
- Glassmorphism: Frosted glass effects with backdrop blur

**Light Mode Specifications**:
- Background: Clean whites (#FFFFFF) to light grays (#F8FAFC)
- Surface: Subtle shadows and borders for depth
- Text: Dark grays (#1E293B) for readability
- Accents: Same vibrant colors adjusted for light backgrounds
- Maintain visual hierarchy and contrast ratios

### User Usage Tracking & Analytics

**Individual User Usage Dashboard**:
- Real-time query count and usage metrics
- Personal analytics and insights
- Query history with full context
- Performance metrics (avg response time, success rate)
- Most queried tables and patterns
- Time-based usage trends (daily, weekly, monthly)
- Exportable usage reports

**Admin Usage Analytics**:
- Organization-wide usage statistics
- Per-user usage breakdown
- Department/team analytics (if applicable)
- Usage trends and patterns
- Peak usage times and query volume
- Resource utilization metrics
- Cost tracking per user/team (for billing purposes)

**Usage Limits & Notifications**:
- Display current usage vs. plan limits
- Progress bars for query quotas
- Proactive notifications when approaching limits (80%, 90%, 100%)
- Upgrade prompts when limits are reached
- Usage forecasting based on historical data

**Privacy & Data Retention**:
- Users can view all their tracked data
- Option to export personal usage data
- Clear data retention policies
- GDPR-compliant data handling
- Option to delete query history (with admin override for compliance)


Complete UI/UX Documentation
1. Public Marketing Pages
1.1 Landing Page
Purpose: Convert visitors into signed-up businesses
Sections:

Hero Section

Headline: "Let your team talk to data in plain English"
Subheadline: "No SQL knowledge required. QueryForge turns natural language into powerful database queries."
Primary CTA: "Start Free Trial" (prominent, above fold)
Secondary CTA: "See How It Works" (demo video)
Hero visual: Animated illustration showing text input transforming into SQL query with results


Problem Statement Section

"Data locked behind technical barriers"
Three pain points with icons:

Waiting on data teams for simple queries
Limited access to business intelligence
Costly BI tool implementations




How It Works (3 Steps)

Step 1: Connect your database (5-minute setup)
Step 2: Customize AI understanding (teach it your business)
Step 3: Empower your team (instant insights)


Features Showcase

Smart table detection
Context-aware queries
Usage analytics & feedback loops
Enterprise-grade security
Role-based access control


Social Proof Section

Customer logos
Testimonials with results ("Reduced query turnaround from 2 days to 2 minutes")
Usage statistics if available


Pricing Preview

Three tiers: Starter, Professional, Enterprise
"See full pricing" link


Footer

Product links, Resources, Company, Legal
Social media links
Newsletter signup



1.2 Pricing Page
Layout:

Comparison table with 3-4 tiers
Toggle: Monthly/Annual (show savings)
Feature comparison matrix
FAQ section addressing common concerns
"Contact Sales" for Enterprise

Tiers:

Starter: Small teams (up to 5 users), 1 database, 1000 queries/month
Professional: Growing teams (up to 25 users), 3 databases, unlimited queries
Enterprise: Custom users, unlimited databases, dedicated support, SSO


2. Authentication Flow
2.1 Sign Up Page
Layout:

Split screen design
Left: Benefits recap with rotating testimonials
Right: Sign-up form

Form Fields:

Business email (primary)
Full name
Create password (strength indicator)
Company name (pre-fills for onboarding)
"Sign up with Google" option
Terms acceptance checkbox
"Already have an account? Log in" link

UX Considerations:

Real-time email validation
Password requirements clearly shown
Auto-focus on first field
Error messages inline, contextual

2.2 Login Page
Layout:

Centered form, clean and minimal
Company logo/name at top
Email and password fields
"Remember me" checkbox
"Forgot password?" link
"Sign in with Google" option
"Don't have an account? Sign up" link


3. Onboarding Flow
3.1 Welcome Screen
Purpose: Set expectations and reduce abandonment
Content:

"Welcome to QueryForge, [Name]!"
"Let's set up your workspace in 5 minutes"
Progress indicator: 6 steps shown
"The information you provide helps our AI understand your database and deliver accurate results"
Primary CTA: "Get Started"
Secondary: "Skip for now" (saves partial progress)

3.2 Step 1: Business Information
Layout:

Progress bar at top (1/6 complete)
Card-based design with ample white space

Fields:

Business Name (pre-filled from signup)
Business Description

Placeholder: "e.g., E-commerce platform selling outdoor equipment"
Helper text: "Describe what your business does. This helps AI understand context."
Character count: 500 max
Optional: Industry dropdown (for better defaults)



Navigation:

"Next" button (validates fields)
"Save & Exit" link (top right)

3.3 Step 2: Database Connection
Layout:

Progress bar (2/6)
Visual database icon selector

Fields:

Database Dialect (radio buttons with logos)

PostgreSQL
MySQL
SQL Server
Oracle
SQLite
Other (text input)


Connection Method (tabs)

Direct URI
Individual parameters (host, port, database, user, password)


Database URI (if Direct URI selected)

Text input with masked password
"Test Connection" button
Security notice: "Your credentials are encrypted and never stored in plain text"
Connection status indicator (green checkmark or red error)



UX Considerations:

Show example URI format based on selected dialect
Real-time connection testing
Clear error messages with troubleshooting links
"Need help?" expandable section with firewall/IP whitelisting info

3.4 Step 3: Table Selection
Layout:

Progress bar (3/6)
Two-column layout

Left Column: Available Tables

Search bar to filter tables
List of all detected tables with row counts
Checkbox selection
"Select All" / "Deselect All" options
Table names with schema prefix if applicable

Right Column: Selected Tables Preview

Count of selected tables
Selected tables listed with remove option
Estimated setup time based on selection

Features:

Drag-and-drop to reorder selected tables
Hover shows table schema preview (first 5 columns)
Warning if selecting >50 tables (performance consideration)

Navigation:

"Back" button
"Next" (requires at least 1 table selected)

3.5 Step 4: Primary Tables Configuration
Layout:

Progress bar (4/6)
Card design with clear explanation

Content:

Header: "Which tables will be used most frequently?"
Subtext: "Select tables that appear in 70%+ of queries. This helps AI prioritize them for faster, more accurate results."

Interface:

Multi-select dropdown or tag-based selection
Only shows previously selected tables
Visual indicator: "Primary" badge
Suggested limit: 3-5 tables
Example: "For an e-commerce business: orders, customers, products"

UX:

Reorderable (drag to prioritize)
"Why does this matter?" tooltip
Can select none (skip this optimization)

3.6 Step 5: Table Instructions (Optional)
Layout:

Progress bar (5/6)
Expandable accordion for each selected table

Content:

Header: "Add context about your tables (Optional but recommended)"
Subtext: "Help AI understand when to use each table"

Per Table:

Table name header with expand/collapse
Text area: "When should this table be used?"

Placeholder: "e.g., Use 'order_history' for past purchases, refunds, and transaction dates"
300 character limit
Character counter


Examples link (shows modal with common patterns)

Features:

AI-generated suggestions based on table/column names
"Apply suggestion" button
Save individual table instructions as you go
"Skip this step" prominently displayed

3.7 Step 6: Column Usage Instructions (Optional)
Layout:

Progress bar (6/6)
Similar accordion design to Step 5

Content:

Header: "Fine-tune column understanding (Optional - Advanced)"
Subtext: "Specify which columns to use for common query patterns"

Per Table:

Table name with selected columns shown
Add instruction button
Each instruction row:

Column selector (multi-select)
Use case description
Example: "Use customer_id and order_date for customer purchase history queries"
Remove button



Features:

Template library (common patterns)
AI auto-suggestions
Preview how instruction affects query selection
"I'll do this later" skip option

3.8 Onboarding Complete
Layout:

Success animation/confetti
Summary card

Content:

"You're all set up!"
Quick summary:

Database connected ✓
X tables configured ✓
Y primary tables identified ✓


"What's Next?" section:

"Test your first query in Sandbox"
"Invite team members"
"Explore admin dashboard"



CTAs:

Primary: "Go to Dashboard"
Secondary: "Try Sandbox"
Tertiary: "Review Settings"


4. Admin Dashboard
4.1 Overview/Home Page
Layout: Grid-based dashboard with cards
Top Section: Key Metrics (4 cards)

Total Queries (this month)

Trend indicator vs last month
Sparkline graph


Active Users

User count with avatars
"Invite more" quick action


Average Response Time

Milliseconds with color coding (green <500ms, yellow <2s, red >2s)


Success Rate

Percentage with trend
Click to see failed queries



Middle Section: Charts (2 columns)

Left: Query Volume Over Time

Line graph (last 30 days)
Filterable by date range
Hover shows exact counts


Right: Most Queried Tables

Horizontal bar chart
Top 10 tables
Click to see query details



Bottom Section: Recent Activity

Table view of last 20 queries
Columns: Timestamp, User, Query (truncated), Tables Used, Response Time, Status
Color-coded status (success/failed/warning)
Quick actions: View Details, View Feedback
"View All Queries" link to logs page

Sidebar Quick Actions:

Invite Users
Test in Sandbox
Review Feedback
Database Settings

4.2 User Management
Layout: Table with action toolbar
Top Toolbar:

Search users (by name/email)
Filter by role (Admin/User)
Filter by status (Active/Inactive/Pending)
"Invite Users" button (primary)
Export list button

Table Columns:

Avatar & Name
Email
Role (with inline edit for admins)
Status (Active/Pending/Inactive badge)
Last Active
Total Queries
Actions menu (•••)

View Activity
Change Role
Deactivate/Reactivate
Resend Invitation (if pending)
Remove User



Invite Users Modal:

Email addresses (comma-separated or multi-line)
Role selection (default: User)
Custom welcome message option
"Send Invitations" button
Shows confirmation: "X invitations sent"

User Detail Drawer (slide-in from right):

User profile header
Stats: Total queries, Success rate, Avg response time
Query history (last 50)
Feedback submitted
Activity timeline

4.3 Query Logs
Layout: Advanced filterable table
Filter Bar:

Date range picker (presets: Today, Last 7 days, Last 30 days, Custom)
User filter (multi-select dropdown)
Table filter (multi-select)
Status filter (Success/Failed/Warning)
Search by query text
"Clear Filters" button
Export filtered results (CSV/JSON)

Table Columns:

Timestamp (sortable)
User (with avatar)
Natural Language Query (expandable)
Generated SQL (collapsible, syntax highlighted)
Tables Used (tags)
Response Time (color-coded)
Status (icon + text)
Feedback (thumbs up/down icon if provided)
Actions:

View Full Details
Copy SQL
Re-run in Sandbox
Flag for Review



Query Detail Modal:

Full natural language question
Generated SQL (copyable, syntax highlighted)
Execution plan visualization
Result preview (first 10 rows)
Metadata: User, timestamp, response time, rows returned
Feedback if provided
Error details if failed
"Test Similar Query" button (opens sandbox)

Bulk Actions:

Select multiple queries
Export selected
Flag for review
Add to training set

4.4 Feedback Dashboard
Layout: Card-grid with detail view
Summary Cards (top row):

Total Feedback Items
Positive Feedback % (thumbs up)
Negative Feedback % (thumbs down)
Pending Reviews

Feedback Filter:

Type: All / Positive / Negative / Neutral
Status: All / New / Reviewed / Resolved
Date range
User filter

Feedback Items (card layout):
Each card shows:

User avatar and name
Feedback type (thumbs up/down icon)
Original query (truncated)
User comment/note
Timestamp
Status badge (New/Reviewed/Resolved)
"Review" button

Feedback Detail Modal:

Full query context
User's feedback text
Generated SQL
Query results (if successful)
Admin notes section (editable)
Status dropdown (New/In Review/Resolved/Won't Fix)
Related queries (if pattern detected)
"Mark as Reviewed" / "Resolve" buttons
"Use for Training" checkbox

Features:

Sentiment analysis visualization
Common themes/tags
Feedback trends over time
Export feedback data

4.5 Sandbox (Testing Environment)
Layout: Split-screen editor interface
Left Panel: Input (40% width)

Natural Language Input

Large text area
Placeholder: "Ask a question about your data..."
Character counter
"Example queries" dropdown with templates


Settings Panel (collapsible)

Database selection (if multiple)
Table context override (which tables to consider)
Debug mode toggle (shows AI reasoning)
Response format options


Action Buttons

"Generate SQL" (primary)
"Clear"
"Load from logs" (opens query history)
"Save as template"



Right Panel: Output (60% width)

Tabs:

SQL Query
Results
Execution Plan
Debug Info (if enabled)


SQL Query Tab:

Syntax-highlighted SQL
Copy button
"Edit SQL" toggle (makes editable)
Explain button (shows line-by-line explanation)
Format/Beautify button


Results Tab:

Data table with pagination
Row count indicator
Export options (CSV, JSON, Excel)
Column sorting
Full-screen mode toggle


Execution Plan Tab:

Visual query plan diagram
Performance metrics
Index suggestions
Optimization tips


Debug Info Tab:

Table selection reasoning
Column selection reasoning
Confidence score
Alternative interpretations
Timestamp and processing time



Bottom Bar:

Status indicator (Ready/Processing/Success/Error)
Response time display
"Apply to Production" button (if satisfied with results)
"Report Issue" button

Features:

Query history within sandbox (session-based)
Side-by-side comparison mode (compare two queries)
Keyboard shortcuts (Cmd/Ctrl + Enter to run)
Auto-save draft queries
Share sandbox session (generate shareable link for admins)

4.6 Business Settings
Layout: Tabbed settings panel
Tabs:

General
Database
Tables & Instructions
AI Configuration
Security
Billing

4.6.1 General Tab

Business Name (editable)
Business Description (editable)
Business Logo Upload

Drag-and-drop area
Preview
Recommended size: 200x200px


Industry/Category (dropdown)
Timezone
Date/Time format preferences
"Save Changes" button

4.6.2 Database Tab

Connected Databases (if supporting multiple)

List of databases with status indicators
Primary database designation
Connection test button
Last tested timestamp


Database Connection Details

Dialect (display only, can't change easily)
Connection URI (partially masked)
"Edit Connection" button (opens modal with test)
Connection pool settings (advanced)


Connection Health

Status: Healthy/Warning/Error
Last successful query
Uptime percentage
"Test Connection Now" button


Add Database button (if multi-database supported)

4.6.3 Tables & Instructions Tab

Selected Tables Management

Search/filter tables
Table list with toggle switches (include/exclude)
Schema refresh button
Last refreshed timestamp


Primary Tables

Drag-and-drop ranking interface
Visual weighting indicators
"Auto-detect from usage" button


Table Instructions

Searchable list of tables
Each table expandable to show/edit instructions
Rich text editor for instructions
AI suggestion generator
Preview how instruction affects queries
Version history (see previous instructions)


Column Instructions

Similar interface to table instructions
Per-table expandable sections
Column-level instruction editor
Common patterns library


Bulk Actions

Import instructions (JSON/CSV)
Export instructions
Reset to defaults
AI-optimize all (run AI suggestions on all tables)



4.6.4 AI Configuration Tab

Model Selection

Model version dropdown
Description of each model's strengths
Performance vs accuracy slider


Query Understanding

Strictness level (slider: Flexible ↔ Strict)
Enable fuzzy matching (toggle)
Handle ambiguous queries (dropdown: Ask for clarification / Best guess / Show alternatives)


Response Formatting

Default row limit
Date format preferences
Number formatting (decimals, thousands separator)


Advanced Settings

Temperature/creativity level (for AI responses)
Context window size
Enable query caching (toggle)
Cache duration (hours)


Training Data

Use feedback for improvements (toggle)
Manual training data upload
Review training queries
Clear training cache



4.6.5 Security Tab

Access Control

Require 2FA for admins (toggle)
Session timeout (dropdown: 1hr/4hr/8hr/24hr)
IP whitelist (text area, comma-separated)


Data Security

Encryption status (display)
PII detection (toggle)
Data masking rules (create rules for sensitive columns)


Audit Logs

Enable comprehensive logging (toggle)
Log retention period
"View Audit Logs" button


API Access

API keys management
Generate new API key
Revoke keys
Webhook configurations



4.6.6 Billing Tab (if applicable)

Current plan display with features
Usage this month (progress bars)

Queries used / limit
Users / limit
Databases / limit


"Upgrade Plan" button
Payment method on file
Billing history table
Invoice downloads

Global Settings Features:

Unsaved changes warning
"Discard Changes" option
Change history/audit trail
"Restore Previous Settings" capability

4.7 Analytics & Reports
Layout: Dashboard with customizable widgets
Top Section: Custom Date Range Selector

Presets: Last 7 days, Last 30 days, Last quarter, Last year
Custom date picker
Compare to previous period toggle

Metric Widgets (draggable/customizable):

Query Trends

Time-series chart
Overlay: success rate, response time
Drill-down to specific dates


User Engagement

Active users over time
Queries per user
Most active users leaderboard
Adoption funnel


Table Usage Heatmap

Visual heatmap of table access frequency
Time-of-day patterns
Day-of-week patterns


Performance Metrics

Response time distribution (histogram)
Slowest queries
Cache hit rate
Error rate trends


Business Impact

Time saved estimate (vs manual SQL writing)
Cost savings calculation
ROI metrics
Self-service analytics adoption



Report Generation:

"Create Report" button
Report templates (Weekly Summary, Monthly Business Review, Executive Dashboard)
Schedule automated reports
Email distribution lists
Export formats (PDF, PowerPoint, Excel)

Custom Dashboards:

"Create Dashboard" button
Widget library
Drag-and-drop builder
Save and share dashboards
Set as default for role


5. User Dashboard
5.1 User Home/Chat Interface
Layout: Chat-focused, minimal distractions
Main Chat Area (center, 60% width):

Header:

QueryForge logo/workspace name
Current database indicator
User profile menu (top right)


Chat Interface:

Message history (scrollable)
Each message shows:

Timestamp
Question asked
SQL generated (collapsible)
Results table
Response time
Feedback buttons (👍 👎)




Input Area:

Large text input: "Ask a question about your data..."
"Send" button
Voice input button (optional)
Example questions prompt (first time user)
Upload CSV/Excel for ad-hoc queries (optional feature)


Features:

Syntax highlighting for SQL
Copy SQL button
Copy results button
Export results (CSV/Excel)
"Explain this query" button (shows plain English explanation)
"Show me more like this" (suggests related queries)



Left Sidebar (20% width, collapsible):

Recent Conversations

List of recent query sessions
Grouped by date (Today, Yesterday, Last 7 days, etc.)
Click to load conversation
Delete conversation option


Suggested Questions

Context-aware suggestions based on:

User's role/department
Common queries in organization
Recent data changes


Click to auto-fill


Quick Stats

Your queries this month
Your most-used tables
Average response time



Right Sidebar (20% width, collapsible):

Current Query Context

Tables being used (tags)
Columns included
Filters applied
Row count returned


Export Options

CSV
Excel
Google Sheets
Copy to clipboard


Query Refinement

"Add filter" button
"Change date range" button
"Sort by..." dropdown
"Limit results" input


Help & Resources

Example queries
Video tutorials
Keyboard shortcuts
Contact support



Bottom Bar:

Status indicator
Query processing indicator (with progress)
Connection status

5.2 User History Page
Layout: Timeline-based query history
Filter/Search Bar:

Search by query text
Date range picker
Filter by table
Filter by success/failed
Sort options (Recent, Most used, Slowest, Fastest)

Query Timeline:

Chronological list of all queries
Each item shows:

Date/time (relative: "2 hours ago")
Question asked (truncated)
Status indicator
Quick actions:

Re-run query
View results
Copy SQL
Star/favorite
Delete





Query Detail View (click to expand):

Full question
Generated SQL (collapsible)
Results preview (first 10 rows)
Full results link
Metadata: tables used, response time, row count
Edit and re-run capability
Share with admin (for help)

Features:

Infinite scroll or pagination
Bulk actions (delete multiple)
Export history
Favorites/starred queries section

5.3 User Stats Page
Layout: Personal analytics dashboard
Overview Cards:

Total Queries (all time)
This Month's Queries (with trend)
Average Response Time
Favorite Table (most queried)

Charts:

Query Activity Over Time

Line chart (last 90 days)
Toggle between daily/weekly/monthly views


Most Queried Tables

Pie chart or bar chart
Click to see specific queries


Query Complexity Distribution

Simple/Medium/Complex categorization
Visual breakdown


Performance Metrics

Response time trends
Success rate over time



Personal Insights:

"You're most active on [day of week] at [time]"
"Your most common question type is [analysis/reporting/lookup]"
"You've saved approximately [X hours] this month"
Badges/achievements (gamification):

"Early Adopter" - First 10 queries
"Power User" - 100+ queries
"Speed Demon" - 50 queries in one day
"Data Explorer" - Queried 10+ different tables



Leaderboard (optional, if company culture fits):

Top users by query count
Most helpful feedback providers
Toggle visibility on/off

5.4 User Settings
Layout: Simple settings page
Sections:
Profile:

Profile picture upload
Display name
Email (view only, contact admin to change)
Role (view only)
Department/Team (optional)

Preferences:

**Theme Settings:**
- Theme Mode (Radio buttons with live preview):
  - Dark Mode (Default) - Shows dark theme preview
  - Light Mode - Shows light theme preview
  - System Preference - Auto-switches based on OS settings
- Theme toggle also available in:
  - Top navigation bar (animated moon/sun icon)
  - Quick settings dropdown menu
  - Keyboard shortcut: Ctrl/Cmd + Shift + T
- Smooth transition animation (200ms) when switching
- Live preview of current theme colors

**Notification Settings:**
- Email notifications:
  - Query completion (for long-running queries)
  - Weekly usage summary
  - Platform updates and new features
  - Usage limit warnings (80%, 90%, 100%)
- In-app notifications:
  - Real-time query status
  - System announcements
  - Feedback responses from admins

**Display Preferences:**
- Default export format (CSV/Excel/JSON)
- Results per page (10, 25, 50, 100)
- Language preference
- Date/time format
- Number format (decimals, separators)

**Usage & Analytics:**
- Personal Usage Dashboard:
  - Current month query count with animated progress bar vs. plan limit
  - Total queries (all time) with milestone badges
  - Average response time with trend indicator
  - Success rate percentage with color coding
  - Most queried tables (top 5 with usage bars)
  - Interactive query activity chart (last 30 days)
  - Peak usage hours heatmap
  - Query complexity breakdown (simple/medium/complex)
- Export Options:
  - Download usage report (PDF/CSV/Excel)
  - Custom date range selector
  - Select specific metrics to include
  - Scheduled reports (daily/weekly/monthly)
- Usage Limit Notifications:
  - Visual alert at 80% of query limit (yellow warning)
  - Prominent alert at 90% of query limit (orange warning)
  - Block with upgrade prompt at 100% (red alert)
  - Notification delivery: email, in-app, or both
  - Forecast when limit will be reached based on usage patterns
- Privacy Controls:
  - Toggle to include/exclude from team analytics
  - Option to clear query history (keeps last 30 days for compliance)
  - Download all personal data (GDPR compliance)
  - View data retention policies

Accessibility:

- Font size adjustment (Small, Medium, Large, Extra Large)
  - Live preview of size changes
  - Applies globally across the application
- High contrast mode toggle
  - Enhanced color contrast ratios (7:1 for AAA compliance)
  - Works with both dark and light themes
- Screen reader optimizations
  - ARIA labels on all interactive elements
  - Descriptive alt text for images
  - Semantic HTML structure
- Keyboard shortcuts
  - Enable/disable keyboard navigation
  - Customizable shortcut keys
  - Shortcut reference guide (accessible via ?)
- Reduced motion option
  - Disables animations for users sensitive to motion
- Focus indicators
  - Enhanced visible focus states
  - Customizable focus ring colors

Privacy:

- Data usage for AI improvements (opt-in/opt-out toggle)
  - Clear explanation of what data is used
  - Can be changed at any time
- Query history retention preference
  - Keep for 30 days, 90 days, 1 year, or indefinitely
  - Automatic deletion based on preference
  - Admin override for compliance requirements
- Share anonymous usage data (opt-in/opt-out)
  - Helps improve product features
  - Completely anonymized
- Data export and deletion
  - Download all personal data (GDPR right to access)
  - Request account deletion (GDPR right to be forgotten)
  - View data processing activities
- Cookie preferences
  - Essential cookies (always on)
  - Analytics cookies (optional)
  - Marketing cookies (optional)

Help & Support:

- Getting started guide
  - Interactive tutorial for first-time users
  - Video walkthroughs
  - Step-by-step documentation
- Keyboard shortcuts reference
  - Searchable shortcut list
  - Printable cheat sheet
  - Accessible via ? key
- Submit feedback
  - In-app feedback form
  - Rate your experience
  - Suggest new features
  - Track feedback status
- Contact admin
  - Direct message to workspace admins
  - Request assistance with queries
  - Report issues
- Report a bug
  - Detailed bug report form
  - Automatic system info collection
  - Screenshot attachment
  - Priority level selection
- Live chat support (if available)
  - Real-time assistance
  - AI-powered help bot
- Knowledge base
  - Searchable documentation
  - FAQ section
  - Community forum links


6. Responsive Design Considerations
Mobile (320px - 768px)

Admin Dashboard: Simplified cards, vertical stacking, hamburger menu for navigation
User Chat: Full-screen chat, swipeable sidebars
Tables: Horizontal scroll with fixed first column
Forms: Single column, larger touch targets

Tablet (768px - 1024px)

Admin Dashboard: 2-column grid for cards
User Chat: Side panel remains visible on landscape
Condensed navigation

Desktop (1024px+)

Full layout as described
Keyboard shortcuts enabled
Multi-panel views
Hover states and tooltips


7. Design System Foundations

### Color Palette

**DARK MODE (Default Theme)**

Primary Brand Colors:
- Primary: Vibrant Blue (#3B82F6) - CTAs, links, active states
- Primary Hover: Brighter Blue (#60A5FA)
- Secondary: Teal (#14B8A6) - Success, positive actions
- Secondary Hover: Bright Teal (#2DD4BF)
- Accent: Purple (#A855F7) - Highlights, badges
- Accent Hover: Bright Purple (#C084FC)

Background Colors:
- App Background: Deep Navy (#0F172A)
- Surface: Slate (#1E293B)
- Surface Elevated: Lighter Slate (#334155)
- Surface Hover: (#475569)
- Overlay: rgba(15, 23, 42, 0.8) with backdrop blur

Text Colors:
- Primary Text: Near White (#F8FAFC)
- Secondary Text: Light Gray (#CBD5E1)
- Tertiary Text: Medium Gray (#94A3B8)
- Disabled Text: Dark Gray (#64748B)

Border Colors:
- Default Border: (#334155)
- Subtle Border: (#1E293B)
- Focus Border: Primary Blue (#3B82F6)

Semantic Colors:
- Success: Emerald (#10B981)
- Success Background: rgba(16, 185, 129, 0.1)
- Warning: Amber (#F59E0B)
- Warning Background: rgba(245, 158, 11, 0.1)
- Error: Red (#EF4444)
- Error Background: rgba(239, 68, 68, 0.1)
- Info: Sky Blue (#0EA5E9)
- Info Background: rgba(14, 165, 233, 0.1)

**LIGHT MODE**

Primary Brand Colors:
- Primary: Deep Blue (#2563EB) - CTAs, links, active states
- Primary Hover: Darker Blue (#1D4ED8)
- Secondary: Teal (#0D9488) - Success, positive actions
- Secondary Hover: Darker Teal (#0F766E)
- Accent: Purple (#7C3AED) - Highlights, badges
- Accent Hover: Darker Purple (#6D28D9)

Background Colors:
- App Background: Off White (#F8FAFC)
- Surface: Pure White (#FFFFFF)
- Surface Elevated: Light Gray (#F1F5F9)
- Surface Hover: (#E2E8F0)
- Overlay: rgba(255, 255, 255, 0.9) with backdrop blur

Text Colors:
- Primary Text: Near Black (#0F172A)
- Secondary Text: Dark Gray (#475569)
- Tertiary Text: Medium Gray (#64748B)
- Disabled Text: Light Gray (#94A3B8)

Border Colors:
- Default Border: (#E2E8F0)
- Subtle Border: (#F1F5F9)
- Focus Border: Primary Blue (#2563EB)

Semantic Colors:
- Success: Green (#059669)
- Success Background: rgba(5, 150, 105, 0.1)
- Warning: Orange (#D97706)
- Warning Background: rgba(217, 119, 6, 0.1)
- Error: Red (#DC2626)
- Error Background: rgba(220, 38, 38, 0.1)
- Info: Blue (#0284C7)
- Info Background: rgba(2, 132, 199, 0.1)

**Glassmorphism Effects** (Both Themes):
- Dark Mode: background: rgba(30, 41, 59, 0.7), backdrop-filter: blur(12px), border: 1px solid rgba(148, 163, 184, 0.1)
- Light Mode: background: rgba(255, 255, 255, 0.7), backdrop-filter: blur(12px), border: 1px solid rgba(226, 232, 240, 0.8)

Typography

Headings: Inter or SF Pro (clean, modern sans-serif)

H1: 32px/40px, Bold
H2: 24px/32px, Semibold
H3: 20px/28px, Semibold
H4: 16px/24px, Medium


Body: Inter or SF Pro

Large: 16px/24px, Regular
Base: 14px/20px, Regular
Small: 12px/16px, Regular


Code: JetBrains Mono or Fira Code

14px, Medium, monospace



Spacing

Use 8px base grid
Common spacing: 4px, 8px, 16px, 24px, 32px, 48px, 64px

Components

**All components must be fully functional, production-ready, and support both dark and light themes.**

Buttons:

**Dark Mode:**
- Primary: Solid background (#3B82F6), white text (#F8FAFC), rounded corners (8px)
  - Hover: Brighter background (#60A5FA), subtle glow effect
  - Active: Pressed state with scale(0.98) transform
- Secondary: Outlined (1px solid #3B82F6), transparent background, blue text
  - Hover: Subtle background (#1E293B), border brightens
- Ghost: No border, subtle text (#CBD5E1)
  - Hover: Background (#1E293B)
- Sizes: Small (36px), Medium (44px), Large (52px)
- All buttons include loading states with spinner animations

**Light Mode:**
- Primary: Solid background (#2563EB), white text (#FFFFFF), rounded corners (8px)
  - Hover: Darker background (#1D4ED8), subtle shadow
  - Active: Pressed state with scale(0.98) transform
- Secondary: Outlined (1px solid #2563EB), transparent background, blue text
  - Hover: Subtle background (#F1F5F9), border darkens
- Ghost: No border, subtle text (#475569)
  - Hover: Background (#F1F5F9)
- Sizes: Small (36px), Medium (44px), Large (52px)
- All buttons include loading states with spinner animations


Inputs & Form Fields:

**Dark Mode:**
- Height: 44px (medium), 52px (large)
- Border radius: 8px
- Background: Surface (#1E293B)
- Border: 1px solid #334155
- Text: Primary text (#F8FAFC)
- Placeholder: Tertiary text (#94A3B8)
- Focus: Blue ring (#3B82F6), 2px offset, glow effect
- Error: Red border (#EF4444), error message below
- Success: Green border (#10B981), checkmark icon
- Disabled: Darker background (#0F172A), disabled text (#64748B)

**Light Mode:**
- Height: 44px (medium), 52px (large)
- Border radius: 8px
- Background: White (#FFFFFF)
- Border: 1px solid #E2E8F0
- Text: Primary text (#0F172A)
- Placeholder: Tertiary text (#64748B)
- Focus: Blue ring (#2563EB), 2px offset, subtle shadow
- Error: Red border (#DC2626), error message below
- Success: Green border (#059669), checkmark icon
- Disabled: Light gray background (#F1F5F9), disabled text (#94A3B8)


Cards:

**Dark Mode:**
- Background: Surface (#1E293B)
- Border: 1px solid #334155
- Border radius: 12px
- Shadow: 0 4px 6px rgba(0, 0, 0, 0.3)
- Hover: Elevated shadow, subtle border glow
- Padding: 20px (small), 24px (medium), 32px (large)
- Glassmorphism variant: rgba(30, 41, 59, 0.7) with backdrop-blur(12px)

**Light Mode:**
- Background: White (#FFFFFF)
- Border: 1px solid #E2E8F0
- Border radius: 12px
- Shadow: 0 1px 3px rgba(0, 0, 0, 0.1)
- Hover: Elevated shadow (0 4px 6px rgba(0, 0, 0, 0.1))
- Padding: 20px (small), 24px (medium), 32px (large)
- Glassmorphism variant: rgba(255, 255, 255, 0.7) with backdrop-blur(12px)


Tables:

**Dark Mode:**
- Background: Surface (#1E293B)
- Header: Surface Elevated (#334155), bold text (#F8FAFC)
- Rows: Alternating stripes (transparent / rgba(51, 65, 85, 0.3))
- Hover: Row highlight (#475569)
- Borders: Minimal, subtle (#334155)
- Text: Primary (#F8FAFC) and Secondary (#CBD5E1)
- Selected row: Blue tint (rgba(59, 130, 246, 0.1))

**Light Mode:**
- Background: White (#FFFFFF)
- Header: Light gray (#F1F5F9), bold text (#0F172A)
- Rows: Alternating stripes (transparent / #F8FAFC)
- Hover: Row highlight (#E2E8F0)
- Borders: Minimal, light gray (#E2E8F0)
- Text: Primary (#0F172A) and Secondary (#475569)
- Selected row: Blue tint (rgba(37, 99, 235, 0.05))


Modals & Overlays:

**Dark Mode:**
- Backdrop: rgba(15, 23, 42, 0.9) with backdrop-blur(4px)
- Modal background: Surface (#1E293B)
- Border: 1px solid #334155
- Border radius: 16px
- Shadow: 0 20px 25px rgba(0, 0, 0, 0.5)
- Close button: Ghost style with hover effect

**Light Mode:**
- Backdrop: rgba(15, 23, 42, 0.5) with backdrop-blur(4px)
- Modal background: White (#FFFFFF)
- Border: 1px solid #E2E8F0
- Border radius: 16px
- Shadow: 0 20px 25px rgba(0, 0, 0, 0.15)
- Close button: Ghost style with hover effect


Notifications & Toasts:

**Dark Mode:**
- Success: Background (#10B981), white text, checkmark icon
- Warning: Background (#F59E0B), dark text (#0F172A), warning icon
- Error: Background (#EF4444), white text, error icon
- Info: Background (#0EA5E9), white text, info icon
- Border radius: 8px
- Shadow: 0 4px 6px rgba(0, 0, 0, 0.3)
- Auto-dismiss: 5 seconds with progress bar

**Light Mode:**
- Success: Background (#059669), white text, checkmark icon
- Warning: Background (#D97706), white text, warning icon
- Error: Background (#DC2626), white text, error icon
- Info: Background (#0284C7), white text, info icon
- Border radius: 8px
- Shadow: 0 4px 6px rgba(0, 0, 0, 0.1)
- Auto-dismiss: 5 seconds with progress bar


Navigation & Sidebar:

**Dark Mode:**
- Background: Deep Navy (#0F172A)
- Active item: Surface (#1E293B) with blue accent border
- Hover: Subtle background (#1E293B)
- Text: Secondary (#CBD5E1), Active: Primary (#F8FAFC)
- Icons: Match text colors
- Dividers: Subtle border (#1E293B)

**Light Mode:**
- Background: White (#FFFFFF) or Off-white (#F8FAFC)
- Active item: Light gray (#F1F5F9) with blue accent border
- Hover: Subtle background (#F1F5F9)
- Text: Secondary (#475569), Active: Primary (#0F172A)
- Icons: Match text colors
- Dividers: Subtle border (#E2E8F0)


Animations

Page transitions: 200ms ease-in-out
Hover effects: 150ms
Loading states: Skeleton screens, smooth fade-ins
Micro-interactions: Button press (scale 0.98), checkbox check


8. Key UX Patterns
Progressive Disclosure

Show essentials first, hide advanced features
"Show more" / "Advanced options" expandable sections
Tooltips for additional context

Feedback & Confirmation

Toast notifications for actions (top-right)
Confirmation modals for destructive actions
Inline validation for forms
Success animations (checkmarks, confetti)

Empty States

Helpful illustrations
Clear calls-to-action
Guidance on what to do first
Examples of what to expect

Loading States

Skeleton screens for tables and cards
Progress indicators for long operations
Optimistic UI updates where possible
Timeout handling with retry options

Error Handling

Friendly, non-technical language
Specific guidance on resolution
Contact support option
Log errors for admin review

Accessibility

WCAG 2.1 AA compliance
Keyboard navigation throughout
Screen reader optimization
Focus indicators
Color contrast ratios: 4.5:1 for text
Alt text for images
ARIA labels where needed


9. User Flows
Admin User Flow: Investigating a Failed Query

See alert on dashboard (failed query rate spike)
Click into Query Logs
Filter by "Failed" status
Review failed query details
Notice pattern in error messages
Open Sandbox
Load failing query
Adjust table instructions
Test in sandbox
Deploy fix to production
Monitor results

End User Flow: First-Time Query

Land on chat interface
See example questions
Click an example or type question
Watch SQL generate in real-time
See results displayed
Export to Excel
Provide thumbs up feedback
Ask follow-up question with refinement

Admin User Flow: Onboarding New Team Member

Navigate to User Management
Click "Invite Users"
Enter email and select role
Send invitation
New user receives email
New user signs up and auto-assigned to workspace
Admin sees user appear as "Active"

10. Theme Toggle Component Specifications

**Component Placement:**

Primary Locations:
- Top navigation bar (right side, near user profile)
  - Icon button with animated moon (dark mode) / sun (light mode) icon
  - Tooltip on hover: "Switch to Light/Dark Mode"
  - Badge indicator showing current theme
- User Settings page
  - Full theme selector with radio buttons
  - Live preview cards for each theme option
  - Detailed description of each mode
- Quick Settings Menu
  - Dropdown accessible from user profile
  - Quick toggle without page navigation
  - Shows current selection with checkmark

**Visual Design:**

**Dark Mode (Default):**
- Icon: Moon icon (#F8FAFC) with subtle glow
- Background: Transparent, hover: (#1E293B)
- Border radius: 8px
- Size: 40px × 40px
- Animation: Rotate 180° on theme switch

**Light Mode:**
- Icon: Sun icon (#F59E0B) with rays
- Background: Transparent, hover: (#F1F5F9)
- Border radius: 8px
- Size: 40px × 40px
- Animation: Rotate 180° on theme switch

**System Preference Mode:**
- Icon: Monitor/device icon with auto symbol
- Automatically switches based on OS dark mode setting
- Shows current active theme in parentheses

**Interaction Behavior:**

Click Action:
1. User clicks theme toggle
2. Smooth 200ms transition begins
3. All colors fade/morph to new theme
4. Icon rotates 180° with bounce effect
5. Toast notification: "Switched to [Theme Name]"
6. Preference saved to user settings
7. Syncs across all open tabs/windows

Keyboard Shortcut:
- Ctrl/Cmd + Shift + T to toggle
- Focus indicator appears on toggle button
- Accessible via Tab navigation

**Theme Transition Animation:**

Smooth Color Morphing:
- All background colors: 200ms ease-in-out
- All text colors: 200ms ease-in-out
- All border colors: 200ms ease-in-out
- Shadows: 150ms ease-in-out
- No jarring flashes or sudden changes

Icon Animation:
- Rotate: 180deg with spring physics
- Scale: 0.9 → 1.1 → 1.0 (bounce effect)
- Opacity: Fade out old icon (100ms) → Fade in new icon (100ms)
- Total duration: 300ms

**Persistence & Sync:**

Local Storage:
- Theme preference stored in localStorage
- Key: "queryforge_theme_preference"
- Values: "dark", "light", "system"

Database Sync:
- User preference saved to user profile
- Syncs across devices
- Overrides local storage on login

Multi-Tab Sync:
- Uses BroadcastChannel API
- All tabs update simultaneously
- No page refresh required

**Accessibility:**

ARIA Labels:
- aria-label="Toggle theme"
- aria-pressed="true/false"
- role="switch"

Keyboard Navigation:
- Fully accessible via Tab key
- Enter or Space to toggle
- Focus visible indicator (blue ring)

Screen Reader:
- Announces current theme on toggle
- "Theme switched to Dark Mode"
- "Theme switched to Light Mode"

**System Preference Detection:**

Auto-Detection:
- Uses CSS media query: prefers-color-scheme
- JavaScript: window.matchMedia('(prefers-color-scheme: dark)')
- Listens for OS theme changes in real-time
- Updates automatically when OS theme changes

User Override:
- Manual selection overrides system preference
- "Use System Preference" option to re-enable auto-detection
- Clear indicator when using system vs. manual selection

**Edge Cases & Error Handling:**

Browser Support:
- Fallback to dark mode if localStorage unavailable
- Graceful degradation for older browsers
- CSS variables for theme colors (IE11 fallback)

Performance:
- Debounce rapid toggle clicks (prevent animation stacking)
- Lazy load theme assets
- Preload both theme stylesheets for instant switching

Error States:
- If theme fails to load, show error toast
- Fallback to default dark theme
- Retry mechanism with exponential backoff
- Log error to admin dashboard

**Implementation Notes:**

CSS Variables:
- Use CSS custom properties for all theme colors
- Single source of truth for color tokens
- Easy to extend with new themes in future

React/Vue Component:
- Reusable ThemeToggle component
- Context/Store for global theme state
- Hooks for theme detection and switching

Testing:
- Unit tests for theme switching logic
- E2E tests for user flows
- Visual regression tests for both themes
- Accessibility audit with axe-core
