# Build Stage
# First pull Golang image
FROM golang:1.17-alpine as build-env
 
# Set environment variable
ENV APP_NAME devops-test-app
ENV CMD_PATH main.go
 
# Copy application data into image
COPY . $GOPATH/src/$APP_NAME
WORKDIR $GOPATH/src/$APP_NAME
 
# Budild application
RUN CGO_ENABLED=0 go build -v -o /$APP_NAME $GOPATH/src/$APP_NAME/$CMD_PATH
 
# Run Stage
FROM alpine:3.14

ARG APP_JWT_SECRET

# Set environment variable

ENV APP_NAME devops-test-app
ENV APP_JWT_SECRET=$APP_JWT_SECRET

COPY --from=build-env /$APP_NAME .
 
# Expose application port
EXPOSE 3000
 
# Start app
CMD ./$APP_NAME