package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello World!")
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Starting Restful services...")
    fmt.Println("Using port:8002")
    err := http.ListenAndServe(":6000", nil)
    log.Print(err)
    errorHandler(err)
}

func errorHandler(err error){
	if err!=nil {
		fmt.Println(err)
		os.Exit(1)
	}
}