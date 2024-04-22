#include <windows.h>
#include <stdio.h>

void playSound(char *note) {
    char command[100];
    sprintf(command, "open %s type sequencer alias note", note);
    mciSendString(command, NULL, 0, NULL);
    mciSendString("play note", NULL, 0, NULL);
}

int main() {
    while(1) {
        if(GetAsyncKeyState('A')) {
            playSound("C");
        }
        if(GetAsyncKeyState('S')) {
            playSound("D");
        }
    }
    return 0;
}