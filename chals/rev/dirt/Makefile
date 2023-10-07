all: Main.jar

Main.jar: Main.java
	javac "$<"
	jar cfe "$@" Main Main.class


clean:
	rm -f Main.jar Main.class
