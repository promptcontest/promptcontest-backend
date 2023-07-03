```python
from supabase_config import supabase_client
from supabase.py import create_client

def create_table():
    try:
        result = supabase_client.sql().raw('''
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255),
                password VARCHAR(255),
                email VARCHAR(255)
            )
        ''')
        if result.error:
            raise Exception(result.error.message)
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_user(username, password, email):
    try:
        result = supabase_client.from_('users').insert([
            {'username': username, 'password': password, 'email': email}
        ])
        if result.error:
            raise Exception(result.error.message)
    except Exception as e:
        print(f"Error inserting user: {e}")

def select_all_users():
    try:
        result = supabase_client.from_('users').select()
        if result.error:
            raise Exception(result.error.message)
        return result.data
    except Exception as e:
        print(f"Error selecting all users: {e}")

def update_user(id, username, password, email):
    try:
        result = supabase_client.from_('users').update({
            'username': username,
            'password': password,
            'email': email
        }).match({'id': id})
        if result.error:
            raise Exception(result.error.message)
    except Exception as e:
        print(f"Error updating user: {e}")

def delete_user(id):
    try:
        result = supabase_client.from_('users').delete().match({'id': id})
        if result.error:
            raise Exception(result.error.message)
    except Exception as e:
        print(f"Error deleting user: {e}")
```