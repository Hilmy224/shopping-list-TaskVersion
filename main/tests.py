from django.test import TestCase, Client
from main.models import Item

# Create your tests here.

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')


    def setUp(self):
        #Item.objects.create(name="Human Corpse1",amount=2,causeOfDeath="Supernatural Means",spiritStatus="None",
                            #description="""What once was a loving couple reduced to a inanimate object. Some sources say they met a 
                            #being that had the power to consume a persons soul leaving their body to rot.""")
        Item.objects.create(name="Human Corpse",amount=1, causeOfDeath="Killed", spiritStatus="Vengefull",
                            description="""An ordinary looking person that died in the middle of a coup d'état was a infamous serial killer, 
                            his victims now haunts this body even though the owner of the spirit has been dragged to hell""")
        Item.objects.create(name="Animal Carcass",amount=20, causeOfDeath="Killed",spiritStatus="None",
                            description="""A beast laid rampant in a farmers field killing of all his sheeps, the beast had venomous claws making the farmer unable to sell the meat.
                            Seeking to make a profit he sold the corpse of the sheeps here""")
    
    def test_items_can_created(self):
        subject1 = Item.objects.get(name="Human Corpse")
        subject2 = Item.objects.get(name="Animal Carcass")
        self.assertEqual(subject2.name, "Animal Carcass")
        self.assertEqual(subject2.causeOfDeath, "Killed")
        self.assertEqual(subject1.amount, 1)
        self.assertEqual(subject1.spiritStatus, "Vengefull")