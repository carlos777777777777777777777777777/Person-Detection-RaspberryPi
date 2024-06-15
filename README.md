# Person Detection using Raspberry Pi

## Descripción del Proyecto
Este proyecto utiliza un modelo de detección de personas implementado en un Raspberry Pi. Se emplean modelos de aprendizaje automático (ML) y redes neuronales convolucionales (CNN) para detectar personas en tiempo real a través de una cámara.

## Tecnologías Utilizadas
- Python
- TensorFlow
- Keras
- OpenCV
- Raspberry Pi

## Para instalar 
1. Clona el repositorio:
   ```sh
   git clone https://github.com/carlos777777777777777777777777777/Person-Detection-RaspberryPi.git
   cd Person-Detection-RaspberryPi
- instaka las dependencias con pip install -r requirements.txt
- para entrenar ML python train_ml_model.py
- para setectar en tienpo real:python main.py
Estructura del Proyecto

	•	main.py: Script principal para ejecutar la detección en tiempo real.
	•	src/: Contiene los módulos de código fuente, incluyendo los modelos y la preprocesamiento de imágenes.
	•	data/: Carpeta para almacenar los datos de entrenamiento y validación.
	•	models/: Carpeta para almacenar los modelos entrenados.
	•	results/: Carpeta para almacenar los resultados y las salidas del modelo.
