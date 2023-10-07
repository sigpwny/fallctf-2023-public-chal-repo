(TeX-add-style-hook
 "refs"
 (lambda ()
   (LaTeX-add-bibitems
    "site:xkcd"))
 '(or :bibtex :latex))

