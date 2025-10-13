from fastapi import APIRouter
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from dateutil import parser

load_dotenv()

router = APIRouter()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)


@router.get("/maintenance")
def get_maintenance():
    now_utc = datetime.now(timezone.utc)
    response = supabase.table("system_maintenance").select("*").execute()

    active = []
    for m in response.data or []:
        from dateutil import parser
        start = parser.isoparse(m["start_time"])
        end = parser.isoparse(m["end_time"])
        if start <= now_utc <= end:
            active.append(m)

    if active:
        print("✅ Mantenimiento activo encontrado:", active[0])
        return {"active": True, "message": active[0]["message"]}
    else:
        print("❌ No hay mantenimiento activo.")
        return {"active": False}