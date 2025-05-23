from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def mm_to_p(mm):
    return mm / 0.352777

pdf = canvas.Canvas('./cartaMagnus.pdf', pagesize=A4)

mensagem = """
Se eu fosse uma nuvem, pairaria só sobre você —  
porque em qualquer lugar que você vai, o clima muda...  
fica mais leve, mais bonito, mais vivo.

Você é o meu anticiclone tropical:  
toda vez que se aproxima, meu coração aquece e a pressão sobe.

E no campo da biologia, você é como uma célula-tronco:  
tem o poder de transformar qualquer momento simples em algo extraordinário.

Teu sorriso libera mais serotonina que qualquer hormônio natural,  
e tua presença tem fotossíntese própria — me dá vida só de te ver.

Se amar fosse ciência, eu te estudaria todos os dias,  
porque você é o meu fenômeno favorito,  
meu ecossistema perfeito,  
minha previsão de felicidade a longo prazo.

— Com carinho (e uma leve frente de paixão), Magnus 🌦️🌿
"""

# Escreve a mensagem no PDF em múltiplas linhas
y = mm_to_p(270)
for linha in mensagem.strip().split('\n'):
    pdf.drawString(mm_to_p(20), y, linha.strip())
    y -= mm_to_p(10)

pdf.save()
