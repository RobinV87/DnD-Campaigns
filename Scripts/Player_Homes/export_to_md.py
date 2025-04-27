import sqlite3

DB_PATH = "vault.db"
OUTPUT_MD = "vault_export.md"

def export_to_markdown():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vault_items")
    items = cursor.fetchall()
    conn.close()

    if not items:
        print("No items to export.")
        return

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("# 🧭 Party Vault Inventory\n\n")
        f.write("Welcome to the updated inventory of magical items held in the Refurbished Redbrand Hideout vault.\n\n")
        f.write("---\n\n")

        for item in items:
            f.write(f"## 📦 Item: {item[1]}\n")
            f.write(f"- **Type**: {item[2]}  \n")
            f.write(f"- **Rarity**: {item[3]}  \n")
            f.write(f"- **Owner**: {item[4]}  \n")
            f.write(f"- **Location**: {item[5]}  \n")
            f.write(f"- **Cursed**: {'Yes ☠️' if item[7] else 'No'}  \n")
            f.write(f"- **Description**: {item[6]}\n\n")
            f.write("---\n\n")

    print(f"✅ Exported {len(items)} items to {OUTPUT_MD}")

if __name__ == "__main__":
    export_to_markdown()
