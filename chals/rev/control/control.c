#include <stdio.h>

int unlocked;

int door_1() {
    return unlocked;
}

int door_2(int access_code) {
    return 0;
}

void print_flag() {
    char flag[29] = {104, 158, 182, 8, 140, 66, 228, 212, 8, 34, 174, 6, 108, 242, 186, 166, 100, 14, 124, 28, 194, 184, 102, 180, 200, 132, 18, 226, 36};
    for (int i = 0; i < 29; i++) {
        int a = i*2 + 2304;
        a = a ^ (a >> 4);
        a = a ^ (i << 7);
        a = a ^ (a >> 11);
        int b = a;
        while (b != 0) {
            a += (a >> 3);
            b >>= 1;
        }
        flag[i] = ((flag[i] >> unlocked) ^ a) & 0x7f;
    }
    for (int i = 0; i < 29; i++) {
        char tmp = flag[i];
        flag[i] = flag[(i*2)%29];
        flag[(i*2)%29] = tmp;
    }
    printf("Flag: %s\n", flag);
}

void main() {
    unlocked = 0;
    puts("Welcome to CONTROL headquarters.");
    if (door_1()) {
        int access_code;
        puts("Door 1 unlocked.");
        printf("Enter door 2 access code: ");
        scanf("%d", &access_code);
        if (door_2(access_code)) {
            puts("Door 2 unlocked.");
            print_flag();
        } else {
            puts("Door 2 locked.");
        }
    } else {
        puts("Door 1 locked.");
    }
    puts("Unauthorized access attempt detected. CONTROL agents have been dispatched to this location.");
}
