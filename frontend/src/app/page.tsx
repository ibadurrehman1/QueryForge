import { ThemeToggle } from "@/components/theme-toggle";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export default function Home() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      {/* Header */}
      <header className="border-b bg-background">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <h1 className="text-2xl font-bold text-foreground">QueryForge</h1>
            <Badge variant="secondary">MVP</Badge>
          </div>
          <div className="flex items-center gap-4">
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20 text-center">
        <h2 className="text-5xl font-bold mb-4 text-foreground">
          Transform Conversations into Insights
        </h2>
        <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
          Convert natural language queries into SQL with AI. Connect your database and start querying in seconds.
        </p>
        <div className="flex gap-4 justify-center">
          <Button size="lg">Get Started</Button>
          <Button size="lg" variant="outline">
            Learn More
          </Button>
        </div>
      </section>

      {/* Features */}
      <section className="container mx-auto px-4 py-16">
        <h3 className="text-3xl font-bold text-center mb-12 text-foreground">Features</h3>
        <div className="grid md:grid-cols-3 gap-6">
          <Card className="bg-card text-card-foreground">
            <CardHeader>
              <CardTitle className="text-foreground">AI-Powered SQL Generation</CardTitle>
              <CardDescription>
                Transform natural language into optimized SQL queries using advanced AI
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                Simply describe what you want to find, and our AI will generate the perfect SQL query for you.
              </p>
            </CardContent>
          </Card>

          <Card className="bg-card text-card-foreground">
            <CardHeader>
              <CardTitle className="text-foreground">Multiple Database Support</CardTitle>
              <CardDescription>
                Connect to PostgreSQL, MySQL, and more
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                Seamlessly connect to your existing databases and start querying instantly.
              </p>
            </CardContent>
          </Card>

          <Card className="bg-card text-card-foreground">
            <CardHeader>
              <CardTitle className="text-foreground">Query History & Analytics</CardTitle>
              <CardDescription>
                Track your queries and analyze usage patterns
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                View your query history, success rates, and performance metrics all in one place.
              </p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t mt-20 bg-background">
        <div className="container mx-auto px-4 py-8 text-center text-sm text-muted-foreground">
          <p>&copy; 2026 QueryForge. All rights reserved.</p>
        </div>
      </footer>
    </main>
  );
}
