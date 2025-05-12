# API-Tester
Proyecto para manejar el testeo de APIs 

# 🧪 Simulador de Rendimiento para APIs REST

![Diagrama general](img\Diagrama.png)

## 🚀 Descripción del Proyecto

Este proyecto tiene como objetivo evaluar el rendimiento de una API en sus distintos endpoints, simulando múltiples usuarios concurrentes que envían solicitudes `GET` y `POST`. El sistema está diseñado para identificar **el punto de saturación de la API**, analizar métricas clave y visualizar los resultados mediante una interfaz interactiva construida con **Streamlit**.

---

## 🎯 Objetivos

- Simular carga personalizada para evaluar la resiliencia de endpoints REST.
- Medir rendimiento en tiempo real mediante métricas clave.
- Visualizar gráficas dinámicas y detalladas de los resultados obtenidos.
- Identificar cuellos de botella, degradación progresiva o fallos bajo estrés.

---

## ⚙️ Funcionalidades

- Configuración de pruebas:
  - Número de usuarios concurrentes.
  - Frecuencia de solicitudes.
  - Tipo de método (`GET` / `POST`).
  - Payloads y endpoints personalizados.
- Recolección de métricas en tiempo real.
- Visualización con **gráficas interactivas**.
- Panel de control mediante **Streamlit**.

---

## 📊 Métricas de Rendimiento

| Métrica               | Descripción                                                        |
|-----------------------|--------------------------------------------------------------------|
| Latencia              | Promedio, Mínimo, Máximo, P50, P90, P95, P99                      |
| RPS                   | Peticiones por segundo                                             |
| Throughput            | Tráfico transmitido (KB/s o MB/s)                                 |
| Código de respuesta   | 2xx, 4xx, 5xx, timeouts                                            |
| Tasa de errores       | Porcentaje de fallos en relación al total de solicitudes          |
| Tiempo de ejecución   | Duración total de la prueba                                        |

---

## 📈 Visualizaciones

- Gráfica de línea: Latencia vs tiempo
- Boxplot: Distribución de latencias por endpoint
- Barras apiladas: Status codes (200, 404, 500...)
- Histogramas de latencia
- RPS vs tiempo
- Comparativas entre endpoints

---

## 🛠️ Tecnologías Utilizadas

- 🐍 Python 3.x
- 📊 Streamlit
- 📦 Requests / HTTPX (cliente HTTP)
- 📉 Matplotlib, Seaborn, Plotly
- 🧪 (Futuro) Locust / asyncio / multiprocessing

---

## 🚧 Roadmap (Próximas versiones)

- [ ] Soporte para `PUT` y `DELETE`.
- [ ] Exportación de resultados (CSV, PDF).
- [ ] Simulación distribuida desde múltiples máquinas.
- [ ] Comparador de versiones de la API.
- [ ] Panel avanzado con autenticación y monitoreo continuo.

---

## 📦 Instalación

```bash
git clone https://github.com/K31NER/API-Tester.git
cd API-Tester
pip install -r requirements.txt
streamlit run app.py
