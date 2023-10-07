#include <stdio.h>
#include <string.h>

char flag[] = {82, 67, 70, 90, 86, 68, 88, 81, 85, 66, 16, 89, 126, 76, 17, 88, 18, 89, 85, 117, 16, 89, 126, 89, 77, 26, 86, 87, };

static int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n-1);
}

static int combination(int n, int k) {
    if (k == 0 || k == n) {
        return 1;
    }
    return combination(n-1, k-1) + combination(n-1, k);
}

static void decode_flag(int key) {
    for (int i = 0; i < strlen(flag); i++) {
        if (i % 2 == 0)
            flag[i] ^= key & 0xff;
        else
            flag[i] ^= key >> 8;
    }
    printf("Flag: %s\n", flag);
}

/* static void encode_flag() { */
/*     char flag[] = "sigpwny{th1s_f0r3st_1s_sl0w}"; */
/*     int key = 42 << 8 | 33; */
/*     for (int i = 0; i < strlen(flag); i++) { */
/*         if (i % 2 == 0) */
/*             flag[i] ^= key & 0xff; */
/*         else */
/*             flag[i] ^= key >> 8; */
/*     } */
/*     printf("char flag[] = {" ); */
/*     for (int i = 0; i < strlen(flag); i++) { */
/*         printf("%d, ", flag[i] & 0xff); */
/*     } */
/*     printf("};\n"); */
/* } */

int main() {
    int a, b;
    printf("How many trees are in the forest? ");
    scanf("%d", &a);
    printf("How many trees are not in the forest? ");
    scanf("%d", &b);
    int x = combination(a, b);
    int y = factorial(b);
    if (x == 445891810 && y == -2147483648)
        decode_flag(a << 8 | b);
    else
        printf("Sorry, that's not the right answer.\n");
    return 0;
}
