from texsnip import Snip, pptx_snips

preamble = r"\usepackage{libertine}"

snips = [
    Snip("rendering-equation-6", 6,
        r"Rendering equation: $L_o = L_e + \int_\Omega L_i f \cos\theta_i \,\mathrm{d}\omega_i$"
    ),
    Snip("rendering-equation-12", 12,
        r"Rendering equation: $L_o = L_e + \int_\Omega L_i f \cos\theta_i \,\mathrm{d}\omega_i$"
    ),
    Snip("rendering-equation-24", 24,
        r"Rendering equation: $L_o = L_e + \int_\Omega L_i f \cos\theta_i \,\mathrm{d}\omega_i$"
    ),
    Snip("rendering-equation-100", 100,
        r"Rendering equation: $L_o = L_e + \int_\Omega L_i f \cos\theta_i \,\mathrm{d}\omega_i$"
    ),
]

pptx_snips(snips, preamble=preamble, intermediate_dir="logs")