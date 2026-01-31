export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-center font-mono text-sm flex flex-col gap-8">
        <h1 className="text-6xl font-bold text-center bg-gradient-to-r from-blue-500 to-purple-600 bg-clip-text text-transparent">
          QueryForge
        </h1>
        <p className="text-xl text-center text-muted-foreground">
          Transform conversations into insights
        </p>
        <div className="flex gap-4">
          <div className="px-6 py-3 bg-primary text-primary-foreground rounded-lg font-semibold hover:opacity-90 transition-opacity cursor-pointer">
            Get Started
          </div>
          <div className="px-6 py-3 bg-card text-card-foreground border border-border rounded-lg font-semibold hover:bg-accent transition-colors cursor-pointer">
            Learn More
          </div>
        </div>
        <div className="mt-8 text-center text-sm text-muted-foreground">
          <p>🚀 Sprint 1, Day 1-2: Project Setup Complete</p>
          <p className="mt-2">Backend: FastAPI | Frontend: Next.js 14</p>
        </div>
      </div>
    </main>
  );
}
