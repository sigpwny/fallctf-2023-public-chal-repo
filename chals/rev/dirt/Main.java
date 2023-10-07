/*
 * This is a reverse engineering challenge for a beginner CTF. The user is only
 * given the compiled jar. The goal is to get them thinking about basic reverse
 * engineering principles. The intended solve will be to decompile the jar and
 * look through the decompiled source to find the flag.
 *
 * There are several comparison for the user to find and figure out. At the end,
 * the program generates and prints the flag. This flag generation function is
 * complex and much harder to reverse engineer than the basic comparisons, so
 * hopefully the user will find the flag by passing the comparisons and not
 * reverse engineering the flag generation function.
 *
 * This challenge is themed around the "jar of dirt" from Pirates of the
 * Caribbean. The questions are all related to the jar of dirt.
 *
 * To run, compile the jar and run it with the command:
 * java -jar Main.jar
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Jar of Dirt Challenge!");
        System.out.println("To find the flag, you must answer some questions related to the jar of dirt.");

        // Basic comparisons
        int question1 = askQuestion("How heavy is the jar of dirt? (in pounds): ");
        int question2 = askQuestion("How many grains of dirt are in the jar? (in millions): ");
        int question3 = askQuestion("How many pirates are in the jar?: ");

        // Flag generation
        if (question1 == 4 && question2 == 77 && question3 == 1) {
            String flag = generateFlag(question2);
            System.out.println("Congratulations! You found the flag: " + flag);
        } else {
            System.out.println("Sorry, you didn't find the flag. Keep trying!");
        }
    }

    private static int askQuestion(String question) {
        Scanner scanner = new Scanner(System.in);
        System.out.print(question);
        String answer = scanner.nextLine().trim().toLowerCase();
        return Integer.parseInt(answer);
    }

    private static String generateFlag(int key) {
        // flag: "sigpwny{ive_g0t_A_J4r_oF_D1rT}" XOR with 77
        int[] encrypted = {62, 36, 42, 61, 58, 35, 52, 54, 36, 59, 40, 18, 42, 125, 57, 18, 12, 18, 7, 121, 63, 18, 34, 11, 18, 9, 124, 63, 25, 48};
        StringBuilder decryptedFlag = new StringBuilder();
        for (int enc : encrypted) {
            char decryptedChar = (char) (enc ^ key);
            decryptedFlag.append(decryptedChar);
        }
        return decryptedFlag.toString();
    }
}
