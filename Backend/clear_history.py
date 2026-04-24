import sqlite3
import os
# Get the directory where this script resides
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Point to analysis.db in that same directory
DB_PATH = os.path.join(SCRIPT_DIR, "analysis.db")

def clear_analysis_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM analysis_requests")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='analysis_requests'")
    
    conn.commit()
    conn.close()

    return {"message": "✅ All analysis history cleared!"}


# Keep this for manual use (optional)
if __name__ == "__main__":
    print(clear_analysis_history())