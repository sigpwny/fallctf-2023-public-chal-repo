This is a stego challenge. Theres a comment hinting at this

```html
<!-- data? image? data in an image?? -->
<img src="pikachu.png" alt="Pikachu Image">
```

The flag is appended to `pikachu.png`. You can find it by using `strings`.

```
$ strings pikachu.png | tail -n 1
sigpwny{8_p0rt4ble_n3tw0rk_gr4phic5}
```