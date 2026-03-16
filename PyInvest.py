#Importação das bibliotecas

import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Entradas

capital = float(input('Capital inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual (%): '))/100
percentual_cdb = float(input('Percentual do CDI (%): '))/100
percentual_da_lci = float(input('Percentual da LCI (%): '))/100
taxa_fii = float(input('Rentabilidade menasal FII (%): '))/100
meta = float(input('Meta finaceira (R$):'))

#Conversão CDI
cdi_mensal = math.pow(1 + cdi_anual, 1/12) -1 

#Total Investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * percentual_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses) + (aporte * meses))
lucro_cdb = montante_cdb - total_investido
montante_do_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_da_lci = cdi_mensal * percentual_da_lci
montante_lci = (capital * math.pow((1 + taxa_da_lci), meses) + (aporte * meses))

#Poupança
taxa_da_poupanca = 0.005
montante_da_poupanca = (capital * math.pow((1 + taxa_da_poupanca), meses) + (aporte * meses))

#FII - Simulações
montante_fii = capital * math.pow((1 + taxa_fii), meses) + (aporte * meses)
v1 = random.uniform(-0.03, 0.03)
v2 = random.uniform(-0.03, 0.03)
v3 = random.uniform(-0.03, 0.03)
v4 = random.uniform(-0.03, 0.03)
v5 = random.uniform(-0.03, 0.03)
fii1 = montante_fii * (1 + v1)
fii2 = montante_fii * (1 + v2)
fii3 = montante_fii * (1 + v3)
fii4 = montante_fii * (1 + v4)
fii5 = montante_fii * (1 + v5)
media_fii = statistics.mean([fii1, fii2, fii3, fii4, fii5])
mediana_fii = statistics.median([fii1, fii2, fii3, fii4, fii5])
desvio_fii = statistics.stdev([fii1, fii2, fii3, fii4, fii5])

#Data
data_simulacao = datetime.date.today()
dias = meses * 30
data_resgate = data_simulacao + datetime.timedelta(days=dias)

#Formatação
total_investido_formatado = locale.currency(total_investido, grouping=True)
cdb_formatado = locale.currency(montante_do_cdb_liquido, grouping=True)
lci_formatado = locale.currency(montante_lci, grouping=True)
poupanca_formatado = locale.currency(montante_da_poupanca, grouping=True)
fii_formatado = locale.currency(media_fii, grouping=True)
data_simulacao_formatada = data_simulacao.strftime("%d/%m/%Y")
data_resgate_formatada = data_resgate.strftime("%d/%m/%Y")
#metas
meta_cdb = montante_do_cdb_liquido >= meta
meta_lci = montante_lci >= meta
meta_poupanca = montante_da_poupanca >= meta
meta_fii = media_fii >= meta

#gráficos
grafico_cdb = "█" * int(montante_do_cdb_liquido / 1000)
grafico_lci = "█" * int(montante_lci / 1000)
grafico_poupanca = "█" * int(montante_da_poupanca / 1000)
grafico_fii = "█" * int(media_fii / 1000)

#relatório
print("\n===== RELATÓRIO DE INVESTIMENTO =====")

print("Data da simulação:", data_simulacao_formatada)
print("Data estimada de resgate:", data_resgate_formatada)

print("\nTotal investido:", total_investido_formatado)

print("\n--- RESULTADOS ---")

print("CDB:", cdb_formatado)
print("LCI:", lci_formatado)
print("Poupança:", poupanca_formatado)
print("FII (média):", fii_formatado)

print("\n--- Estatísticas FII ---")
print("Média:", locale.currency(media_fii, grouping=True))
print("Mediana:", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(desvio_fii, grouping=True))

print("\n--- Meta Financeira ---")
print("CDB bateu a meta?", meta_cdb)
print("LCI bateu a meta?", meta_lci)
print("Poupança bateu a meta?", meta_poupanca)
print("FII bateu a meta?", meta_fii)

print("\n--- Gráficos ---")
print("CDB:", grafico_cdb)
print("LCI:", grafico_lci)
print("Poupança:", grafico_poupanca)
print("FII:", grafico_fii)
