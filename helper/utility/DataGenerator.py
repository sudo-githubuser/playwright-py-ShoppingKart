import random
from typing import Dict

from faker import Faker
from unidecode import unidecode


class TestDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def _generate_email(self) -> str:
        """Email with @ and .com/.in domain"""
        domains = ["com", "in", "io"]
        return f"{self.fake.user_name()}{random.randint(100,999)}@{self.fake.domain_word()}.{random.choice(domains)}"

    def _generated_data(self) -> Dict[str, str]:
        """Generate test user data with specific formatting rules"""
        return {
            "first name": unidecode(self.fake.first_name())[:10],
            "last name": unidecode(self.fake.last_name())[:8],
            "email": self._generate_email(),
            "password": self.fake.password(length=12, special_chars=True)
        }

    @property
    def user_data(self) -> Dict[str, str]:
        return self._generated_data()