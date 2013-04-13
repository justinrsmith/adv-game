from nose.tools import *
from adv.game import BuildHero
from adv.game import Engine
from adv.game import Outskirts
from adv.game import Depart
from adv.game import Shop
from adv.game import Rest
from adv.game import Outskirts
from adv.game import Downtown
from adv.game import Tunnels
from adv.game import Subway
from adv.game import Battle

def test_BuildHero():
	hero = BuildHero('Paperboy')
	hero.printStats()
	
def test_Engine():
	engine = Engine(1,'Paperboy')
	engine.Run(1,'Paperboy')
	
def test_Depart():
	depart = Depart('Paperboy')
	depart.Action()
	
def test_Shop():
	shop = Shop('Paperboy', 'Subway')
	shop.Action()
	
def test_Rest():
	rest = Rest('Paperboy', 'Subway')
	rest.Action()
	
def test_Outskirts():
	outskirts = Outskirts('Paperboy')
	outskirts.Action()
	
def test_Downtown():
	downtown = Downtown('Paperboy','Outskirts')
	downtown.Action()
	
def test_Subway():
	subway = Subway('Paperboy','Downtown')
	subway.Action()
	
def test_Tunnels():
	tunnels = Tunnels('Paperboy','Subway')
	tunnels.Action()
	
def test_Battle():
	buildhero = BuildHero('Paperboy')
	battle = Battle(buildhero)
	battle.Action()
	battle.Attack(200,150,75,50,'Crony')
	battle.Defend(200,150,75,50,'Crony')