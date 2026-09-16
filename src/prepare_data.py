import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data():
    """
    Carrega o dataset de transações financeiras e aplica
    a padronização (StandardScaler) nas colunas de tempo e valor.
    """
    url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
    print("Carregando dataset de transações do repositório remoto...")
    df = pd.read_csv(url)

    # Instancia o escalonador
    scaler = StandardScaler()

    # Normaliza as colunas 'Amount' e 'Time'
    df['scaled_amount'] = scaler.fit_transform(df[['Amount']])
    df['scaled_time'] = scaler.fit_transform(df[['Time']])

    # Remove as colunas originais 'Amount' e 'Time' que foram normalizadas
    df_processed = df.drop(columns=['Time', 'Amount'])

    print(f"Dataset processado com sucesso! Formato: {df_processed.shape}")
    return df_processed

if __name__ == "__main__":
    df = load_and_preprocess_data()
    print(df.head())