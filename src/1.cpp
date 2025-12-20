#include <stdio.h>

void calculate_area(int width, int height) {
    int area = width * height;
    printf("Area: %d\n", area);
}

int main() {

    int ancho=0,alto=0;  // A large number
    printf("Calculadora del area de un rectangulo.\n");
    printf("Introduce el ancho.\n");
    scanf("%d",&ancho);
    printf("Introduce el alto.\n");
    scanf("%d",&alto);
    calculate_area(ancho, alto);
    return 0;
}