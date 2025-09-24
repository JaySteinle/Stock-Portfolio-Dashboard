"""
Direct Python Command Fix
Creates python.bat and pip.bat in your project folder so you can use simple commands
"""

import os
import subprocess

def create_python_shortcuts():
    """Create python.bat and pip.bat shortcuts in current directory"""
    
    python_path = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Python\Python313\python.exe")
    pip_path = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Python\Python313\Scripts\pip.exe")
    
    print("🔧 Creating Python command shortcuts...")
    print(f"📍 Python path: {python_path}")
    
    # Create python.bat
    python_bat_content = f'@echo off\n"{python_path}" %*\n'
    with open('python.bat', 'w') as f:
        f.write(python_bat_content)
    
    # Create pip.bat
    pip_bat_content = f'@echo off\n"{pip_path}" %*\n'
    with open('pip.bat', 'w') as f:
        f.write(pip_bat_content)
    
    print("✅ Created python.bat and pip.bat in current folder")
    print()
    print("🎉 Now you can use simple commands in this folder:")
    print("   python --version")
    print("   python -m streamlit run dashboard.py")
    print("   pip install package")
    print()
    
    # Test the shortcuts
    print("🧪 Testing the shortcuts...")
    try:
        result = subprocess.run(['python.bat', '--version'], capture_output=True, text=True, cwd='.')
        if result.returncode == 0:
            print(f"✅ python.bat works: {result.stdout.strip()}")
        else:
            print(f"❌ python.bat failed: {result.stderr}")
    except Exception as e:
        print(f"❌ Error testing python.bat: {e}")

if __name__ == "__main__":
    print("🚀 PYTHON COMMAND SHORTCUT CREATOR")
    print("=" * 50)
    create_python_shortcuts()