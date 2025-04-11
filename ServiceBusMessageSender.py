import tkinter as tk
from tkinter import messagebox, scrolledtext
from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Replace these values
CONNECTION_STR = "Endpoint=sb://127.0.0.1;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=SAS_KEY_VALUE;UseDevelopmentEmulator=true;"
QUEUE_NAME = "queue.1"
TOPIC_NAME = "topic.1"

def send_message_to_servicebus(message_text, send_to):
    try:
        with ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR) as client:
            if send_to == "queue":
                sender = client.get_queue_sender(queue_name=QUEUE_NAME)
            else:
                sender = client.get_topic_sender(topic_name=TOPIC_NAME)

            with sender:
                message = ServiceBusMessage(
                    message_text,
                    content_type="application/json" if send_to == "topic" else None
                )
                sender.send_messages(message)

        return True, f"Message sent to {send_to} successfully!"
    except Exception as e:
        return False, f"Failed to send message: {str(e)}"

def on_send_click():
    message_text = message_textbox.get("1.0", tk.END).strip()
    if not message_text:
        messagebox.showwarning("Input Required", "Please enter a message.")
        return

    send_to = msg_type.get()
    success, feedback = send_message_to_servicebus(message_text, send_to)
    if success:
        messagebox.showinfo("Success", feedback)
        message_textbox.delete("1.0", tk.END)
    else:
        messagebox.showerror("Error", feedback)

# --- UI Setup ---
root = tk.Tk()
root.title("Service Bus Sender")
root.geometry("600x500")

tk.Label(root, text="Enter Message:").pack(pady=5)

message_textbox = scrolledtext.ScrolledText(root, width=150, height=20, wrap=tk.WORD)
message_textbox.pack(pady=5, padx=10)

msg_type = tk.StringVar(value="topic")
tk.Label(root, text="Send To:").pack(pady=5)
tk.Radiobutton(root, text="Topic", variable=msg_type, value="topic").pack()
tk.Radiobutton(root, text="Queue", variable=msg_type, value="queue").pack()

send_button = tk.Button(root, text="Send Message", command=on_send_click)
send_button.pack(pady=15)

root.mainloop()