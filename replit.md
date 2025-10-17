# AI Symptom Checker

## Overview

This is a web-based AI-powered symptom checker application that allows users to input their symptoms and receive AI-generated suggestions for probable medical conditions and recommended next steps. The application leverages Google's Gemini AI to analyze symptoms and provide educational health information. It features a simple, user-friendly interface with a gradient purple design and provides structured medical insights based on user input.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Technology**: Vanilla HTML/CSS/JavaScript (no framework)
- **Design Pattern**: Single-page application with inline styles
- **UI/UX Approach**: Gradient background (purple theme) with centered white container card design
- **Rationale**: Minimal dependencies and fast loading times; suitable for a focused single-purpose application

### Backend Architecture
- **Framework**: FastAPI (Python)
- **API Design**: RESTful API with POST endpoint `/check_symptoms`
- **Request/Response Model**: Pydantic models for type validation
  - `SymptomRequest`: Validates user symptom input
  - `SymptomResponse`: Structures AI-generated response
- **Error Handling**: HTTP exceptions for empty input validation and AI response failures; server-side error logging with user-safe error messages
- **Logging**: Python logging module configured for server-side error tracking
- **Rationale**: FastAPI provides async support, automatic API documentation, and built-in validation - ideal for a lightweight AI service wrapper

### Data Storage
- **Current Implementation**: No persistent data storage
- **Session Management**: None (stateless application)
- **Rationale**: This is a query-based tool that doesn't require user accounts or history persistence; keeps the application simple and privacy-focused

### Security & CORS
- **CORS Configuration**: Permissive (allows all origins)
- **Rationale**: Designed for open access; suitable for demonstration/prototype but should be restricted for production deployment

### Static File Serving
- **Approach**: FastAPI serves static HTML files directly
- **Rationale**: Eliminates need for separate web server; simplifies deployment on platforms like Replit

## External Dependencies

### AI Service Integration
- **Provider**: Google Gemini AI (gemini-2.5-flash model)
- **Library**: `google-genai` Python SDK
- **Authentication**: API key via environment variable (`GEMINI_API_KEY`)
- **Purpose**: Natural language processing of symptoms to generate medical condition suggestions
- **Integration Pattern**: Direct API calls with prompt engineering for medical context

### Python Packages
- **fastapi**: Web framework for API endpoints
- **pydantic**: Data validation and serialization
- **google-genai**: Google's Gemini AI client library
- **uvicorn** (implied): ASGI server for running FastAPI

### Environment Variables
- `GEMINI_API_KEY`: Required for Google Gemini API authentication

### Deployment Considerations
- Application designed to run on Replit with environment secrets
- No database connection required
- Scalability depends on Gemini API rate limits and FastAPI async capabilities