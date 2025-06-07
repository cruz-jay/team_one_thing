import os
import subprocess

class PhoneTasks:
    def __init__(self, phone: str) -> None:
        self.phone = phone

    def make_call_sim(self, number: str) -> None:
        print(f"Calling {number} from {self.phone}...")

    def send_message_sim(self, number: str, message: str) -> None:
        print(f"Sending message to {number} from {self.phone}: {message}")

    def check_balance_sim(self) -> None:
        # simulate checking balance for the phone number:
        print(f"Checking balance for {self.phone}...")
        
    def take_screenshot_sim(self) -> None:
        # simulate taking a screenshot
        print(f"Taking screenshot on {self.phone}...")
        
    def open_app_sim(self, app_name: str) -> None:
        # simulate opening an app on the phone
        print(f"Opening {app_name} on {self.phone}...")
        
    def close_app_sim(self, app_name: str) -> None:
        # simulate closing an app on the phone
        print(f"Closing {app_name} on {self.phone}...")
    
    def restart_phone_sim(self) -> None:
        # simulate restarting the phone
        print(f"Restarting {self.phone}...")
    
    def shutdown_phone_sim(self) -> None:  
        # simulate shutting down the phone
        print(f"Shutting down {self.phone}...")
        
    def clear_cache_sim(self) -> None:
        # simulate clearing cache on the phone
        print(f"Clearing cache on {self.phone}...") 
        
    def update_phone_sim(self) -> None:   
        # simulate updating the phone
        print(f"Updating {self.phone} to the latest version...")
        
    def locate_phone_sim(self) -> None:
        # simulate locating the phone
        print(f"Locating {self.phone}...")
       
       
    # set up real implementations for the methods below 
    def make_call(self, number: str) -> None:
        subprocess.run(["open", f"tel:{number}"], check=True, text=True)
    
    def send_message(self, number: str, message: str) -> None:  
        subprocess.run(["open", f"sms:{number}?body={message}"], check=True, text=True)
        
    def take_photo(self) -> None:
        subprocess.run(["screencapture", "-x", f"{self.phone}_screenshot.png"], check=True, text=True)
    
phoneTasks = PhoneTasks("MyPhone")
phoneTasks.make_call_sim("1234567890")
phoneTasks.send_message_sim("1234567890", "Hello!")
phoneTasks.check_balance_sim()
phoneTasks.take_screenshot_sim()
phoneTasks.open_app_sim("Calculator")
phoneTasks.close_app_sim("Calculator")
phoneTasks.restart_phone_sim()
phoneTasks.shutdown_phone_sim()
phoneTasks.clear_cache_sim()
phoneTasks.update_phone_sim()
phoneTasks.locate_phone_sim()
phoneTasks.make_call("1234567890")
phoneTasks.send_message("1234567890", "Hello!")
phoneTasks.take_photo()
print("All tasks completed.")
