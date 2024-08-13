#include "s21_string.h"
#include <stdio.h>

// #define NULL ((void*)0)

int s21_strlen(char *str) {
    int count = 0;
    while (*str++) count++;
    return count;
}

// 1 если символ в первой строке больше символа во второй.
// -1 если этот первый различающийся символ меньше в первой строке.
// 0 если строки равны между собой (нет различающихся символов).

int s21_strcmp(char *str1, char *str2) {
    while (*str1 == *str2 && *str1 != '\0' && *str2 != '\0') {
        str1++;
        str2++;
    }
    return ((*str1 == '\0' && *str2 == '\0') ? 0 : (*str1 > *str2) ? 1 : -1);
}

char *s21_strcpy(char *str1, char *str2) {
    char *current = str1;
    while (*str2 != '\0') {
        *current = *str2;
        current++;
        str2++;
    }
    *current = '\0';
    return str1;
}

char *s21_strcat(char *str1, char *str2) {
    int len = s21_strlen(str1);
    for (int i = 0; str2[i] != '\0'; i++) {
        str1[len + i] = str2[i];
    }
    str1[len + s21_strlen(str2)] = '\0';
    return str1;
}

char *s21_strchr(char *str, int n) {
    while (*str != (char)n && *str != '\0') str++;
    return (*str == (char)n || (char)n == '\0') ? str : "NULL";
}

char *s21_strstr(char *str1, char *str2) {
    int flag = 1;

    for (; *str1 && flag != 0; str1++) {
        char *s1 = str1, *s2 = str2;
        while (*s1 && *s2 && *s1 == *s2) {
            s1++;
            s2++;
        }
        if (!*s2) flag = 0;
    }
    return (flag == 0) ? --str1 : "NULL";
}


// char *s21_strtok(char *str, char *del) {
//     char *end = s21_strstr(str, del);

//     int count = 0;
//     while (*str != *end) {count++; str++;}
    
//     char temp[count] = {};


//     // printf("%s\n", putstr);
//     printf("%s", end);
//     printf("%d", count);

    

//     return "Lya";
// }



char* s21_strtok(char* str1, char* str2)
{
	int n = s21_strlen(str2), i, j, k = 0;
	char* st;
	for(i = 0, j = 0; s21_strlen(str2); i++, j++)
		if(str1[i] == str2[j])
		{
			k++;
		}
    if (n == k)
    { 
		for(int l = 0, m = 0; l < (i + 1); l++, m++)
		{
		      st[l] = str1[m];
        }
        printf("%s", st);
    }
	return NULL;
}