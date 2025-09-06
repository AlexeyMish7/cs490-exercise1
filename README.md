# CS490 – Exercise 1

This project contains my solution for **CS490 Exercise 1**.  
The script submits my student information to the course API.

---

## Setup

1. **Clone the repository** (or download the files).  

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - **Windows (Command Prompt)**:
     ```cmd
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

Run the script with one of the following actions:

```bash
python submit_info.py post
python submit_info.py get
python submit_info.py put
python submit_info.py delete
```

If no action is provided, it defaults to **post**.
