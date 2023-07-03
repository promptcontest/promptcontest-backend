```python
from supabase_config import supabase_client
from user_authentication import user_id, auth_token

def update_data(table_name, data):
    try:
        if not user_id or not auth_token:
            raise Exception("User is not authenticated")

        response = supabase_client.from_(table_name).update(data).match({'id': user_id}).execute()

        if response.error:
            raise Exception(response.error.message)

        return response.data

    except Exception as e:
        return str(e)

def update_user_data(data):
    return update_data('users', data)
```