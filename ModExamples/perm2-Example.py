#Mods can add new ChatCommands and new help texts.
#They can also modify current ChatCommands and help text.
#ChatCommands are loaded A-Z.
#Output syntax:
#mod_output_ = (help texts (dictionary), chat command funcs (dictionary), perm level (integer, 0-2 (0=any user, 1=admin only, 2=root user)))

# Permission level for all defined ChatCommands in this mod
permLevel = 2 #0=any user ; 1=admin user ; 2=root/console only

# Example ChatCommand
def chatCommand(args, user):
    tellRaw('Root Test:\n'+str(args), 'FromText', user)
def moddedChatCommand(args, user):
    tellRaw('Root Modified help (user='+str(user)+', args='+str(args)+')', None, user)
    writeCommand('say Test')

# Example help text
helpTxts = {
    'chatcommandtest | cctest': 'A test command, loaded through a mod!',
    'help [*command]': 'The modified "help" command, through a mod',
}
chatCommandFuncs = {
    'chatcommandtest': chatCommand,
    'cctest': chatCommand, #Multiple can point to the same command
}

# Return the data
mod_output_ = (helpTxts, chatCommandFuncs, permLevel) #You MUST use "mod_output_ = [your outputs]" here, as anything else won't work!
