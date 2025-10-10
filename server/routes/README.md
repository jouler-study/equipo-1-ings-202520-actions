# Availability documentation

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

## 📌 Next steps

Once the API is deployed, integration with UptimeRobot will be performed.