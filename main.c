#include <stdio.h>
#include <stdlib.h>
int cmp_int(const void *a, const void *b)
{ 
    int x=*(const int*)a, y=*(const int*)b; 
    return (x>y)-(x<y); 
}
int main(void){
    int n;
    scanf("%d",&n);
    // TODO: malloc n, leer, qsort, compactar unicos, (opcional) realloc
    // Salida:
    // k
    // a0 a1 ... a(k-1)
    // TODO: free
    return 0;
}
