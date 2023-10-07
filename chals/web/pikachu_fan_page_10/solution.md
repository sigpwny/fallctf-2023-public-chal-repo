This one is much harder. You have to first find `admin.html` from the previous challenge (Pikachu Fan Page 9).

You must reverse-engineer the password checker.

Basically, we have to get a pre-image for the `confounder` function. This is a function that takes in a string and returns an array of half the length.

The specifics aren't important, but `confounder` operates in groups of two characters in reverse, so we we can define a map of all possible outputs to all possible inputs. Then, we can use this map to invert the function for each output in `clarity` (the encoded flag).

Here's the code:

```javascript
const map = new Map()
for (let a = 0; a < 256; ++a) {
    for (let b = 0; b < 256; ++b) {
        const s = String.fromCharCode(a) + String.fromCharCode(b);
        const c = confounder(s)[0];
        map.set(c, s)
    }
}
const clarity = [18589015185, 87457918842644, 24644425819073, 45176732451089, 27446148711181, 53806695662277, 3155514927104, 94790815812385, 64786397412435, 3422202134961, 13449305162530, 37832204240560, 83971431238790, 94655845646313, 54364008070221, 44508923477814];
const flag = clarity.map(c => map.get(c)).reverse().join("")
```

```
sigpwny{10_r_u_c0nfuzzl3d_yet?}
```