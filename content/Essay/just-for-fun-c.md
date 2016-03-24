Title: 反序输入指定行数的字符串
Date: 2016-03-24 22:15
Modified: 2016-03-24 22:15
Tags: fun, c
Slug: just-for-fun-c
Authors: Henry Chen
Summary:
Status: published

[TOC]

好久没写c语言了，今天帮一同学写个例子  
要求如下  

先输入行数，然后依次输入字符串，  
输入完成后，反序输出每行的字符串  

代码如下:  

``` c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_CHARS_PER_LINE 30

typedef struct node {
    char *data;
    struct node *next;
}str_node, *pstr_node;


void print_reversed(char *buf) {
    int i, len = strlen(buf);
    for (i=len-1; i>=0; i--) {
        printf("%c", buf[i]);
    }
    printf("\n");
}


pstr_node create_str_node(char *buf, int len) {
    pstr_node node;
    node = (pstr_node)malloc(sizeof(str_node));
    if (node == NULL) {
        perror("malloc str node error!");
        return NULL;
    }
    
    node->data = (char *)malloc((len+1)*sizeof(char));
    if (node->data == NULL) {
        perror("malloc node data error!");
        return NULL;
    }

    strcpy(node->data, buf);
    node->data[len] = '\0';

    node->next = NULL;

    return node;
}


int free_all(pstr_node head) {
    pstr_node cur_node = head;

    pstr_node tmp_node;
    while (cur_node != NULL) {
        tmp_node = cur_node;
        cur_node = tmp_node->next;
        free(tmp_node->data);
        free(tmp_node);
    }

    return 0;
}


int main() {
    char input_buffer[MAX_CHARS_PER_LINE + 1];
    int total;
    pstr_node head = create_str_node(input_buffer, 0);

    printf("how many lines: ");
    scanf("%d", &total);

    int i = 1;
    int len;
    pstr_node cur_node = head;
    while (i<=total) {
        printf("line %d: ", i);
        scanf("%s", input_buffer);
        len = strlen(input_buffer);
        if (len > MAX_CHARS_PER_LINE) {
            printf("max chars per line is %d\n", MAX_CHARS_PER_LINE);
            return 1;
        }

        pstr_node new_node = create_str_node(input_buffer, strlen(input_buffer));
        if (new_node == NULL) {
            return 1;
        }

        cur_node->next = new_node;
        cur_node = new_node;       

        i++;
    }

    cur_node = head;
    while (cur_node != NULL) {
        print_reversed(cur_node->data);
        cur_node = cur_node->next;
    }

    if (free_all(head) == 0) {
        printf("free all.\n");
    } else {
        printf("some space is not free.\n");
    }

    return 0;
}
```

结果：
``` text
how many lines: 2
line 1: hello
line 2: world

olleh
dlrow
free all.
```

好久没写c语言了，写写开心下。
