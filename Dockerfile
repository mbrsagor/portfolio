# Use the official nginx image
FROM nginx:alpine

# Copy website files to nginx's public directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80
