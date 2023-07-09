from django.test import TestCase
from http import HTTPStatus


# Create your tests here.
class TestCalculus(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn('Проектировка защитного заземление', response.content.decode())
        self.assertIn('Подборка площади сечения нулевого провода', response.content.decode())

    def test_task1(self):
        response = self.client.get('/task1/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn(
            'Определить параметры заземляющего устройства', response.content.decode()
        )
        self.assertIn(
            'Спроектировать защитное заземление оборудования лаборатории', response.content.decode()
        )

    def test_task2(self):
        response = self.client.get('/task2/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn(
            'Цель расчета зануления – определить сечение защитного нулевого провода', response.content.decode()
        )

        self.assertIn(
            'Подобрать площадь сечения нулевого провода', response.content.decode()
        )

    def test_info(self):
        response = self.client.get('/info-task1/')
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_about_team(self):
        response = self.client.get('/about_team/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn('Состав команды', response.content.decode())

    def test_targets(self):
        response = self.client.get('/targets/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn('Цели проекта', response.content.decode())
