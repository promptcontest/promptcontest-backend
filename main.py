import supabase_config
import user_authentication
import database_operations
import data_retrieval
import data_update
import data_deletion

def main():
    # Initialize Supabase client
    supabase = supabase_config.initialize_supabase()

    # User login
    user_id, auth_token = user_authentication.login(supabase)

    # Perform database operations
    database_operations.create_table(supabase, user_id, auth_token)

    # Retrieve data
    data = data_retrieval.retrieve_data(supabase, user_id, auth_token)

    # Update data
    data_update.update_data(supabase, user_id, auth_token, data)

    # Delete data
    data_deletion.delete_data(supabase, user_id, auth_token)

if __name__ == "__main__":
    main()