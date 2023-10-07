(TeX-add-style-hook
 "crypto"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "letterpaper")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "style"
    "algo")
   (LaTeX-add-labels
    "fig:xkcd"
    "tab:xor")
   (LaTeX-add-bibliographies
    "refs"))
 :latex)

