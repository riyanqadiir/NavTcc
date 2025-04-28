# Q7: Message Logger with Nonlocal Count
# python
# Copy
# Edit

def logger():
    count = 0
    def log_message():
        nonlocal count
        count += 1
        print(f"Message logged. Total count: {count}")
    return log_message

# Demo
log = logger()
log()
log()
log()

