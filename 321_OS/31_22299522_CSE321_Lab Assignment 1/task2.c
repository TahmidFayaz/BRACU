#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

int N; 
int table[2] = {-1, -1}; 
int sandwiches_made = 0;

pthread_mutex_t mutex;
sem_t sem_bread;    
sem_t sem_cheese;  
sem_t sem_lettuce; 
sem_t sem_supplier; 

const char* get_ingredient_name(int ing)
{
    switch(ing)
    {
        case 0: return "Bread";
        case 1: return "Cheese";
        case 2: return "Lettuce";
        default: return "Unknown";
    }
}

void *supplier_thread()
{
    for (int i = 0; i < N; i++)
    {
        sem_wait(&sem_supplier);
        
        pthread_mutex_lock(&mutex);
        
        int ing1 = rand() % 3;
        int ing2;
        do {
            ing2 = rand() % 3;
        } while (ing2 == ing1);
        
        table[0] = ing1;
        table[1] = ing2;
        
        printf("Supplier places: %s and %s\n", 
               get_ingredient_name(ing1), get_ingredient_name(ing2));
        
        pthread_mutex_unlock(&mutex);
        
        if ((ing1 == 0 && ing2 == 1) || (ing1 == 1 && ing2 == 0))
        {
            sem_post(&sem_lettuce);
        }
        else if ((ing1 == 1 && ing2 == 2) || (ing1 == 2 && ing2 == 1))
        {
            sem_post(&sem_bread);
        }
        else if ((ing1 == 0 && ing2 == 2) || (ing1 == 2 && ing2 == 0))
        {
            sem_post(&sem_cheese);
        }
        
        sleep(1);
    }
}

void *Maker_A()
{
    while (1)
    {
        sem_wait(&sem_bread);
        
        pthread_mutex_lock(&mutex);
        
        printf("Maker A picks up %s and %s\n", 
               get_ingredient_name(table[0]), get_ingredient_name(table[1]));
        
        table[0] = -1;
        table[1] = -1;
        
        printf("Maker A is making the sandwich......\n");
        pthread_mutex_unlock(&mutex);
        
        sleep(1);
        
        pthread_mutex_lock(&mutex);
        printf("Maker A finished making the sandwich and eats it\n");
        printf("Maker A signals Supplier\n\n");
        
        sandwiches_made++;
        
        if (sandwiches_made == N)
        {
            pthread_mutex_unlock(&mutex);
            sem_post(&sem_supplier);
            break;
        }
        
        pthread_mutex_unlock(&mutex);
        sem_post(&sem_supplier);
    }
}

void *Maker_B()
{
    while (1)
    {
        sem_wait(&sem_cheese);
        
        pthread_mutex_lock(&mutex);
        
        printf("Maker B picks up %s and %s\n", 
               get_ingredient_name(table[0]), get_ingredient_name(table[1]));
        
        table[0] = -1;
        table[1] = -1;
        
        printf("Maker B is making the sandwich......\n");
        pthread_mutex_unlock(&mutex);
        
        sleep(1);
        
        pthread_mutex_lock(&mutex);
        printf("Maker B finished making the sandwich and eats it\n");
        printf("Maker B signals Supplier\n\n");
        
        sandwiches_made++;
        
        if (sandwiches_made == N)
        {
            pthread_mutex_unlock(&mutex);
            sem_post(&sem_supplier);
            break;
        }
        
        pthread_mutex_unlock(&mutex);
        sem_post(&sem_supplier);
    }
}

void *Maker_C()
{
    while (1)
    {
        sem_wait(&sem_lettuce);
        
        pthread_mutex_lock(&mutex);
        
        printf("Maker C picks up %s and %s\n", 
               get_ingredient_name(table[0]), get_ingredient_name(table[1]));
        
        table[0] = -1;
        table[1] = -1;
        
        printf("Maker C is making the sandwich......\n");
        pthread_mutex_unlock(&mutex);
        
        sleep(1);
        
        pthread_mutex_lock(&mutex);
        printf("Maker C finished making the sandwich and eats it\n");
        printf("Maker C signals Supplier\n\n");
        
        sandwiches_made++;
        
        if (sandwiches_made == N)
        {
            pthread_mutex_unlock(&mutex);
            sem_post(&sem_supplier);
            break;
        }
        
        pthread_mutex_unlock(&mutex);
        sem_post(&sem_supplier);
    }
}

int main(){

    srand((int)getpid());
    
    printf("Enter the number of sandwiches to make: ");
    scanf("%d", &N);
    printf("\n");
    
    pthread_t supplier;
    pthread_t maker_a_thread;
    pthread_t maker_b_thread;
    pthread_t maker_c_thread;
    
    pthread_mutex_init(&mutex, NULL);
    sem_init(&sem_bread, 0, 0);
    sem_init(&sem_cheese, 0, 0);
    sem_init(&sem_lettuce, 0, 0);
    sem_init(&sem_supplier, 0, 1);
    
    pthread_create(&supplier, NULL, supplier_thread, NULL);
    pthread_create(&maker_a_thread, NULL, Maker_A, NULL);
    pthread_create(&maker_b_thread, NULL, Maker_B, NULL);
    pthread_create(&maker_c_thread, NULL, Maker_C, NULL);
    
    pthread_join(supplier, NULL);
    pthread_join(maker_a_thread, NULL);
    pthread_join(maker_b_thread, NULL);
    pthread_join(maker_c_thread, NULL);
    
    pthread_mutex_destroy(&mutex);
    sem_destroy(&sem_bread);
    sem_destroy(&sem_cheese);
    sem_destroy(&sem_lettuce);
    sem_destroy(&sem_supplier);
        
    return 0;
}
