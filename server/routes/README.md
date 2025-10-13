# 🧩 Availability documentation

### Availability monitoring (monthly uptime)

You can test it by entering the server folder and running:

```PowerShell
uvicorn main:app --reload
```

If you encounter problems with the execution, try:

```PowerShell
python -m uvicorn main:app --reload 
```
---

- **Health endpoint:** `/health`
- **Purpose:** Validate backend availability.
- **Example response:**
```json
  {“status”: “ok”, ‘message’: “Service online”}
```

* Note: Currently being tested locally at http://127.0.0.1:8000/health.
When the system is deployed, this endpoint will be monitored with UptimeRobot.

You can verify that monitoring is working by simulating a failure:
1. Stop the server (Ctrl + C).
2. Try opening http://127.0.0.1:8000/health again.
3. You will see that it no longer responds — that would be a system “outage.”

This will be the behavior of UptimeRobot when the backend is unavailable.

---
### 🧩 Scheduled maintenance notifications (48-hour notice)
A maintenance management feature was added to the backend through the /maintenance endpoint.
This allows system administrators to register and announce planned maintenance events stored in Supabase under the system_maintenance table.

Each record includes:
* start_time (UTC)
* end_time (UTC)
* message (maintenance description)

The system checks whether the current time falls within any active maintenance window.
If an active maintenance is detected, the /maintenance endpoint returns:

```json
{"active": true, "message": "Scheduled maintenance in progress"}
```

Otherwise:

```json
{"active": false}
```
These maintenances must be created at least 48 hours in advance, ensuring users receive timely notice of service interruptions.
Notifications will be displayed through a web banner once the frontend is integrated.

---

### ⚙️ Redundancy and load balancing
To improve availability and reduce downtime risk, the project simulates redundancy and load balancing locally:

1. Two backend instances can be run simultaneously on different ports:
```PowerShell
uvicorn server.mainTEMPORAL:app --port 8000 --reload
uvicorn server.mainTEMPORAL:app --port 8001 --reload
```

2. A lightweight load balancer implemented in FastAPI (load_balancer.py) distributes incoming requests between these instances:
```PowerShell
uvicorn server.load_balancer:app --port 8080 --reload
```
The load balancer randomly forwards each request to one of the running backend instances:
* http://127.0.0.1:8000
* http://127.0.0.1:8001

If one instance becomes unavailable, the other continues serving requests, demonstrating resilience against node failures.

In production, this setup can be extended with Nginx or cloud-managed load balancers for real-world fault tolerance.

---

### ⚙️ Requirements and dependencies

Before running any of the availability features, make sure you have the following installed:

> fastapi, uvicorn, httpx, python-dotenv, supabase-py

📦 Install them with:
```PowerShell
pip install fastapi uvicorn python-dotenv httpx supabase
```

✅ Environment variables
Create a .env file in the project root with the following keys:

SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_SERVICE_KEY=<your-service-role-key>

> ⚠️ Use the Service Role Key, since it grants read/write permissions needed for backend operations.

---

## 📌 Next steps
Once the API is deployed:

* UptimeRobot will be integrated to monitor the /health endpoint and record uptime.

* Maintenance notifications will be displayed via frontend banners.

* Load balancing can be upgraded to an Nginx or cloud-managed setup for production reliability.