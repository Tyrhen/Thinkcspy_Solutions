"""Select Problems from Chapter 12 'How to Think Like a Computer Scientist'"""

from unit_tester import test
#P7
def myreplace(old,new,s):
        """ Replaces occurences of a user defined text with an alternative in a string"""
	result = new.join(s.split(old))
	return result


#P8.1
def cleanword(text):
    """ removes punctuation from a string"""
    import string
    not_letters = string.punctuation
    clean_string = ''
    for char in text:
            if char not in not_letters:
                clean_string+= char
    return clean_string

#P8.2
def has_dashdash(text):
    """ confirms whether a string contains a double dash"""
    doubleDash = '--'
    if doubleDash in text:
        return True
    else:
        return False


#P8.3
def extract_words(text):
        """ extracts a list exclusively of the words in a string"""
        clean_string = cleanword(text)
        result = clean_string.split()
        return result
    

#P8.4
def wordcount(word, text):
    """ Counts the number of occurences of a specific word in a string"""
    count = 0
    for words in text:
            if words == word:
                    count += 1
    return count

#P8.5
def wordset(listarray):
        """returns an ordered list of unique words"""
        result = []
        for word in listarray:
                if word not in result:
                        result.append(word)
        result.sort()
        return result

#P8.6
def longestword(listarray):
        """ returns the length of the longest word in a array"""
        if len(listarray) < 1:
                return 0
        word_length = []
        for word in listarray:
            word_length.append(len(word))
        return max(word_length)



def test_suite():
        print('\n8.1 Test Suite')
        test(cleanword('what?')=='what')
        test(cleanword("'now!'")=='now')
        test(cleanword("'?+='w-o-r-d!,@$()'")=='word')

        print('\n8.2 Test Suite')
        test(has_dashdash('distance--but'))
        test(not has_dashdash('several'))
        test(has_dashdash('spoke--'))
        test(has_dashdash('distance--but'))
        test(not has_dashdash('-yo-yo-'))

        print('\n8.3 Test Suite')
        test(extract_words("Now is the time! 'Now', is the time? Yes, now.")==
         ['Now','is','the','time','Now','is','the','time','Yes','now'])
        test(extract_words("She tried to curtsey as she spoke fancy")==
         ['She','tried','to','curtsey','as','she','spoke','fancy'])

        print('\n8.4 Test Suite')
        test(wordcount('now', ['now','is','time','is','now','is','is'])== 2)
        test(wordcount('is', ['now','is','time','is','now','is','is'])== 4)
        test(wordcount('time', ['now','is','time','is','now','is','is'])== 1)
        test(wordcount('frog',['now','is','time','is','now','is','is'])== 0)

        print('\n8.5 Test Suite')
        test(wordset(['now','is','time','is','now','is','is'])==
         ['is','now','time'])
        test(wordset(['I','a','a','is','a','is','I','am'])==
         ['I','a','am','is'])
        test(wordset(['or','a','am','is','are','be','but','am']) ==
         ['a','am','are','be','but','is','or'])

        print('\n8.5 Test Suite')
        test(longestword(['a','apple','pear','grape'])== 5)
        test(longestword(['a','am','I','be'])== 2)
        test(longestword(['this','supercalifragilisticexpialidocious'])== 34)
        test(longestword([])== 0 )
    
test_suite()
