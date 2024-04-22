#include <stdio.h>  
#include <time.h>  
  
int main() {  
    int year, month, day;  
    scanf("%d %d %d", &year, &month, &day);  
    struct tm date = {0};  
    date.tm_year = year - 1900;  
    date.tm_mon = month - 1;  
    date.tm_mday = day;  
    date.tm_isdst = -1;  
    time_t time = mktime(&date);  
    char* weekdays[] = {"星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"};  
    printf("%s\n", weekdays[localtime(&time)->tm_wday]);  
    return 0;  
}
