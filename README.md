### **README.md – Child Recovery Platform**  

# **Child Recovery Platform**  
An AI-powered web application designed to assist in locating missing children in India using **facial recognition technology**. The platform enables users to **search for missing children**, **report cases**, and provides **law enforcement & NGOs** with case management tools.  

---

## **🚀 Project Overview**  

### **Key Features**  
✔ **AI-Based Facial Recognition** – Uses **DeepFace** & **OpenCV** for real-time missing child identification.  
✔ **Secure Case Management** – Enables law enforcement and NGOs to manage and track missing child cases.  
✔ **Multi-Language Support** – Supports regional languages for wider accessibility.  
✔ **Real-Time Alerts** – Sends **SMS & email notifications** for potential matches.  
✔ **Geo-Tagging & Mapping** – Displays last-seen locations of missing children.  
✔ **Chatbot Assistance** – AI-powered chatbot guides users in reporting & searching cases.  
✔ **Role-Based Access** – Separate dashboards for **parents, police, and NGOs**.  
✔ **Data Security & Compliance** – Secure authentication, GDPR & IT Act compliance.  

---

## **📌 Research & Insights**  

### **Existing Solutions & Gaps Identified**  

| **Platform** | **Country** | **Key Features** | **Limitations** |
|-------------|------------|------------------|----------------|
| **TrackChild** | India | Government-run, law enforcement access | Limited public access, outdated UI |
| **MissingKids (NCMEC)** | USA | AI-based search, legal assistance | US-focused, lacks real-time updates |
| **Interpol Yellow Notices** | Global | International missing persons database | No direct public engagement |
| **FaceSearch (Private)** | Global | AI-powered facial recognition | Paid access, not child-specific |
| **ReUnite India** | India | Public database, NGO support | No AI search, manual reporting |

### **Key Takeaways for Our Platform**
✔ **AI-powered search** for **real-time** child recovery.  
✔ **Multi-language accessibility** for Indian users.  
✔ **Law enforcement & NGO tools** for streamlined operations.  
✔ **Real-time notifications** to parents & officials.  
✔ **Role-based dashboards** for enhanced privacy & security.  

---

## **🛠️ Tech Stack**  

### **Frontend:**  
- **Next.js (React)** – Server-side rendering & optimized UI.  
- **Zustand** – Lightweight global state management.  
- **Tailwind CSS** – Rapid UI development with utility classes.  

### **Backend:**  
- **FastAPI (Python)** – High-performance API development.  
- **PostgreSQL** – Scalable relational database for structured data.  
- **Redis** – Caching for fast response times.  
- **Celery & RabbitMQ** – Asynchronous background tasks (e.g., notifications).  
- **OpenCV + DeepFace** – AI-powered facial recognition.  

### **Deployment & Infrastructure:**  
- **Docker & Kubernetes** – Containerized deployment with auto-scaling.  
- **NGINX** – Reverse proxy & load balancing.  
- **Prometheus & Grafana** – System monitoring & analytics.  

---

## **📂 Project Structure**  

```
child_recovery_platform/
├── backend/
│   ├── api/
│   │   ├── auth.py          # User authentication API
│   │   ├── children.py      # Missing child case management API
│   │   ├── face.py          # Facial recognition API
│   │   ├── notifications.py # SMS/Email notifications
│   ├── services/
│   │   ├── face_recognition.py # DeepFace-based recognition
│   │   ├── background_tasks.py # Asynchronous Celery tasks
│   ├── models/
│   │   ├── child.py        # Child profile database schema
│   │   ├── user.py         # User authentication & roles
│   │   ├── logs.py         # System event logging
│   ├── scripts/
│   │   ├── init_db.py      # Database initialization script
│   │   ├── start_celery.py # Celery worker startup
│   ├── tests/
│   │   ├── test_auth.py    # Authentication API tests
│   │   ├── test_face.py    # Face recognition tests
│   ├── main.py             # Backend entry point
│   ├── config.py           # Environment configurations
│   ├── requirements.txt    # Backend dependencies
│   ├── logs/               # Logs directory
│   │   ├── app.log
│
├── frontend/
│   ├── components/
│   │   ├── SearchBar.tsx      # Search bar for missing children
│   │   ├── UploadForm.tsx     # Image upload form
│   │   ├── FaceMatchResult.tsx # Face recognition match display
│   │   ├── ChildDetails.tsx   # Child profile details
│   │   ├── AdminUserList.tsx  # Admin user management
│   │   ├── Chatbot.tsx        # AI-powered chatbot
│   │   ├── MapView.tsx        # Last-seen location mapping
│   ├── pages/
│   │   ├── index.tsx         # Homepage
│   │   ├── search.tsx        # Search results page
│   │   ├── report.tsx        # Missing child report form
│   │   ├── login.tsx         # User authentication page
│   │   ├── admin.tsx         # Admin dashboard
│   ├── state/
│   │   ├── store.ts          # Global state management
│   │   ├── authSlice.ts      # Authentication state
│   │   ├── searchSlice.ts    # Face search state
│   ├── utils/
│   │   ├── api.ts            # API request handler
│   │   ├── faceUtils.ts      # Facial recognition utilities
│   ├── styles/
│   │   ├── globals.css       # Global styles
│   │   ├── tailwind.css      # Tailwind configuration
│   ├── next.config.js        # Next.js configurations
│
├── infra/
│   ├── docker-compose.yml     # Docker multi-container setup
│   ├── kubernetes/
│   │   ├── deployment.yaml    # Kubernetes deployment
│   │   ├── service.yaml       # Kubernetes service
│   ├── nginx.conf             # Reverse proxy configuration
│
├── monitoring/
│   ├── prometheus.yml         # Prometheus monitoring setup
│   ├── grafana_dashboard.json # Grafana dashboard configuration
│
├── ci_cd/
│   ├── github-actions.yaml    # CI/CD pipeline setup
│   ├── docker-build.sh        # Automated Docker builds
│
├── docs/
│   ├── api.md                 # API documentation
│   ├── security.md            # Security & data privacy guidelines
│   ├── monitoring.md          # Monitoring & logging setup
│
├── Dockerfile
├── Makefile
├── README.md (You are here!)
```

---

## **🚀 Getting Started**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-org/child_recovery_platform.git
cd child_recovery_platform
```

### **2️⃣ Set Up Backend**  
```sh
cd backend
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### **3️⃣ Set Up Frontend**  
```sh
cd frontend
npm install
npm run dev
```

### **4️⃣ Run with Docker**  
```sh
docker-compose up --build
```

---

## **📊 Monitoring & Logging**  
- **Prometheus**: `http://localhost:9090`  
- **Grafana**: `http://localhost:3000`  
- **Backend Logs**: `backend/logs/app.log`  

---

## **🛡️ Security & Compliance**  
- **Encryption**: All images & user data are securely encrypted.  
- **Access Control**: Multi-role authentication (Admin, NGO, Police, Public).  
- **Legal Compliance**: Follows **GDPR** & **Indian IT Act**.  

---

## **📜 License**  
This project is licensed under the **MIT License**.  

---

💡 **Contributions & Issues?** Open a PR or create an issue! 🚀


