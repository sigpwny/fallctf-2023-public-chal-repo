# Control

Goal is to bypass `door_1` and `door_2`. To do this, look at the code in Ghidra. `door_1` is controlled by a global variable, which can be set in GDB with `set unlocked=1`. `door_2` is configured to always return 0. You can manually set the return value in GDB. Break after the `door_2` call, and then set the return value (which is stored in `$rax`), to 1: `set $rax=1`.
