### **Python Keylogger with Telegram Integration**  

#### **Overview**  
This script is a simple yet powerful keylogger that logs keystrokes and sends them to a Telegram bot in batches of 20 keystrokes. It is developed for **ethical hacking, cybersecurity research, and educational purposes**.  

#### **How It Works**  
- Captures all keyboard inputs using the `pynput` library.  
- Stores the keystrokes in a local file (`keylog.txt`).  
- Sends the collected keystrokes to a **Telegram bot** after every **20 key presses**.  
- Stops execution when the **Escape (ESC)** key is pressed.  

#### **Features**  
✅ Logs all keystrokes, including special keys.  
✅ Sends logs to Telegram in real time but in controlled batches.  
✅ Clears the log file after sending to Telegram to avoid duplication.  
✅ Runs silently in the background without user interference.  

#### **Installation & Setup**  
**Requirements:**  
- Python 3.x  
- Required libraries: `pynput` and `requests`  

To install dependencies, run:  
```bash
pip install pynput requests
```

**Steps to Run:**  
1. Replace `"your_bot_token"` and `"your_chat_id"` with your actual **Telegram bot** credentials.  
2. Run the script:  
   ```bash
   python keylogger.py
   ```
3. Press **ESC** to stop logging at any time.  

#### **Use Cases**  
- Ethical hacking & penetration testing.  
- Monitoring keystrokes for security research.  
- Analyzing user behavior (with consent).  

#### **Important Disclaimer**  
🚨 **This script is for educational and ethical research purposes only.** Unauthorized use of keyloggers is illegal and can result in severe legal consequences. **Always obtain permission before deploying this script on any system.**  

---


