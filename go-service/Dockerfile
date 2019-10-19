FROM golang:1.13.2-alpine
RUN mkdir /app 
ADD . /app/ 
WORKDIR /app 
EXPOSE 6000
RUN go build -o main . 
CMD ["/app/main"]