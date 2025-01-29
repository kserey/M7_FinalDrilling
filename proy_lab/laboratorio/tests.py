from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Configura los datos iniciales para las pruebas."""
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Test",
            ciudad="Santiago",
            pais="Chile"
        )

    def test_laboratorio_data(self):
        """Verifica que los datos guardados coincidan con los creados en setUpTestData."""
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio Test")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")

    def test_laboratorio_url(self):
        response = self.client.get(reverse('laboratorio_list'))
        self.assertEqual(response.status_code, 200)


    def test_laboratorio_view_reverse(self):
        """Verifica que reverse encuentra la URL y que la vista usa la plantilla correcta."""
        response = self.client.get(reverse("laboratorio_update", args=[self.laboratorio.id]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "laboratorio/laboratorio_form_update.html")
        self.assertContains(response, "Laboratorio Test")
