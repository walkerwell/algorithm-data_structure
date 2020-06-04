package main

import (
	"io"
	"log"
	"net"
	"time"
)

func main() {
	listner, err := net.Listen("tcp", "127.0.0.1:8888")
	if err != nil {
		log.Fatal(err)
	}
	log.Print("server is start")
	for {
		conn, err := listner.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go handleConn(conn)
	}
}

func handlConn11(conn net.Conn) {
	for {
		conn.Close()

	}
}

func handleConn(conn net.Conn) {
	defer conn.Close()
	for {
		_, err := io.WriteString(conn, time.Now().Format("2020-01-02 15:04:05\n"))
		if err != nil {
			log.Print("handleConn err:", err)
			return
		}
		time.Sleep(1 * time.Second)
	}
}
