# Dual Application Workspace

## Overview

This workspace contains two separate web applications:

### 1. PawMeet - Meeting Scheduler Application
PawMeet is a full-stack web application for scheduling and managing meetings with timezone support. It features a mobile-first design with a React frontend, Express.js backend, and PostgreSQL database using Drizzle ORM. The application is designed as a pet-themed meeting scheduler with modern UI components and real-time meeting management capabilities.

### 2. Simple Flask Chatbot
A clean, web-based chatbot built with Flask and vanilla JavaScript. Features a modern chat interface with contextual responses, typing indicators, and mobile-responsive design. The chatbot handles greetings, help requests, weather queries, and general conversation.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite for fast development and optimized builds
- **UI Framework**: Tailwind CSS with shadcn/ui component library
- **State Management**: TanStack Query (React Query) for server state management
- **Routing**: Wouter for lightweight client-side routing
- **Forms**: React Hook Form with Zod validation
- **Mobile-First Design**: Responsive layout optimized for mobile devices

### Backend Architecture
- **Runtime**: Node.js with Express.js framework
- **Language**: TypeScript with ES modules
- **API Style**: RESTful API endpoints
- **Development**: Hot reload with tsx for development server
- **Production**: Compiled with esbuild for optimal performance

### Database Architecture
- **Database**: PostgreSQL with Neon serverless hosting
- **ORM**: Drizzle ORM for type-safe database operations
- **Schema Management**: Drizzle Kit for migrations and schema management
- **Connection**: @neondatabase/serverless for edge-compatible connections

## Key Components

### Database Schema
- **Users Table**: Stores user information including timezone preferences
- **Meetings Table**: Stores meeting details with timezone-aware timestamps
- **Shared Types**: Common TypeScript types and Zod schemas for validation

### API Endpoints
- `GET /api/user` - Retrieve current user information
- `PATCH /api/user/timezone` - Update user timezone preference
- `GET /api/meetings/upcoming` - Get upcoming meetings for user
- `POST /api/meetings` - Create new meeting
- `PUT/DELETE /api/meetings/:id` - Update/delete existing meetings

### UI Components
- **Mobile Layout**: Responsive container with bottom navigation
- **Meeting Cards**: Display meeting information with timezone conversion
- **Timezone Selector**: Multi-timezone support with current time display
- **Create Meeting Modal**: Form for scheduling new meetings
- **Calendar View**: Weekly calendar interface for meeting visualization

### Storage Layer
- **Interface**: IStorage interface for data operations abstraction
- **Implementation**: PostgreSQL database with Drizzle ORM
- **Operations**: CRUD operations for users and meetings with persistent storage
- **Database**: Neon PostgreSQL with connection pooling and serverless compatibility

## Data Flow

1. **User Authentication**: Simplified with default user stored in PostgreSQL database
2. **Meeting Creation**: Form validation → API call → PostgreSQL storage → UI update
3. **Timezone Handling**: Client-side conversion using date-fns-tz library
4. **Real-time Updates**: React Query for automatic data synchronization
5. **Mobile Navigation**: Bottom tab navigation with floating action button
6. **Database Persistence**: All user data and meetings persist across application restarts

## External Dependencies

### Core Dependencies
- **@neondatabase/serverless**: PostgreSQL connection for serverless environments
- **drizzle-orm**: Type-safe database ORM
- **@tanstack/react-query**: Server state management
- **@radix-ui/***: Accessible UI primitives
- **date-fns**: Date manipulation and timezone handling
- **zod**: Runtime type validation

### Development Tools
- **Vite**: Fast build tool with HMR
- **TypeScript**: Static type checking
- **Tailwind CSS**: Utility-first styling
- **ESLint/Prettier**: Code formatting and linting

### UI Component Library
- **shadcn/ui**: Modern, accessible component library built on Radix UI
- **Lucide React**: Icon library
- **class-variance-authority**: Component variant management

## Deployment Strategy

### Development Environment
- **Hot Reload**: Vite dev server with Express.js backend
- **Database**: Neon PostgreSQL with connection pooling
- **Environment Variables**: DATABASE_URL for database connection

### Production Build
- **Frontend**: Vite build to static assets in dist/public
- **Backend**: ESBuild compilation to dist/index.js
- **Serving**: Express serves both API and static files

### Replit Integration
- **Cartographer Plugin**: Development-only plugin for Replit integration
- **Runtime Error Modal**: Development error handling
- **Replit Banner**: Development mode indicator

## Application Access

- **PawMeet (React/Express)**: http://localhost:5000
- **Flask Chatbot**: http://localhost:8080

## Flask Chatbot Architecture

### Technology Stack
- **Backend**: Flask (Python) with CORS support
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Design**: Mobile-responsive with gradient UI
- **Features**: Real-time chat, typing indicators, contextual responses

### File Structure
- `app.py`: Main Flask application with chatbot logic
- `run.py`: Application runner script  
- `templates/index.html`: Complete frontend with embedded CSS/JS
- `README.md`: Comprehensive documentation

### Response Categories
- Greetings and goodbyes
- Help and support requests
- Weather and time queries
- General conversation responses

### Key Architectural Decisions

1. **Mobile-First Design**: Addresses primary use case of on-the-go meeting scheduling
2. **Timezone-Aware**: Core feature for global meeting coordination
3. **Type Safety**: TypeScript + Zod + Drizzle for end-to-end type safety
4. **Component Reusability**: shadcn/ui for consistent, accessible components
5. **Serverless Ready**: Neon PostgreSQL and stateless backend for scalability
6. **Development Experience**: Fast build times with Vite and hot reload
7. **Dual Application Support**: Flask chatbot runs independently on port 8080