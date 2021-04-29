import pandas as pd

#tabelad de IDH
df_mun = pd.read_csv('municipios_micro_regiao.csv')
df_idh = pd.read_csv('idh.csv')
df_mun = df_mun.rename(columns={'municipio': 'Município'})
df_idh = df_idh.merge(df_mun, on='Município', how='left')
print(df_idh.head())
print()
#quando precisar criar um csv do dataframe acima
#df_idh_new = df_idh.to_csv('acho_que_agora_vai_idh.csv')

#tabela de PIB
df_pib = pd.read_csv('pib_pop.csv')
print('PIB estado de Santa Catarina:')
df_pib = df_pib.merge(df_mun, on='Município', how='left')
print(df_pib.head())
#quando precisar criar um csv do dataframe acima
#df_pib_new = df_pib.to_csv('perfil_dos_municipios.csv')

#tabela saldo de emprego
print('Saldo de empregos de Santa Catarina: ')
df_saldo = pd.read_csv('saldoempregos.csv', delimiter=';', encoding='latin1')
df_saldo = df_saldo.merge(df_mun, on='Município', how='left')
print(df_saldo.head())
#comando abaixo usado para criar um csv
#df_saldo_new = df_saldo.to_csv('saldo_empregos_sc.csv')

#tabela com a escolaridade
print('Escolaridade dos trabalhadores de SC:')
df_escol = pd.read_csv('escolaridade_new.csv', delimiter=';')
print(df_escol.head(10))
print(df_escol.isnull().sum())
#deletando a coluna Unnamed 4
df_escol_new = df_escol.drop(columns=['Unnamed: 4'])
print(df_escol_new.head(50))
print(f'O dataframe original possui {df_escol_new.shape[0]} linhas e {df_escol_new.shape[1]} colunas.')
#agrupando as linhas conforme município, setor e escolaridade
df_escol_new = df_escol_new.groupby(['Município', 'Setor', 'Escolaridade'], as_index=False).sum()
print(f'O dataframe atualizado possui {df_escol_new.shape[0]} linhas e {df_escol_new.shape[1]} colunas.')
print(df_escol_new.head(50))
#adicionando a vice-presidencia
df_escol_new = df_escol_new.merge(df_mun, on='Município', how='left')
print(df_escol_new.head())
df_escol_new.to_csv('escolaridade_para_enviar.csv')