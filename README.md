# Service Bus Message Sender (Python + Tkinter GUI)

This is a simple Python GUI app built with **Tkinter** that allows you to send messages to an **Azure Service Bus Queue** or **Topic**.  
It's especially useful for testing and quick debugging when working with local or development environments.

---

## 🚀 Features

- ✅ User-friendly GUI built with Tkinter
- ✅ Supports sending to either **Queue** or **Topic**
- ✅ Automatically sets `ContentType = "application/json"` when sending to a topic
- ✅ Multi-line, scrollable input box for JSON or large messages

---

## 📦 How to Run

1. Install dependencies:
   ```bash
   pip install azure-servicebus
   ```

2. Run the app:
   ```bash
   python servicebus_gui.py
   ```

---

## 💬 Notes for .NET Starter Functions

If you're integrating with **.NET Azure Functions**, use the appropriate Service Bus trigger configuration:

- 🟩 **For Service Bus Queue:**

  ```csharp
  [ServiceBusTrigger("queue.1", Connection = "YourConnectionStringSetting")]
  ```

- 🟦 **For Service Bus Topic + Subscription:**

  ```csharp
  [ServiceBusTrigger("topic.1", "subscription.1", Connection = "YourConnectionStringSetting")]
  ```

> ✅ Make sure your `.NET` function app settings include the correct connection string:
```
Endpoint=sb://127.0.0.1;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=SAS_KEY_VALUE;UseDevelopmentEmulator=true;
```

---

## 📌 Requirements

- Python 3.7+
- `azure-servicebus` (install with pip)
- Tkinter (comes pre-installed with Python)

---

## 🙋‍♂️ Let’s Collaborate!

This is a basic implementation.  
Let me know your requirements – JSON validation, sending batches, logging, etc.  
Let me know if you need more details!
```

---

Let me know if you'd like to add a license, screenshots, or contributor section!
