```python
from supabase_config import supabase_client
from supabase.py import create_user, sign_in_user, sign_out_user

def register_user(email, password):
    try:
        user, error = supabase_client.auth.sign_up(email, password)
        if error:
            return {"status": "error", "message": error.message}
        return {"status": "success", "message": "User registered successfully", "user": user}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def login_user(email, password):
    try:
        user, error = supabase_client.auth.sign_in(email, password)
        if error:
            return {"status": "error", "message": error.message}
        return {"status": "success", "message": "User logged in successfully", "user": user}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def logout_user():
    try:
        supabase_client.auth.sign_out()
        return {"status": "success", "message": "User logged out successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
```