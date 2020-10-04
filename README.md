# TeXSnip

A small single-module Python package to generate LaTeX text and equations for your favorite vector graphics tool, with no dependencies required! Except LaTeX, of course.

To get started, simply run:
```
pip install texsnip
```

With a few lines of Python code, you can create .pdf files that you can then drag'n'drop into Inkscape, Illustrator, Corel Draw, or most other vector graphics programms.


```python
from texsnip import Snip

# Here, you can modify the LaTeX preamble, for example to configure fonts.
# We use the 'libertine' package, the fonts for the current ACM SIGGRAPH template.
preamble = r"\usepackage{libertine}"

# Write the rendering equation to a file called 'rendering-equation.pdf'
Snip("rendering-equation", 8,
    r"$L_o = L_e + \int_\Omega L_i f \cos\theta_i \,\mathrm{d}\omega_i$"
).generate(preamble)
```

If .pdfs are not supported, don't worry: the script allows you to easily create .png files as well.

```python
Snip("rendering-equation", 8,
    r"$L_o = L_e + \int_\Omega L_i f \cos\theta_i \,\mathrm{d}\omega_i$"
).generate_png(preamble)
```

If you are using these in presentation slides, you can assemble a list of Snips in a .pptx file (uses .png conversion)

```python
from texsnip import Snip, pptx_snips

# Here, you can modify the LaTeX preamble, for example to configure fonts.
# We use the 'libertine' package, the fonts for the current ACM SIGGRAPH template.
preamble = r"\usepackage{libertine}"

snips = [
    # Write the rendering equation to a file called 'rendering-equation.pdf'
    Snip("rendering-equation", 14,
        r"$L_o = L_e + \int_\Omega L_i f \cos\theta_i \,\mathrm{d}\omega_i$"
    ),

    # Sometimes, you need individual terms
    Snip("omega_i", 14,
        r"$\omega_i$"
    ),

    # Or you might want captions for your illustrations with LaTeX typesetting
    Snip("a-caption", 14,
        r"\textsf{a) Some \textcolor[RGB]{200,110,5}{cool} illustration}"
    )
]

# Lets create a snips.pptx with all these snips in it
# This will also create the corresponding .pdf and .png files for use in other applications
pptx_snips(snips, preamble=preamble)
```


## Dependencies

* Python >= 3.6
* LaTeX with pdfcrop (requires Perl) and xcolor, graphicx, inputenc, fontenc

To generate .png images, you will additionally need:
```
pip install pdf2image
```
which requires Poppler to be installed and in the path.

To generate .pptx files, you will need the .png dependencies and also:
```
pip install python-pptx PyPDF2
```