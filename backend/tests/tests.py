import app
from flask import Flask, request
import unittest

class TestCovidInfo(unittest.TestCase): 

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_case_200(self):
        result = self.app.get('/cases')
        self.assertEqual(result.status_code, 200)

    def test_vaccine_200(self):
        result = self.app.get('/vaccines')
        self.assertEqual(result.status_code, 200)
    
    def test_case_404(self):
        result = self.app.get('/case')
        self.assertEqual(result.status_code, 404)
    
    def test_vaccine_404(self):
        result = self.app.get('/vaccine')
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()
