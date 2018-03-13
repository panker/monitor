from app import db
import os

class LogInfo():
    def __init__(self, gameId, Ymd, type):
        gameInfo = self.getGameInfo(gameId)
        gameCode = gameInfo.code
        log_server = gameInfo.log_server
        self.shell_bash_10m = 'ssh pirate@'+log_server+' "find /home/pirate/log/udplog/'+gameCode+'/'+Ymd+' -name '+type+'.log|xargs wc -l|sort -t \'/\' -k 2"'+"|sort -t '/' -k 2|awk -F '/' '{print $1,$(NF-1)}'"

    def runShell(self):
        self.logInfo = os.system(self.shell_bash_10m)
        print u'%s' % (self.logInfo)

    def getLogInfoBy10m(self):
        print self.logInfo
        return True

    def getLogInfoBy1h(self):
        return True

    def getGameInfo(self, gameId):
        from ..models import game
        gameInfo = db.session.query(game.Game).filter_by(id=gameId).first()
        return gameInfo