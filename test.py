import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Datos para los conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Crear el diagrama de Venn
venn_labels = {'100': 'Set 1', '010': 'Set 2', '110': 'Intersection'}
venn_diagram = venn2([set1, set2])

# Establecer las etiquetas de los conjuntos
venn_diagram.get_label_by_id('100').set_text(venn_labels['100'])
venn_diagram.get_label_by_id('010').set_text(venn_labels['010'])
venn_diagram.get_label_by_id('110').set_text(venn_labels['110'])

# Mostrar el diagrama
plt.show()

