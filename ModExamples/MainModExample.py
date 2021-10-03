#Mods can add new ChatCommands and new help texts.
#They can also modify current ChatCommands and help text.
#They can also run any functions that the normal code can, so be careful when loading them
#ChatCommands are loaded A-Z.
#All of the code in "init_mod" will be used to load the mod. It will be passed 2 arguments:
# An array of dictionaries as the help texts (the 0th index will be base level permission commands, 1st index will be sudo, 2nd will be root)
# An array of dictionaries as the ChatCommands (indexes same as with help texts)
#Nothing will be done with any returned values
#Output syntax:
#def init_mod(helpTxts, chatCommandFuncs):
#   [your code]

def init_mod(helpTxts, chatCommandFuncs):
    # Setup ChatCommands
    def chatCommand(args, user):
        tellRaw('Test:\n'+str(args), 'FromText', user)
    def moddedChatCommand(args, user):
        tellRaw('Modified help (user='+str(user)+', args='+str(args)+')', None, user)
        writeCommand('say Test')

    # Apply ChatCommands
    chatCommandFuncs[0]['chatcommandtest'] = chatCommand
    chatCommandFuncs[0]['cctest'] = chatCommand
    chatCommandFuncs[0]['help'] = moddedChatCommand
    
    # Apply help texts
    helpTxts[0]['chatcommandtest | cctest'] = 'A test command, loaded through a mod'
    helpTxts[0]['help [command*]'] = 'The modified help command'
