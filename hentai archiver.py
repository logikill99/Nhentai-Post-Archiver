import os, random
from hentai import Hentai, Format
from time import sleep

postID = 0
doujins_found = 0
find_doujins =0

with open('post_ids.txt', 'w') as f:
    f.write('')

def checkHentaiIncludeAndExclude(hentaiID, language, tagincluded, tagexcluded):
    print(f'Checking Post ID: {hentaiID}')

    try:
        doujin = Hentai(hentaiID)
    except:
        print(' > Invalid post code.')

        return False

    if language in str(doujin.language) and tagincluded in str(doujin.tag) and tagexcluded not in str(doujin.tag):
        print(' > Valid Doujin! Language is', language,".")
        print(' > Doujin contains tag: ',tagincluded)
        print(' > Doujin does not contain tag: ',tagexcluded)
        print('downloading!')
        doujin.download()

        return True
    else:
        print('> Valid Post but language is not English.')

        return False


def checkHentaiInclude(hentaiID, language, tagincluded):
    print(f'Checking Post ID: {hentaiID}')

    try:
        doujin = Hentai(hentaiID)
    except:
        print(' > Invalid post code.')

        return False


    if language in str(doujin.language) and tagincluded in str(doujin.tag):
        print(' > Valid Doujin! Language is', language,".")
        print(' > Doujin contains tag: ',tagincluded)
        print('downloading!')
        doujin.download()

        return True

    else:
        print('> Valid Post but language is not', language,'.')

        return False


def checkHentaiExclude(hentaiID, language, tagexcluded):
    print(f'Checking Post ID: {hentaiID}')

    try:
        doujin = Hentai(hentaiID)
    except:
        print(' > Invalid post code.')

        return False

    if language in str(doujin.language) and tagexcluded not in str(doujin.tag):
        print(' > Valid Doujin! Language is', language,".")
        print(' > Doujin does not contain tag: ',tagexcluded)
        print('downloading!')
        doujin.download()

        return True
    else:
        print('> Valid Post but language is not', language,'.')

        return False


def checkHentaiLangOnly(hentaiID, language):
    print(f'Checking Post ID: {hentaiID}')

    try:
        doujin = Hentai(hentaiID)
    except:
        print(' > Invalid post code.')

        return False

    if language in str(doujin.language):
        print(' > Valid Doujin! Language is', language,".")
        print('downloading!')
        doujin.download()

        return True
    else:
        print('> Valid Post but language is not', language,'.')

        return False


find_doujins = int(input('Number of doujuins to find: '))
language = input('What language would you like to search for?\n(required): ')
tagincluded = input('Please input a tag to include in search \n(leave blank if none): ')
tagexcluded = input('Please input a tag to exclude in search \n(leave blank if none): ')
postID = int(input('Is there a specific id that you would like to start searching at?\n(enter 0 if not):'))

if tagincluded != '' and tagexcluded != '':

    while(doujins_found < find_doujins):
        postID += 1
        c = checkHentaiIncludeAndExclude(postID,language, tagincluded, tagexcluded)
        if c:
            with open('post_ids.txt', 'a') as f:
                f.write(f'{postID}\n')
            doujins_found += 1
            
                
        sleep(0.02)

elif tagincluded != '' and tagexcluded == '':

    while(doujins_found < find_doujins):
        postID += 1
        c = checkHentaiInclude(postID,language, tagincluded)
        if c:
            with open('post_ids.txt', 'a') as f:
                f.write(f'{postID}\n')
            doujins_found += 1
            
    sleep(0.02)

elif tagexcluded != '' and tagincluded == '':

    while(doujins_found < find_doujins):
        postID += 1
        c = checkHentaiInclude(postID,language, tagexcluded)
        if c:
            with open('post_ids.txt', 'a') as f:
                f.write(f'{postID}\n')
            doujins_found += 1
        
        sleep(0.02)

else:

    while(doujins_found < find_doujins):
        postID += 1
        c = checkHentaiInclude(postID,language, tagexcluded)
        if c:
            with open('post_ids.txt', 'a') as f:
                f.write(f'{postID}\n')
            doujins_found += 1
    
    sleep(0.02)


print('done lol')
