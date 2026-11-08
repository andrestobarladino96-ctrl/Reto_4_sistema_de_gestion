#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initial base for the Integrated Management System - Software FJ
Programming Course - Phase 4 (Collaborative Work) - UNAD
Developed for the initial contribution in the collaborative group forum.
"""

from abc import ABC, abstractmethod
import logging

# =====================================================================
# LOGS SYSTEM CONFIGURATION
# =====================================================================
logging.basicConfig(
    filename='system_management.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    encoding='utf-8'
)

# =====================================================================
# CUSTOM EXCEPTIONS
# =====================================================================
class SoftwareFJError(Exception):
    """Base class for Software FJ system exceptions[cite: 2]."""
    pass

class InvalidClientError(SoftwareFJError):
    """Exception raised when client data is invalid[cite: 1, 2]."""
    pass

class ServiceNotAvailableError(SoftwareFJError):
    """Exception raised when service parameters are incorrect[cite: 2]."""
    pass

# =====================================================================
# ABSTRACT BASE CLASS
# =====================================================================
class BaseEntity(ABC):
    """Abstract class representing general entities in the system[cite: 2]."""
    
    def __init__(self, identifier: str):
        self._identifier = identifier

    @property
    def identifier(self) -> str:
        return self._identifier

    @abstractmethod
    def get_entity_details(self) -> str:
        """Abstract method to detail the entity[cite: 2]."""
        pass

# =====================================================================
# CLIENT CLASS WITH ENCAPSULATION AND VALIDATIONS
# =====================================================================
class Client(BaseEntity):
    """Represents a client with robust validations and encapsulation[cite: 2]."""
    
    def __init__(self, identifier: str, name: str, id_number: str, email: str, phone: str):
        super().__init__(identifier)
        self.name = name
        self.id_number = id_number
        self.email = email
        self.phone = phone

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str) or len(value.strip()) < 3:
            error_msg = f"Invalid client name: '{value}'. Minimum 3 characters."
            logging.error(error_msg)
            raise InvalidClientError(error_msg)
        self._name = value.strip()

    @property
    def id_number(self) -> str:
        return self._id_number

    @id_number.setter
    def id_number(self, value: str):
        if not value or not value.isdigit() or len(value) < 7:
            error_msg = f"Invalid ID number: '{value}'. Must contain only digits (minimum 7)."
            logging.error(error_msg)
            raise InvalidClientError(error_msg)
        self._id_number = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not value or "@" not in value or "." not in value:
            error_msg = f"Invalid email address: '{value}'."
            logging.error(error_msg)
            raise InvalidClientError(error_msg)
        self._email = value.strip()

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if not value or not value.isdigit() or len(value) < 7:
            error_msg = f"Invalid phone number: '{value}'."
            logging.error(error_msg)
            raise InvalidClientError(error_msg)
        self._phone = value

    def get_entity_details(self) -> str:
        return f"Client [ID: {self._identifier}, Name: {self._name}, ID Number: {self._id_number}]"


# =====================================================================
# ABSTRACT SERVICE CLASS (EXTENSION POINT FOR THE TEAM)
# =====================================================================
class Service(BaseEntity, ABC):
    """Base abstract class for Software FJ services[cite: 2]."""
    
    def __init__(self, identifier: str, service_name: str, base_cost: float):
        super().__init__(identifier)
        self.service_name = service_name
        self.base_cost = base_cost

    @abstractmethod
    def calculate_cost(self, *args, **kwargs) -> float:
        """Polymorphic abstract method to calculate costs[cite: 2]."""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Abstract method to describe the service[cite: 2]."""
        pass


# TODO FOR GROUP MATES:
# 1. Implement at least three service classes derived from Service (e.g., RoomReservation, EquipmentRental, SpecializedConsulting)[cite: 2].
# 2. Implement the Reservation class integrating client, service, duration, and states with try/except/else/finally handling[cite: 2].
# 3. Develop the simulation of the 10 operations in the main block (`if __name__ == "__main__":`)[cite: 3].