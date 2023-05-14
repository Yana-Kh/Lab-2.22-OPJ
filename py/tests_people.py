#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sqlite3
from pathlib import Path
from id_21 import create_db, add_human, select_all,find_human


class HumanTests(unittest.TestCase):
    # Метод действует на уровне класса, т.е. выполняется
    # перед запуском тестов класса.
    @classmethod
    def setUpClass(cls):
        """Set up for class"""

        print("setUpClass")
        print("==========")

    # Запускается после выполнения всех методов класса
    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    # Метод вызывается перед запуском теста. Как правило,
    # используется для подготовки окружения для теста.
    def setUp(self):
        """Set up for test"""
        print(f"\nSet up for [{self.shortDescription()}]")

    # Метод вызывается после завершения работы теста.
    # Используется для “приборки” за тестом.
    def tearDown(self):
        """Tear down for test"""
        print(f"Tear down for [{self.shortDescription()}]")

    def test_create_db(self):
        """ Checking the database creation."""
        database_path = "test.db"
        if Path(database_path).exists():
            Path(database_path).unlink()

        create_db(database_path)
        self.assertTrue(Path(database_path).is_file())
        Path(database_path).unlink()

    def test_add_human(self):
        """ Checking the addition."""
        database_path = "test.db"
        create_db(database_path)
        add_human(database_path, "Халимендик Яна", 9188871234, "05.05.2003")
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM people
            """
        )
        row = cursor.fetchone()
        self.assertEqual(row, (1, "Халимендик Яна", "05.05.2003"))
        conn.close()
        Path(database_path).unlink()

    def test_select_all(self):
        """ Checking the selection all """
        database_path = "test.db"
        create_db(database_path)
        add_human(database_path, "Иванов Иван", "10.09.2001",  9876754327)
        add_human(database_path, "Сидоров Сидр", "31.08.2017", 9871112233)

        comparison_output = [
            {"name": "Иванов Иван", "phone": '9876754327', "birthday": "10.09.2001"},
            {"name": "Сидоров Сидр", "phone": '9871112233', "birthday": "31.08.2017"},
        ]
        self.assertEqual(select_all(database_path), comparison_output)
        Path(database_path).unlink()

    def test_select_zz(self):
        """ Checking the selection by phone number """
        database_path = "test.db"
        create_db(database_path)
        add_human(database_path, "Иванов Иван", 9876754327, "10.09.2001")
        add_human(database_path, "Сидоров Сидр", 9871112233, "31.08.2017")
        comparison_output = [
            {"name": "Иванов Иван", "phone": 9876754327, "birthday": "10.09.2001"},
        ]
        self.assertEqual(find_human(database_path, "Иванов"), comparison_output)
        Path(database_path).unlink()
