package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"
	"strings"
)

func connectServer() {
	conn, err := net.Dial("tcp", "localhost:8888")
	checkError(err)
	fmt.Println("connect success")
	inputReader := bufio.NewReader(os.Stdin)
	fmt.Println("enter your name")
	name, _ := inputReader.ReadString('\n')
	trimName := strings.Trim(name, "\r\n")
	conn.Write([]byte(trimName))
	fmt.Println("press quit to exit")

	for {
		input, _ := inputReader.ReadString('\n')
		trimInput := strings.Trim(input, "\r\n")
		if trimInput == "quit" {
			fmt.Println("disconnect")
			conn.Write([]byte(" disconnect "))
			return
		}
		_, err = conn.Write([]byte(trimInput))
	}
}

func checkError(err error) {
	if err != nil {
		log.Fatal("an error!", err.Error())
	}
}

//主函数
func main() {
	connectServer()
}
