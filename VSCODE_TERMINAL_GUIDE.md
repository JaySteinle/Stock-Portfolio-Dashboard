# 💻 **Running update_and_push.bat in VS Code Terminal**

## 🎯 **VS Code Terminal Methods:**

### ⚡ **Method 1: Direct Execution (Recommended)**
```bash
# In VS Code terminal, just type:
.\update_and_push.bat

# Note: Use backslash (\) on Windows, not forward slash (/)
```

### 💻 **Method 2: PowerShell Execution**
```powershell
# If you're in PowerShell terminal:
& ".\update_and_push.bat"

# Or:
cmd /c "update_and_push.bat"
```

### 🔧 **Method 3: Command Prompt Mode**
```bash
# Switch to cmd mode in terminal:
cmd

# Then run:
update_and_push.bat
```

---

## 🛠️ **VS Code Terminal Setup:**

### **🔍 Check Current Directory:**
```bash
# Make sure you're in the right folder:
pwd
# Should show: C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi
```

### **📁 Navigate if Needed:**
```bash
# If not in the right folder:
cd "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"
```

### **✅ Verify File Exists:**
```bash
# Check if the batch file exists:
ls update_and_push.bat
# or
dir update_and_push.bat
```

---

## 🚀 **Complete VS Code Workflow:**

### **Step 1: Open VS Code Terminal**
- Press `` Ctrl + ` `` (backtick) to open terminal
- Or: View → Terminal

### **Step 2: Navigate to Project Folder**
```bash
cd "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"
```

### **Step 3: Run the Batch File**
```bash
.\update_and_push.bat
```

### **Step 4: Watch the Process**
The script will:
1. 🔄 Update stock data
2. ➕ Add changes to git
3. 💬 Create commit
4. 📤 Push to GitHub

---

## 🎛️ **Alternative: PowerShell Version**

Create a PowerShell version that works better in VS Code:

```powershell
# Create update_and_push.ps1
Write-Host "📊 Updating Portfolio Repository..." -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Yellow

Write-Host "🔄 Fetching latest stock data..." -ForegroundColor Blue
py stock_tracker.py

Write-Host "➕ Adding changes to git..." -ForegroundColor Blue
git add .

Write-Host "💬 Creating commit..." -ForegroundColor Blue
$today = Get-Date -Format "yyyy-MM-dd"
git commit -m "📊 Portfolio update - $today"

Write-Host "📤 Pushing to GitHub..." -ForegroundColor Blue
git push origin main

Write-Host ""
Write-Host "✅ Portfolio successfully pushed to GitHub!" -ForegroundColor Green
Write-Host "🌐 View at: https://github.com/JaySteinle/Stock-Portfolio-Dashboard" -ForegroundColor Cyan
```

### **Run PowerShell Version:**
```bash
# In VS Code terminal:
.\update_and_push.ps1

# If execution policy blocks it:
powershell -ExecutionPolicy Bypass -File "update_and_push.ps1"
```

---

## 📋 **Quick Commands Reference:**

### **🔄 Update Portfolio Data Only:**
```bash
py stock_tracker.py
```

### **📊 Update Dashboard:**
```bash
py -m streamlit run dashboard.py
```

### **📤 Manual Git Push:**
```bash
git add .
git commit -m "Manual update"
git push origin main
```

### **🚀 One-Click Update & Push:**
```bash
.\update_and_push.bat
```

---

## ⚠️ **Troubleshooting:**

### **If Batch File Won't Run:**
```bash
# Try with cmd:
cmd /c ".\update_and_push.bat"

# Or switch terminal to Command Prompt:
# Click terminal dropdown → Select "Command Prompt"
```

### **If PowerShell Blocks Scripts:**
```bash
# Allow scripts for current session:
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Then run:
.\update_and_push.ps1
```

### **If Git Commands Fail:**
```bash
# Check git status first:
git status

# Check if you're in right directory:
pwd

# Check remote repository:
git remote -v
```

---

## 🎯 **VS Code Integration Tips:**

### **📌 Pin to Tasks:**
Create `.vscode/tasks.json`:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Update Portfolio",
            "type": "shell",
            "command": ".\\update_and_push.bat",
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        }
    ]
}
```

Then: `Ctrl+Shift+P` → "Tasks: Run Task" → "Update Portfolio"

### **🔧 Keyboard Shortcut:**
Add to keybindings.json:
```json
{
    "key": "ctrl+shift+u",
    "command": "workbench.action.tasks.runTask",
    "args": "Update Portfolio"
}
```

---

## ✅ **Ready to Run!**

**In VS Code terminal, simply type:**
```bash
.\update_and_push.bat
```

**And your portfolio will automatically update and push to GitHub!** 🚀📊