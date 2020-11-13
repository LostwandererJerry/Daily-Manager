#!/usr/bin/env python
# -*- coding: utf-8 -*-
import diaryWritter
import webBrowser.emailBrowser
import myPlans.TODOs
import finance.overhead
import betterDiaryWritter
import config

dailyManagerModules = {
    'diary': (betterDiaryWritter.main, (config.DIARYCACHE_FILEPATH,), True),
    'todo': (myPlans.TODOs.main,(config.ACTIVE_FILEPATH, config.ARCHIEVE_FILEPATH), False),
    'overhead': (finance.overhead.main,(config.OVERHEAD_FILEPATH,), False)
}
#the dict above uses module name: (function, parameters, pass command as last parameter) to record the information for each function,
#use () or none if the funcion doesn't require a parameter and True to pass the command as the last parameter

def main():
    inputPrompt = 'What would you like to do?' #entrypoint prompt for input
    for module in dailyManagerModules:
        inputPrompt += '\n---' + module # include the modules for the entrypoint
    inputPrompt += '\nYour input:'
    while True:
        choice = input(inputPrompt)
        for module in dailyManagerModules:
            if module in choice:
                print(20 * '-' + 'entering ' + module + ' section' + 20 * '-')

                currentModule = dailyManagerModules[module]
                func, para = currentModule[0], (currentModule[1] if not currentModule[2] else currentModule[1] + (choice,))
                #add command to the parameter tuple, making it the last parameter if currentModule[2] is true
                func(*para)

                print (20*'-' + 'exiting ' + module + ' section' + 20*'-')
                break #stop looking for other modules (only one modules can be used with one command in entry point)
        else:
            print('command is not understood.')

        if input('terminate(y/n): ') == 'y':
            break #ask whether to end the whole loop after each command

if __name__ == '__main__':
    main()