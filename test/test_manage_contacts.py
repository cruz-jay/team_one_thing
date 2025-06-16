import manage_contacts
#from manage_contacts import ContactManager
import unittest


class TestManageContacts(unittest.TestCase):
    def setUp(self) -> None:
        """set up a contact manager instance for testing."""
        self.contact_manager = manage_contacts.ContactManager("John Black", "1234567890")

    def test_create_contact(self) -> None:
        """test creating a contact."""
        self.contact_manager.CreateContact()
        self.assertIn("John Black", self.contact_manager.contact)
        self.assertEqual(self.contact_manager.contact["John Black"], "1234567890")

    def test_update_contact(self) -> None:
        """test updating a contact."""
        self.contact_manager.CreateContact()
        self.contact_manager.UpdateContact(name="John Black", phone_number="0987654321")
        self.assertEqual(self.contact_manager.contact["John Black"], "0987654321")

    def test_delete_contact(self) -> None:
        """test deleting a contact."""
        self.contact_manager.CreateContact()
        self.contact_manager.DeleteContact("John Black")
        self.assertNotIn("John Black", self.contact_manager.contact)

    def test_read_contact( self) -> None:
        """test reading a contact."""
        self.contact_manager.CreateContact()
        with self.assertLogs(level='INFO') as log:
            self.contact_manager.ReadContact(name="John Black")
            self.assertIn("Contact found: Test Contact - 1234567890", log.output[0])