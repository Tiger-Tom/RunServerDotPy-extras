#Mods can add new ChatCommands and new help texts.
#They can also modify current ChatCommands and help text.
#They can also run any functions that the normal code can, so be careful when loading them
#ChatCommands are loaded A-Z.
#Output syntax:
# global mod_output_
# mod_output_ = (help texts (dictionary), chat command funcs (dictionary), perm level (integer, 0-2 (0=any user, 1=admin only, 2=root user)))

# Permission level for all defined ChatCommands in this mod
permLevel = 0 #0=any user ; 1=admin user ; 2=root/console only

# Example ChatCommand
def chatCommand(args, user):
    tellRaw('Test:\n'+str(args), 'FromText', user)
def moddedChatCommand(args, user):
    tellRaw('Modified help (user='+str(user)+', args='+str(args)+')', None, user)
    writeCommand('say Test')

# Example help text
helpTxts = {
    'chatcommandtest | cctest': 'A test command, loaded through a mod',
    'help [command*]': 'The modified help command, changed through a mod',
}
chatCommandFuncs = {
    'chatcommandtest': chatCommand,
    'cctest': chatCommand, #Multiple can point to the same command
}

# Return the data
global mod_output_ #"mod_output_" MUST be global
mod_output_ = (helpTxts, chatCommandFuncs, permLevel) #You MUST use "mod_output_ = [your outputs]" here, as anything else won't work!
