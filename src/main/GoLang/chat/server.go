package main

import (
	"fmt"
	"log"
	"net"
)

func startServer() {
	listener, err := net.Listen("tcp", "localhost:8888")
	checkError(err)
	fmt.Println("connect build success!")
	for {
		conn, err := listener.Accept()
		checkError(err)
		go doServerStuff(conn)
	}
}

func doServerStuff(conn net.Conn) {
	nameInfo := make([]byte, 512)
	_, err := conn.Read(nameInfo)
	fmt.Println(string(nameInfo) + " connecting")
	checkError(err)

	for {
		buf := make([]byte, 512)
		_, err := conn.Read(buf) //
		flag := checkError(err)
		if flag == 0 {
			break
		}
		fmt.Println(string(nameInfo) + " says " + string(buf))
	}
}

func checkError(err error) int {
	if err != nil {
		if err.Error() == "EOF" {
			//fmt.Println("用户退出了")
			return 0
		}
		log.Fatal("an error!", err.Error())
		return -1
	}
	return 1
}
func main() {
	startServer()
}
