# Imports
import cProfile
import pstats
import os
# Run profiler
with cProfile.Profile() as pr:
    try:
        import RunServer
    except Exception as e:
        print ('An uncaught exception occured in the program:\n'+str(e))
# Get results
stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
# Display results
stats.print_stats(20)
stats.dump_stats(filename='profile.prof')
os.system('pip3 install snakeviz')
try:
    os.system('snakeviz profile.prof')
except KeyboardInterrupt:
    pass
os.remove('profile.prof')
