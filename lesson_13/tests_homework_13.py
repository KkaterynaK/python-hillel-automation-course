import unittest
import logging
from lesson_13.homework_13 import log_event

class TestLogEvent(unittest.TestCase):

    def test_log_success_info_level(self):
        with self.assertLogs('log_event', level='INFO') as log_context:
            log_event("kateryna_qa", "success")
        self.assertEqual(len(log_context.output), 1)
        self.assertIn("INFO:log_event:Login event - Username: kateryna_qa, Status: success", log_context.output[0])

    def test_log_expired_warning_level(self):
        with self.assertLogs('log_event', level='WARNING') as log_context:
            log_event("user_old_password", "expired")
        self.assertEqual(len(log_context.output), 1)
        self.assertIn("WARNING:log_event:Login event - Username: user_old_password, Status: expired", log_context.output[0])

    def test_log_failed_error_level(self):
        with self.assertLogs('log_event', level='ERROR') as log_context:
            log_event("attacker_user", "failed")
        self.assertEqual(len(log_context.output), 1)
        self.assertIn("ERROR:log_event:Login event - Username: attacker_user, Status: failed", log_context.output[0])

if __name__ == '__main__':
    unittest.main()
