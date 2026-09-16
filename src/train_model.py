import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
from prepare_data import load_and_preprocess_data

def train_isolation_forest():
    # 1. Carrega os dados pré-processados
    df = load_and_preprocess_data()

    # Separação de atributos de entrada (X) e a classe real (y)
    X = df.drop(columns=['Class'])
    y = df['Class']

    # Calcula a taxa real de contaminação (fraudes / total)
    contamination_rate = y.mean()
    print(f"Taxa estimada de contaminação/anomalias: {contamination_rate:.4%}")

    # 2. Inicialização e Treinamento do Isolation Forest
    print("Treinando o modelo Isolation Forest...")
    model = IsolationForest(
        n_estimators=100,
        contamination=contamination_rate,
        random_state=42,
        n_jobs=-1
    )

    # Isolation Forest retorna 1 para normal e -1 para anomalia
    raw_predictions = model.fit_predict(X)

    # Converte predições para a convenção (0 = Normal, 1 = Anomalia/Fraude)
    y_pred = np.where(raw_predictions == -1, 1, 0)

    # 3. Avaliação das Métricas
    print("\n" + "="*50)
    print("RELATÓRIO DE CLASSIFICAÇÃO DA DETECÇÃO DE ANOMALIAS")
    print("="*50)
    print(classification_report(y, y_pred, target_names=['Normal', 'Anomalia/Fraude']))

    # Matriz de Confusão
    cm = confusion_matrix(y, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Normal', 'Fraude'],
                yticklabels=['Normal', 'Fraude'])
    plt.title('Matriz de Confusão - Isolation Forest')
    plt.xlabel('Predito')
    plt.ylabel('Real')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    train_isolation_forest()