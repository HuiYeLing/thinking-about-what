#include <stdio.h>  
#include <string.h>  
  
struct class {  
    int id;  
    char info[20];  
}a[5] = {{1, "aaa"}, {2, "bbb"}, {6, "ccc"}, {7, "ddd"}, {4, "eee"}};  
  
int main() {  
    int id;  
    scanf("%d", &id);  
    int i, j = 0;  
    for (i = 0; i < 5; i++) {  
        if (a[i].id == id) {  
            continue; 
        }  
        a[j].id = a[i].id;  
        strcpy(a[j].info, a[i].info);  
        j++;  
    }  
    for (i = 0; i < j; i++) {  
        printf("%d %s\n", a[i].id, a[i].info);  
    }  
    return 0;  
}