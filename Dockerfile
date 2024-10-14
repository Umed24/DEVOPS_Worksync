# Use node:18-alpine as the base image
FROM node:18-alpine

# Set working directory for the backend
WORKDIR /app/backend

# Copy backend package.json files and install dependencies
COPY backend/package*.json ./
RUN npm install

# Copy the backend code
COPY backend/ .

# Set up environment variables for the backend
ENV NODE_ENV=development

# Move to the frontend directory for setup
WORKDIR /app/frontend

# Copy frontend package.json files and install dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy the frontend code
COPY frontend/ .

# Increase Node.js memory limit for the build process
ENV NODE_OPTIONS="--max-old-space-size=1024"

# Build the frontend (assuming it's a React app)
RUN npm run build

# Move back to the backend directory
WORKDIR /app/backend

# Copy .env file
COPY backend/.env .env

# Expose the ports for the backend and frontend

# Backend
EXPOSE 1000    

# Frontend
EXPOSE 3000  

# Start both backend and frontend
CMD ["sh", "-c", "node /app/backend/app.js & npm start --prefix /app/frontend"]
