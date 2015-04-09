'''
Created on Apr 6, 2015

@author: ds-ga-1007
'''
if __name__ == "__main__":
    import functions as f
    import resultFunctions as rf
    import userInput as ui
    import plot as plt
    
    positions = ui.inputPositions()
    num_trial = ui.inputNum_trial()
    
    results = open('results.txt', 'w')
    
    for position in positions:
        daily_ret = f.investmentInstrument(position, num_trial)
        
        mean = rf.mean(daily_ret, num_trial)
        
        sd = rf.sd(daily_ret)
        
        
        #writing mean and sd to a txt file
        results.write(str(position) + ": mean = " + str(mean) + " standard deviation = " + str(sd) + "\n")
    
        
        #ploting results for each position
        fileName = 'histogram_' + str(position)+'_pos.pdf'
        plt.plotResults(daily_ret, num_trial, fileName)
        
    results.close()