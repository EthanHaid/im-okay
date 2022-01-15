# Build stage
FROM node:16-slim as build-stage
WORKDIR /app

COPY package*.json /app/

RUN npm install && npm cache clean --force

COPY ./ /app/

RUN npm run build


# Dev stage
FROM node:16-slim as dev-stage
WORKDIR /app

COPY --from=build-stage /app /app

CMD npm run dev


# Production stage
FROM nginx:latest as production-stage

COPY --from=build-stage /app/dist/ /usr/share/nginx/html
COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf