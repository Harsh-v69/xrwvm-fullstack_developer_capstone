# Best Cars Dealership - Full-Stack Capstone

A responsive dealership web app: a Django backend serves a React frontend, proxies an Express/MongoDB
dealer + review service, and calls a Flask (NLTK VADER) sentiment-analysis microservice.

- `server/djangoapp`, `server/djangoproj` - Django app (auth, cars, proxy views)
- `server/database` - Express + MongoDB dealer/review API (port 3030)
- `server/djangoapp/microservices` - Flask sentiment analyzer (port 5050)
- `server/frontend` - React UI plus static About/Contact/Home pages

## Run locally
```bash
docker run -d -p 27017:27017 mongo:7
cd server/database && npm install && MONGO_URL=mongodb://localhost:27017/ node app.js
cd server/djangoapp/microservices && pip install flask nltk && python -c "from app import app; app.run(port=5050)"
cd server/frontend && npm install && npm run build
cd server && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver
```
