#include "s21_string.h"

#include <stdio.h>
#include <string.h>

#include "s21_string_test.h"

int main() {
#ifdef STRLEN
    s21_strlen_test();
#endif

#ifdef STRCMP
    s21_strcmp_test();
#endif

#ifdef STRCPY
    s21_strcpy_test();
#endif

#ifdef STRCAT
    s21_strcat_test();
#endif

#ifdef STRCHR
    s21_strchr_test();
#endif

#ifdef STRSTR
    s21_strstr_test();
#endif

#ifdef STRTOK
    s21_strtok_test();
#endif

    return 0;
}

void s21_strlen_test() {
    printf("|%-25s|%-7d|%-7s|\n", "HELLO", s21_strlen("HELLO"),
           s21_strlen("HELLO") == 5 ? "SUCCESS" : "FAIL");

    printf("|%-25s|%-7d|%-7s|\n", "\"\\0\"", s21_strlen("\0"), s21_strlen("\0") == 0 ? "SUCCESS" : "FAIL");

    printf("|%-25s|%-7d|%-7s|\n", "h e l l o w o r l d", s21_strlen("h e l l o w o r l d"),
           s21_strlen("h e l l o w o r l d") == 19 ? "SUCCESS" : "FAIL");

    printf("|%-25s|%-7d|%-7s|\n", "\"\"", s21_strlen(""), s21_strlen("") == 0 ? "SUCCESS" : "FAIL");
}

void s21_strcmp_test() {
    printf("|%-12s|%-12s|%-7d|%-7s|\n", "HELLO", "HELLO", s21_strcmp("HELLO", "HELLO"),
           s21_strcmp("HELLO", "HELLO") == 0 ? "SUCCESS" : "FAIL");

    printf("|%-12s|%-12s|%-7d|%-7s|\n", "HELLO", "WORLD", s21_strcmp("HELLO", "WORLD"),
           s21_strcmp("HELLO", "WORLD") == -1 ? "SUCCESS" : "FAIL");

    printf("|%-12s|%-12s|%-7d|%-7s|\n", "WORLD", "HELLO", s21_strcmp("WORLD", "HELLO"),
           s21_strcmp("WORLD", "HELLO") == 1 ? "SUCCESS" : "FAIL");

    printf("|%-12s|%-12s|%-7d|%-7s|\n", "\" \"", "\" \"", s21_strcmp(" ", " "),
           s21_strcmp(" ", " ") == 0 ? "SUCCESS" : "FAIL");
}

void s21_strcpy_test() {
    char destination1[10];
    printf("|%-15s|%-10d|", "CAT", (int)sizeof(destination1));
    if (s21_strlen("CAT") > (int)sizeof(destination1)) {
        printf("%-15s|%-7s|\n", "n/a", "FAIL");
    } else {
        s21_strcpy(destination1, "CAT");
        printf("%-15s|%-7s|\n", destination1, s21_strcmp(destination1, "CAT") == 0 ? "SUCCESS" : "FAIL");
    }

    char destination2[5];
    printf("|%-15s|%-10d|", "HELLO WORLD", (int)sizeof(destination2));

    if (s21_strlen("HELLO WORLD") > (int)sizeof(destination2)) {
        printf("%-15s|%-7s|\n", "n/a", "FAIL");
    } else {
        s21_strcpy(destination2, "HELLO WORLD");
        printf("%-15s|%-7s|\n", destination2,
               s21_strcmp(destination2, "HELLO WORLD") == 0 ? "SUCCESS" : "FAIL");
    }

    char destination3[1];
    printf("|%-15s|%-10d|", "0", (int)sizeof(destination3));

    if (s21_strlen(" ") > (int)sizeof(destination3)) {
        printf("%-15s|%-7s|\n", "n/a", "FAIL");
    } else {
        s21_strcpy(destination3, "0");
        printf("%-15s|%-7s|\n", destination3, s21_strcmp(destination3, "0") == 0 ? "SUCCESS" : "FAIL");
    }
}

