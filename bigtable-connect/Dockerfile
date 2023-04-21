FROM golang:1.18
WORKDIR /
COPY app.go .
COPY go.mod .
RUN go get cloud.google.com/go/bigtable@v1.13.0
CMD ["sleep", "infinity"]
