from django.test import TestCase
from django.urls import reverse

from carros.models import Carro, Lead


class LeadViewTests(TestCase):
    def test_criar_lead_salva_telefone_e_carro(self):
        carro = Carro.objects.create(
            marca='Ford',
            modelo='Ka',
            km=12000,
            placa='ABC1234',
            cor='Prata',
        )

        response = self.client.post(
            reverse('criar-lead'),
            {
                'carro_id': carro.pk,
                'carro_modelo': carro.modelo,
                'telefone': '(11) 99999-0000',
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Lead.objects.count(), 1)
        lead = Lead.objects.get()
        self.assertEqual(lead.telefone, '(11) 99999-0000')
        self.assertEqual(lead.carro, carro)
        self.assertEqual(lead.origem, 'Site')
