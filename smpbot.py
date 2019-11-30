import time
import random
from termcolor import colored 
from simpleeval import simple_eval

class Bot:
    wait = 1

    def __init__(self,runtype="once"):
        self.runtype = runtype
        self.question = ''
        self.ansower = ''
    
    def _think(self,s):
        return s

    def _format(self,s):
        return colored(s,'blue')

    def _run_once(self):
        time.sleep(Bot.wait)
        print(self._format(self.question))
        self.ansower = input()
        time.sleep(Bot.wait)
        print(self._format(self._think(self.ansower)))

    def _run_looped(self):
        time.sleep(Bot.wait)
        print(self._format(self.question))
        while True:
            pd = ["x","q","quit","exit"]
            self.ansower = input()
            if self.ansower.lower() in pd:
                break
            try:
                print(self._format(self._think(self.ansower)))
            except:
                print("输入'x','q','exit'或'quit'将退出计算器，其他字符无效!!!")
                
    def run(self):
        if self.runtype == "once":
            self._run_once()
        elif self.runtype == "loop":
            self._run_looped()
    
class HelloBot(Bot):
    def __init__(self,runtype="once"):
        super().__init__(runtype)
        self.question = "Hi what's your name?"

    def _think(self,s):
        return f"hello {s}"

class GreetionBot(Bot):
    def __init__(self,runtype="once"):
        super().__init__(runtype)
        self.question = "How are you?"

    def _think(self,s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return f"I'm {s} too"
        else:
            return "Sorry to hear that"

class FavoriteColorBot(Bot):
    def __init__(self,runtype="once"):
        super().__init__(runtype)
        self.question = "What's your favoriter color?"

    def _think(self,s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"Your favorite color is {s}? My favoriter color is {random.choice(colors)}"

class CalcBot(Bot):
    #计算器
    def __init__(self,runtype="once"):
        super().__init__(runtype)
        self.question = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try:"
    
    def _think(self,s):
        result = simple_eval(s)
        return f"Done. Result = {result}"

class SmpBot:
    def __init__(self,wait):
        Bot.wait = wait
        self.bots = []

    def add(self,bot):
        self.bots.append(bot)

    def _prompt(self,s):
        print(s)
        print()

    def run(self):
        self._prompt("This is SmpBot dialog sysytem. Let's talk.")
        for bot in self.bots:
            bot.run()

smpBot = SmpBot(1)
smpBot.add(HelloBot())
#smpBot.add(GreetionBot())
#smpBot.add(FavoriteColorBot())
smpBot.add(CalcBot('loop'))
smpBot.run()