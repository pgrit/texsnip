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

# We also could have generated just the .pdfs, which requires no dependencies and is a bit faster
snips[0].generate(preamble=preamble)
