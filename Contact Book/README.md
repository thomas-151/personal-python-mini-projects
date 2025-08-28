# 📒 Contact Book (Python CLI App)
Developed By Thomas Sasikanth Singadi  

A simple **command-line Contact Book** built in Python for managing contacts with **name, phone, and email**.  
The program allows you to **add, view, search, delete, and save contacts** with proper **validations**.  
All contacts are stored in a text file for persistence.  

## ▶️ Demo

![contact_book](https://github.com/user-attachments/assets/6fc5372d-df7d-43c1-8e44-258a5240f825)

## ✨ Features
- ➕ **Add New Contact** (with validation for name, phone & email)  
- 📋 **View All Contacts** in a clean **table format** (using `tabulate`)  
- 🔍 **Search Contacts** by name (case-insensitive)  
- ❌ **Delete Contact** by name  
- 💾 **Save contacts persistently** into `contacts.txt`  
- 📂 **Auto-load saved contacts** when the app starts  
- ⚠️ **Error handling** for wrong inputs & duplicates  


## 📖 Rules & Validations
1. **Name**
   - Cannot be empty.  
   - Must be unique (case-insensitive).  

2. **Phone Number**
   - Must be exactly **10 digits**.  
   - Cannot be a duplicate.  

3. **Email**
   - Must follow valid **email format**.  
   - Must be unique.  

4. **General**
   - Menu allows choices `1 to 5`.  
   - Prevents crashes with **error handling** for invalid input.  


## ⚠️ Error Handling
- Duplicate **name**, **phone**, or **email** → Not allowed  
- Wrong **phone format** (non-digit or not 10 digits) → Rejected  
- Incorrect **email format** → Rejected  
- Invalid **menu choice** → Shows warning message  


## 💡 Learning From This Project
- Using **lists & dictionaries** for contact management  
- Applying **input validation** with `validator_collection`  
- Displaying data in clean **tabular format** with `tabulate`  
- File handling in Python (**save & load data**)  
- Building **loop-based CLI menus** with error handling  


## 👨‍💻 Author
Made with ❤️ in Python to make learning **data validation, file handling, and CLI apps** fun!  
