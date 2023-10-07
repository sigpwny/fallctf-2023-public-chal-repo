This one gets a bit harder. You have to use the `robots.txt` file to find the flag. This is used by search engines and other web crawlers to find out what pages they should not index.

Here's what the `robots.txt` file looks like:

```
User-agent: *
Disallow: /admin.html
```

The admin page has the flag as ascii art in a comment. Make sure to view the file in a way that shows this in an easy-to-read way (don't have line wrapping on.) You can use view-source, or you can use the devtools to look at the Network or Sources tab.

```html
<!--
        _                                                __   ___                            _        ___    _                          _               _   _                     ___    _                               _         __   
       (_)                                              / /  / _ \                          | |      / _ \  | |                        | |             | | | |                   / _ \  | |                             | |        \ \  
  ___   _    __ _   _ __   __      __  _ __    _   _   | |  | (_) |           _ __    ___   | |__   | | | | | |_   ___            ___  | |__     __ _  | | | |           _ __   | | | | | |_            _ __     __ _  / __)  ___   | | 
 / __| | |  / _` | | '_ \  \ \ /\ / / | '_ \  | | | | / /    \__, |          | '__|  / _ \  | '_ \  | | | | | __| / __|          / __| | '_ \   / _` | | | | |          | '_ \  | | | | | __|          | '_ \   / _` | \__ \ / __|   \ \
 \__ \ | | | (_| | | |_) |  \ V  V /  | | | | | |_| | \ \      / /           | |    | (_) | | |_) | | |_| | | |_  \__ \          \__ \ | | | | | (_| | | | | |          | | | | | |_| | | |_           | |_) | | (_| | (   / \__ \   / /
 |___/ |_|  \__, | | .__/    \_/\_/   |_| |_|  \__, |  | |    /_/            |_|     \___/  |_.__/   \___/   \__| |___/          |___/ |_| |_|  \__,_| |_| |_|          |_| |_|  \___/   \__|          | .__/   \__,_|  |_|  |___/  | | 
             __/ | | |                          __/ |   \_\          ______                                              ______                                 ______                         ______  | |                         /_/  
            |___/  |_|                         |___/                |______|                                            |______|                               |______|                       |______| |_|                               
-->
```

This is read as:

```
sigpwny{9_rob0ts_shall_n0t_pa$s}
```
