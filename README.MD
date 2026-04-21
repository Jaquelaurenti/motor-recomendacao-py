# 🤖 AI Recommendation Engine

Sistema de recomendação baseado em Machine Learning (SVD) com API REST utilizando FastAPI.

---

## 🚀 Visão Geral

Este projeto implementa um motor de recomendação capaz de sugerir itens para usuários com base em padrões de comportamento.

O sistema utiliza **Filtragem Colaborativa (Matrix Factorization)** para prever preferências.

---

## 🧠 Arquitetura

- Clean Architecture
- Separação de responsabilidades
- Camadas desacopladas

### Estrutura:

app/
├── domain/
├── application/
├── infrastructure/
├── interfaces/

---

## ⚙️ Tecnologias

- Python
- FastAPI
- Scikit-surprise
- Pandas
- NumPy

---

## 🧬 Modelo de Machine Learning

O modelo utiliza decomposição de matriz:

R ≈ P × Qᵀ

Onde:

- R = matriz usuário-item
- P = vetor de usuários
- Q = vetor de itens

---

## 📊 Dataset

Formato:

user_id | item_id | rating | timestamp

---

## 🔌 API

### GET /recommendations/{user_id}

Retorna recomendações personalizadas.

#### Exemplo:

{
"user_id": 1,
"recommendations": [
{"item_id": 105, "score": 3.99}
]
}

---

## ▶️ Como rodar

```bash
git clone ...
cd project

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

# 🤖 AI Recommendation Engine

Sistema de recomendação híbrido baseado em Machine Learning, combinando **Filtragem Colaborativa (SVD)** com **Content-Based Filtering**, exposto via API REST utilizando FastAPI.

---

# 🧠 Arquitetura

O sistema segue princípios de **Clean Architecture**, garantindo:

- Separação de responsabilidades
- Baixo acoplamento
- Alta testabilidade
- Escalabilidade

---

# 📁 Estrutura do Projeto

```
app/
├── domain/
│   ├── services/
│   │   ├── recommendation_service.py
│   │   └── content_based.py
│
├── application/
│   └── use_cases/
│       └── get_recommendations.py
│
├── infrastructure/
│   ├── data/
│   │   ├── dataset_loader.py
│   │   └── items_loader.py
│   │
│   ├── model/
│   │   ├── svd_model.py
│   │   └── model_persistence.py
│
├── interfaces/
│   └── api/
│       └── routes.py
│
├── train_model.py
└── main.py
```

---

# 🧩 Descrição dos Componentes

## 📊 DatasetLoader (`dataset_loader.py`)

Responsável por carregar e validar o dataset de interações:

- user_id
- item_id
- rating

Garante integridade dos dados antes do treino.

---

## 📦 ItemsLoader (`items_loader.py`)

Carrega dados de itens:

- item_id
- category

Utilizado no modelo baseado em conteúdo.

---

## 🤖 SVDRecommender (`svd_model.py`)

Implementa o modelo de Machine Learning:

- Baseado em Matrix Factorization (SVD)
- Aprende padrões de comportamento dos usuários
- Prediz preferências

---

## 💾 ModelPersistence (`model_persistence.py`)

Responsável por:

- Salvar modelo treinado (pickle)
- Carregar modelo na API

Permite separação entre treino e inferência.

---

## 🧠 ContentBasedRecommender (`content_based.py`)

Modelo baseado em similaridade entre itens:

- Usa cosine similarity
- Baseado em categorias
- Gera score semântico entre itens

---

## 🎯 RecommendationService (`recommendation_service.py`)

Coração do sistema.

Responsável por:

- Combinar:
  - score colaborativo (SVD)
  - score baseado em conteúdo

- Gerar ranking de recomendações

Fórmula:

```
score_final = 0.7 * CF + 0.3 * Content
```

---

## 📌 Use Case (`get_recommendations.py`)

Orquestra a execução da recomendação:

- Recebe user_id
- Executa serviço
- Retorna resultado

---

## 🌐 API (`routes.py`)

Camada de interface:

- Expõe endpoint REST
- Injeta dependências
- Retorna JSON

Endpoint:

```
GET /recommendations/{user_id}
```

---

## 🚀 Treinamento (`train_model.py`)

Script responsável por:

- Carregar dataset
- Treinar modelo
- Persistir modelo em disco

---

## 🧩 Main (`main.py`)

Ponto de entrada da aplicação:

- Inicializa FastAPI
- Registra rotas

---

# 🔄 Fluxo de Execução

1. Treinamento offline (`train_model.py`)
2. Modelo salvo em disco
3. API carrega modelo na inicialização
4. Requisição chega
5. Sistema gera recomendação híbrida
6. Retorna resposta JSON

---

# 🧬 Modelo de Recomendação

## Filtragem Colaborativa

Baseada em decomposição de matriz:

```
R ≈ P × Qᵀ
```

---

## Content-Based

Baseado em similaridade de features:

- categoria
- atributos

---

## Híbrido

Combinação:

```
score = 0.7 * colaborativo + 0.3 * conteúdo
```

---

# 🚀 Como rodar

```
python -m app.train_model
uvicorn app.main:app --reload
```

---

# 🔮 Próximos Passos

- Streaming com Kafka
- Deploy em cloud
- Feature store
- Recomendação em tempo real

---

# 👨‍💻 Autor

Jaque Laurenti para estudos de Modelos
