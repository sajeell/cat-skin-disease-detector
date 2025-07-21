# Cat Skin Disease Detector

A Django REST API for detecting skin diseases in cats using image uploads and a Roboflow-trained machine learning model.

## Features
- Upload cat skin images and receive disease predictions (class, confidence, bounding boxes, etc.)
- Uses Roboflow for model inference
- CORS enabled for easy frontend integration

## Requirements
- Python 3.11+
- Django 5.x
- Django REST Framework
- Roboflow Python SDK
- Pillow, OpenCV, and other dependencies (see `requirements.txt`)

## Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd cat-skin-disease-detector
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set your Roboflow API key:**
   - Create a `.env` file or set the `ROBofLOW_API_KEY` environment variable.

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## API Usage

### Predict Skin Disease
- **Endpoint:** `POST /api/predict/`
- **Payload:** Multipart form with an `image` field (file upload)
- **Response:** JSON with prediction results from Roboflow

#### Example using `curl`:
```sh
curl -X POST -F "image=@/path/to/cat.jpg" http://localhost:8000/api/predict/
```

## Project Structure
```
cat-skin-disease-detector/
├── csd_detector/         # Django project settings
├── predictor/           # App with prediction logic and API
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Notes
- Make sure your Roboflow model and API key are set up correctly.
- For production, set `DEBUG = False` and configure allowed hosts and security settings.

## License
MIT License
