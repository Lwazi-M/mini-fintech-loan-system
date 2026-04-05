# STAGE 1: Build the React App
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# We pass the production API URL in during the build process!
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL
RUN npm run build

# STAGE 2: Serve with Nginx
FROM nginx:alpine
# Copy the compiled React files from Step 1 into Nginx
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]