package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net"
	"os"
	"time"
)

func main() {
	//test()
	conn, err := net.Dial("tcp", "127.0.0.1:8888")
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	mustCopy(os.Stdout, conn)
}

func test() {
	pwd, _ := os.Getwd()
	fmt.Println("pwd:", pwd)
	fileInfoList, _ := ioutil.ReadDir(pwd)
	fmt.Println("文件数量:", len(fileInfoList))
	for i := range fileInfoList {
		fmt.Println(fileInfoList[i].Name()) //打印当前文件或目录下的文件或目录名
	}
	os.Exit(0)
}

func mustCopy(dst io.Writer, src io.Reader) {
	if _, err := io.Copy(dst, src); err != nil {
		log.Fatal(err)
	}
	time.Sleep(1 * time.Second)
}
