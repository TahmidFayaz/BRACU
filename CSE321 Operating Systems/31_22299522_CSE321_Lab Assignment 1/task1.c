#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

int a = 0;
int b = 1;

int numbers;
int search_count;

void *F_Sequence(void *nums);
void *F_Search(void *nums);

int main() {
    pthread_t t1;
    pthread_t t2;

    do {
        printf("Enter the term of fibonacci sequence: ");
        scanf("%d", &numbers);
    } while (!(numbers >= 0 && numbers <= 40));

    do {
        printf("How many numbers are you trying to search? ");
        scanf("%d", &search_count);
    } while (search_count < 0);

    numbers++;
    search_count++;

    int *x = (int *)malloc(numbers * sizeof(int));
    if (x == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    pthread_create(&t1, NULL, F_Sequence, (void *)x);
    pthread_join(t1, NULL);

    pthread_create(&t2, NULL, F_Search, (void *)x);
    pthread_join(t2, NULL);

    free(x);
    return 0;
}

void *F_Sequence(void *nums) {
    int *arr = (int *)nums;

    arr[0] = a;
    arr[1] = b;
    printf("a[0] = %d\n", arr[0]);
    printf("a[1] = %d\n", arr[1]);

    for (int i = 2; i < numbers; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
        printf("a[%d] = %d\n", i, arr[i]);
    }

    pthread_exit(NULL);
}

void *F_Search(void *nums) {
    int *arr = (int *)nums;
    int search_index;

    for (int i = 1; i < search_count; i++) {
        printf("Enter Search %d: ", i);
        scanf("%d", &search_index);

        printf("Result of search #%d = ", i);
        if (search_index < 0 || search_index >= numbers) {
            printf("-1\n");
        } else {
            printf("%d\n", arr[search_index]);
        }
    }

    pthread_exit(NULL);
}


