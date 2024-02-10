#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    char S[1000001];
    int alphabet[26] = {0,};
    int max = 0;
    char result;
    scanf("%s", S);

    int length = strlen(S);
    for(int i = 0; i < length; i++) {
        S[i] = toupper(S[i]);
        alphabet[S[i] - 'A']++;
    }

    for(int i = 0; i < 26; i++) {
        if(alphabet[i] > max) {
            max = alphabet[i];
            result = i + 'A';
        }
    }

    for(int i = 0; i < 26; i++) {
        if(i + 'A' != result && alphabet[i] == max) {
            printf("?");
            return 0;
        }
    }

    printf("%c", result);
    return 0;
}