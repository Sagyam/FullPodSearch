# Frontend Development Dockerfile optimized for pnpm
FROM node:22-alpine

WORKDIR /app

# Install pnpm globally
RUN corepack enable && corepack prepare pnpm@latest --activate

# First, copy only the pnpm files for better layer caching
COPY pnpm-lock.yaml package.json ./

# Install dependencies using pnpm
RUN pnpm install --frozen-lockfile

# Copy the rest of the application
COPY . .

# Start development server
CMD ["pnpm", "dev"]