import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Leaf, Upload, Zap, Shield, Users, CheckCircle, Camera, Brain, TrendingUp } from 'lucide-react'
import Image from "next/image"
import Link from "next/link"

export default function MangoLeafLandingPage() {
  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-b from-green-50 to-white">
      {/* Header */}
      <header className="px-4 lg:px-6 h-16 flex items-center border-b bg-white/80 backdrop-blur-sm sticky top-0 z-50">
        <Link href="/" className="flex items-center justify-center gap-2">
          <Leaf className="h-8 w-8 text-green-600" />
          <span className="text-xl font-bold text-green-800">MangoAI</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link href="#features" className="text-sm font-medium hover:text-green-600 transition-colors">
            Features
          </Link>
          <Link href="#how-it-works" className="text-sm font-medium hover:text-green-600 transition-colors">
            How It Works
          </Link>
          <Link href="#pricing" className="text-sm font-medium hover:text-green-600 transition-colors">
            Pricing
          </Link>
          <Link href="#contact" className="text-sm font-medium hover:text-green-600 transition-colors">
            Contact
          </Link>
        </nav>
      </header>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <div className="grid gap-6 lg:grid-cols-[1fr_400px] lg:gap-12 xl:grid-cols-[1fr_600px]">
              <div className="flex flex-col justify-center space-y-4">
                <div className="space-y-2">
                  <Badge variant="secondary" className="w-fit bg-green-100 text-green-800">
                    AI-Powered Agriculture
                  </Badge>
                  <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none text-gray-900">
                    Detect Mango Leaf Diseases in{" "}
                    <span className="text-green-600">Seconds</span>
                  </h1>
                  <p className="max-w-[600px] text-gray-600 md:text-xl">
                    Protect your mango crops with our advanced AI classification system. Upload a photo and get instant, accurate disease identification with treatment recommendations.
                  </p>
                </div>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Button size="lg" className="bg-green-600 hover:bg-green-700">
                    <Camera className="mr-2 h-4 w-4" />
                    Try It Now
                  </Button>
                  <Button variant="outline" size="lg">
                    Watch Demo
                  </Button>
                </div>
                <div className="flex items-center gap-4 text-sm text-gray-600">
                  <div className="flex items-center gap-1">
                    <CheckCircle className="h-4 w-4 text-green-600" />
                    <span>99.2% Accuracy</span>
                  </div>
                  <div className="flex items-center gap-1">
                    <CheckCircle className="h-4 w-4 text-green-600" />
                    <span>Instant Results</span>
                  </div>
                  <div className="flex items-center gap-1">
                    <CheckCircle className="h-4 w-4 text-green-600" />
                    <span>Free to Try</span>
                  </div>
                </div>
              </div>
              <div className="flex items-center justify-center">
                <Image
                  src="/placeholder-mb51n.png"
                  width="600"
                  height="400"
                  alt="Mango leaf disease detection interface"
                  className="mx-auto aspect-video overflow-hidden rounded-xl object-cover shadow-2xl"
                />
              </div>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="w-full py-12 md:py-24 lg:py-32 bg-gray-50">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-gray-900">
                  Powerful Features for Modern Farming
                </h2>
                <p className="max-w-[900px] text-gray-600 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Our AI-powered platform combines cutting-edge technology with agricultural expertise to help you maintain healthy mango crops.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-3 lg:gap-12">
              <Card className="border-0 shadow-lg">
                <CardHeader className="text-center">
                  <Brain className="mx-auto h-12 w-12 text-green-600 mb-4" />
                  <CardTitle>AI Disease Detection</CardTitle>
                  <CardDescription>
                    Advanced machine learning algorithms trained on thousands of mango leaf images for precise disease identification.
                  </CardDescription>
                </CardHeader>
              </Card>
              <Card className="border-0 shadow-lg">
                <CardHeader className="text-center">
                  <Zap className="mx-auto h-12 w-12 text-green-600 mb-4" />
                  <CardTitle>Instant Analysis</CardTitle>
                  <CardDescription>
                    Get results in under 3 seconds. Simply upload a photo and receive immediate disease classification and confidence scores.
                  </CardDescription>
                </CardHeader>
              </Card>
              <Card className="border-0 shadow-lg">
                <CardHeader className="text-center">
                  <Shield className="mx-auto h-12 w-12 text-green-600 mb-4" />
                  <CardTitle>Treatment Recommendations</CardTitle>
                  <CardDescription>
                    Receive expert-backed treatment suggestions and preventive measures for each identified disease condition.
                  </CardDescription>
                </CardHeader>
              </Card>
            </div>
          </div>
        </section>

        {/* How It Works Section */}
        <section id="how-it-works" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-gray-900">
                  How It Works
                </h2>
                <p className="max-w-[900px] text-gray-600 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Three simple steps to protect your mango crops from diseases.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-3 lg:gap-12">
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-green-100">
                  <Upload className="h-8 w-8 text-green-600" />
                </div>
                <h3 className="text-xl font-bold">1. Upload Image</h3>
                <p className="text-gray-600">
                  Take a clear photo of the mango leaf and upload it to our platform using your phone or camera.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-green-100">
                  <Brain className="h-8 w-8 text-green-600" />
                </div>
                <h3 className="text-xl font-bold">2. AI Analysis</h3>
                <p className="text-gray-600">
                  Our advanced AI model analyzes the image and identifies potential diseases with high accuracy.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-green-100">
                  <TrendingUp className="h-8 w-8 text-green-600" />
                </div>
                <h3 className="text-xl font-bold">3. Get Results</h3>
                <p className="text-gray-600">
                  Receive instant results with disease classification, confidence scores, and treatment recommendations.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Stats Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 bg-green-600">
          <div className="container px-4 md:px-6">
            <div className="grid gap-6 lg:grid-cols-3 lg:gap-12">
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="text-4xl font-bold text-white">99.2%</div>
                <div className="text-green-100">Detection Accuracy</div>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="text-4xl font-bold text-white">50K+</div>
                <div className="text-green-100">Images Analyzed</div>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="text-4xl font-bold text-white">15+</div>
                <div className="text-green-100">Disease Types Detected</div>
              </div>
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 border-t">
          <div className="container grid items-center justify-center gap-4 px-4 text-center md:px-6">
            <div className="space-y-3">
              <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight text-gray-900">
                Ready to Protect Your Mango Crops?
              </h2>
              <p className="mx-auto max-w-[600px] text-gray-600 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                Join thousands of farmers who trust MangoAI to keep their crops healthy and productive.
              </p>
            </div>
            <div className="mx-auto w-full max-w-sm space-y-2">
              <form className="flex gap-2">
                <Input type="email" placeholder="Enter your email" className="max-w-lg flex-1" />
                <Button type="submit" className="bg-green-600 hover:bg-green-700">
                  Get Started
                </Button>
              </form>
              <p className="text-xs text-gray-500">
                Start with our free plan. No credit card required.{" "}
                <Link href="/terms" className="underline underline-offset-2 hover:text-green-600">
                  Terms & Conditions
                </Link>
              </p>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t bg-gray-50">
        <div className="flex items-center gap-2">
          <Leaf className="h-5 w-5 text-green-600" />
          <p className="text-xs text-gray-500">
            © {new Date().getFullYear()} MangoAI. All rights reserved.
          </p>
        </div>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link href="#" className="text-xs hover:underline underline-offset-4 text-gray-500 hover:text-green-600">
            Privacy Policy
          </Link>
          <Link href="#" className="text-xs hover:underline underline-offset-4 text-gray-500 hover:text-green-600">
            Terms of Service
          </Link>
          <Link href="#" className="text-xs hover:underline underline-offset-4 text-gray-500 hover:text-green-600">
            Support
          </Link>
        </nav>
      </footer>
    </div>
  )
}
