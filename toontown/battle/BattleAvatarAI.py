#make a class called BattleAvatarAI thats a DistributedObjectAI

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.task import Task

from toontown.toonbase import ToontownGlobals

class BattleAvatarAI(DistributedObjectAI.DistributedObjectAI):
    
    def __init__(self, isSuit):
        self.battleId = -1
        self.battle = None
        self.isInBattle = 0
        
        #Battle Specific
        self.oppenentsKilled = []
        self.isVulnerable = 0
        self.vulnerableOpponents = []
        self.isSuit = isSuit
        self.healsGiven = {}
    
    def delete(self):
        self.battle = None
        DistributedObjectAI.DistributedObjectAI.delete(self)
    
    def getBattleId(self):
        return self.battleId
    
    def getIsSuit(self):
        return self.isSuit
    
    def getIsInBattle(self):
        return self.isInBattle
    
    def getOpponentsKilled(self):
        return self.opponentsKilled
    
    def getIsVulnerable(self):
        return self.isVulnerable
    
    def getVulnerableOpponents(self):
        return self.vulnerableOpponents
    
    def setBattleId(self, battleId):
        self.battleId = battleId
    
    def setBattle(self, battle):
        self.battle = battle
    
    def setIsInBattle(self, isInBattle):
        self.isInBattle = isInBattle
    