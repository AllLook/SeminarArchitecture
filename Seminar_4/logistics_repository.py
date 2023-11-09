from abc import ABC, abstractmethod
from datetime import datetime


class Transport_company_repository:
    users = {}
    baggages = {}
    id_bus = []  # просто список доступных id автобусов чтобы один из них закрепить за водителем
    drivers = {}
    tickets = {}
