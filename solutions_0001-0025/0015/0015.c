#include <stdio.h>
#include <inttypes.h>


/** defines para 20x20 */
#define NUM_NODOS		441
#define NUM_NODOS_N 	21
#define LEN_CAMINO 		40


/** defines para 2x2 */
/* #define NUM_NODOS 	9 */
/* #define NUM_NODOS_N 	3 */
/* #define LEN_CAMINO	4 */

/** defines para 3x3 */
/* #define NUM_NODOS 		16 */
/* #define NUM_NODOS_N 	4 */
/* #define LEN_CAMINO		6 */


/* Cabeceras */
void mult_matrix(uint64_t a[][NUM_NODOS], uint64_t b[][NUM_NODOS], uint64_t r[][NUM_NODOS]);
void matrizcpy(uint64_t orig[][NUM_NODOS], uint64_t des[][NUM_NODOS]);
void prlong_matrix(uint64_t a[][NUM_NODOS]);
void elevar_matriz(uint64_t m[][NUM_NODOS], uint64_t potencia);

/* funciones */
void elevar_matriz(uint64_t m[][NUM_NODOS], uint64_t potencia)
{
    uint64_t i;
    uint64_t aux[NUM_NODOS][NUM_NODOS];
    uint64_t resul[NUM_NODOS][NUM_NODOS];

    if (potencia < 2)
    {
        return;
    }

    mult_matrix(m, m, resul);

    for (i = 2; i < potencia; i++)
    {
        mult_matrix(m, resul, resul);
    }

    matrizcpy(resul, m);
}


void matrizcpy(uint64_t orig[][NUM_NODOS], uint64_t des[][NUM_NODOS])
{
    uint64_t i;
    uint64_t j;


    for (i = 0; i < NUM_NODOS; i++)
    {
        for (j = 0; j < NUM_NODOS; j++)
        {
            des[i][j] = orig[i][j];
        }
    }
}



void prlong_matrix(uint64_t a[][NUM_NODOS])
{
    uint64_t i, j;
    for (i = 0; i < NUM_NODOS; i++) {
        for (j = 0; j < NUM_NODOS; j++) {
            printf("%02d ", a[i][j]);
        }
        printf("\n");
    }

    printf("\n\n");
}


void mult_matrix(uint64_t a[][NUM_NODOS], uint64_t b[][NUM_NODOS], uint64_t r[][NUM_NODOS])
{
    uint64_t i, j, k;

    for (i = 0; i < NUM_NODOS; i++) {
        for (j = 0; j < NUM_NODOS; j++) {
            r[i][j] = 0;
            for (k = 0; k < NUM_NODOS; k++)
                r[i][j] += a[i][k] * b[k][j];
        }
    }
}


void calcula_matriz_adyacencia(uint64_t a[][NUM_NODOS])
{
    uint64_t aux[NUM_NODOS_N][NUM_NODOS_N];
    uint64_t i, j, cont;
    uint64_t i_mas_1, j_mas_1;
    uint64_t x;

    for (i = 0, cont = 0; i < NUM_NODOS_N; i++) {
        for (j = 0; j < NUM_NODOS_N; j++) {
            aux[i][j] = cont++;
        }

    }

    for (i = 0, cont = 0; i < NUM_NODOS_N; i++) {
        for (j = 0; j < NUM_NODOS_N; j++) {

            // vemos cuales son los que vamos a tratar
            x = aux[i][j];

            if (j < NUM_NODOS_N - 1) {
                j_mas_1 = aux[i][j + 1];
                a[x][j_mas_1] = 1;
            }

            if (i < NUM_NODOS_N - 1) {
                i_mas_1 = aux[i + 1][j];
                a[x][i_mas_1] = 1;
            }
        }
    }
}



int main(void)
{
    uint64_t m1[NUM_NODOS][NUM_NODOS];

    uint64_t i, j;
    for (i = 0; i < NUM_NODOS; i++) {
        for (j = 0; j < NUM_NODOS; j++) {
            m1[i][j] = 0;
        }
    }

    calcula_matriz_adyacencia(m1);

    /* se elevará al número k dependiendo del número del camino */
    elevar_matriz(m1, LEN_CAMINO);

    printf("%" PRIu64 "\n", m1[0][NUM_NODOS-1]);

    return 0;
}
