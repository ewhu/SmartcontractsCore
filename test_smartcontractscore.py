# test_smartcontractscore.py
"""
Tests for SmartcontractsCore module.
"""

import unittest
from smartcontractscore import SmartcontractsCore

class TestSmartcontractsCore(unittest.TestCase):
    """Test cases for SmartcontractsCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartcontractsCore()
        self.assertIsInstance(instance, SmartcontractsCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartcontractsCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
