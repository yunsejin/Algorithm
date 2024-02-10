#include <stdio.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    char S[101];
    int alphabet[26];
    scanf("%s", S);

    for(int i = 0; i < 26; i++) 
        alphabet[i] = -1;

    for(int i = 0; i < strlen(S); i++) {
        if(alphabet[S[i] - 'a'] == -1)
           alphabet[S[i] - 'a'] = i;
    }

    for(int i = 0; i < 26; i++) 
        printf("%d ", alphabet[i]);

    return 0;
}