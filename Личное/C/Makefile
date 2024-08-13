CC = gcc
CFLAGS = -Wall -Wextra -Werror -std=c11

BUILD_PATH = ../build/
SRC = $(wildcard *.c)


all : strlen_tests strcmp_tests strcpy_tests strcat_tests strchr_tests strtok_tests


strlen_tests :
	$(CC) $(CFLAGS) -DSTRLEN $(SRC) -o $(BUILD_PATH)/Quest_1

strcmp_tests :
	$(CC) $(CFLAGS) -DSTRCMP $(SRC) -o $(BUILD_PATH)/Quest_2

strcpy_tests :
	$(CC) $(CFLAGS) -DSTRCPY $(SRC) -o $(BUILD_PATH)/Quest_3

strcat_tests :
	$(CC) $(CFLAGS) -DSTRCAT $(SRC) -o $(BUILD_PATH)/Quest_4

strchr_tests :
	$(CC) $(CFLAGS) -DSTRCHR $(SRC) -o $(BUILD_PATH)/Quest_5

strstr_tests :
	$(CC) $(CFLAGS) -DSTRSTR $(SRC) -o $(BUILD_PATH)/Quest_6

strtok_tests :
	$(CC) $(CFLAGS) -DSTRTOK $(SRC) -o $(BUILD_PATH)/Quest_7


clean :
	rm *.o
	rm $(BUILD_PATH)/*

format : 
	clang-format -i *.c
	clang-format -i *.h

