#include <stdio.h>

void main() {
    char secret1[] = {253, 156, 168, 95, 145, 177, 108, 121, 187, 238, 12, 85, 233, 29, 35, 188, 243, 228, 81, 145, 125, 170, 67, 167, 81, 251, 51, 246, 120, 208, 113, 184, 46, 67, 229, 224, 201, 84, 147, 7, 185, 221, 84, 188, 76, 248, 199, 189, 175, 63, 140, 170, 187, 6, 29, 23, 102, 1, 202, 253, 225, 0};
    char secret2[] = {142, 245, 207, 47, 230, 223, 21, 2, 204, 134, 109, 33, 182, 116, 80, 227, 135, 140, 98, 206, 28, 155, 49, 248, 34, 139, 0, 197, 28, 143, 7, 221, 66, 115, 134, 137, 189, 45, 204, 104, 223, 130, 53, 210, 19, 141, 169, 209, 155, 91, 191, 196, 228, 117, 106, 118, 87, 109, 165, 138, 156, 0};
    char input[1024];
    puts("Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.");
    printf("What is your name? ");
    scanf("%1023[^\n]", input);
    getchar();
    printf("What is your quest? ");
    scanf("%1023[^\n]", input);
    getchar();
    printf("What is the flag? ");
    scanf("%1023[^\n]", input);
    getchar();
    for (int i = 0; i < sizeof(secret1); i++) {
        if ((input[i] ^ secret1[i]) != secret2[i]) {
            puts("Wrong! I cast you into the Gorge of Eternal Peril.");
            return;
        }
    }
    puts("You have answered my three questions, hence you may cross.");
}
