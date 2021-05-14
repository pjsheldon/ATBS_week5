'''--------By: PJ Sheldon---------
	--------Date: 8/8/20---------
	ATBS_week5.py madlibs
	SEC-290 Wilmington University'''


	import re

regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

"""copy the input.txt to file on computer 
    then copy destinatation to the file
    copy that same path with output.txt in place or input.txt 
    I used my destination for the file as an example.
    The output.txt is automatically created when the program runs."""

def mad_libs(source, destination): # self defined function
    
    with open(source, 'r') as source, open(destination, 'w') as out: # grabs the destination
        text = source.read() # reads the text

        if regex.findall(text): 
            for match in regex.findall(text): # for loop to find the keywords in input.txt
                replacement = input(f'Enter a{"n" if match.startswith("A") else ""}' # input function for Libs
                                    f' {match.lower()}: ') # make the input lower case no matter what is typed
                text = text.replace(match, replacement, 1) # replace the keywords with input 

            out.write(text) # writes the output text 
            print('\n' + text) # output text 
            print('Thanks for playing that was fun!') # fun message at the end


if __name__ == "__main__": 
    mad_libs(source='/Users/pj/Desktop/WILMU/SEC 290/ATBS/input.txt', destination='/Users/pj/Desktop/WILMU/SEC 290/ATBS/output.txt') # reads the destination and set the output