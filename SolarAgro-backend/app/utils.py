# import numpy as np

# def calcular_viabilidade(soil_data):
#     """ Função para calcular a viabilidade de instalação de painéis solares """
#     if soil_data['ph'] > 7.5:
#         return 'Solo ácido, não recomendado para instalação'
#     elif soil_data['moisture'] > 50:
#         return 'Solo com alta umidade, instalação difícil'
#     else:
#         return 'Solo apto para instalação de painéis solares'

# def estimar_producao_energia(area):
#     """ Função para estimar a produção de energia """
#     eficiencia_painel = 0.18  # Eficiência média de um painel solar
#     irradiancia_media = 5.5  # Média de radiação solar por dia (kWh/m²)
#     producao = area * eficiencia_painel * irradiancia_media * 365  # Produção anual
#     return producao

# def gerar_relatorio_pdf(terrain_data):
#     """ Função para gerar relatório em PDF do terreno """
#     from reportlab.lib.pagesizes import letter
#     from reportlab.pdfgen import canvas

#     filename = "relatorio_solaragro.pdf"
#     c = canvas.Canvas(filename, pagesize=letter)
#     c.drawString(100, 750, f"Avaliação do terreno: {terrain_data['area']} m²")
#     c.save()
#     return filename







def calculate_solar_potential(soil_data):
    # Função utilitária para cálculo
    return 100 * soil_data.get('suitability_score', 0)
