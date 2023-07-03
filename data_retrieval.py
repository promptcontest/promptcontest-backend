from supabase_config import supabase_client
from user_authentication import user_id, auth_token

def retrieve_data():
    try:
        response = supabase_client.from('users').select().eq('id', user_id).execute()
        if response.error:
            raise Exception('Data retrieval failed: ', response.error)
        else:
            return response.data
    except Exception as e:
        print('Error: ', e)

def retrieve_specific_data(column_name):
    try:
        response = supabase_client.from('users').select(column_name).eq('id', user_id).execute()
        if response.error:
            raise Exception('Data retrieval failed: ', response.error)
        else:
            return response.data
    except Exception as e:
        print('Error: ', e)