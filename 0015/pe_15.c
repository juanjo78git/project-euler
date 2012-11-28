# include "stdio.h"



/** defines para 20x20 */
#define NUM_NODOS		441
#define NUM_NODOS_N 	21
#define LEN_CAMINO 		40


/** defines para 2x2 */
/*
#define NUM_NODOS 	9
#define NUM_NODOS_N 	3
#define LEN_CAMINO	4
*/

/** defines para 3x3 */
/*
#define NUM_NODOS 		16
#define NUM_NODOS_N 	4
#define LEN_CAMINO		6
*/

/** defines para 4x4 */
/*
#define NUM_NODOS 		25
#define NUM_NODOS_N 	5
#define LEN_CAMINO		8
*/


void mult_matrix(long a[][NUM_NODOS], long b[][NUM_NODOS], long r[][NUM_NODOS]);
void matrizcpy(long orig[][NUM_NODOS], long des[][NUM_NODOS]);
void prlong_matrix(long a[][NUM_NODOS]);

void elevar_matriz(long m[][NUM_NODOS], long potencia)
{
	long i;
	long aux[NUM_NODOS][NUM_NODOS];
	long resul[NUM_NODOS][NUM_NODOS];
	
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


void matrizcpy(long orig[][NUM_NODOS], long des[][NUM_NODOS])
{
	long i;
	long j;

	
	for (i = 0; i < NUM_NODOS; i++)
	{
		for (j = 0; j < NUM_NODOS; j++)
		{
			des[i][j] = orig[i][j];
		}
	}
}



void prlong_matrix(long a[][NUM_NODOS])
{
    long i, j;
    for (i = 0; i < NUM_NODOS; i++) {
	for (j = 0; j < NUM_NODOS; j++) {
	    printf("%d\t", a[i][j]);
	}
	printf("\n");
    }

    printf("\n\n");
}

void prlong_matrix2(long a[][NUM_NODOS_N])
{
    long i, j;
    for (i = 0; i < NUM_NODOS_N; i++) {
	for (j = 0; j < NUM_NODOS_N; j++) {
	    printf("%d\t", a[i][j]);
	}
	printf("\n");
    }

    printf("\n\n");
}

void
mult_matrix(long a[][NUM_NODOS], long b[][NUM_NODOS], long r[][NUM_NODOS])
{
    long i, j, k;

    for (i = 0; i < NUM_NODOS; i++) {
	for (j = 0; j < NUM_NODOS; j++) {
	    r[i][j] = 0;
	    for (k = 0; k < NUM_NODOS; k++)
		r[i][j] += a[i][k] * b[k][j];
	}
    }
}

void calcula_matriz_adyacencia(long a[][NUM_NODOS])
{

    long aux[NUM_NODOS_N][NUM_NODOS_N];

    long i, j, cont;
    long i_mas_1, j_mas_1;
    long x;

    //long

    for (i = 0, cont = 0; i < NUM_NODOS_N; i++) {
	for (j = 0; j < NUM_NODOS_N; j++) {
	    aux[i][j] = cont++;
	}

    }

    prlong_matrix2(aux);

    for (i = 0, cont = 0; i < NUM_NODOS_N; i++) {
	for (j = 0; j < NUM_NODOS_N; j++) {

	    // vemos cuales son los que vamos a tratar
	    x = aux[i][j];

	    //printf("valores de i e j [%d][%d]\n", i, j);

	    if (j < NUM_NODOS_N - 1) {
		j_mas_1 = aux[i][j + 1];
		a[x][j_mas_1] = 1;

		//printf("no estamos en borde por j, x[%d], j_mas_1[%d]\n",
		       //x, j_mas_1);
	    }

	    if (i < NUM_NODOS_N - 1) {
		i_mas_1 = aux[i + 1][j];
		a[x][i_mas_1] = 1;
		//printf("no estamos en borde por i, x[%d], i_mas_1[%d]\n",
		      // x, j_mas_1);
	    }


	    //prlong_matrix(a);

	}

    }

    //prlong_matrix(a);

}




main()
{
    //long mult[NUM_NODOS][NUM_NODOS];

    long m1[NUM_NODOS][NUM_NODOS];
    //long m2[NUM_NODOS][NUM_NODOS];

    long i, j;
    for (i = 0; i < NUM_NODOS; i++) {
	for (j = 0; j < NUM_NODOS; j++) {
	    m1[i][j] = 0;
	    //m2[i][j] = 0;
	}
    }

    calcula_matriz_adyacencia(m1);

    //calcula_matriz_adyacencia(m2);

	//prlong_matrix(m1);

/*
        printf("Multiplication of the Matrices:\n");
        for(i=0;i<r1;i++)
        {
            for(j=0;j<c2;j++)
            {
                mult[i][j]=0;
                for(k=0;k<r1;k++)
                    mult[i][j]+=m1[i][k]*m2[k][j];
            }
        }
*/


	/* se elevará al número k dependiendo del número del camino */



	elevar_matriz(m1, LEN_CAMINO);

	//prlong_matrix(m1);
	
	printf("Número de caminos: [%ld]\n", m1[0][NUM_NODOS-1]);
	
	return 0;



	
	/* la primera multiplicacion para realizar el M² */
/*	mult_matrix(m1, m2, mult);
	
	for (i = 1; i < LEN_CAMINO - 1; i++)
	{
		mult_matrix(m1, mult, mult);
	
	
	}

    

    prlong_matrix(mult);

    mult_matrix(m1, mult, mult);


    prlong_matrix(mult);

    

    prlong_matrix(mult);

    mult_matrix(m1, mult, mult);

    prlong_matrix(mult);

    mult_matrix(m1, mult, mult);

    prlong_matrix(mult);


    return 0;
    
    */
}



