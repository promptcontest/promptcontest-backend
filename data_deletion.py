```python
from supabase_config import supabase_client
from user_authentication import user_id, auth_token

def delete_user_data():
    try:
        response = supabase_client.from('users').delete().match({'id': user_id}).execute()
        if response.error:
            raise Exception(response.error.message)
        return response.data
    except Exception as e:
        return str(e)

def delete_data(table_name, condition):
    try:
        response = supabase_client.from(table_name).delete().match(condition).execute()
        if response.error:
            raise Exception(response.error.message)
        return response.data
    except Exception as e:
        return str(e)

def delete_all_user_data():
    try:
        response = delete_user_data()
        if 'error' in response:
            raise Exception(response['error']['message'])
        return response
    except Exception as e:
        return str(e)
```