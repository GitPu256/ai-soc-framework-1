from fastapi import APIRouter
from fastapi import APIRouter
from pydantic import BaseModel
from app.algorithms import quicksort, binary_search
import sqlite3
import time

router = APIRouter(prefix="/logs", tags=["Logs"])

class LogBatch(BaseModel):
    severities: list[int]
    lookup_value: int


def save_to_db(sorted_list, index):
    conn = sqlite3.connect("soc.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sorted_values TEXT,
            lookup_index INTEGER
        )
    """)
    cursor.execute("INSERT INTO results (sorted_values, lookup_index) VALUES (?, ?)",
                   (str(sorted_list), index))
    conn.commit()
    conn.close()


@router.post("/process")
def process_logs(batch: LogBatch):
    start = time.time()

    # Sorting and searching
    sorted_values = quicksort(batch.severities)
    index = binary_search(sorted_values, batch.lookup_value)

    end = time.time()

    # Save results to DB
    save_to_db(sorted_values, index)

    return {
        "sorted_values": sorted_values,
        "lookup_index": index,
        "latency": end - start
    }
