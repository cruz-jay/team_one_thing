import phone_tasks
import unittest
from unittest.mock import patch, call
from phone_tasks import PhoneTasks

class TestPhoneTasksSimMethods(unittest.TestCase):
    def setUp(self):
        self.phone = "TestPhone"
        self.phoneTask = PhoneTasks(self.phone)

    @patch("builtins.print")
    def test_make_call_sim(self, mock_print):
        self.phoneTask.make_call_sim("5551234")
        mock_print.assert_called_once_with(f"Calling 5551234 from {self.phone}...")

    @patch("builtins.print")
    def test_send_message_sim(self, mock_print):
        self.phoneTask.send_message_sim("5551234", "Hi!")
        mock_print.assert_called_once_with(f"Sending message to 5551234 from {self.phone}: Hi!")

    @patch("builtins.print")
    def test_check_balance_sim(self, mock_print):
        self.phoneTask.check_balance_sim()
        mock_print.assert_called_once_with(f"Checking balance for {self.phone}...")

    @patch("builtins.print")
    def test_take_screenshot_sim(self, mock_print):
        self.phoneTask.take_screenshot_sim()
        mock_print.assert_called_once_with(f"Taking screenshot on {self.phone}...")

    @patch("builtins.print")
    def test_open_app_sim(self, mock_print):
        self.phoneTask.open_app_sim("Maps")
        mock_print.assert_called_once_with(f"Opening Maps on {self.phone}...")

    @patch("builtins.print")
    def test_close_app_sim(self, mock_print):
        self.phoneTask.close_app_sim("Maps")
        mock_print.assert_called_once_with(f"Closing Maps on {self.phone}...")

    @patch("builtins.print")
    def test_restart_phone_sim(self, mock_print):
        self.phoneTask.restart_phone_sim()
        mock_print.assert_called_once_with(f"Restarting {self.phone}...")

    @patch("builtins.print")
    def test_shutdown_phone_sim(self, mock_print):
        self.phoneTask.shutdown_phone_sim()
        mock_print.assert_called_once_with(f"Shutting down {self.phone}...")

    @patch("builtins.print")
    def test_clear_cache_sim(self, mock_print):
        self.phoneTask.clear_cache_sim()
        mock_print.assert_called_once_with(f"Clearing cache on {self.phone}...")

    @patch("builtins.print")
    def test_update_phone_sim(self, mock_print):
        self.phoneTask.update_phone_sim()
        mock_print.assert_called_once_with(f"Updating {self.phone} to the latest version...")

    @patch("builtins.print")
    def test_locate_phone_sim(self, mock_print):
        self.phoneTask.locate_phone_sim()
        mock_print.assert_called_once_with(f"Locating {self.phone}...")

class TestPhoneTasksRealMethods(unittest.TestCase):
    def setUp(self):
        self.phone = "TestPhone"
        self.phoneTask = PhoneTasks(self.phone)

    @patch("subprocess.run")
    def test_make_call(self, mock_run):
        self.phoneTask.make_call("5551234")
        mock_run.assert_called_once_with(["open", "tel:5551234"], check=True, text=True)

    @patch("subprocess.run")
    def test_send_message(self, mock_run):
        self.phoneTask.send_message("5551234", "Hi!")
        mock_run.assert_called_once_with(["open", "sms:5551234?body=Hi!"], check=True, text=True)

    @patch("subprocess.run")
    def test_take_photo(self, mock_run):
        self.phoneTask.take_photo()
        mock_run.assert_called_once_with(["screencapture", "-x", f"{self.phone.lower()}_screenshot.png"], check=True, text=True)
            