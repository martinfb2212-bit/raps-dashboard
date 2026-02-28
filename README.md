# 🌿 RAPS GmbH – Dashboard Estratégico de Transformación Digital

> **Caso académico:** *"How RAPS Spiced Up the German Butcher's Trade"*
> Glismann, K., Jöhnk, J., Kratsch, W., Nüske, N. & Schmied, F. (2021). *Digitalization Cases Vol. 2*. Springer Nature.

---

## 📌 Descripción

Dashboard gerencial desarrollado como solución estratégica integral para el caso RAPS GmbH, empresa alemana fabricante de especias que introdujo servicios digitales en la industria cárnica tradicional a través de **myRAzept**, una aplicación web independiente de plataforma.

El dashboard traduce los OKRs ejecutivos de la transformación digital de RAPS en visualizaciones orientadas a Board, permitiendo monitorear el avance estratégico por pivote.

---

## 🎯 Pivotes estratégicos

| Pivote | Enfoque |
|--------|---------|
| ⚙️ Alineamiento Dinámico | Integración de procesos internos, ERP y cadena de valor DeliCo en torno a myRAzept |
| 💡 Liderazgo Digital | Posicionamiento de RAPS como referente digital y construcción de capacidades internas |
| 🤝 Innovación Centrada en el Cliente | Generación continua de valor para el carnicero como socio estratégico |

---

## 📊 Secciones del dashboard

| Sección | Contenido |
|---------|-----------|
| 🏠 Resumen Ejecutivo | KPIs Board + scorecard estratégico de los 3 pivotes |
| ⚙️ Alineamiento Dinámico | OBJ-AD-01 / 02 / 03 · 7 Key Results |
| 💡 Liderazgo Digital | OBJ-LD-01 / 02 / 03 / 04 · 9 Key Results |
| 🤝 Innovación en el Cliente | OBJ-IC-01 / 02 / 03 / 04 · 9 Key Results |

Cada sección incluye gauge charts, tendencias temporales, comparación meta vs actual y la explicación estratégica de por qué se mide cada KR.

---

## 🗂️ Archivos del repositorio

```
raps-dashboard/
├── app.py            # Dashboard completo con datos embebidos
├── requirements.txt  # Dependencias Python
└── README.md         # Este archivo
```

> Los datos están embebidos directamente en `app.py`. No se requieren archivos CSV ni scripts adicionales.

---

## 🛠️ Stack tecnológico

| Herramienta | Uso |
|-------------|-----|
| Streamlit | Framework del dashboard web |
| Plotly | Visualizaciones interactivas |
| Pandas | Manejo de datos |
| Python 3.9+ | Lenguaje base |

---

## ▶️ Ejecución local

```bash
git clone https://github.com/tu-usuario/raps-dashboard.git
cd raps-dashboard
pip install -r requirements.txt
streamlit run app.py
```

Abrir en: `http://localhost:8501`

---

## 📋 OKRs monitoreados

**Alineamiento Dinámico**
- OBJ-AD-01 · myRAzept como eje del modelo DeliCo
- OBJ-AD-02 · Alineamiento interdepartamental IT – Marketing – Ventas
- OBJ-AD-03 · Escalamiento a subsidiarias internacionales

**Liderazgo Digital**
- OBJ-LD-01 · Imagen innovadora de RAPS ante la industria
- OBJ-LD-02 · Capacidades digitales internas sostenibles
- OBJ-LD-03 · Performance tracking digital integrado
- OBJ-LD-04 · Talento digital especializado

**Innovación Centrada en el Cliente**
- OBJ-IC-01 · Escalar base de usuarios myRAzept
- OBJ-IC-02 · Profundidad de uso en la operación del carnicero
- OBJ-IC-03 · Vínculo relacional carnicero – representante RAPS
- OBJ-IC-04 · Innovación continua basada en feedback

---

## 👥 Contexto académico

Proyecto desarrollado como análisis de transformación digital aplicado al caso RAPS GmbH, con foco en la introducción de servicios digitales en una industria no-digital. El caso original fue publicado en *Digitalization Cases Vol. 2* (Springer, 2021). Los datos utilizados son simulados y coherentes con la narrativa del caso.
