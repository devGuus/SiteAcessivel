from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)


# Informando o arquivo
df = pd.read_excel("Dados\processamento-petroleo-m3-1990-2023.xls")
df2 = pd.read_excel("Dados\importacoes-exportacoes-petroleo-2000-2023.xls")

# Exibindo o Grafico
fig = px.bar(df, x="UNIDADE DA FEDERAÇÃO", y="ANO", color="PROCESSADO", barmode="group")
meses = list(df["MÊS"].unique()) # pegando os mesês e garantindo que n vai repetir
meses.append("Meses")

app.layout = html.Div(children=[
    html.H1(children='Navegue entre os dados'), # Titulo
    html.H3(children='Analise do funcionamento de Petróleo no Brasil'), # Sub-Titulo
    html.P(children=''' 
        Importação, Exportação e Processamento de Petróleo 
    '''), # Descrição

    dcc.Dropdown(meses, value='Todos os Meses', id='lista_meses'),

    dcc.Graph(
        id='Grafico_Petroleo',
        figure=fig
    )
])

@callback( #Chamando o Grafico
    Output('Grafico_Petroleo', 'figure'),
    Input('lista_meses', 'value')
)
def update_output(value):
    if value == "Todos os Meses":
        fig = px.bar(df, x="UNIDADE DA FEDERAÇÃO", y="ANO", color="PROCESSADO", barmode="group")
    else:
        meses_filtrados = df.loc[df["MÊS"]==value, :]
        fig = px.bar(meses_filtrados, x="UNIDADE DA FEDERAÇÃO", y="ANO", color="PROCESSADO", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True) #Coloca o site no ar