void s21_strcat_test() {
    char destination1[15] = "CAT";
    printf("|%-15s|%-15s|%-10d|", destination1, " AND DOG", (int)sizeof(destination1));

    if ((int)sizeof(destination1) < s21_strlen(destination1) + s21_strlen(" AND DOG")) {
        printf("%-20s|%-7s|\n", "n/a", "FAIL");
    } else {
        s21_strcat(destination1, " AND DOG");
        printf("%-20s|%-7s|\n", destination1,
               (s21_strcmp(destination1, "CAT AND DOG") == 0) ? "SUCCESS" : "FAIL");
    }

    char destination2[10] = "CAT";
    printf("|%-15s|%-15s|%-10d|", destination2, " AND DOG", (int)sizeof(destination2));

    if ((int)sizeof(destination2) < s21_strlen(destination2) + s21_strlen(" AND DOG")) {
        printf("%-20s|%-7s|\n", "n/a", "FAIL");
    } else {
        s21_strcat(destination2, " AND DOG");
        printf("%-20s|%-7s|\n", destination1,
               (s21_strcmp(destination2, "CAT AND DOG") == 0) ? "SUCCESS" : "FAIL");
    }

    char destination3[5] = "CAT";
    printf("|%-15s|%-15s|%-10d|", destination3, " ", (int)sizeof(destination3));

    if ((int)sizeof(destination3) < s21_strlen(destination3) + s21_strlen(" ")) {
        printf("%-20s|%-7s|\n", "n/a", "FAIL");
    } else {
        s21_strcat(destination3, " ");
        printf("%-20s|%-7s|\n", destination3, (s21_strcmp(destination3, "CAT ") == 0) ? "SUCCESS" : "FAIL");
    }
}

void s21_strchr_test() {
    printf("|%-10s|%-5s|%-10s|%-10s|\n", "CAT", "A", s21_strchr("CAT", 'A'),
           s21_strcmp(s21_strchr("CAT", 'A'), "AT") == 0 ? "SUCCESS" : "FAIL");

    printf("|%-10s|%-5s|%-10s|%-10s|\n", "DOG", "A", s21_strchr("DOG", 'A'),
           s21_strcmp(s21_strchr("DOG", 'A'), "NULL") == 0 ? "SUCCESS" : "FAIL");

    printf("|%-10s|%-5s|%-10s|%-10s|\n", "DOG", "\"\\0\"", s21_strchr("DOG", '\0'),
           s21_strcmp(s21_strchr("DOG", '\0'), "") == 0 ? "SUCCESS" : "FAIL");
}

void s21_strstr_test() {
    printf("|%-10s|%-5s|%-10s|%-10s|\n", "CAT", "T", s21_strstr("CAT", "T"),
           s21_strcmp(s21_strstr("CAT", "T"), "T") == 0 ? "SUCCESS" : "FAIL");

    printf("|%-10s|%-5s|%-10s|%-10s|\n", "DOG", "", s21_strstr("DOG", ""),
           s21_strcmp(s21_strstr("DOG", ""), "DOG") == 0 ? "SUCCESS" : "FAIL");

    printf("|%-10s|%-5s|%-10s|%-10s|\n", "\"\\0\"", "\" \"", s21_strstr("\0", " "),
           s21_strcmp(s21_strstr("\0", " "), "NULL") == 0 ? "SUCCESS" : "FAIL");
}


void s21_strtok_test() {
      
    // char *token; 
    char *str = "Python, C, Java";
    s21_strtok(str, ", ");
    // while (token != NULL){
    //     printf("%s ", token);
    //     // str += token;
    //     token = s21_strtok(str, ", ");
    // }


    // token = strtok("Python, C, Java", ", ");
    // while (token != NULL){
    //     printf("%s ", token);
    //     token = strtok(NULL, ", ");
    // }


}


