# Stage 1: Build Stage
FROM node:20 AS build-stage

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files and build the app
COPY . .

# Build the application (assuming `dist` folder is generated here)
RUN npm run build

# Stage 2: Production Stage
FROM nginx:1.23 AS production-stage

# Copy the built files from the build stage (only dist folder)
COPY --from=build-stage /app/dist /usr/share/nginx/html

# # Optional: Copy a custom Nginx configuration file
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]