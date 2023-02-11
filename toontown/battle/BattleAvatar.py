#create a class called BattleAvatar thats a DistributedObject

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.distributed.ClockDelta import *
from direct.task import Task

from toontown.toonbase import ToontownGlobals

class BattleAvatar(DistributedObject.DistributedObject):
    
    def __init__(self):
        self.isInBattle = 0
    
    def isInBattle(self):
        if self.isInBattle:
            return 1