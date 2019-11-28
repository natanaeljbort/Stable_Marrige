#include <math.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

float stencil ( float v1, float v2, float v3, float v4 )
{
  return (v1 + v2 + v3 + v4)/4;
}
/*
void laplace_step ( float *in, float *out, int n, int m )
{
  int i, j;
  float error=0.0f;
  for ( i=1; i < m-1; i++ ){
    for ( j=1; j < n-1; j++ ){
      out[j*m+i]= stencil(in[j*m+i+1], in[j*m+i-1], in[(j-1)*m+i], in[(j+1)*m+i]);
      }}}
*/
float laplace_error ( float *old, float *new, int n, int m )
{
  int i, j;
  float error=0.0f;
  for ( i=1; i < m-1; i++ ){
    for ( j=1; j < n-1; j++ ){
        new[j*m+i]= stencil(old[j*m+i+1], old[j*m+i-1], old[(j-1)*m+i], old[(j+1)*m+i]);
      error = fmaxf( error, sqrtf( fabsf( old[j*m+i] - new[j*m+i] )));}}
  return error;
}

void laplace_copy ( float *in, float *out, int n, int m )
{
  int i, j;
  for ( i=1; i < m-1; i++ )
    for ( j=1; j < n-1; j++ )
      out[j*m+i]= in[j*m+i];
}


void laplace_init ( float *in, int n, int m )
{
  int i, j;
  const float pi  = 2.0f * asinf(1.0f);
  memset(in, 0, n*m*sizeof(float));
  for (i=0; i<m; i++)  in[    i    ] = 0.f;
  for (i=0; i<m; i++)  in[(n-1)*m+i] = 0.f;
  for (j=0; j<n; j++)  in[   j*m   ] = sinf(pi*j / (n-1));
  for (j=0; j<n; j++)  in[ j*m+m-1 ] = sinf(pi*j / (n-1))*expf(-pi);
}

int main(int argc, char** argv)
{
  int n = 409, m = 409;
  int iter_max = 1000;
  float *A, *Anew;

  const float tol = 1.0e-4f;
  float error= 1.0f;

  // get runtime arguments: n, m and iter_max
  if (argc>1) {  n        = atoi(argv[1]); }
  if (argc>2) {  m        = atoi(argv[2]); }
  if (argc>3) {  iter_max = atoi(argv[3]); }

  A    = (float*) malloc( n*m*sizeof(float) );
  Anew = (float*) malloc( n*m*sizeof(float) );

  //  set boundary conditions
  laplace_init (A, n, m);
  A[(n/128)*m+m/128] = 1.0f; // set singular point

  printf("Jacobi relaxation Calculation: %d x %d mesh,"
         " maximum of %d iterations\n",
         n, m, iter_max );

  int iter = 0;
  while ( error > tol && iter < iter_max )
  {
    iter++;
    //laplace_error (A, Anew, n, m);
    error= laplace_error (A, Anew, n, m);
    laplace_copy (Anew, A, n, m);
    if (iter % (iter_max/10) == 0) printf("%5d, %0.6f\n", iter, error);
  }
  printf("Total Iterations: %5d, ERROR: %0.6f, ", iter, error);
  printf("A[%d][%d]= %0.6f\n", n/128, m/128, A[(n/128)*m+m/128]);

  free(A);
  free(Anew);
}
