# Ativar/Desativar *Forms*

Precisaremos de criar um *script* que permita abrir ou fechar o *Forms* a respostas.

**Nota:** Isto é necessário fazer com um script exterior visto que o **Microsoft Forms** não fornece uma API que permita abrir ou fechar automaticamente.

**Nota 2:** É possível configurar o *Forms* de forma a ele começar numa data e terminar noutra, mas não é possível configurar para este intervalo repetir-se de forma automática.

Isto será feito pelo script [**toggle_forms.py**](../../../src/toggle_forms.py). Este script irá utilizar **Playwright** para simular os cliques necessários para abrir ou fechar o inquérito, dependendo do *input* que receber.

Esta funcionalidade não exige nenhum *setup* adicional ao que foi apresentado no [readme.md anterior](../readme.md).