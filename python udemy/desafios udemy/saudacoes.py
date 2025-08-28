#essa função pega a hora atual, minutos tambem soq eu n sei ainda
from datetime import datetime
hora = (datetime.now().hour)

#manha
if hora>=6 and hora<=12:
    print(f"""Atualmente são {hora} da manhã.""")
#tarde
elif hora>12 and hora<=18:
    print(f"""Atualmente são {hora} da tarde.""")
#noite/madrugada
else:
    print(f"""Atualmente são {hora} da noite/madrugada.""")