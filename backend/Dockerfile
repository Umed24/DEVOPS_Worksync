# Use an official Node.js runtime as the base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the backend code
COPY . .

# Expose the port that the backend will use
EXPOSE 5000

# Command to run the backend server
CMD ["node", "app.js"]
