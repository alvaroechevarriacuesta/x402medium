#!/usr/bin/env python3
"""
Quick deployment readiness check for Railway
"""
import os
from pathlib import Path

def check_file_exists(filename):
    """Check if a file exists"""
    exists = Path(filename).exists()
    status = "✅" if exists else "❌"
    print(f"{status} {filename}")
    return exists

def check_env_var(var_name):
    """Check if environment variable is set"""
    value = os.getenv(var_name)
    status = "✅" if value else "❌"
    masked_value = f"{value[:10]}..." if value and len(value) > 10 else value
    print(f"{status} {var_name}: {masked_value if value else 'NOT SET'}")
    return bool(value)

print("🚀 Railway Deployment Readiness Check\n")

print("📁 Required Files:")
files_ok = all([
    check_file_exists("Procfile"),
    check_file_exists("railway.toml"),
    check_file_exists("requirements.txt"),
    check_file_exists("app/main.py"),
])

print("\n🔑 Environment Variables (from .env):")
from dotenv import load_dotenv
load_dotenv()

env_ok = all([
    check_env_var("BASE_URL"),
    check_env_var("API_KEY"),
    check_env_var("RAPID_API_HOST"),
    check_env_var("ADDRESS"),
])

print("\nℹ️  Optional Variables:")
check_env_var("FACILITATOR_URL")

print("\n" + "="*50)
if files_ok and env_ok:
    print("✅ Ready for Railway deployment!")
    print("\nNext steps:")
    print("1. Push to GitHub: git push origin main")
    print("2. Go to railway.app")
    print("3. Create new project from GitHub repo")
    print("4. Set environment variables in Railway dashboard")
    print("5. Deploy! 🚀")
else:
    print("❌ Not ready for deployment")
    if not files_ok:
        print("   - Missing required files")
    if not env_ok:
        print("   - Missing required environment variables")
    print("\nRefer to DEPLOYMENT.md for setup instructions")

