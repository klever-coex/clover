FROM billryan/gitbook AS builder

COPY docs /gitbook

RUN gitbook build

FROM nginx:1.29.3-alpine-slim

COPY --from=builder /gitbook/_book /usr/share/nginx/html

COPY docker/docs/nginx.conf /etc/nginx/default.conf

CMD ["nginx", "-g", "daemon off;"]
