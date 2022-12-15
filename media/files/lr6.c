#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <string.h>
#include <semaphore.h>

sem_t bath;
pthread_mutex_t bath_m;
pthread_mutex_t female_mut;
pthread_mutex_t male_mut;

int MAX_THREADS = 2;
int female_cnt = 0;
int male_cnt = 0;

typedef struct param {
    char *name;
    pthread_mutex_t *mutex;
    int *cnt;
} param;

void work(void *attrs) {
    srand(time(NULL));
    int t;
    param *p = (param *)attrs;
    char *name = p->name;
    pthread_mutex_t *mutex = p->mutex;
    int *cnt = p->cnt;
    while (1) {
        pthread_mutex_lock(mutex);
        printf("%s хочет внутрь\n", name);
        if (*cnt == 0) {
            // sem_wait(&bath);
            pthread_mutex_lock(&bath_m);
        }
        (*cnt)++;
        printf("%s внутри\n", name);
        pthread_mutex_unlock(mutex);
        
        t = rand() % 1000 + 500;
        usleep(t * 1000);
        
        pthread_mutex_lock(mutex);
        (*cnt)--;
        if (*cnt == 0) {
            // sem_post(&bath);
            pthread_mutex_unlock(&bath_m);
        }
        pthread_mutex_unlock(mutex);
        printf("%s снаружи, затрачено %.2f секунд(ы)\n", name, (float)t / 1000.0);
        
        t = rand() % 1500 + 1000;
        usleep(t * 1000);
    }
}

int main(int argc, char const *argv[])
{
    pthread_t male[MAX_THREADS];
    pthread_t female[MAX_THREADS];
    pthread_mutex_init(&female_mut, NULL);
    pthread_mutex_init(&male_mut, NULL);
    // sem_init(&bath, 0, 1);
    pthread_mutex_init(&bath_m, NULL);
    
    for (size_t i = 0; i < MAX_THREADS; i++)
    {
        char *name = malloc(sizeof(char) * 7);
        strncpy(name, "male_ ", 7);
        name[5] = i + 48;
        param *p = malloc(sizeof(p));
        p->name = name;
        p->cnt = &male_cnt;
        p->mutex = &male_mut;
        pthread_create(&male[i], NULL, (void *)work, (void *)p);
    }
    
    for (size_t i = 0; i < MAX_THREADS; i++)
    {
        char *name = malloc(sizeof(char) * 9);
        strncpy(name, "female_ ", 9);
        name[7] = i + 48;
        param *p = malloc(sizeof(p));
        p->name = name;
        p->cnt = &female_cnt;
        p->mutex = &female_mut;
        pthread_create(&female[i], NULL, (void *)work, (void *)p);
    }
    
    while (1) sleep(10);
    
    return 0;
}
