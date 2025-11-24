def titulo_pagina(arquivo=None) -> str:
    if arquivo is None:
        titulo_da_pagina = "Sem título - Bloco de Notas"
        return titulo_da_pagina
    else:
        titulo_da_pagina = arquivo + " - Bloco de Notas"
        return titulo_da_pagina


class TituloPagina:
    pass
