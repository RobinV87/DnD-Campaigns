import sqlite3

DB_PATH = "vault.db"

def connect():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vault_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT,
            rarity TEXT,
            owner TEXT,
            location TEXT,
            description TEXT,
            is_cursed BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def create_item():
    name = input("Item name: ")
    type_ = input("Type (e.g., Weapon, Relic): ")
    rarity = input("Rarity (Common, Rare, etc.): ")
    owner = input("Owner (player name or 'Party'): ")
    location = input("Location in vault: ")
    description = input("Description: ")
    is_cursed = input("Is it cursed? (yes/no): ").strip().lower() == "yes"

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vault_items (name, type, rarity, owner, location, description, is_cursed)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, type_, rarity, owner, location, description, is_cursed))
    conn.commit()
    conn.close()
    print("✅ Item added!")

def view_items():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vault_items")
    items = cursor.fetchall()
    conn.close()

    if not items:
        print("No items found.")
        return

    for item in items:
        print(f"ID: {item[0]} | Name: {item[1]} | Type: {item[2]} | Rarity: {item[3]} | Owner: {item[4]}")
        print(f"Location: {item[5]} | Cursed: {'Yes' if item[7] else 'No'}")
        print(f"Description: {item[6]}")
        print("-" * 60)

def search_items():
    keyword = input("Search by name or owner: ").lower()
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM vault_items
        WHERE LOWER(name) LIKE ? OR LOWER(owner) LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    items = cursor.fetchall()
    conn.close()

    if not items:
        print("No matching items found.")
        return

    for item in items:
        print(f"ID: {item[0]} | Name: {item[1]} | Type: {item[2]} | Rarity: {item[3]} | Owner: {item[4]}")
        print(f"Location: {item[5]} | Cursed: {'Yes' if item[7] else 'No'}")
        print(f"Description: {item[6]}")
        print("-" * 60)

def delete_item():
    item_id = input("Enter the ID of the item to delete: ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vault_items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    print("🗑️ Item deleted.")

def main():
    create_table()
    while True:
        print("\n--- D&D Vault Manager ---")
        print("1. Add item")
        print("2. View all items")
        print("3. Search items")
        print("4. Delete item")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            create_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_items()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Exiting Vault Manager. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
